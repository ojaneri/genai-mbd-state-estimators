#!/usr/bin/env python3
"""Fidelidade × utilidade (artigo, Sec. V-G). Spearman entre o score de fidelidade do DDPM e a mudança de erro do
gen_rfill_w0.3 vs só-real, por fração no veículo 1 (score id; J009_A usa o score vs teste, única medida que tinha) e por
domínio nas baterias (score de forma, discr_id_dyn_gen). Rodar da raiz do repositório."""
import json
from scipy.stats import spearmanr
B = 'experiments/data_reduction/desktop_results/'
def pts(jobs, key):
    out = []
    for j in jobs:
        for r in json.load(open(B + j + '/results.json'))['runs']:
            g = r['v'].get('gen_rfill_w0.3'); f = key(r)
            if g and f is not None: out.append((r['frac'], f, 100 * (g['flow_MAE'] / r['v']['real']['flow_MAE'] - 1)))
    return out
v1 = pts(['J012/J012', 'J024/J024_opel', 'J031/J031_ddpm_big', 'J009/J009_A'], lambda r: r.get('discr_id_gen', r.get('discr_gen_vs_test')))
for fr in sorted({x[0] for x in v1}):
    s = [x for x in v1 if x[0] == fr]; rho, p = spearmanr([x[1] for x in s], [x[2] for x in s]); print(f'vehicle 1, {fr:.0%}: n={len(s)} rho={rho:+.2f} p={p:.2f}')
bat = pts(['J020b/J020b', 'J023/J023_bat', 'J032b/J032b_bess', 'J035c/J035c_besstemp'], lambda r: r.get('discr_id_dyn_gen'))
print(f'batteries: n={len(bat)} shape score {min(x[1] for x in bat):.2f}-{max(x[1] for x in bat):.2f}, change in error {min(x[2] for x in bat):+.0f}% to {max(x[2] for x in bat):+.0f}%')
