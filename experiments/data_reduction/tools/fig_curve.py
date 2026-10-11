#!/usr/bin/env python3
"""Figura: curva de aprendizado do caso A (Opel), todos os geradores, sementes 0–4, teste tanques 18–22.
Fontes (results.json no desktop_results): J009_A (1–10 %: real, DDPM, aumento simples) + J016 (3, 20, 30 %),
J014 (bootstrap e physonly, 1–10 %), J018 (VAR, 1–10 %). Teto = 100 % real (J009_A)."""
import json, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
B = 'experiments/data_reduction/desktop_results/'
L = lambda p: json.load(open(B + p))
def curve(rs, k):
    fr = sorted({x['frac'] for x in rs}); return fr, [np.mean([x['v'][k]['flow_MAE'] for x in rs if x['frac'] == f]) for f in fr]
a = L('J009/J009_A/results.json'); c = L('J016/J016_curva/results.json'); b = L('J014/J014_boot/results.json'); v = L('J018/J018_var/results.json')
both = a['runs'] + c['runs']
plt.figure(figsize=(3.5, 2.6))
for rs, k, lab, st in [(both, 'real', 'Real only', 'k-o'), (both, 'gen_rfill_w0.3', 'Real + DDPM', 'b-s'),
                       (b['runs'], 'gen_rfill_w0.3', 'Real + bootstrap', 'g-^'), (b['runs'], 'physonly', 'Physics-structured', 'r-d'),
                       (both, 'aug_rfill_w0.3', 'Real + simple aug.', 'm-v'), (v['runs'], 'gen_rfill_w0.3', 'Real + VAR', 'c-x')]:
    f, m = curve(rs, k); plt.plot(np.array(f) * 100, m, st, ms=3.5, lw=1, label=lab)
plt.axhline(a['upper_bound_100pct_real']['flow_MAE'], color='gray', ls=':', lw=0.8, label='100 % real')
plt.xscale('log'); plt.xticks([1, 2, 3, 5, 10, 20, 30], ['1', '2', '3', '5', '10', '20', '30'])
plt.xlabel('Real training data (% of trips)', fontsize=7); plt.ylabel('Fuel-flow MAE (mL/min)', fontsize=7)
plt.ylim(2.0, 5.2); plt.tick_params(labelsize=6); plt.legend(fontsize=5.5, ncol=2, frameon=False); plt.tight_layout()
plt.savefig(sys.argv[1]); print('ok', sys.argv[1])
