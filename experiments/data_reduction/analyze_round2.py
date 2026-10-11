#!/usr/bin/env python3
"""Recalcula no servidor as estatísticas de um job da rodada 2 a partir dos results.json.
Uso: python3 analyze_round2.py <pasta do job> -> imprime markdown e grava <pasta>/server_summary.json"""
import json, glob, sys, math, statistics as st
D = sys.argv[1]
fs = sorted(glob.glob(f'{D}/**/results.json', recursive=True))
R = [json.load(open(f)) for f in fs]
def ms(v): return (st.mean(v), st.stdev(v) if len(v) > 1 else 0.0)
def sign_p(k, n):  # bilateral exato
    if n == 0: return None
    m = min(k, n - k); return min(1.0, 2 * sum(math.comb(n, i) for i in range(m + 1)) / 2 ** n)
out = dict(files=fs, meta=[{k: r['meta'][k] for k in ('gen', 'model', 'mode', 'test_segments', 'cuda', 'gpu', 'iters', 'hidden', 'latent', 'seeds', 'fracs')} for r in R],
           ceiling=[r.get('upper_bound_100pct_real') for r in R], table={}, paired={})
runs = [x for r in R for x in r['runs']]
fracs = sorted({x['frac'] for x in runs})
variants = sorted({v for x in runs for v in x['v']})
lines = ['| fração | variante | flow_MAE (média ± dp) | litres_MAE | Δflow vs real | pior/total | p (sinal) |', '|---|---|---|---|---|---|---|']
for f in fracs:
    rs = [x for x in runs if x['frac'] == f]
    for v in variants:
        rv = [x for x in rs if v in x['v']]
        if not rv: continue
        fl = ms([x['v'][v]['flow_MAE'] for x in rv]); li = ms([x['v'][v]['litres_MAE'] for x in rv])
        d = [x['v'][v]['flow_MAE'] - x['v']['real']['flow_MAE'] for x in rv if 'real' in x['v']] if v != 'real' else []
        k = sum(z > 0 for z in d); p = sign_p(k, len(d)) if d else None
        out['table'][f'{f}|{v}'] = dict(flow=fl, litres=li, dflow=ms(d) if len(d) > 1 else None, worse=k, n=len(d), p=p)
        lines.append(f"| {f:g} | {v} | {fl[0]:.3f} ± {fl[1]:.3f} | {li[0]:.3f} ± {li[1]:.3f} | " +
                     (f"{st.mean(d):+.3f}" if d else '—') + f" | {k}/{len(d)} | " + (f"{p:.3g}" if p is not None else '—') + ' |')
    out['paired'][f] = dict(discr_gen=ms([x['discr_gen_vs_test'] for x in rs if x.get('discr_gen_vs_test') is not None]),
                           discr_realtrain=ms([x['discr_realtrain_vs_test'] for x in rs]), audit=ms([x['audit_pass'] for x in rs]),
                           n_real=ms([x['n_real'] for x in rs]))
lines.append('')
lines.append('| fração | discr gerador vs teste | discr real-treino vs teste | aprovação auditoria | janelas reais |')
lines.append('|---|---|---|---|---|')
for f in fracs:
    p = out['paired'][f]
    lines.append(f"| {f:g} | {p['discr_gen'][0]:.3f} ± {p['discr_gen'][1]:.3f} | {p['discr_realtrain'][0]:.3f} | {p['audit'][0]:.3f} | {p['n_real'][0]:.0f} |")
# melhor variante por fração e quantas variantes bateram o real em média
best = {}
for f in fracs:
    cand = [(k.split('|')[1], v['flow'][0]) for k, v in out['table'].items() if k.startswith(f'{f}|')]
    best[f] = min(cand, key=lambda t: t[1])
    beat = [k.split('|')[1] for k, v in out['table'].items() if k.startswith(f'{f}|') and v['dflow'] and v['dflow'][0] < 0]
    lines.append(f"\nfração {f:g}: melhor = {best[f][0]} ({best[f][1]:.3f}); variantes com Δ médio < 0 vs real: {beat if beat else 'nenhuma'}")
json.dump(out, open(f'{D}/server_summary.json', 'w'), indent=1)
print('\n'.join(lines))
print('\nmeta:', out['meta']); print('teto:', out['ceiling'])
