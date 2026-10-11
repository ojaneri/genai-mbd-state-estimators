#!/usr/bin/env python3
"""Validação do framework por redução de dados (decisão d-0005), caso A com dados públicos.

Tarefa: sensor virtual de vazão de combustível no Opel Corsa 2012 (Kaggle pedro2025, CC BY 4.0).
Entradas do modelo: velocidade, RPM, borboleta (sem MAF e sem carga, que é derivada do MAF). Alvo:
vazão calculada pelo MAF com correção de trim (REAL_FUEL_USAGE_ML_MIN). Verdade física: litros da bomba por tanque (refueling_history.csv, linha k =
segmento k do log).

Protocolo: teste reservado = tanques 18–22 (últimos no tempo, nunca vistos). Do restante (1–17),
treino = tanques 8–17 (onde há vazão corrigida); frações de viagens f ∈ {0.1, 0.25, 0.5, 1.0}. Condições por fração: real; real + TimeGAN auditado;
real + aumento simples; e 100 % real como teto. 3 sementes. Mais: fidelidade (discriminative score,
TSTR) e cenário ausente (sem rodovia >80 km/h no treino, teste só em rodovia).

Uso: python3 run.py <pasta_opel> <pasta_saida> [--quick]
"""
import os, sys, json, time
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from timegan import TimeGAN
import torch; torch.set_num_threads(int(os.environ.get("OMP_NUM_THREADS", "2")))

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
QUICK = '--quick' in sys.argv
FEAT = ['SPEED', 'RPM', 'THROTTLE_POS']; TGT = 'REAL_FUEL_USAGE_ML_MIN'   # ENGINE_LOAD excluída: é derivada do MAF (vazamento)
VAL = '--val' in sys.argv   # ajuste de hiperparâmetros: valida em 15–17, treina em 8–14; o teste 18–22 fica intocado
POOL_SEGS = list(range(8, 18))   # vazão com correção de trim só existe a partir do segmento 8
CH = FEAT + [TGT]
L, STRIDE = 24, 4
TEST_SEGS = [18, 19, 20, 21, 22]
if VAL:
    TEST_SEGS, POOL_SEGS = [15, 16, 17], list(range(8, 15))
FRACS = [float(x) for x in (sys.argv[sys.argv.index('--fracs') + 1].split(',') if '--fracs' in sys.argv else ['0.1', '0.25', '0.5'])] + [1.0]
def _arg(k, d):
    return type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
SEEDS = [_arg('--seed', 0)] if '--seed' in sys.argv else ([0, 1, 2] if not QUICK else [0])
ITERS = _arg('--iters', 2000 if not QUICK else 200)
HIDDEN = _arg('--hidden', 24)
SCENARIO = '--no-scenario' not in sys.argv
t0 = time.time()

# ------------------------------------------------------------------ dados
df = pd.read_csv(f'{SRC}/dataset.csv', usecols=['timestamp', 'segment_id', 'segment_file'] + CH, parse_dates=['timestamp'])
df.loc[df.SPEED > 200, 'SPEED'] = np.nan                       # 255 = inválido no OBD
df = df.sort_values('timestamp')
df[CH] = df.groupby('segment_file')[CH].transform(lambda s: s.ffill().bfill())
df = df[df.segment_id.isin(POOL_SEGS + TEST_SEGS)].dropna(subset=CH)
df['dt'] = df.groupby('segment_file').timestamp.diff().dt.total_seconds().fillna(0).clip(0, 5)
pump = pd.read_csv(f'{SRC}/refueling_history.csv').set_index('Lp')['Refueling']   # linha k = segmento k
lo, hi = df[CH].quantile(0.001).values, df[CH].quantile(0.999).values
def scale(a): return np.clip((a - lo) / (hi - lo), 0, 1)
def unscale(a): return a * (hi - lo) + lo

trips = {f: g for f, g in df.groupby('segment_file')}
pool = sorted(f for f, g in trips.items() if g.segment_id.iloc[0] in POOL_SEGS)
test = sorted(f for f, g in trips.items() if g.segment_id.iloc[0] in TEST_SEGS)

def windows(files, stride=STRIDE, mask_hw=False):
    W = []
    for f in files:
        a = scale(trips[f][CH].values)
        for i in range(0, len(a) - L + 1, stride):
            w = a[i:i + L]
            if mask_hw and unscale(w)[:, 0].max() > 80: continue
            W.append(w)
    return np.array(W, dtype=np.float32).reshape(-1, L, len(CH))

def feats(W):  # W escalado (n, L, 5); usa só os 4 canais de entrada
    x = W[:, :, :3]
    return np.concatenate([x[:, -8:, :].reshape(len(x), -1), x.mean(1), x.std(1), x[:, -1] - x[:, -9]], 1)

# ------------------------------------------------------------------ auditoria física (portão)
q = df[CH]; dsp = df.groupby('segment_file').SPEED.diff().abs(); drp = df.groupby('segment_file').RPM.diff().abs()
idle = df[(df.SPEED < 1) & (df.RPM.between(600, 1100))][TGT]
LIM = dict(dspeed=float(dsp.quantile(0.999)), drpm=float(drp.quantile(0.999)),
           idle_lo=float(idle.quantile(0.01)), idle_hi=float(idle.quantile(0.99)),
           ratio_hi=float((q[TGT] / (q.RPM + 1)).quantile(0.999)))
def audit(Wsc):
    W = unscale(Wsc); sp, rpm, th, fl = [W[:, :, i] for i in range(4)]
    t1 = (sp >= 0).all(1) & (sp <= 200).all(1) & (rpm >= 0).all(1) & (rpm <= 6500).all(1) & (fl >= 0).all(1)
    t2 = ~((rpm < 400) & (fl > 2)).any(1)                                            # motor desligado → sem vazão
    idl = (sp < 1) & (rpm > 600) & (rpm < 1100)
    t3 = ~(idl & ((fl < LIM['idle_lo']) | (fl > LIM['idle_hi']))).any(1)           # marcha lenta coerente
    t4 = (np.abs(np.diff(sp, axis=1)) <= LIM['dspeed']).all(1) & (np.abs(np.diff(rpm, axis=1)) <= LIM['drpm']).all(1)
    t5 = (fl / (rpm + 1) <= LIM['ratio_hi']).all(1)                                  # vazão coerente com RPM
    ok = t1 & t2 & t3 & t4 & t5
    return ok, dict(t1=float(t1.mean()), t2=float(t2.mean()), t3=float(t3.mean()), t4=float(t4.mean()), t5=float(t5.mean()), all=float(ok.mean()))

def simple_aug(W, n, rng):
    idx = rng.integers(0, len(W), n); A = W[idx].copy()
    A = A * rng.uniform(0.9, 1.1, (n, 1, A.shape[2])) + rng.normal(0, 0.03, A.shape)
    return np.clip(A, 0, 1).astype(np.float32)

# ------------------------------------------------------------------ avaliação no teste reservado
Xtest_rows = []
for f in test:
    a = scale(trips[f][CH].values); pad = np.repeat(a[:1], L - 1, 0); a2 = np.vstack([pad, a])
    Xtest_rows.append((f, np.lib.stride_tricks.sliding_window_view(a2, (L, len(CH))).reshape(-1, L, len(CH))))
def evaluate(model):
    errs, seg_l = [], {}
    for f, Wt in Xtest_rows:
        pred = np.clip(unscale(np.c_[np.zeros((len(Wt), 3)), model.predict(feats(Wt))])[:, 3], 0, None)
        g = trips[f]; errs.append(np.abs(pred - g[TGT].values))
        sid = int(g.segment_id.iloc[0]); seg_l[sid] = seg_l.get(sid, 0) + (pred * g.dt.values / 60).sum() / 1000
    e = np.concatenate(errs)
    lit = {s: (seg_l[s], float(pump[s])) for s in seg_l}
    return dict(flow_MAE=float(e.mean()), litres_MAE=float(np.mean([abs(a - b) for a, b in lit.values()])),
                litres=({s: round(a, 2) for s, (a, b) in lit.items()}))
def fit(W):
    m = HistGradientBoostingRegressor(max_iter=300, random_state=0)
    return m.fit(feats(W), W[:, -1, 3])

ref = {}
for f in test:
    g = trips[f]; s = int(g.segment_id.iloc[0]); ref[s] = ref.get(s, 0) + (g[TGT] * g.dt / 60).sum() / 1000
res = dict(meta=dict(mode='validation' if VAL else 'test', test_segments=TEST_SEGS, pool_trips=len(pool), test_trips=len(test), window=L, stride=STRIDE,
                     iters=ITERS, hidden=HIDDEN, seeds=SEEDS, audit_limits=LIM,
                     torch=torch.__version__, cuda=torch.cuda.is_available(),
                     gpu=torch.cuda.get_device_name(0) if torch.cuda.is_available() else None),
           reference_MAF_vs_pump=dict(litres_MAE=float(np.mean([abs(ref[s] - pump[s]) for s in ref])),
                                      per_segment={s: (round(ref[s], 2), float(pump[s])) for s in ref}),
           runs=[])
Wfull = windows(pool)
print('janelas pool', Wfull.shape, 'viagens teste', len(test), f'{time.time()-t0:.0f}s', flush=True)
full_eval = evaluate(fit(Wfull))
res['upper_bound_100pct_real'] = full_eval
print('100% real', full_eval, flush=True)

def discr(real_test_W, syn, seed):
    n = min(len(real_test_W), len(syn), 4000); r = np.random.default_rng(seed)
    a = real_test_W[r.choice(len(real_test_W), n, replace=False)]; b = syn[r.choice(len(syn), n, replace=False)]
    X = np.r_[a.reshape(n, -1), b.reshape(n, -1)]; y = np.r_[np.zeros(n), np.ones(n)]
    acc = cross_val_score(HistGradientBoostingClassifier(max_iter=200), X, y, cv=5).mean()
    return float(abs(acc - 0.5))
Wtest = windows(test)

for seed in SEEDS:
    rng = np.random.default_rng(seed)
    for frac in FRACS[:-1]:
        files = list(rng.choice(pool, max(1, int(round(frac * len(pool)))), replace=False))
        Wr = windows(files); n_fill = max(0, len(Wfull) - len(Wr))
        tg = TimeGAN(len(CH), hidden=HIDDEN, seed=seed).fit(Wr, iters=ITERS)
        syn = tg.sample(int(n_fill * 1.6) + 1000, L); ok, aud = audit(syn); syn_ok = syn[ok][:n_fill]
        aug = simple_aug(Wr, n_fill, rng)
        run = dict(seed=seed, frac=frac, n_real=len(Wr), n_fill=n_fill, n_syn_audited=len(syn_ok), audit=aud, tg_log=tg.log,
                   real=evaluate(fit(Wr)),
                   real_timegan=evaluate(fit(np.r_[Wr, syn_ok])) if len(syn_ok) else None,
                   real_timegan_noaudit=evaluate(fit(np.r_[Wr, syn[:n_fill]])),
                   real_simpleaug=evaluate(fit(np.r_[Wr, aug])),
                   tstr_timegan=evaluate(fit(syn_ok)) if len(syn_ok) > 100 else None,
                   discr_timegan=discr(Wtest, syn_ok, seed) if len(syn_ok) > 100 else None,
                   discr_simpleaug=discr(Wtest, aug, seed), discr_real_train=discr(Wtest, Wr, seed))
        res['runs'].append(run)
        print(seed, frac, {k: (run[k]['litres_MAE'] if isinstance(run[k], dict) and 'litres_MAE' in run[k] else run[k])
                           for k in ['real', 'real_timegan', 'real_simpleaug']}, 'audit', round(aud['all'], 3), f'{time.time()-t0:.0f}s', flush=True)
        json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)

# ------------------------------------------------------------------ cenário ausente (sem rodovia no treino)
hw_test = [(f, W) for f, W in Xtest_rows]
def eval_hw(model):
    e = []
    for f, Wt in Xtest_rows:
        m = unscale(Wt)[:, -1, 0] > 80
        if m.sum() == 0: continue
        pred = np.clip(unscale(np.c_[np.zeros((m.sum(), 3)), model.predict(feats(Wt[m]))])[:, 3], 0, None)
        e.append(np.abs(pred - trips[f][TGT].values[m]))
    return float(np.concatenate(e).mean())
res['scenario_absent'] = []
for seed in (SEEDS if SCENARIO else []):
    rng = np.random.default_rng(100 + seed)
    files = list(rng.choice(pool, int(round(0.25 * len(pool))), replace=False))
    Wn = windows(files, mask_hw=True); n_fill = max(0, len(Wfull) - len(Wn))
    tg = TimeGAN(len(CH), hidden=HIDDEN, seed=seed).fit(Wn, iters=ITERS)
    syn = tg.sample(int(n_fill * 1.6) + 1000, L); ok, aud = audit(syn); syn_ok = syn[ok][:n_fill]
    sc = dict(seed=seed, n_real_no_hw=len(Wn), syn_max_speed=float(unscale(syn_ok)[:, :, 0].max()) if len(syn_ok) else None,
              hw_MAE_real=eval_hw(fit(Wn)), hw_MAE_real_timegan=eval_hw(fit(np.r_[Wn, syn_ok])),
              hw_MAE_real_simpleaug=eval_hw(fit(np.r_[Wn, simple_aug(Wn, n_fill, rng)])), hw_MAE_full_real=eval_hw(fit(Wfull)))
    res['scenario_absent'].append(sc); print('cenário ausente', sc, flush=True)
    json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)
res['meta']['runtime_s'] = time.time() - t0
json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)
print('fim', f'{time.time()-t0:.0f}s')
