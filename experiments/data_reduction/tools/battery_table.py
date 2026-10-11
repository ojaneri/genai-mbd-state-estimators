#!/usr/bin/env python3
"""Tabela do artigo (Sec. V-D/V-E): erro absoluto no teste de cada candidato, célula SOC, BESS SOC e BESS temperatura,
média de 5 sementes (0–4) por fração. Imprime linhas LaTeX. Rodar da raiz do repositório."""
import json, numpy as np
B = 'experiments/data_reduction/desktop_results/'
L = lambda p: json.load(open(B + p + '/results.json'))['runs']
FR = [0.01, 0.02, 0.05, 0.1]
DOM = {  # (escala, {linha: (job, variante)})
 'cell': (100, {'Real only': ('J020b/J020b', 'real'), 'Simple augmentation': ('J020b/J020b', 'aug_rfill_w0.3'), 'Bootstrap': ('J021/J021_boot', 'gen_rfill_w0.3'),
          'DDPM': ('J020b/J020b', 'gen_rfill_w0.3'), 'DDPM, physics labels': ('J020b/J020b', 'genphys_rfill_w0.3'), 'Physics': ('J020b/J020b', 'physonly'),
          'Physics + DDPM residual': ('J023/J023_bat', 'hyb_resid_w0.3'), 'Physics input, real only': ('J023/J023_bat', 'hyb_feat_real'), 'Physics input + DDPM': ('J023/J023_bat', 'hyb_feat_w0.3')}),
 'bess': (100, {'Real only': ('J032b/J032b_bess', 'real'), 'Simple augmentation': ('J032b/J032b_bess', 'aug_rfill_w0.3'), 'Bootstrap': ('J033b/J033b_bessboot', 'gen_rfill_w0.3'),
          'DDPM': ('J032b/J032b_bess', 'gen_rfill_w0.3'), 'DDPM, physics labels': ('J032b/J032b_bess', 'genphys_rfill_w0.3'), 'Physics': ('J032b/J032b_bess', 'physonly'),
          'Physics + DDPM residual': ('J032b/J032b_bess', 'hyb_resid_w0.3'), 'Physics input, real only': ('J032b/J032b_bess', 'hyb_feat_real'), 'Physics input + DDPM': ('J032b/J032b_bess', 'hyb_feat_w0.3')}),
 'btemp': (1, {'Real only': ('J035c/J035c_besstemp', 'real'), 'Simple augmentation': ('J035c/J035c_besstemp', 'aug_rfill_w0.3'), 'Bootstrap': ('J040/J040_besstemp_boot', 'gen_rfill_w0.3'),
          'DDPM': ('J035c/J035c_besstemp', 'gen_rfill_w0.3'), 'DDPM, physics labels': ('J035c/J035c_besstemp', 'genphys_rfill_w0.3'), 'Physics': ('J035c/J035c_besstemp', 'physonly'),
          'Physics + DDPM residual': ('J035c/J035c_besstemp', 'hyb_resid_w0.3'), 'Physics input, real only': ('J035c/J035c_besstemp', 'hyb_feat_real'), 'Physics input + DDPM': ('J035c/J035c_besstemp', 'hyb_feat_w0.3')}),
}
vals = {}
for d, (sc, rows) in DOM.items():
    for lab, (job, var) in rows.items():
        rs = L(job); vals[(d, lab)] = [np.mean([r['v'][var]['flow_MAE'] for r in rs if abs(r['frac'] - f) < 1e-9 and r['seed'] in range(5)]) * sc for f in FR]
        assert sorted(r['seed'] for r in rs if abs(r['frac'] - 0.01) < 1e-9) == [0, 1, 2, 3, 4], job
for lab in DOM['cell'][1]:
    cells = []
    for d, nd in (('cell', 2), ('bess', 2), ('btemp', 3)):
        col = [vals[(d, l)] for l in DOM[d][1]]; best = [min(c[i] for c in col) for i in range(4)]
        cells += [('\\textbf{%.*f}' if abs(v - best[i]) < 1e-12 else '%.*f') % (nd, v) for i, v in enumerate(vals[(d, lab)])]
    print(lab, '&', ' & '.join(cells), '\\\\')
