#!/usr/bin/env python3
"""Recalcula, no servidor, as estatísticas da execução do desktop a partir dos results.json
(independente do RUN-REPORT). Uso: python3 analyze_desktop.py <pasta desktop_results/STAMP>"""
import json, glob, sys, statistics as st, math
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = sys.argv[1]
R = [json.load(open(f)) for f in sorted(glob.glob(f'{D}/final_seed*/results.json'))]
C = ['real', 'real_timegan', 'real_timegan_noaudit', 'real_simpleaug']
out = {'n_seeds': len(R), 'upper': R[0]['upper_bound_100pct_real'], 'ref_maf_pump': R[0]['reference_MAF_vs_pump']['litres_MAE'], 'by_frac': {}, 'paired': {}, 'scenario': {}}
fracs = sorted({r['frac'] for x in R for r in x['runs']})
def ms(v): return (st.mean(v), st.stdev(v) if len(v) > 1 else 0.0)
for f in fracs:
    runs = [r for x in R for r in x['runs'] if r['frac'] == f]
    out['by_frac'][f] = {c: {m: ms([r[c][m] for r in runs]) for m in ('flow_MAE', 'litres_MAE')} for c in C}
    out['by_frac'][f]['discr_timegan'] = ms([r['discr_timegan'] for r in runs])
    out['by_frac'][f]['discr_real_train'] = ms([r['discr_real_train'] for r in runs])
    out['by_frac'][f]['audit_all'] = ms([r['audit']['all'] for r in runs])
    out['by_frac'][f]['tstr_flow'] = ms([r['tstr_timegan']['flow_MAE'] for r in runs])
    for c in C[1:]:
        for m in ('flow_MAE', 'litres_MAE'):
            d = [r[c][m] - r['real'][m] for r in runs]
            out['paired'].setdefault(f'{c}-{m}', {})[f] = dict(mean=st.mean(d), sd=st.stdev(d), worse=sum(x > 0 for x in d), n=len(d))
# teste de sinal exato (todas as frações): quantas vezes TimeGAN piorou a vazão
d_all = [r['real_timegan']['flow_MAE'] - r['real']['flow_MAE'] for x in R for r in x['runs']]
k, n = sum(x > 0 for x in d_all), len(d_all)
p = sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
out['sign_test_timegan_worse_flow'] = dict(worse=k, n=n, p_one_sided=p)
sc = [s for x in R for s in x['scenario_absent']]
for m in ('hw_MAE_real', 'hw_MAE_real_timegan', 'hw_MAE_real_simpleaug', 'hw_MAE_full_real'):
    out['scenario'][m] = ms([s[m] for s in sc])
json.dump(out, open(f'{D}/server_recomputed.json', 'w'), indent=1)
# figura: curva de aprendizado (vazão) + teto
plt.rcParams.update({'font.size': 8, 'font.family': 'serif'})
fig, ax = plt.subplots(figsize=(3.5, 2.3))
lab = {'real': 'Real fraction only', 'real_timegan': 'Real + TimeGAN (audited)', 'real_simpleaug': 'Real + simple augmentation'}
for c, mk in [('real', 'o'), ('real_timegan', 's'), ('real_simpleaug', '^')]:
    y = [out['by_frac'][f][c]['flow_MAE'] for f in fracs]
    ax.errorbar([100 * f for f in fracs], [a for a, b in y], yerr=[b for a, b in y], marker=mk, capsize=2, label=lab[c])
ax.axhline(out['upper']['flow_MAE'], color='k', ls='--', lw=1, label='100 % real (ceiling)')
ax.set_xlabel('Real training data used (%)'); ax.set_ylabel('Fuel-flow MAE (mL/min)'); ax.set_xticks([10, 25, 50])
ax.legend(fontsize=6); ax.grid(alpha=0.3); plt.tight_layout()
plt.savefig('../../Figures/generated/data_reduction_flow.pdf')
print(json.dumps({k: out[k] for k in ('n_seeds', 'sign_test_timegan_worse_flow', 'ref_maf_pump')}, indent=1))
for f in fracs:
    b = out['by_frac'][f]
    print(f, {c: tuple(round(v, 3) for v in b[c]['flow_MAE']) for c in C}, 'litros', {c: tuple(round(v, 3) for v in b[c]['litres_MAE']) for c in C})
print('upper', out['upper']['flow_MAE'], out['upper']['litres_MAE'])
print('scenario', {k: tuple(round(v, 3) for v in x) for k, x in out['scenario'].items()})
print('discr', {f: round(out['by_frac'][f]['discr_timegan'][0], 4) for f in fracs}, 'audit', {f: round(out['by_frac'][f]['audit_all'][0], 3) for f in fracs})
