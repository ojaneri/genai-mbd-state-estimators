"""Geradores adicionais para a rodada 3: difusão (DDPM 1D), autorregressão vetorial (VAR) e bootstrap de
blocos reais. Todos recebem janelas escaladas (n, L, C) em [0, 1] e devolvem janelas do mesmo formato."""
import math
import numpy as np
import torch
import torch.nn as nn


# ------------------------------------------------------------------ DDPM (Ho et al., 2020), versão compacta 1D
class _Denoiser(nn.Module):
    def __init__(self, c, h=64, temb=32):
        super().__init__()
        self.temb = temb
        self.t = nn.Sequential(nn.Linear(temb, h), nn.SiLU(), nn.Linear(h, h))
        self.inp = nn.Conv1d(c, h, 3, padding=1)
        self.blocks = nn.ModuleList([nn.Conv1d(h, h, 3, padding=d, dilation=d) for d in (1, 2, 4, 8, 1, 2)])
        self.norms = nn.ModuleList([nn.GroupNorm(8, h) for _ in self.blocks])
        self.out = nn.Conv1d(h, c, 3, padding=1)

    def _emb(self, t):
        half = self.temb // 2
        f = torch.exp(-math.log(10000) * torch.arange(half, device=t.device) / half)
        a = t.float()[:, None] * f[None]
        return torch.cat([a.sin(), a.cos()], 1)

    def forward(self, x, t):  # x: (n, C, L)
        h = self.inp(x) + self.t(self._emb(t))[:, :, None]
        for b, nrm in zip(self.blocks, self.norms):
            h = h + b(torch.nn.functional.silu(nrm(h)))
        return self.out(torch.nn.functional.silu(h))


class DDPM:
    def __init__(self, dim, hidden=64, steps=200, seed=0, device=None):
        torch.manual_seed(seed); np.random.seed(seed)
        self.dev = torch.device(device or ('cuda' if torch.cuda.is_available() else 'cpu'))
        self.T = steps
        self.net = _Denoiser(dim, hidden).to(self.dev)
        b = torch.linspace(1e-4, 0.02, steps, device=self.dev)
        self.beta, self.alpha = b, 1 - b
        self.abar = torch.cumprod(self.alpha, 0)
        self.log = {'device': str(self.dev), 'gen': 'ddpm', 'steps': steps}

    def fit(self, X, iters=6000, bs=256, lr=2e-4):
        opt = torch.optim.Adam(self.net.parameters(), lr=lr)
        for _ in range(iters):
            x0 = torch.tensor(X[np.random.randint(0, len(X), bs)], dtype=torch.float32, device=self.dev).transpose(1, 2) * 2 - 1
            t = torch.randint(0, self.T, (bs,), device=self.dev)
            e = torch.randn_like(x0); ab = self.abar[t][:, None, None]
            loss = ((self.net(ab.sqrt() * x0 + (1 - ab).sqrt() * e, t) - e) ** 2).mean()
            opt.zero_grad(); loss.backward(); opt.step()
        self.log['loss'] = float(loss.detach())
        return self

    @torch.no_grad()
    def sample(self, n, L):
        out = []
        C = self.net.out.out_channels
        for i in range(0, n, 4096):
            m = min(4096, n - i); x = torch.randn(m, C, L, device=self.dev)
            for t in reversed(range(self.T)):
                tt = torch.full((m,), t, device=self.dev, dtype=torch.long)
                eps = self.net(x, tt); a, ab, b = self.alpha[t], self.abar[t], self.beta[t]
                x = (x - b / (1 - ab).sqrt() * eps) / a.sqrt()
                if t > 0: x = x + b.sqrt() * torch.randn_like(x)
            out.append(((x.clamp(-1, 1) + 1) / 2).transpose(1, 2).cpu().numpy())
        return np.concatenate(out)


# ------------------------------------------------------------------ VAR(p) com resíduos reamostrados
class VAR:
    def __init__(self, dim, p=3, seed=0, **_):
        self.p, self.rng = p, np.random.default_rng(seed)
        self.log = {'gen': 'var', 'p': p}

    def fit(self, X, **_):
        p = self.p; n, L, C = X.shape
        Y = X[:, p:, :].reshape(-1, C)
        Z = np.concatenate([X[:, p - k - 1:L - k - 1, :] for k in range(p)], 2).reshape(-1, C * p)
        Z1 = np.c_[Z, np.ones(len(Z))]
        self.A, *_ = np.linalg.lstsq(Z1, Y, rcond=None)
        self.res = Y - Z1 @ self.A
        self.init = X[:, :p, :]
        self.log['resid_sd'] = float(self.res.std())
        return self

    def sample(self, n, L):
        p, C = self.p, self.init.shape[2]
        S = np.zeros((n, L, C), dtype=np.float32)
        S[:, :p] = self.init[self.rng.integers(0, len(self.init), n)]
        for t in range(p, L):
            z = np.concatenate([S[:, t - k - 1] for k in range(p)], 1)
            S[:, t] = np.c_[z, np.ones(n)] @ self.A + self.res[self.rng.integers(0, len(self.res), n)]
        return np.clip(S, 0, 1)


# ------------------------------------------------------------------ bootstrap de blocos reais com costura
class BlockBootstrap:
    """Novas janelas = primeira metade de uma janela real + segunda metade de outra janela real cujo início
    é o mais próximo (em todos os canais) do fim da primeira. Referência de 'realismo alcançável'."""
    def __init__(self, dim, seed=0, **_):
        self.rng = np.random.default_rng(seed); self.log = {'gen': 'bootstrap'}

    def fit(self, X, **_):
        self.X = X; return self

    def sample(self, n, L):
        h = L // 2; X = self.X
        A = X[self.rng.integers(0, len(X), n), :h]
        cand = X[self.rng.integers(0, len(X), (n, 32))]          # 32 candidatas por janela
        d = np.abs(cand[:, :, L - h, :] - A[:, None, -1, :]).sum(2)
        B = cand[np.arange(n), d.argmin(1), L - h:]
        return np.concatenate([A, B], 1).astype(np.float32)


# ------------------------------------------------------------------ DDPM v2 (no espírito do Diffusion-TS, ICLR 2024)
class DDPM2:
    """Predição de x0, agenda cosseno, EMA dos pesos, perda de Fourier, amostragem DDIM e escolha de
    checkpoint por discr num subconjunto reservado do TREINO (nunca validação/teste). Suporta geração
    condicional em canais conhecidos (ex.: velocidade real) por substituição a cada passo (RePaint/inpainting)."""
    def __init__(self, dim, hidden=128, steps=500, seed=0, device=None, fourier=0.1, ema=0.999):
        import copy
        torch.manual_seed(seed); np.random.seed(seed)
        self.dev = torch.device(device or ('cuda' if torch.cuda.is_available() else 'cpu'))
        self.T, self.fourier, self.ema_rate = steps, fourier, ema
        self.net = _Denoiser(dim, hidden).to(self.dev)
        self.ema = copy.deepcopy(self.net).eval()
        s = 0.008; t = torch.linspace(0, steps, steps + 1, device=self.dev) / steps
        ab = torch.cos((t + s) / (1 + s) * math.pi / 2) ** 2; ab = ab / ab[0]
        self.abar = ab[1:].clamp(1e-5, 0.9999)
        self.log = {'device': str(self.dev), 'gen': 'ddpm2', 'steps': steps, 'fourier': fourier, 'ema': ema}
        self.select_fn = None

    def _ema_update(self):
        with torch.no_grad():
            for p, q in zip(self.ema.parameters(), self.net.parameters()): p.mul_(self.ema_rate).add_(q, alpha=1 - self.ema_rate)

    def fit(self, X, iters=30000, bs=256, lr=2e-4, eval_every=5000):
        import copy
        opt = torch.optim.Adam(self.net.parameters(), lr=lr)
        best, best_state, hist = None, None, []
        for i in range(1, iters + 1):
            x0 = torch.tensor(X[np.random.randint(0, len(X), bs)], dtype=torch.float32, device=self.dev).transpose(1, 2) * 2 - 1
            t = torch.randint(0, self.T, (bs,), device=self.dev)
            e = torch.randn_like(x0); ab = self.abar[t][:, None, None]
            x0h = self.net(ab.sqrt() * x0 + (1 - ab).sqrt() * e, t)
            loss = ((x0h - x0) ** 2).mean()
            if self.fourier:
                loss = loss + self.fourier * (torch.fft.rfft(x0h, dim=2) - torch.fft.rfft(x0, dim=2)).abs().mean()
            opt.zero_grad(); loss.backward(); opt.step(); self._ema_update()
            if self.select_fn is not None and (i % eval_every == 0 or i == iters):
                sc = self.select_fn(self)
                hist.append((i, sc))
                if best is None or sc < best: best, best_state = sc, copy.deepcopy(self.ema.state_dict())
        if best_state is not None: self.ema.load_state_dict(best_state)
        self.log.update(loss=float(loss.detach()), select_hist=hist, best_select=best)
        return self

    @torch.no_grad()
    def sample(self, n, L, cond=None, cond_ch=(0,), ddim_steps=50):
        """cond: janelas (m, L, C) escaladas de onde se copiam os canais conhecidos (amostradas com reposição)."""
        C = self.net.out.out_channels; out = []
        ts = torch.linspace(self.T - 1, 0, ddim_steps, device=self.dev).long()
        for i in range(0, n, 4096):
            m = min(4096, n - i); x = torch.randn(m, C, L, device=self.dev)
            if cond is not None:
                k = torch.tensor(cond[np.random.randint(0, len(cond), m)], dtype=torch.float32, device=self.dev).transpose(1, 2) * 2 - 1
            for j, t in enumerate(ts):
                ab = self.abar[t]
                if cond is not None:   # substitui os canais conhecidos pelo valor real ruidoso no nível t
                    x[:, list(cond_ch)] = ab.sqrt() * k[:, list(cond_ch)] + (1 - ab).sqrt() * torch.randn_like(k[:, list(cond_ch)])
                x0h = self.ema(x, torch.full((m,), int(t), device=self.dev, dtype=torch.long)).clamp(-1, 1)
                eps = (x - ab.sqrt() * x0h) / (1 - ab).sqrt()
                abn = self.abar[ts[j + 1]] if j + 1 < len(ts) else torch.tensor(1.0, device=self.dev)
                x = abn.sqrt() * x0h + (1 - abn).sqrt() * eps
            if cond is not None: x[:, list(cond_ch)] = k[:, list(cond_ch)]
            out.append(((x.clamp(-1, 1) + 1) / 2).transpose(1, 2).cpu().numpy())
        return np.concatenate(out)
