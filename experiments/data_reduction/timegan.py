"""TimeGAN (Yoon, Jarrett, van der Schaar, NeurIPS 2019) em PyTorch, versão compacta.
Redes GRU: embedder, recovery, generator, supervisor, discriminator; treino em 3 fases
(autoencoder, supervisionado, conjunto), como no artigo original."""
import numpy as np
import torch
import torch.nn as nn


class _Net(nn.Module):
    def __init__(self, i, h, o, layers, act):
        super().__init__()
        self.rnn = nn.GRU(i, h, num_layers=layers, batch_first=True)
        self.fc = nn.Linear(h, o)
        self.act = act

    def forward(self, x):
        y, _ = self.rnn(x)
        y = self.fc(y)
        return torch.sigmoid(y) if self.act else y


class TimeGAN:
    def __init__(self, dim, hidden=24, layers=2, seed=0, device=None):
        torch.manual_seed(seed); np.random.seed(seed)
        self.dev = torch.device(device or ('cuda' if torch.cuda.is_available() else 'cpu'))
        self.dim, self.h = dim, hidden
        self.E = _Net(dim, hidden, hidden, layers, True)
        self.R = _Net(hidden, hidden, dim, layers, True)
        self.G = _Net(dim, hidden, hidden, layers, True)
        self.S = _Net(hidden, hidden, hidden, layers - 1 or 1, True)
        self.D = _Net(hidden, hidden, 1, layers, False)
        for n in (self.E, self.R, self.G, self.S, self.D): n.to(self.dev)
        self.log = {'device': str(self.dev)}

    def _batch(self, X, bs):
        idx = np.random.randint(0, len(X), bs)
        return torch.tensor(X[idx], dtype=torch.float32, device=self.dev)

    def fit(self, X, iters=2000, bs=128, gamma=1.0):
        mse, bce = nn.MSELoss(), nn.BCEWithLogitsLoss()
        oER = torch.optim.Adam(list(self.E.parameters()) + list(self.R.parameters()))
        oS = torch.optim.Adam(self.S.parameters())
        oG = torch.optim.Adam(list(self.G.parameters()) + list(self.S.parameters()))
        oD = torch.optim.Adam(self.D.parameters())
        T = X.shape[1]
        # fase 1: autoencoder
        for _ in range(iters):
            x = self._batch(X, bs); h = self.E(x); xt = self.R(h)
            l = 10 * torch.sqrt(mse(xt, x)); oER.zero_grad(); l.backward(); oER.step()
        self.log['recon'] = float(l.detach())
        # fase 2: supervisor
        for _ in range(iters):
            x = self._batch(X, bs); h = self.E(x).detach(); hs = self.S(h)
            l = mse(hs[:, :-1], h[:, 1:]); oS.zero_grad(); l.backward(); oS.step()
        self.log['sup'] = float(l.detach())
        # fase 3: conjunto
        for _ in range(iters):
            for _k in range(2):
                x = self._batch(X, bs); z = torch.rand(bs, T, self.dim, device=self.dev)
                eh = self.G(z); hh = self.S(eh); xh = self.R(hh)
                h = self.E(x); hs = self.S(h)
                yf, yfe = self.D(hh), self.D(eh)
                lu = bce(yf, torch.ones_like(yf)) + gamma * bce(yfe, torch.ones_like(yfe))
                ls = mse(hs[:, :-1], h[:, 1:])
                lv = (torch.abs(xh.std(0) - x.std(0)).mean() + torch.abs(xh.mean(0) - x.mean(0)).mean())
                lg = lu + 100 * torch.sqrt(ls) + 100 * lv
                oG.zero_grad(); lg.backward(); oG.step()
                x = self._batch(X, bs); h = self.E(x); xt = self.R(h); hs = self.S(h)
                le = 10 * torch.sqrt(mse(xt, x)) + 0.1 * mse(hs[:, :-1], h[:, 1:])
                oER.zero_grad(); le.backward(); oER.step()
            x = self._batch(X, bs); z = torch.rand(bs, T, self.dim, device=self.dev)
            with torch.no_grad():
                h = self.E(x); eh = self.G(z); hh = self.S(eh)
            yr, yf, yfe = self.D(h), self.D(hh), self.D(eh)
            ld = bce(yr, torch.ones_like(yr)) + bce(yf, torch.zeros_like(yf)) + gamma * bce(yfe, torch.zeros_like(yfe))
            if ld.item() > 0.15:
                oD.zero_grad(); ld.backward(); oD.step()
        self.log.update(g=float(lg.detach()), d=float(ld.detach()))
        return self

    @torch.no_grad()
    def sample(self, n, T):
        out = []
        for i in range(0, n, 1024):
            z = torch.rand(min(1024, n - i), T, self.dim, device=self.dev)
            out.append(self.R(self.S(self.G(z))).cpu().numpy())
        return np.concatenate(out)
