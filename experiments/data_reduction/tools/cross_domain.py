#!/usr/bin/env python3
"""Tabela e figura entre domínios (artigo, Sec. de validação do estágio generativo).
Cada Δ é relativo ao só-real DO MESMO job (mesmas sementes e mesmos dados); fontes por linha em SRC.
Uso: python cross_domain.py <saida_fig.pdf>  (rodar da raiz do repositório)."""
import json, os, sys, numpy as np
B = 'experiments/data_reduction/desktop_results/'
L = lambda p: json.load(open(B + p))['runs']
FR = [0.01, 0.02, 0.05, 0.1]
# domínio: (unidade, escala, {coluna: (job, variante)}); 'auto' = portão de utilidade
SRC = {
 'Vehicle 1 fuel flow':  ('mL/min', 1,   {'real': ('J012/J012', 'real'), 'ddpm': ('J012/J012', 'gen_rfill_w0.3'),
                          'boot': ('J014/J014_boot', 'gen_rfill_w0.3'), 'phys': ('J012/J012', 'physonly'),
                          'hyb': ('J024/J024_opel', 'hyb_resid_w0.3'), 'auto': ('J026/J026_auto_opel', 'auto')}),
 'Vehicle 2 fuel flow':  ('cc/min', 1,   {'real': ('J013/J013', 'real'), 'ddpm': ('J013/J013', 'gen_rfill_w0.3'),
                          'boot': ('J039/J039_ita_boot', 'gen_rfill_w0.3'), 'phys': ('J013/J013', 'physonly'), 'hyb': ('J025/J025_ita', 'hyb_resid_w0.3'),
                          'auto': ('J036/J036_ita_auto', 'auto')}),
 'Cell SOC (lab)':       ('pp', 100,     {'real': ('J020b/J020b', 'real'), 'ddpm': ('J020b/J020b', 'gen_rfill_w0.3'),
                          'boot': ('J021/J021_boot', 'gen_rfill_w0.3'), 'phys': ('J020b/J020b', 'physonly'),
                          'hyb': ('J023/J023_bat', 'hyb_resid_w0.3'), 'auto': ('J027/J027_auto_bat', 'auto')}),
 'BESS SOC (field)':     ('pp', 100,     {'real': ('J032b/J032b_bess', 'real'), 'ddpm': ('J032b/J032b_bess', 'gen_rfill_w0.3'),
                          'boot': ('J033b/J033b_bessboot', 'gen_rfill_w0.3'), 'phys': ('J032b/J032b_bess', 'physonly'),
                          'hyb': ('J032b/J032b_bess', 'hyb_resid_w0.3'), 'auto': ('J034b/J034b_bessauto', 'auto')}),
 'BESS cell temp. (field)': ('degC', 1,  {'real': ('J035c/J035c_besstemp', 'real'), 'ddpm': ('J035c/J035c_besstemp', 'gen_rfill_w0.3'),
                          'boot': ('J040/J040_besstemp_boot', 'gen_rfill_w0.3'), 'phys': ('J035c/J035c_besstemp', 'physonly'), 'hyb': ('J035c/J035c_besstemp', 'hyb_resid_w0.3'),
                          'auto': ('J037/J037_besstemp_auto', 'auto')}),
}
def val(r, var): return r['auto_test_MAE'] if var == 'auto' else r['v'][var]['flow_MAE']
out = {}
for dom, (unit, sc, cols) in SRC.items():
    out[dom] = {'unit': unit}
    for c, (job, var) in cols.items():
        if not os.path.exists(B + job + '/results.json'): continue   # job ainda não rodou
        rs = L(job + '/results.json'); row = []
        for f in FR:
            rr = [r for r in rs if abs(r['frac'] - f) < 1e-9]
            if not rr: row.append(None); continue
            m = np.mean([val(r, var) for r in rr]) * sc; base = np.mean([r['v']['real']['flow_MAE'] for r in rr]) * sc
            worse = sum(val(r, var) > r['v']['real']['flow_MAE'] for r in rr)
            row.append({'mean': m, 'base': base, 'delta': 100 * (m / base - 1), 'worse': worse, 'n': len(rr)})
        out[dom][c] = row
    # fidelidade (forma) e auditoria, job DDPM principal
    rs = L(cols['ddpm'][0] + '/results.json')
    g = [r.get('discr_id_dyn_gen') for r in rs if r.get('discr_id_dyn_gen') is not None]
    q = [r.get('discr_id_dyn_real') for r in rs if r.get('discr_id_dyn_real') is not None]
    a = [r['audit_pass'] for r in rs]
    out[dom]['fid'] = {'shape_gen': [min(g), max(g)] if g else None, 'shape_real': [min(q), max(q)] if q else None, 'audit': [min(a), max(a)]}
json.dump(out, open('experiments/data_reduction/cross_domain.json', 'w'), indent=1)
for dom, d in out.items():
    print(dom, d['unit'], 'fid', d['fid'])
    for c in ['real', 'ddpm', 'boot', 'phys', 'hyb', 'auto']:
        if c in d: print('  %-5s' % c, ' '.join('—' if x is None else ('%.3g' % x['mean'] if c == 'real' else '%+.1f%%(%d/%d)' % (x['delta'], x['worse'], x['n'])) for x in d[c]))
if len(sys.argv) > 1:
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    plt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42})   # sem fontes Type 3 (IEEE PDF eXpress)
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 2.3), sharey=True)
    sty = {'Vehicle 1 fuel flow': ('#2a78d6', 'o'), 'Vehicle 2 fuel flow': ('#eb6834', 's'), 'Cell SOC (lab)': ('#1baf7a', '^'), 'BESS SOC (field)': ('#eda100', 'D'), 'BESS cell temp. (field)': ('#e87ba4', 'v')}   # mesmas cores de paper_figs.py
    for ax, c, t in [(axs[0], 'ddpm', 'Real + DDPM windows'), (axs[1], 'auto', 'Utility gate (selected model)')]:
        for dom, d in out.items():
            if c in d: ax.plot([f * 100 for f in FR], [x['delta'] if x else np.nan for x in d[c]], color=sty[dom][0], marker=sty[dom][1], ms=3.5, lw=1.2, label=dom)
        ax.axhline(0, color='k', lw=0.6); ax.set_xscale('log'); ax.set_xticks([1, 2, 5, 10]); ax.set_xticklabels(['1', '2', '5', '10'])
        ax.set_title(t, fontsize=7); ax.set_xlabel('Real training data (%)', fontsize=7); ax.tick_params(labelsize=6)
    axs[0].set_ylabel('Error vs. real only (%)', fontsize=7); axs[0].legend(fontsize=5.5, frameon=False, loc='lower right')
    plt.tight_layout(); plt.savefig(sys.argv[1]); print('ok', sys.argv[1])
