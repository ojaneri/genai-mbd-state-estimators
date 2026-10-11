#!/usr/bin/env python3
"""Resumo do portão de utilidade por domínio (artigo, Sec. V-F): escolhas, arrependimento vs oráculo, comparação com o
melhor método fixo e com só-real, tamanho da validação interna. Rodar da raiz do repositório; usa os jobs que existirem."""
import json, os, numpy as np
B = 'experiments/data_reduction/desktop_results/'
JOBS = [('Vehicle 1', 'J026/J026_auto_opel'), ('Vehicle 2', 'J036/J036_ita_auto'), ('Cell SOC', 'J027/J027_auto_bat'),
        ('BESS SOC', 'J034b/J034b_bessauto'), ('BESS temp.', 'J037/J037_besstemp_auto')]
GROUP = {'real': 'real only', 'physonly': 'physics only', 'hyb_feat_real': 'physics input, real only',
         'gen_rfill_w0.3': 'DDPM', 'genphys_rfill_w0.3': 'DDPM, physics labels', 'hyb_resid_w0.3': 'physics + DDPM residual', 'hyb_feat_w0.3': 'physics input + DDPM'}
SYN = {'gen_rfill_w0.3', 'genphys_rfill_w0.3', 'hyb_resid_w0.3', 'hyb_feat_w0.3'}
for dom, j in JOBS:
    if not os.path.exists(B + j + '/results.json'): print(f'{dom}: (ainda não rodou)'); continue
    rs = json.load(open(B + j + '/results.json'))['runs']; ch = {}
    reg, vsfix, vsreal, nval, syn_ch = [], [], [], [], 0
    cands = [k for k in GROUP if all(k in r['v'] for r in rs)]
    fixed_best = {}
    for f in sorted({r['frac'] for r in rs}):
        R = [r for r in rs if r['frac'] == f]
        fixed_best[f] = min(cands, key=lambda k: np.mean([r['v'][k]['flow_MAE'] for r in R]))
    for r in rs:
        c = r['auto_choice']; ch[GROUP[c]] = ch.get(GROUP[c], 0) + 1; syn_ch += c in SYN
        a = r['auto_test_MAE']; orc = min(r['v'][k]['flow_MAE'] for k in cands); fb = r['v'][fixed_best[r['frac']]]['flow_MAE']
        reg.append(100 * (a / orc - 1)); vsfix.append(100 * (a / fb - 1)); vsreal.append(100 * (a / r['v']['real']['flow_MAE'] - 1)); nval.append(r.get('n_val', 0))
    print(f"{dom}: n={len(rs)} | escolheu sintético em {syn_ch}/{len(rs)} | escolhas {dict(sorted(ch.items(), key=lambda x: -x[1]))}")
    print(f"   vs só-real: média {np.mean(vsreal):+.1f} %, pior caso {max(vsreal):+.1f} % | arrependimento vs oráculo: mediana {np.median(reg):.1f} %, máx {max(reg):.1f} %"
          f" | vs melhor método fixo (escolhido no teste): média {np.mean(vsfix):+.1f} % | validação interna {min(nval)}–{max(nval)} janelas")
