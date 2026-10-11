"""VAE recorrente para séries temporais multivariadas (no espírito do TimeVAE, Desai et al. 2021),
versão compacta em PyTorch: codificador GRU -> (mu, logvar) por sequência; decodificador GRU a
partir do latente repetido no tempo; perda = reconstrução (MSE somado no tempo) + beta * KL."""
import numpy as np
import torch
import torch.nn as nn


class TimeVAE(nn.Module):
    def __init__(self, dim, hidden=48, latent=16, seed=0, device=None, beta=1.0):
        super().__init__()
        torch.manual_seed(seed); np.random.seed(seed)
        self.dev = torch.device(device or ('cuda' if torch.cuda.is_available() else 'cpu'))
        self.dim, self.latent, self.beta = dim, latent, beta
        self.enc = nn.GRU(dim, hidden, num_layers=2, batch_first=True)
        self.mu, self.lv = nn.Linear(hidden, latent), nn.Linear(hidden, latent)
        self.dec_in = nn.Linear(latent, hidden)
        self.dec = nn.GRU(hidden, hidden, num_layers=2, batch_first=True)
        self.out = nn.Linear(hidden, dim)
        self.to(self.dev)
        self.log = {'device': str(self.dev), 'gen': 'timevae'}

    def _decode(self, z, T):
        h = self.dec_in(z).unsqueeze(1).repeat(1, T, 1)
        y, _ = self.dec(h)
        return torch.sigmoid(self.out(y))

    def fit(self, X, iters=3000, bs=128, lr=1e-3):
        opt = torch.optim.Adam(self.parameters(), lr=lr)
        T = X.shape[1]
        for i in range(iters):
            x = torch.tensor(X[np.random.randint(0, len(X), bs)], dtype=torch.float32, device=self.dev)
            _, h = self.enc(x); h = h[-1]
            mu, lv = self.mu(h), self.lv(h)
            z = mu + torch.randn_like(mu) * torch.exp(0.5 * lv)
            xr = self._decode(z, T)
            rec = ((xr - x) ** 2).sum((1, 2)).mean()
            kl = (-0.5 * (1 + lv - mu ** 2 - lv.exp()).sum(1)).mean()
            loss = rec + self.beta * kl
            opt.zero_grad(); loss.backward(); opt.step()
        self.log.update(rec=float(rec.detach()), kl=float(kl.detach()))
        return self

    @torch.no_grad()
    def sample(self, n, T):
        out = []
        for i in range(0, n, 2048):
            z = torch.randn(min(2048, n - i), self.latent, device=self.dev)
            out.append(self._decode(z, T).cpu().numpy())
        return np.concatenate(out)
