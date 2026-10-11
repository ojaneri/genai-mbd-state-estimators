#!/usr/bin/env python3
"""Avaliação pré-registrada (d-0030) dos jobs J036–J040. Roda da raiz do repositório; analisa só os jobs que já existem.
Regra d-0010: média menor que a referência e no máximo 1/5 sementes pior. H6s: portão não pior que só-real em >= 4/5 sementes.
Unidades: fuel em mL/min ou cm3/min (escala 1); bess_temp em °C (escala 1)."""
import json, os, numpy as np
from scipy.stats import ttest_rel
B = 'experiments/data_reduction/desktop_results/'
def runs(p): return json.load(open(B + p))['runs'] if os.path.exists(B + p) else None
def by(rs, f): return sorted([r for r in rs if abs(r['frac'] - f) < 1e-9], key=lambda r: r['seed'])
def rule(a, b):  # a = método, b = referência (listas pareadas por semente)
    a, b = np.array(a), np.array(b); worse = int((a > b).sum()); p = ttest_rel(a, b).pvalue if len(a) > 1 else float('nan')
    return f"{a.mean():.4g} vs {b.mean():.4g} ({100*(a.mean()/b.mean()-1):+.1f} %; piores {worse}/{len(a)}; p {p:.3g}) -> {'SIM' if a.mean() < b.mean() and worse <= 1 else 'não'}"
for job, name in [('J036/J036_ita_auto/results.json', 'J036 portão, veículo 2'), ('J037/J037_besstemp_auto/results.json', 'J037 portão, BESS temperatura')]:
    rs = runs(job); print(f'\n== {name}', '(ainda não chegou)' if rs is None else '')
    if rs is None: continue
    for f in sorted({r['frac'] for r in rs}):
        R = by(rs, f); auto = [r['auto_test_MAE'] for r in R]; real = [r['v']['real']['flow_MAE'] for r in R]
        cands = [k for k in R[0]['v'] if k != 'real' or True]
        oracle = [min(r['v'][k]['flow_MAE'] for k in r['v']) for r in R]
        h6s = sum(a <= b for a, b in zip(auto, real))
        ch = {}; [ch.__setitem__(r['auto_choice'], ch.get(r['auto_choice'], 0) + 1) for r in R]
        print(f"  {f:.0%}: H6 {rule(auto, real)} | H6s não pior em {h6s}/{len(R)} -> {'SIM' if h6s >= 4 else 'NÃO'} | arrependimento {np.mean(np.array(auto)-np.array(oracle)):.4g} | escolhas {ch}")
print('\n== J038 MLP, sementes 0–4 (J019 0–2 + J038 3–4)')
a, b = runs('J019/J019_mlp/results.json'), runs('J038/J038_mlp/results.json')
if b is None: print('  (J038 ainda não chegou)')
else:
    hgb = runs('J009/J009_A/results.json')
    for f in sorted({r['frac'] for r in a + b}):
        R = by(a + b, f); seeds = [r['seed'] for r in R]
        mg = [r['v']['gen_rfill_w0.3']['flow_MAE'] for r in R]; mr = [r['v']['real']['flow_MAE'] for r in R]
        H = {r['seed']: r for r in by(hgb, f)}; hr = [H[s]['v']['real']['flow_MAE'] for s in seeds if s in H]
        print(f"  {f:.0%} (sementes {seeds}): MLP+DDPM vs MLP só-real {rule(mg, mr)}")
        if len(hr) == len(mg): print(f"        MLP+DDPM vs HGB só-real (J009_A) {rule(mg, hr)}")
for job, ref, name in [('J039/J039_ita_boot/results.json', 'J013/J013/results.json', 'J039 bootstrap, veículo 2 (DDPM = J013)'),
                       ('J040/J040_besstemp_boot/results.json', 'J035c/J035c_besstemp/results.json', 'J040 bootstrap, BESS temperatura (DDPM = J035c)')]:
    rs = runs(job); print(f'\n== {name}', '(ainda não chegou)' if rs is None else '')
    if rs is None: continue
    dd = runs(ref)
    for f in sorted({r['frac'] for r in rs}):
        R = by(rs, f); D = {r['seed']: r for r in by(dd, f)}
        bo = [r['v']['gen_rfill_w0.3']['flow_MAE'] for r in R]; re_ = [r['v']['real']['flow_MAE'] for r in R]
        dg = [D[r['seed']]['v']['gen_rfill_w0.3']['flow_MAE'] for r in R]
        same = all(abs(r['v']['real']['flow_MAE'] - D[r['seed']]['v']['real']['flow_MAE']) < 1e-9 for r in R)
        print(f"  {f:.0%}: bootstrap vs só-real {rule(bo, re_)} | DDPM vs bootstrap {rule(dg, bo)} | só-real idêntico ao job DDPM: {same}")
