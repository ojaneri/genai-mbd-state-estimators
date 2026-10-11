#!/usr/bin/env python3
"""Fig. 2 do artigo: curvas R→V medidas (dissertação, Ap. A, Tab. A.54–A.59), mediana e envelope C1–C9.
Fontes TrueType embutidas (pdf.fonttype 42) — o IEEE PDF eXpress rejeita Type 3. Uso: python fig_vf_curves.py <saida.pdf>"""
import sys, pandas as pd, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42, 'font.family': 'serif', 'font.size': 7})
D = 'data/thesis_vf_curves/'
fig, axs = plt.subplots(1, 3, figsize=(7.16, 2.3))
for ax, v in zip(axs, 'ABC'):
    r, e = pd.read_csv(f'{D}vehicle{v}_real.csv'), pd.read_csv(f'{D}vehicle{v}_envelope.csv')
    ec = [c for c in e.columns if c != 'R_ohm']; tc = [c for c in r.columns if c.startswith('c')]
    ax.fill_between(e.R_ohm, e[ec].min(1), e[ec].max(1), color='0.85', lw=0, label='Envelope $C_1$–$C_9$')
    for i, c in enumerate(tc): ax.plot(r.R_ohm, r[c], color='tab:blue', lw=0.6, label='Measured tanks' if i == 0 else None)
    ax.plot(r.R_ohm, r.Med_L, 'k', lw=1.3, label='Median')
    ax.set_title(f'Vehicle {v} ({len(tc)} tanks)', fontsize=8); ax.set_xlabel(r'Sender resistance $R$ ($\Omega$)'); ax.grid(alpha=0.3, lw=0.5)
axs[0].set_ylabel('Fuel volume (L)'); axs[0].legend(fontsize=6)
plt.tight_layout(); plt.savefig(sys.argv[1]); print('ok', sys.argv[1])
