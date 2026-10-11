#!/usr/bin/env python3
"""Figuras e tabelas de evidência do artigo (OJVT, Sec. V), todas a partir dos results.json. Rodar da raiz do repositório:
  python experiments/data_reduction/tools/paper_figs.py <pasta_saida>
Gera: seed_paired.pdf, battery_curves.pdf, gate_choices.pdf, fid_util.pdf e imprime as tabelas LaTeX (estatística, auditoria).
Paleta categórica validada (dataviz validate_palette.js, modo claro): cores fixas por entidade + marcadores (contraste < 3:1)."""
import json, os, sys, numpy as np
from scipy import stats
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42, 'font.family': 'serif', 'font.size': 7, 'axes.linewidth': 0.6,
                     'axes.spines.top': False, 'axes.spines.right': False, 'axes.edgecolor': '#555', 'xtick.color': '#444', 'ytick.color': '#444'})
B = 'experiments/data_reduction/desktop_results/'; OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
L = lambda p: json.load(open(B + p + '/results.json'))['runs'] if os.path.exists(B + p + '/results.json') else None
FR = [0.01, 0.02, 0.05, 0.1]; GRID = '#e6e6e3'; INK = '#333'
DOMS = [  # (rótulo, cor, marcador, job DDPM, job portão, escala)
 ('Vehicle 1 fuel flow', '#2a78d6', 'o', 'J012/J012', 'J026/J026_auto_opel', 1),
 ('Vehicle 2 fuel flow', '#eb6834', 's', 'J013/J013', 'J036/J036_ita_auto', 1),
 ('Cell SOC (lab)', '#1baf7a', '^', 'J020b/J020b', 'J027/J027_auto_bat', 100),
 ('BESS SOC (field)', '#eda100', 'D', 'J032b/J032b_bess', 'J034b/J034b_bessauto', 100),
 ('BESS cell temp. (field)', '#e87ba4', 'v', 'J035c/J035c_besstemp', 'J037/J037_besstemp_auto', 1)]
def at(rs, f): return sorted([r for r in rs if abs(r['frac'] - f) < 1e-9], key=lambda r: r['seed'])
def val(r, k): return r['auto_test_MAE'] if k == 'auto' else r['v'][k]['flow_MAE']
def pct(rs, k, f): R = at(rs, f); return np.array([100 * (val(r, k) / r['v']['real']['flow_MAE'] - 1) for r in R])
def style(ax):
    ax.grid(axis='y', color=GRID, lw=0.5); ax.set_axisbelow(True); ax.tick_params(length=2, width=0.5)
# ---------- F1: diferenças pareadas por semente
fig, axs = plt.subplots(1, 5, figsize=(7.16, 1.85), sharey=False)
for ax, (lab, c, mk, jd, jg, sc) in zip(axs, DOMS):
    rd, rg = L(jd), L(jg)
    for i, f in enumerate(FR):
        y = pct(rd, 'gen_rfill_w0.3', f); ax.scatter(np.full(len(y), i - 0.14) + np.linspace(-0.05, 0.05, len(y)), y, s=9, c=c, marker=mk, lw=0, label='DDPM' if i == 0 else None)
        if rg:
            g = pct(rg, 'auto', f); ax.scatter(np.full(len(g), i + 0.14) + np.linspace(-0.05, 0.05, len(g)), g, s=9, facecolors='none', edgecolors=c, marker=mk, lw=0.7, label='Utility gate' if i == 0 else None)
    ax.axhline(0, color=INK, lw=0.6); style(ax); ax.set_xticks(range(4)); ax.set_xticklabels(['1', '2', '5', '10'])
    ax.set_title(lab, fontsize=6.5, color=INK); ax.set_xlabel('Real data (%)', fontsize=6.5)
axs[0].set_ylabel('Change vs. real only (%)', fontsize=6.5)
from matplotlib.lines import Line2D
fig.legend(handles=[Line2D([], [], ls='', marker='o', color='#555', ms=3.5, label='Real + DDPM (filled)'), Line2D([], [], ls='', marker='o', mfc='none', mec='#555', ms=3.5, label='Utility gate (hollow)')],
           loc='lower center', ncol=2, fontsize=6, frameon=False)
plt.tight_layout(w_pad=0.6, rect=(0, 0.08, 1, 1)); plt.savefig(f'{OUT}/seed_paired.pdf'); plt.close()
# ---------- F2: curvas das baterias com todos os candidatos principais
CANDS = [('Real only', '#555555', 'o', 'real'), ('DDPM', '#2a78d6', 's', 'gen_rfill_w0.3'), ('Bootstrap', '#eb6834', 'x', 'boot'),
         ('Physics', '#1baf7a', '^', 'physonly'), ('Physics + DDPM residual', '#eda100', 'D', 'hyb_resid_w0.3'), ('Physics input + DDPM', '#e87ba4', 'v', 'hyb_feat_w0.3')]
BAT = [('Cell SOC (pp)', 100, {'main': 'J020b/J020b', 'boot': 'J021/J021_boot', 'hyb': 'J023/J023_bat'}),
       ('BESS SOC (pp)', 100, {'main': 'J032b/J032b_bess', 'boot': 'J033b/J033b_bessboot', 'hyb': 'J032b/J032b_bess'}),
       ('BESS cell temperature ($^\\circ$C)', 1, {'main': 'J035c/J035c_besstemp', 'boot': 'J040/J040_besstemp_boot', 'hyb': 'J035c/J035c_besstemp'})]
fig, axs = plt.subplots(1, 3, figsize=(7.16, 2.0))
for ax, (lab, sc, J) in zip(axs, BAT):
    for name, c, mk, k in CANDS:
        rs = L(J['boot']) if k == 'boot' else L(J['hyb']) if k.startswith('hyb') else L(J['main']); kk = 'gen_rfill_w0.3' if k == 'boot' else k
        y = [np.mean([val(r, kk) for r in at(rs, f)]) * sc for f in FR]
        ax.plot([f * 100 for f in FR], y, color=c, marker=mk, ms=3.5, lw=1.2, label=name)
    ax.set_xscale('log'); ax.set_xticks([1, 2, 5, 10]); ax.set_xticklabels(['1', '2', '5', '10']); ax.minorticks_off()
    style(ax); ax.set_title(lab, fontsize=7, color=INK); ax.set_xlabel('Real training data (%)', fontsize=6.5)
axs[0].set_ylabel('Test error (mean of 5 seeds)', fontsize=6.5)
h, l = axs[0].get_legend_handles_labels(); fig.legend(h, l, loc='lower center', ncol=6, fontsize=6, frameon=False)
plt.tight_layout(rect=(0, 0.1, 1, 1)); plt.savefig(f'{OUT}/battery_curves.pdf'); plt.close()
# ---------- F3: escolhas do portão
GROUPS = [('No synthetic data', '#9a9a95', {'real', 'physonly', 'hyb_feat_real'}), ('DDPM (alone or physics labels)', '#2a78d6', {'gen_rfill_w0.3', 'genphys_rfill_w0.3'}),
          ('Physics + DDPM residual', '#eda100', {'hyb_resid_w0.3'}), ('Physics input + DDPM', '#e87ba4', {'hyb_feat_w0.3'})]
rows = [(lab, L(jg)) for lab, c, mk, jd, jg, sc in DOMS if L(jg)]
fig, ax = plt.subplots(figsize=(3.45, 0.75 + 0.3 * len(rows)))
for yi, (lab, rs) in enumerate(rows):
    left = 0
    for gname, gc, keys in GROUPS:
        n = sum(r['auto_choice'] in keys for r in rs)
        if n: ax.barh(yi, n, left=left, color=gc, edgecolor='white', lw=1.0, height=0.62); ax.text(left + n / 2, yi, str(n), ha='center', va='center', fontsize=6, color='white' if gc in ('#2a78d6', '#9a9a95') else INK)
        left += n
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.5); ax.invert_yaxis(); ax.set_xlim(0, 20)
ax.set_xlabel('Number of runs (5 seeds, 4 fractions)', fontsize=6.5, labelpad=2); ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=gc, label=g) for g, gc, _ in GROUPS], fontsize=5.5, frameon=False, ncol=2, loc='upper center', bbox_to_anchor=(0.4, -0.42))
plt.subplots_adjust(left=0.27, right=0.98, top=0.97, bottom=0.42); plt.savefig(f'{OUT}/gate_choices.pdf', bbox_inches='tight'); plt.close()
# ---------- F4: fidelidade x utilidade
fig, axs = plt.subplots(1, 2, figsize=(3.45, 1.9), sharey=False)
FRC = {0.01: '#9ec5f4', 0.02: '#5598e7', 0.05: '#256abf', 0.1: '#0d366b'}
for j in ['J012/J012', 'J024/J024_opel', 'J031/J031_ddpm_big', 'J009/J009_A']:
    for r in L(j):
        f = r.get('discr_id_gen', r.get('discr_gen_vs_test')); g = r['v'].get('gen_rfill_w0.3')
        if f is not None and g: axs[0].scatter(f, 100 * (g['flow_MAE'] / r['v']['real']['flow_MAE'] - 1), s=7, color=FRC[r['frac']], lw=0)
for fr, c in FRC.items(): axs[0].scatter([], [], s=7, color=c, label=f'{fr:.0%}')
axs[0].legend(fontsize=5, frameon=False, title='Real data', title_fontsize=5, loc='upper right', handletextpad=0.1, labelspacing=0.2, borderaxespad=0); axs[0].set_title('Vehicle 1', fontsize=7)
for (lab, c, mk, jd, jg, sc), j in zip(DOMS[2:], ['J020b/J020b', 'J032b/J032b_bess', 'J035c/J035c_besstemp']):
    for r in L(j):
        f = r.get('discr_id_dyn_gen'); g = r['v']['gen_rfill_w0.3']
        if f is not None: axs[1].scatter(f, 100 * (g['flow_MAE'] / r['v']['real']['flow_MAE'] - 1), s=8, color=c, marker=mk, lw=0)
    axs[1].scatter([], [], s=8, color=c, marker=mk, label=lab.split(' (')[0])
axs[1].legend(fontsize=5, frameon=False, loc='upper left', handletextpad=0.1, labelspacing=0.2, borderaxespad=0); axs[1].set_title('Battery targets (shape score)', fontsize=7)
for ax in axs: style(ax); ax.axhline(0, color=INK, lw=0.6); ax.set_xlabel('Fidelity score', fontsize=6)
axs[0].set_ylabel('Change vs. real only (%)', fontsize=6.5)
plt.tight_layout(w_pad=0.8); plt.savefig(f'{OUT}/fid_util.pdf'); plt.close()
# ---------- T1: estatística (IC 95 % da mudança média por semente, tamanho de efeito d_z)
print('% T1 stats: target & frac & mean [95% CI] & d_z & p   (DDPM vs real only)')
for lab, c, mk, jd, jg, sc in DOMS:
    for f in FR:
        R = at(L(jd), f); a = np.array([r['v']['gen_rfill_w0.3']['flow_MAE'] for r in R]); b = np.array([r['v']['real']['flow_MAE'] for r in R])
        d = 100 * (a / b - 1); m, se = d.mean(), d.std(ddof=1) / np.sqrt(len(d)); h = se * stats.t.ppf(0.975, len(d) - 1)
        dz = (a - b).mean() / (a - b).std(ddof=1); p = stats.ttest_rel(a, b).pvalue
        print(f'{lab} & {f:.0%} & ${m:+.1f}$ [${m-h:+.1f}$, ${m+h:+.1f}$] & ${dz:+.2f}$ & {p:.3g} \\\\')
# ---------- T2: auditoria por nível (média das rodadas), sintético / real
print('% T2 audit tiers: target & tier1..5 synthetic/real & overall')
for lab, j in [('Vehicle 1', 'J024/J024_opel'), ('Vehicle 2', 'J025/J025_ita'), ('Cell SOC', 'J020b/J020b'), ('BESS SOC', 'J032b/J032b_bess'), ('BESS cell temp.', 'J035c/J035c_besstemp')]:
    rs = L(j); s = np.mean([r['audit_tiers'] for r in rs], 0) * 100; q = np.mean([r['audit_tiers_real'] for r in rs], 0) * 100
    ov = np.mean([r['audit_pass'] for r in rs]) * 100; ovr = np.mean([r['audit_pass_real'] for r in rs]) * 100
    print(lab + ' & ' + ' & '.join(f'{x:.1f} / {y:.1f}' for x, y in zip(s, q)) + f' & {ov:.1f} / {ovr:.1f} \\\\')
print('ok', OUT)
# ---------- T3: equivalência de dados (d-0032): fração real que iguala o erro de real + DDPM
def _curve(jobs, var):
    pts = {}
    for j in jobs:
        for r in (L(j) or []):
            if var in r['v']: pts.setdefault(r['frac'], []).append(r['v'][var]['flow_MAE'])
    return {f: np.mean(v) for f, v in pts.items()}
def _equiv(real, target):
    fs = sorted(real)
    for a, b in zip(fs[:-1], fs[1:]):
        if real[a] >= target >= real[b]:
            w = (real[a] - target) / (real[a] - real[b]); return float(np.exp(np.log(a) + w * (np.log(b) - np.log(a))))
    return None
print('% T3 equivalence: target & per fraction "equivalent real fraction (factor)"')
for lab, jobs in [('Vehicle 1', ['J009/J009_A', 'J016/J016_curva']), ('Vehicle 2', ['J013/J013']), ('Cell SOC', ['J020b/J020b', 'J041/J041_cell_long']),
                  ('BESS SOC', ['J032b/J032b_bess', 'J042/J042_bess_long']), ('BESS cell temp.', ['J035c/J035c_besstemp'])]:
    real, gen = _curve(jobs, 'real'), _curve(jobs, 'gen_rfill_w0.3'); cells = []
    for f in FR:
        e = _equiv(real, gen[f]) if f in gen else None
        cells.append('%.1f\\%% ($\\times$%.1f)' % (100 * e, e / f) if e else ('$>$%.0f\\%%' % (100 * max(real)) if gen.get(f, 1e9) < min(real.values()) else '$<$%.0f\\%%' % (100 * min(real))))
    print(lab + ' & ' + ' & '.join(cells) + ' \\\\')
# ---------- T4: distância até o modelo com todos os dados (teto = só-real HGB com 100 % do pool, uma rodada por job)
NAMES = {'real': 'real only', 'physonly': 'physics', 'gen_rfill_w0.3': 'DDPM', 'genphys_rfill_w0.3': 'DDPM, physics labels', 'hyb_resid_w0.3': 'physics + DDPM residual',
         'hyb_feat_real': 'physics input, real only', 'hyb_feat_w0.3': 'physics input + DDPM', 'aug_rfill_w0.3': 'simple augmentation'}
print('% T4 gap: target & frac & real & DDPM (gap closed) & best candidate (gap closed) & ceiling')
for lab, jm, jh, sc, nd in [('Cell SOC', 'J020b/J020b', 'J023/J023_bat', 100, 2), ('BESS SOC', 'J032b/J032b_bess', 'J032b/J032b_bess', 100, 2), ('BESS cell temp.', 'J035c/J035c_besstemp', 'J035c/J035c_besstemp', 1, 3)]:
    D = json.load(open(B + jm + '/results.json')); ub = D['upper_bound_100pct_real']['flow_MAE'] * sc; H = L(jh)
    for f in FR:
        R, RH = at(D['runs'], f), at(H, f); re_ = np.mean([r['v']['real']['flow_MAE'] for r in R]) * sc
        g = np.mean([r['v']['gen_rfill_w0.3']['flow_MAE'] for r in R]) * sc
        k, b = min(((k, np.mean([r['v'][k]['flow_MAE'] for r in RH]) * sc) for k in RH[0]['v']), key=lambda x: x[1])
        gc = lambda x: 100 * (re_ - x) / (re_ - ub)
        print(f"{lab} & {f:.0%} & {re_:.{nd}f} & {g:.{nd}f} ({gc(g):.0f}\\%) & {NAMES[k]}: {b:.{nd}f} ({gc(b):.0f}\\%) & {ub:.{nd}f} \\\\")
# ---------- T5: detecção por canal e amostras repetidas (média de todas as rodadas do job DDPM)
print('% T5 channels: target & per-channel score synthetic/real-train & repeated-sample fraction real/synthetic')
for lab, j in [('Cell SOC', 'J020b/J020b'), ('BESS SOC', 'J032b/J032b_bess'), ('BESS cell temp.', 'J035c/J035c_besstemp')]:
    rs = L(j); chs = list(rs[0]['discr_channels_gen'])
    sg = {c: np.mean([r['discr_channels_gen'][c] for r in rs]) for c in chs}; sr = {c: np.mean([r['discr_channels_realtrain'][c] for r in rs]) for c in chs}
    rr = np.mean([r['repeat_frac_real'] for r in rs], 0); rgn = np.mean([r['repeat_frac_gen'] for r in rs], 0)
    print(lab + ' & ' + '; '.join(f'{c}: {sg[c]:.2f}/{sr[c]:.2f}' for c in chs) + ' & ' + '; '.join(f'{c}: {100*a:.0f}/{100*b:.0f}\\%' for c, a, b in zip(chs, rr, rgn)) + ' \\\\')
