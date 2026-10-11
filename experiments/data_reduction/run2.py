#!/usr/bin/env python3
"""Rodada 2 da validação por redução de dados (caso A público, Opel Corsa) — grade pré-registrada.

Mesma tarefa, divisão e métricas da rodada 1 (run.py): sensor virtual de vazão; entradas velocidade,
RPM, borboleta; alvo REAL_FUEL_USAGE_ML_MIN; treino tanques 8–17; teste 18–22 (ou validação 15–17
com --val, treino 8–14). O gerador é treinado UMA vez por (semente, fração) e o mesmo conjunto
sintético é avaliado em várias variantes:

  real                         só a fração real
  {gen,aug}_r{0.5,1,fill}_w{1,0.3}   sintético do gerador (gen) ou aumento simples (aug), em
                               quantidade 0,5x / 1x da fração real ou até completar o pool (fill),
                               com peso de amostra 1 ou 0,3
  gen_dfilt_q{0.5,0.2}         portão estatístico: classificador real-treino vs sintético; mantém
                               os q mais "reais" (prob. de real mais alta); quantidade 1x, peso 1
  gen_pretrain                 pré-treina no sintético (fill) e continua o treino só no real

Uso: python3 run2.py <pasta_opel> <saida> --gen timegan|timevae --seeds 0,1,2,3,4
     --fracs 0.01,0.02,0.05,0.1 [--iters N] [--hidden H] [--latent L] [--model hgb|mlp] [--val]
     [--variants real,gen_r1_w1,...] [--no-ceiling]
"""
import os, sys, json, time
os.environ.setdefault('OMP_NUM_THREADS', '2')
import numpy as np, pandas as pd
import torch; torch.set_num_threads(int(os.environ['OMP_NUM_THREADS']))
from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score

def arg(k, d, cast=str):
    return cast(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
GEN = arg('--gen', 'timegan'); MODEL = arg('--model', 'hgb')
SEEDS = [int(x) for x in arg('--seeds', '0').split(',')]
FRACS = [float(x) for x in arg('--fracs', '0.01,0.02,0.05,0.1').split(',')]
ITERS = arg('--iters', 6000 if GEN == 'timegan' else 3000, int)
HIDDEN = arg('--hidden', 24 if GEN == 'timegan' else 48, int); LATENT = arg('--latent', 16, int)
VAL = '--val' in sys.argv
ONLY = arg('--variants', None)
FEAT = ['SPEED', 'RPM', 'THROTTLE_POS']; TGT = 'REAL_FUEL_USAGE_ML_MIN'; CH = FEAT + [TGT]
TEST_SEGS, POOL_SEGS = ([15, 16, 17], list(range(8, 15))) if VAL else ([18, 19, 20, 21, 22], list(range(8, 18)))
L, STRIDE = 24, 4
t0 = time.time()

# ------------------------------------------------------------------ dados (idêntico à rodada 1)
df = pd.read_csv(f'{SRC}/dataset.csv', usecols=['timestamp', 'segment_id', 'segment_file'] + CH, parse_dates=['timestamp'])
df.loc[df.SPEED > 200, 'SPEED'] = np.nan
df = df.sort_values('timestamp')
df[CH] = df.groupby('segment_file')[CH].transform(lambda s: s.ffill().bfill())
df = df[df.segment_id.isin(POOL_SEGS + TEST_SEGS)].dropna(subset=CH)
df['dt'] = df.groupby('segment_file').timestamp.diff().dt.total_seconds().fillna(0).clip(0, 5)
pump = pd.read_csv(f'{SRC}/refueling_history.csv').set_index('Lp')['Refueling']
lo, hi = df[CH].quantile(0.001).values, df[CH].quantile(0.999).values
def scale(a): return np.clip((a - lo) / (hi - lo), 0, 1)
def unscale(a): return a * (hi - lo) + lo
trips = {f: g for f, g in df.groupby('segment_file')}
pool = sorted(f for f, g in trips.items() if g.segment_id.iloc[0] in POOL_SEGS)
test = sorted(f for f, g in trips.items() if g.segment_id.iloc[0] in TEST_SEGS)
def windows(files, stride=STRIDE):
    W = []
    for f in files:
        a = scale(trips[f][CH].values)
        for i in range(0, len(a) - L + 1, stride): W.append(a[i:i + L])
    return np.array(W, dtype=np.float32).reshape(-1, L, len(CH))
def feats(W):
    x = W[:, :, :3]
    return np.concatenate([x[:, -8:, :].reshape(len(x), -1), x.mean(1), x.std(1), x[:, -1] - x[:, -9]], 1)

# auditoria física (mesmos 5 níveis da rodada 1)
q = df[CH]; dsp = df.groupby('segment_file').SPEED.diff().abs(); drp = df.groupby('segment_file').RPM.diff().abs()
idle = df[(df.SPEED < 1) & (df.RPM.between(600, 1100))][TGT]
LIM = dict(dspeed=float(dsp.quantile(0.999)), drpm=float(drp.quantile(0.999)), idle_lo=float(idle.quantile(0.01)),
           idle_hi=float(idle.quantile(0.99)), ratio_hi=float((q[TGT] / (q.RPM + 1)).quantile(0.999)))
def audit(Wsc):
    W = unscale(Wsc); sp, rpm, th, fl = [W[:, :, i] for i in range(4)]
    t1 = (sp >= 0).all(1) & (sp <= 200).all(1) & (rpm >= 0).all(1) & (rpm <= 6500).all(1) & (fl >= 0).all(1)
    t2 = ~((rpm < 400) & (fl > 2)).any(1)
    idl = (sp < 1) & (rpm > 600) & (rpm < 1100)
    t3 = ~(idl & ((fl < LIM['idle_lo']) | (fl > LIM['idle_hi']))).any(1)
    t4 = (np.abs(np.diff(sp, axis=1)) <= LIM['dspeed']).all(1) & (np.abs(np.diff(rpm, axis=1)) <= LIM['drpm']).all(1)
    t5 = (fl / (rpm + 1) <= LIM['ratio_hi']).all(1)
    return t1 & t2 & t3 & t4 & t5
def simple_aug(W, n, rng):
    A = W[rng.integers(0, len(W), n)].copy()
    A = A * rng.uniform(0.9, 1.1, (n, 1, A.shape[2])) + rng.normal(0, 0.03, A.shape)
    return np.clip(A, 0, 1).astype(np.float32)

# avaliação no conjunto reservado (idêntica à rodada 1)
Xtest_rows = []
for f in test:
    a = scale(trips[f][CH].values); a2 = np.vstack([np.repeat(a[:1], L - 1, 0), a])
    Xtest_rows.append((f, np.lib.stride_tricks.sliding_window_view(a2, (L, len(CH))).reshape(-1, L, len(CH))))
def evaluate(model):
    errs, seg_l = [], {}
    for f, Wt in Xtest_rows:
        pred = np.clip(unscale(np.c_[np.zeros((len(Wt), 3)), model.predict(feats(Wt))])[:, 3], 0, None)
        g = trips[f]; errs.append(np.abs(pred - g[TGT].values))
        sid = int(g.segment_id.iloc[0]); seg_l[sid] = seg_l.get(sid, 0) + (pred * g.dt.values / 60).sum() / 1000
    return dict(flow_MAE=float(np.concatenate(errs).mean()),
                litres_MAE=float(np.mean([abs(seg_l[s] - pump[s]) for s in seg_l])))

def make_model(warm=False):
    if MODEL == 'mlp':
        return MLPRegressor(hidden_layer_sizes=(64, 64), early_stopping=True, max_iter=200, random_state=0, warm_start=warm)
    return HistGradientBoostingRegressor(max_iter=300, random_state=0, warm_start=warm)
def fit(W, w=None):
    X, y = feats(W), W[:, -1, 3]
    return make_model().fit(X, y, sample_weight=w)
def fit_pretrain(Wsyn, Wreal):
    if MODEL == 'mlp':   # sem early_stopping: o sklearn não continua (warm_start) um MLP treinado com early_stopping
        m = MLPRegressor(hidden_layer_sizes=(64, 64), early_stopping=False, max_iter=100, random_state=0, warm_start=True)
        m.fit(feats(Wsyn), Wsyn[:, -1, 3])
        m.set_params(max_iter=200); m.fit(feats(Wreal), Wreal[:, -1, 3]); return m
    # HGB: warm_start em outro conjunto reaproveita os bins do sintético e diverge (rodada 2/J001);
    # pré-treino correto = modelo no sintético + segundo modelo nos resíduos do real.
    m1 = HistGradientBoostingRegressor(max_iter=300, random_state=0).fit(feats(Wsyn), Wsyn[:, -1, 3])
    Xr, yr = feats(Wreal), Wreal[:, -1, 3]
    m2 = HistGradientBoostingRegressor(max_iter=300, random_state=0).fit(Xr, yr - m1.predict(Xr))
    class _Sum:
        def predict(self, X): return m1.predict(X) + m2.predict(X)
    return _Sum()
def discr(A, B, seed):
    n = min(len(A), len(B), 4000); r = np.random.default_rng(seed)
    a = A[r.choice(len(A), n, replace=False)]; b = B[r.choice(len(B), n, replace=False)]
    X = np.r_[a.reshape(n, -1), b.reshape(n, -1)]; y = np.r_[np.zeros(n), np.ones(n)]
    return float(abs(cross_val_score(HistGradientBoostingClassifier(max_iter=200), X, y, cv=5).mean() - 0.5))
def realness(Wreal, Wsyn, seed):
    """Classificador real-treino vs sintético; devolve prob. de 'real' para cada janela sintética.
    Usa só dados de treino (sem o teste)."""
    r = np.random.default_rng(seed); n = min(len(Wreal), len(Wsyn))
    a = Wreal[r.choice(len(Wreal), n, replace=len(Wreal) < n)].reshape(n, -1)
    b = Wsyn[r.choice(len(Wsyn), n, replace=False)].reshape(n, -1)
    c = HistGradientBoostingClassifier(max_iter=200).fit(np.r_[a, b], np.r_[np.ones(n), np.zeros(n)])
    return c.predict_proba(Wsyn.reshape(len(Wsyn), -1))[:, 1]

def make_gen(seed):
    if GEN == 'timevae':
        from timevae import TimeVAE
        return TimeVAE(len(CH), hidden=HIDDEN, latent=LATENT, seed=seed)
    from timegan import TimeGAN
    return TimeGAN(len(CH), hidden=HIDDEN, seed=seed)

Wfull = windows(pool); Wtest = windows(test)
res = dict(meta=dict(round=2, gen=GEN, model=MODEL, mode='validation' if VAL else 'test', test_segments=TEST_SEGS,
                     pool_trips=len(pool), iters=ITERS, hidden=HIDDEN, latent=LATENT, seeds=SEEDS, fracs=FRACS,
                     torch=torch.__version__, cuda=torch.cuda.is_available(),
                     gpu=torch.cuda.get_device_name(0) if torch.cuda.is_available() else None, audit_limits=LIM),
           runs=[])
if '--no-ceiling' not in sys.argv:
    res['upper_bound_100pct_real'] = evaluate(fit(Wfull))
    print('teto 100% real', res['upper_bound_100pct_real'], flush=True)
def want(v): return ONLY is None or v in ONLY.split(',')

for seed in SEEDS:
    rng = np.random.default_rng(seed)
    for frac in FRACS:
        files = list(rng.choice(pool, max(1, int(round(frac * len(pool)))), replace=False))
        Wr = windows(files); n_fill = max(0, len(Wfull) - len(Wr))
        tg0 = time.time(); g = make_gen(seed).fit(Wr, iters=ITERS); t_gen = time.time() - tg0
        raw = g.sample(int(n_fill * 1.6) + 2000, L); ok = audit(raw); syn = raw[ok]
        aug_pool = simple_aug(Wr, n_fill, rng)
        run = dict(seed=seed, frac=frac, n_real=len(Wr), n_fill=n_fill, n_syn_audited=len(syn),
                   audit_pass=float(ok.mean()), gen_log=g.log, gen_seconds=t_gen,
                   discr_gen_vs_test=discr(Wtest, syn, seed) if len(syn) > 100 else None,
                   discr_aug_vs_test=discr(Wtest, aug_pool, seed), discr_realtrain_vs_test=discr(Wtest, Wr, seed), v={})
        if want('real'): run['v']['real'] = evaluate(fit(Wr))
        for src, P in (('gen', syn), ('aug', aug_pool)):
            for r_name, n in (('0.5', len(Wr) // 2), ('1', len(Wr)), ('fill', n_fill)):
                for wv in (1.0, 0.3):
                    name = f'{src}_r{r_name}_w{wv:g}'
                    if not want(name) or len(P) == 0: continue
                    S = P[:min(n, len(P))]
                    w = np.r_[np.ones(len(Wr)), np.full(len(S), wv)]
                    run['v'][name] = dict(evaluate(fit(np.r_[Wr, S], w)), n_syn=len(S))
        if len(syn) > 100:
            pr = realness(Wr, syn, seed)
            for qq in (0.5, 0.2):
                name = f'gen_dfilt_q{qq:g}'
                if not want(name): continue
                k = max(1, int(qq * len(syn))); top = syn[np.argsort(-pr)[:k]]   # q mais "reais"
                S = top[np.random.default_rng(seed).choice(len(top), min(len(Wr), len(top)), replace=False)]   # amostra 1x deles
                run['v'][name] = dict(evaluate(fit(np.r_[Wr, S])), n_syn=len(S),
                                      discr_vs_test=discr(Wtest, S, seed) if len(S) > 100 else None)
            if want('gen_pretrain'):
                run['v']['gen_pretrain'] = evaluate(fit_pretrain(syn[:n_fill], Wr))
        res['runs'].append(run)
        best = min(run['v'].items(), key=lambda kv: kv[1]['flow_MAE'])
        print(f"seed {seed} frac {frac}: real {run['v'].get('real', {}).get('flow_MAE', float('nan')):.3f} | melhor {best[0]} "
              f"{best[1]['flow_MAE']:.3f} | discr gen {run['discr_gen_vs_test']} | audit {run['audit_pass']:.3f} | "
              f"gen {t_gen:.0f}s | total {time.time()-t0:.0f}s", flush=True)
        json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)
res['meta']['runtime_s'] = time.time() - t0
json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)
print('fim', f'{time.time()-t0:.0f}s')
