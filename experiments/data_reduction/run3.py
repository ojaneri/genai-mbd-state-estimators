#!/usr/bin/env python3
"""Rodada 3 (busca de dados sintéticos de boa qualidade) — derivado de run2.py.

Novidades: --gen ddpm|var|bootstrap além de timegan|timevae; --post quant (quantiza o sintético na
resolução do sensor real: velocidade 1 km/h, RPM 0,25, borboleta 100/255 %, vazão 0,1 mL/min);
distinguibilidade por canal; critério de sucesso: discr_gen_vs_test <= discr_realtrain_vs_test + 0,05.

Rodada 2 da validação por redução de dados (caso A público, Opel Corsa) — grade pré-registrada.

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
GEN = arg('--gen', 'timegan'); MODEL = arg('--model', 'hgb'); POST = arg('--post', 'none')
SEEDS = [int(x) for x in arg('--seeds', '0').split(',')]
FRACS = [float(x) for x in arg('--fracs', '0.01,0.02,0.05,0.1').split(',')]
ITERS = arg('--iters', {'timegan': 6000, 'timevae': 3000, 'ddpm': 6000, 'ddpm2': 30000}.get(GEN, 0), int)
HIDDEN = arg('--hidden', {'timegan': 24, 'timevae': 48, 'ddpm': 64, 'ddpm2': 128}.get(GEN, 24), int)
COND = '--cond-speed' in sys.argv; LATENT = arg('--latent', 16, int)
VAL = '--val' in sys.argv
ONLY = arg('--variants', None)
DOMAIN = arg('--domain', 'fuel')   # fuel = caso A (Opel/Itabira); battery = caso B (LG 18650HG2, tools/convert_lghg2.py)
FEAT = ['SPEED', 'RPM', 'THROTTLE_POS']; TGT = 'REAL_FUEL_USAGE_ML_MIN'; CH = FEAT + [TGT]
TEST_SEGS, POOL_SEGS = ([15, 16, 17], list(range(8, 15))) if VAL else ([18, 19, 20, 21, 22], list(range(8, 18)))
if DOMAIN == 'battery':   # sensor virtual de SOC; segment_id = ciclo (1–4 UDDS/HWFET/LA92/US06, 5–12 Mixed1–8)
    FEAT = ['CURRENT', 'VOLTAGE', 'TEMP']; TGT = 'SOC'; CH = FEAT + [TGT]
    TEST_SEGS, POOL_SEGS = ([7, 8], list(range(1, 7))) if VAL else ([9, 10, 11, 12], list(range(1, 9)))
    CHUNK = 600   # cada ciclo vira trechos de 600 amostras (10 min a 1 Hz; unidade de amostragem da fração)
elif DOMAIN == 'bess_temp':   # d-0020: sensor virtual de TEMPERATURA de célula no BESS (verdade medida); dados de convert_bess.py --temp
    FEAT = ['CURRENT', 'VOLTAGE', 'TREF']; TGT = 'TCELL'; CH = FEAT + [TGT]
    TEST_SEGS, POOL_SEGS = ([5, 6], list(range(1, 5))) if VAL else ([7, 8], list(range(1, 7)))
    CHUNK = 600
BATT = DOMAIN in ('battery', 'bess_temp')
# parâmetros da célula/rack (d-0019): LG 18650HG2 = padrão; BESS (caso C) lê meta.json do conversor
BMETA = json.load(open(f'{SRC}/meta.json')) if (BATT and os.path.exists(f'{SRC}/meta.json')) else {}
BCAP, BDT, BNS = BMETA.get('cap_ah', 3.0), BMETA.get('dt_s', 1.0), BMETA.get('cells_series', 1)
def _segs(txt): return sorted({i for part in txt.split(',') for i in (range(int(part.split('-')[0]), int(part.split('-')[1]) + 1) if '-' in part else [int(part)])})
if '--test-segs' in sys.argv: TEST_SEGS = _segs(arg('--test-segs', ''))   # validação cruzada por blocos de tanques
if '--pool-segs' in sys.argv: POOL_SEGS = _segs(arg('--pool-segs', ''))
AUTO = '--auto-select' in sys.argv   # d-0018: portão de utilidade — escolhe o método por validação interna (últimos 20 % de cada viagem)
PRE_SRC = arg('--pretrain-src', None); PRE_TEMPS = arg('--pretrain-temps', None); PRE_ITERS = arg('--pretrain-iters', 50000, int)   # d-0018: transferência
TEMPS = arg('--temps', None)   # bateria: só estas temperaturas (prefixo do segment_file), p.ex. n20degC,n10degC,0degC
HW_ABSENT = '--hw-absent' in sys.argv   # cenário ausente: sem janelas com velocidade > 80 km/h no treino real (e no gerador)
L, STRIDE = 24, 4
t0 = time.time()

# ------------------------------------------------------------------ dados (idêntico à rodada 1)
df = pd.read_csv(f'{SRC}/dataset.csv', usecols=['timestamp', 'segment_id', 'segment_file'] + CH)
df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601')   # BESS: o conversor gravou dois formatos ISO (alerta do desktop, 04/10); pandas 3 exige isto
if DOMAIN == 'fuel': df.loc[df.SPEED > 200, 'SPEED'] = np.nan
df = df.sort_values(['segment_file', 'timestamp'])
if BATT:
    if BNS != 1: df['VOLTAGE'] = df['VOLTAGE'] / BNS   # tensão média por célula
    df['segment_file'] = df.segment_file + '_c' + (df.groupby('segment_file').cumcount() // CHUNK).astype(str)
_df_all = df.copy() if PRE_TEMPS else None   # fonte da transferência entre temperaturas (antes do filtro)
if TEMPS: df = df[df.segment_file.str.split('_').str[0].isin(TEMPS.split(','))]
df[CH] = df.groupby('segment_file')[CH].transform(lambda s: s.ffill().bfill())
df = df[df.segment_id.isin(POOL_SEGS + TEST_SEGS)].dropna(subset=CH)
df['dt'] = df.groupby('segment_file').timestamp.diff().dt.total_seconds().fillna(0).clip(0, 5)
pump = pd.read_csv(f'{SRC}/refueling_history.csv').set_index('Lp')['Refueling'] if os.path.exists(f'{SRC}/refueling_history.csv') else None   # Itabira: sem litros da bomba
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
AUDIT_TIERS = []
if DOMAIN == 'battery':   # auditoria física da célula (5 níveis): faixas; contagem de carga; dV, dI; dT; tensão em repouso × SOC
    _g = df.groupby('segment_file'); _pool = df[df.segment_id.isin(POOL_SEGS)]
    _cc = (_g.SOC.diff() - _g.CURRENT.shift(0) / 3600 / 3.0).abs()
    _rest = _pool[_pool.CURRENT.abs() < 0.1]; _bins = np.linspace(0, 1.0, 21)
    _band = _rest.groupby(np.digitize(_rest.SOC, _bins)).VOLTAGE.quantile([0.005, 0.995]).unstack()
    # d-0016: contagem de carga e temperatura avaliadas na JANELA (24 s), não por passo de 1 s — a versão por passo exigia
    # precisão de 0,04 % de SOC/s e rejeitou 100 % do sintético no J020. Tolerância = máx(q99,9 % real na janela, piso físico):
    # 1 ponto de SOC em 24 s (≈ 4,5 A de erro sustentado) e 1 °C em 24 s.
    _cw = (_g.SOC.diff(L - 1) - _g.CURRENT.rolling(L - 1).sum().reset_index(level=0, drop=True) * BDT / 3600 / BCAP).abs()
    _tw = _g.TEMP.diff(L - 1).abs()
    BLIM = dict(cc_win=max(float(_cw.quantile(0.999)), 0.01), dv=float(_g.VOLTAGE.diff().abs().quantile(0.999)),
                di=float(_g.CURRENT.diff().abs().quantile(0.999)), dt_win=max(float(_tw.quantile(0.999)), 1.0),
                i_max=20.0 if not BMETA else 1.2 * float(_pool.CURRENT.abs().quantile(0.999)))   # BESS: limite de corrente do rack, dos dados
    def audit(Wsc):
        W = unscale(Wsc); I, V, T, S = [W[:, :, i] for i in range(4)]
        t1 = (V >= 2.4).all(1) & (V <= 4.25).all(1) & (S >= -0.01).all(1) & (S <= 1.02).all(1) & (np.abs(I) <= BLIM['i_max']).all(1)
        t2 = np.abs((S[:, -1] - S[:, 0]) - I[:, 1:].sum(1) * BDT / 3600 / BCAP) <= BLIM['cc_win']
        t3 = (np.abs(np.diff(V, axis=1)) <= BLIM['dv']).all(1) & (np.abs(np.diff(I, axis=1)) <= BLIM['di']).all(1)
        t4 = np.abs(T[:, -1] - T[:, 0]) <= BLIM['dt_win']
        b = np.digitize(S, _bins); lo5 = _band[0.005].reindex(range(22)).values; hi5 = _band[0.995].reindex(range(22)).values
        rest = np.abs(I) < 0.1; ok = np.isnan(lo5[b]) | ((V >= lo5[b]) & (V <= hi5[b]))
        t5 = (~rest | ok).all(1)
        AUDIT_TIERS[:] = [float(t.mean()) for t in (t1, t2, t3, t4, t5)]
        return t1 & t2 & t3 & t4 & t5
    LIM = BLIM
elif DOMAIN == 'bess_temp':   # auditoria térmica (5 níveis): faixas; deriva da célula na janela; dV, dI; deriva da referência; |célula − referência|
    _g = df.groupby('segment_file'); _pool = df[df.segment_id.isin(POOL_SEGS)]
    _q = lambda x: float(x.quantile(0.999))
    TLIM = dict(i_max=1.2 * _q(_pool.CURRENT.abs()), dv=_q(_g.VOLTAGE.diff().abs()), di=_q(_g.CURRENT.diff().abs()),
                dtc_win=max(_q(_g.TCELL.diff(L - 1).abs()), 0.5), dtr_win=max(_q(_g.TREF.diff(L - 1).abs()), 0.5),
                gap=_q((_pool.TCELL - _pool.TREF).abs()) + 1.0)
    def audit(Wsc):
        W = unscale(Wsc); I, V, TR, TC = [W[:, :, i] for i in range(4)]
        t1 = (V >= 2.4).all(1) & (V <= 4.25).all(1) & (np.abs(I) <= TLIM['i_max']).all(1) & (TC > -30).all(1) & (TC < 70).all(1)
        t2 = np.abs(TC[:, -1] - TC[:, 0]) <= TLIM['dtc_win']
        t3 = (np.abs(np.diff(V, axis=1)) <= TLIM['dv']).all(1) & (np.abs(np.diff(I, axis=1)) <= TLIM['di']).all(1)
        t4 = np.abs(TR[:, -1] - TR[:, 0]) <= TLIM['dtr_win']
        t5 = (np.abs(TC - TR) <= TLIM['gap']).all(1)
        AUDIT_TIERS[:] = [float(t.mean()) for t in (t1, t2, t3, t4, t5)]
        return t1 & t2 & t3 & t4 & t5
    LIM = TLIM
else:
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
    AUDIT_TIERS[:] = [float(t.mean()) for t in (t1, t2, t3, t4, t5)]
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
VALW = None
def evaluate(model):
    errs, seg_l, hw = [], {}, []
    for f, Wt in Xtest_rows:
        ysc = model.predict_windows(Wt) if hasattr(model, 'predict_windows') else model.predict(feats(Wt))
        pred = np.clip(unscale(np.c_[np.zeros((len(Wt), 3)), ysc])[:, 3], 0, None)
        g = trips[f]; errs.append(np.abs(pred - g[TGT].values)); hw.append(np.abs(pred - g[TGT].values)[g['SPEED'].values > 80] if DOMAIN == 'fuel' else np.abs(pred - g[TGT].values)[(g['TEMP'] if 'TEMP' in g else g['TREF']).values < 5])
        sid = int(g.segment_id.iloc[0]); seg_l[sid] = seg_l.get(sid, 0) + (pred * g.dt.values / 60).sum() / 1000
    hwc = np.concatenate(hw)
    vm = None
    if AUTO and VALW is not None and len(VALW):   # erro na validação interna (mesma unidade do alvo)
        yv = model.predict_windows(VALW) if hasattr(model, 'predict_windows') else model.predict(feats(VALW))
        pv = np.clip(unscale(np.c_[np.zeros((len(VALW), 3)), yv])[:, 3], 0, None); vm = float(np.abs(pv - unscale(VALW)[:, -1, 3]).mean())
    return dict(flow_MAE=float(np.concatenate(errs).mean()), flow_MAE_hw=float(hwc.mean()) if len(hwc) else None, val_MAE=vm,
                litres_MAE=float(np.mean([abs(seg_l[s] - pump[s]) for s in seg_l])) if pump is not None else None)

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

RES = np.array([1.0, 0.25, 100 / 255, 0.1])   # resolução real do Opel (conferida nos dados em 01/10)
if '--res-auto' in sys.argv or BATT:   # outros veículos: mede a resolução (mediana dos degraus entre valores distintos) no treino
    _r = []
    for c in CH:
        u = np.unique(df[df.segment_id.isin(POOL_SEGS)][c].dropna().round(6).values); dd = np.diff(u); _r.append(float(np.median(dd[dd > 1e-9])))
    RES = np.array(_r)
def quantize(Wsc):
    W = unscale(Wsc); W = np.round(W / RES) * RES
    return scale(W).astype(np.float32)
def discr_channels(A, B, seed):
    out = {}
    for c, name in enumerate(CH):
        n = min(len(A), len(B), 4000); r = np.random.default_rng(seed)
        a = A[r.choice(len(A), n, replace=False), :, c]; b = B[r.choice(len(B), n, replace=False), :, c]
        X = np.r_[a, b]; y = np.r_[np.zeros(n), np.ones(n)]
        out[name] = float(abs(cross_val_score(HistGradientBoostingClassifier(max_iter=100), X, y, cv=3).mean() - 0.5))
    return out
def dequantize(Wsc, rng):
    """Desquantização (Theis et al., ICLR 2016): ruído uniforme dentro do degrau do sensor."""
    W = unscale(Wsc) + rng.uniform(-0.5, 0.5, Wsc.shape) * RES
    return scale(W).astype(np.float32)
def hold(Wsc, target, rng, channels=None):
    """Emula sample-and-hold: repete o valor anterior com prob. p_c por canal, calibrada para que a
    fração final de repetições se aproxime da real (target)."""
    W = Wsc.copy(); cur = repeat_frac(W)
    for c in (channels if channels is not None else range(W.shape[2])):
        if target[c] <= cur[c]: continue
        p = (target[c] - cur[c]) / (1 - cur[c])
        m = rng.random((W.shape[0], W.shape[1] - 1)) < p
        for t in range(1, W.shape[1]):
            W[m[:, t - 1], t, c] = W[m[:, t - 1], t - 1, c]
    return W
def discr_dq(A, B, seed):
    """Distinguibilidade com os dois lados desquantizados: mede a dinâmica, não a grade do sensor."""
    r = np.random.default_rng(seed + 999)
    return discr(dequantize(A, r), dequantize(B, r), seed)
def repeat_frac(W):
    return [float((np.abs(np.diff(unscale(W)[:, :, c], axis=1)) < 1e-9).mean()) for c in range(len(CH))]
def phys_labeler_battery(Wr):
    """Rótulo físico-estruturado de SOC (circuito equivalente de 1ª ordem invertido): OCV ≈ V − R(T)·I, com
    SOC ~ polinômio cúbico da OCV estimada + termos de temperatura, ajustado nos dados reais da fração, mais
    resíduo aprendido (HGB nas features da janela). Reescreve o alvo do último passo."""
    U = unscale(Wr)
    def terms(U):
        I, V, T = U[:, -1, 0], U[:, -1, 1], U[:, -1, 2]; Im = U[:, -8:, 0].mean(1)
        return np.stack([np.ones_like(V), V, V ** 2, V ** 3, I, I * T, Im, Im * T, T, V * T], -1)
    coef, *_ = np.linalg.lstsq(terms(U), U[:, -1, 3], rcond=None)
    res = HistGradientBoostingRegressor(max_iter=200, random_state=0).fit(feats(Wr), U[:, -1, 3] - terms(U) @ coef)
    def relabel(Ws):
        y = np.clip(terms(unscale(Ws)) @ coef + res.predict(feats(Ws)), 0, None)
        W2 = Ws.copy(); W2[:, -1, 3] = np.clip((y - lo[3]) / (hi[3] - lo[3]), 0, 1); return W2
    relabel.phys = lambda Ws: terms(unscale(Ws)) @ coef   # só a parte física (unidades reais), para os híbridos (d-0017)
    return relabel
def phys_labeler_thermal(Wr):
    """Rótulo físico-estruturado de temperatura de célula (modelo térmico concentrado): T_célula ≈ T_ref + a·I² (Joule, com
    médias de 8 e 24 passos para a inércia térmica) + b·I (termo reversível) + c·V + d, ajustado no real da fração, mais
    resíduo aprendido (HGB). Reescreve o alvo do último passo."""
    U = unscale(Wr)
    def terms(U):
        I, V, TR = U[:, -1, 0], U[:, -1, 1], U[:, -1, 2]
        return np.stack([np.ones_like(I), TR, I, I ** 2, (U[:, -8:, 0] ** 2).mean(1), (U[:, :, 0] ** 2).mean(1), V], -1)
    coef, *_ = np.linalg.lstsq(terms(U), U[:, -1, 3], rcond=None)
    res = HistGradientBoostingRegressor(max_iter=200, random_state=0).fit(feats(Wr), U[:, -1, 3] - terms(U) @ coef)
    def relabel(Ws):
        y = terms(unscale(Ws)) @ coef + res.predict(feats(Ws))
        W2 = Ws.copy(); W2[:, -1, 3] = np.clip((y - lo[3]) / (hi[3] - lo[3]), 0, 1); return W2
    relabel.phys = lambda Ws: terms(unscale(Ws)) @ coef
    return relabel
def phys_labeler(Wr):
    if DOMAIN == 'battery': return phys_labeler_battery(Wr)
    if DOMAIN == 'bess_temp': return phys_labeler_thermal(Wr)
    """Modelo físico-estruturado de vazão (regressão nos termos de carga longitudinal: marcha lenta,
    RPM, borboleta, RPM×borboleta, v, v³, v·a⁺) ajustado nos dados reais da fração + resíduo aprendido (HGB
    nas features da janela). Devolve função que reescreve o alvo (último passo, canal de vazão)."""
    U = unscale(Wr); v = U[:, :, 0] / 3.6; rpm, thr, fl = U[:, :, 1], U[:, :, 2], U[:, :, 3]
    a = np.diff(v, axis=1, prepend=v[:, :1]); ap = np.clip(a, 0, None)
    def terms(v, a, rpm, thr):
        return np.stack([np.ones_like(v), rpm, thr, rpm * thr / 100, v, v ** 3, v * np.clip(a, 0, None)], -1)
    Xp = terms(v, a, rpm, thr).reshape(-1, 7); coef, *_ = np.linalg.lstsq(Xp, fl.reshape(-1), rcond=None)
    phys_last = lambda U: terms(U[:, -1, 0] / 3.6, U[:, -1, 0] / 3.6 - U[:, -2, 0] / 3.6, U[:, -1, 1], U[:, -1, 2]) @ coef
    res = HistGradientBoostingRegressor(max_iter=200, random_state=0).fit(feats(Wr), fl[:, -1] - phys_last(U))
    def relabel(Ws):
        Us = unscale(Ws); y = np.clip(phys_last(Us) + res.predict(feats(Ws)), 0, None)
        W2 = Ws.copy(); W2[:, -1, 3] = np.clip((y - lo[3]) / (hi[3] - lo[3]), 0, 1); return W2
    relabel.phys = lambda Ws: phys_last(unscale(Ws))
    return relabel
def make_gen(seed):
    if GEN == 'ddpm2':
        import gens
        return gens.DDPM2(len(CH), hidden=HIDDEN, seed=seed, fourier=float(arg('--fourier', '0.1')))
    if GEN in ('ddpm', 'var', 'bootstrap'):
        import gens
        if GEN == 'ddpm': return gens.DDPM(len(CH), hidden=HIDDEN, seed=seed)
        return (gens.VAR if GEN == 'var' else gens.BlockBootstrap)(len(CH), seed=seed)
    if GEN == 'timevae':
        from timevae import TimeVAE
        return TimeVAE(len(CH), hidden=HIDDEN, latent=LATENT, seed=seed)
    from timegan import TimeGAN
    return TimeGAN(len(CH), hidden=HIDDEN, seed=seed)

Wfull = windows(pool); Wtest = windows(test)
def windows_split(files, frac_val=0.2):
    """Portão de utilidade: em cada viagem da fração, janelas dos primeiros 80 % para treino, dos últimos 20 % para validação."""
    A, B = [], []
    for f in files:
        a = scale(trips[f][CH].values); n = len(a); cut = int(round(n * (1 - frac_val)))
        A += [a[i:i + L] for i in range(0, cut - L + 1, STRIDE)]; B += [a[i:i + L] for i in range(cut, n - L + 1, STRIDE)]
    f32 = lambda X: np.array(X, dtype=np.float32).reshape(-1, L, len(CH))
    return f32(A), f32(B)
Wsrc = None
if PRE_SRC or PRE_TEMPS:   # janelas da fonte, na escala do ALVO (lo/hi do alvo, com corte em [0, 1])
    if PRE_SRC:
        ds = pd.read_csv(f'{PRE_SRC}/dataset.csv', usecols=['timestamp', 'segment_id', 'segment_file'] + CH); ds['timestamp'] = pd.to_datetime(ds['timestamp'], format='ISO8601')
        if DOMAIN == 'fuel': ds.loc[ds.SPEED > 200, 'SPEED'] = np.nan
        ds = ds.sort_values(['segment_file', 'timestamp'])
    else:
        ds = _df_all[_df_all.segment_file.str.split('_').str[0].isin(PRE_TEMPS.split(',')) & _df_all.segment_id.isin(POOL_SEGS)]
    ds = ds.copy(); ds[CH] = ds.groupby('segment_file')[CH].transform(lambda s: s.ffill().bfill()); ds = ds.dropna(subset=CH)
    _W = []
    for _, gsrc in ds.groupby('segment_file'):
        a = scale(gsrc[CH].values); _W += [a[i:i + L] for i in range(0, len(a) - L + 1, STRIDE)]
    Wsrc = np.array(_W, dtype=np.float32).reshape(-1, L, len(CH)); del _W, ds
    print('fonte de pré-treino:', len(Wsrc), 'janelas', flush=True)
PRE_CACHE = {}
res = dict(meta=dict(round=3, domain=DOMAIN, battery_meta=BMETA or None, dataset=os.path.basename(os.path.normpath(SRC)), res_sensor=[float(x) for x in RES], gen=GEN, cond_speed=COND, post=POST, dequant='--dequant' in sys.argv, model=MODEL, mode='validation' if VAL else 'test', test_segments=TEST_SEGS, pool_segments=POOL_SEGS, hw_absent=HW_ABSENT, auto_select=AUTO, pretrain_src=PRE_SRC, pretrain_temps=PRE_TEMPS, pretrain_iters=PRE_ITERS if (PRE_SRC or PRE_TEMPS) else None, temps=TEMPS,
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
        Wr = windows(files)
        if AUTO: Wr, VALW = windows_split(files)
        if HW_ABSENT: Wr = Wr[unscale(Wr)[:, :, 0].max(1) <= 80] if DOMAIN == 'fuel' else Wr[unscale(Wr)[:, :, 2].min(1) >= 5]   # bateria: sem frio (<5 °C)
        n_fill = max(0, len(Wfull) - len(Wr))
        if '--max-syn' in sys.argv: n_fill = min(n_fill, int(arg('--max-syn', '0')))   # só para testes rápidos
        Wgen = dequantize(Wr, np.random.default_rng(seed + 7)) if '--dequant' in sys.argv else Wr
        g = make_gen(seed)
        if GEN == 'ddpm2':   # escolha de checkpoint por discr num subconjunto reservado do TREINO (20 %)
            rs_ = np.random.default_rng(seed + 3); idx = rs_.permutation(len(Wgen)); cut = max(1, int(0.8 * len(Wgen)))
            Wfit, Wsel = Wgen[idx[:cut]], Wr[idx[cut:]]
            def _sel(model, Wsel=Wsel):
                smp = model.sample(min(2000, 4 * len(Wsel)), L, cond=Wsel if COND else None)
                if POST in ('quant', 'quanthold', 'quantholdin'): smp = quantize(smp)
                return discr(Wsel, smp, seed + 5)
            g.select_fn = _sel; Wgen = Wfit
        tg0 = time.time()
        if Wsrc is not None:   # pré-treino na fonte (uma vez por semente) + ajuste fino na fração do alvo
            import copy
            if seed not in PRE_CACHE:
                g0 = make_gen(seed); g0.fit(dequantize(Wsrc, np.random.default_rng(seed + 8)) if '--dequant' in sys.argv else Wsrc, iters=PRE_ITERS)
                PRE_CACHE[seed] = copy.deepcopy(g0.net.state_dict()); del g0
            g.net.load_state_dict(PRE_CACHE[seed]); g.log['pretrained'] = dict(src=PRE_SRC or PRE_TEMPS, iters=PRE_ITERS, n_src=len(Wsrc))
        g = g.fit(Wgen, iters=ITERS); t_gen = time.time() - tg0
        raw = g.sample(int(n_fill * 1.6) + 2000, L, cond=Wr) if (GEN == 'ddpm2' and COND) else g.sample(int(n_fill * 1.6) + 2000, L)
        if POST in ('quant', 'quanthold', 'quantholdin'): raw = quantize(raw)
        if POST == 'quanthold': raw = hold(raw, repeat_frac(Wr), np.random.default_rng(seed + 11))
        if POST == 'quantholdin': raw = hold(raw, repeat_frac(Wr), np.random.default_rng(seed + 11), channels=[0, 1, 2])   # hold só nas entradas, não no alvo (J006: hold no alvo piorou a utilidade)
        ok = audit(raw); syn = raw[ok]
        if '--save-windows' in sys.argv:   # d-0032: só grava amostras para a figura do artigo; não usa rng nem altera nada
            np.savez_compressed(f'{OUT}/windows_s{seed}_f{frac:g}.npz', ch=np.array(CH), real=unscale(Wr[:200]), syn=unscale(syn[:200]),
                                rejected=unscale(raw[~ok][:100]), dt=np.array(BDT if BATT else 1.0))
        aug_pool = simple_aug(Wr, n_fill, rng)
        run = dict(seed=seed, frac=frac, n_real=len(Wr), n_fill=n_fill, n_syn_audited=len(syn), audit_tiers=list(AUDIT_TIERS),
                   audit_pass=float(ok.mean()), audit_pass_real=float(audit(Wr).mean()), audit_tiers_real=list(AUDIT_TIERS), gen_log=g.log, gen_seconds=t_gen,
                   discr_gen_vs_test=discr(Wtest, syn, seed) if len(syn) > 100 else None,
                   discr_aug_vs_test=discr(Wtest, aug_pool, seed) if len(aug_pool) > 100 else None, discr_realtrain_vs_test=discr(Wtest, Wr, seed), v={},
                   discr_dq_gen_vs_test=discr_dq(Wtest, syn, seed) if len(syn) > 100 else None,
                   discr_boot_ref=discr(Wtest, __import__('gens').BlockBootstrap(4, seed=seed).fit(Wr).sample(min(len(Wtest), 8000), L), seed),
                   discr_dq_realtrain_vs_test=discr_dq(Wtest, Wr, seed),
                   discr_channels_gen=discr_channels(Wtest, syn, seed) if len(syn) > 100 else None,
                   discr_channels_realtrain=discr_channels(Wtest, Wr, seed),
                   repeat_frac_real=repeat_frac(Wr), repeat_frac_gen=repeat_frac(syn) if len(syn) else None)
        # Fidelidade "na mesma distribuição" (d-0011): viagens do treino (mesmos tanques) FORA da fração usada
        rest = [f for f in pool if f not in set(files)]
        if rest and len(syn) > 100:
            Wh = windows(rest); Wh = Wh[np.random.default_rng(seed + 21).choice(len(Wh), min(len(Wh), 8000), replace=False)]
            run['discr_id_gen'] = discr(Wh, syn, seed)
            run['discr_id_real'] = discr(Wh, Wr, seed)
            run['discr_id_boot'] = discr(Wh, __import__('gens').BlockBootstrap(4, seed=seed).fit(Wr).sample(min(len(Wh), 8000), L), seed)
            run['success_fidelity_id'] = run['discr_id_gen'] <= run['discr_id_real'] + 0.05
            run['success_vs_boot_id'] = run['discr_id_gen'] <= run['discr_id_boot']
            # fidelidade DINÂMICA (d-0015): tira o nível médio de cada canal na janela; mede a forma, não o ponto
            # de operação (necessária na bateria, onde SOC/temperatura por trecho separam até real × real)
            dyn = lambda W: W - W.mean(1, keepdims=True)
            run['discr_id_dyn_gen'] = discr(dyn(Wh), dyn(syn), seed)
            run['discr_id_dyn_real'] = discr(dyn(Wh), dyn(Wr), seed)
            run['success_fidelity_id_dyn'] = run['discr_id_dyn_gen'] <= run['discr_id_dyn_real'] + 0.05
        run['success_fidelity'] = (run['discr_gen_vs_test'] is not None and
                                   run['discr_gen_vs_test'] <= run['discr_realtrain_vs_test'] + 0.05)
        if want('real'): run['v']['real'] = evaluate(fit(Wr))
        for src, P in (('gen', syn), ('aug', aug_pool)):
            for r_name, n in (('0.5', len(Wr) // 2), ('1', len(Wr)), ('fill', n_fill)):
                for wv in (1.0, 0.3):
                    name = f'{src}_r{r_name}_w{wv:g}'
                    if not want(name) or len(P) == 0: continue
                    S = P[:min(n, len(P))]
                    w = np.r_[np.ones(len(Wr)), np.full(len(S), wv)]
                    run['v'][name] = dict(evaluate(fit(np.r_[Wr, S], w)), n_syn=len(S))
        if want('physonly'):   # controle (d-0015): o rotulador físico+resíduo usado DIRETO como sensor, sem sintético
            _rl = phys_labeler(Wr)
            class _Phys:
                def predict_windows(self, Wt): return _rl(Wt)[:, -1, 3]
            run['v']['physonly'] = evaluate(_Phys())
        # HÍBRIDOS física + IA generativa (d-0017). Parte física ajustada só no real da fração (igual ao physonly).
        if any(want(n) for n in ('hyb_resid_w0.3', 'hyb_feat_real', 'hyb_feat_w0.3')):
            _phys = phys_labeler(Wr).phys
            _sc = lambda y: (y - lo[3]) / (hi[3] - lo[3])
            _y = lambda W: unscale(W)[:, -1, 3]
            S = syn[:min(n_fill, len(syn))]
            if want('hyb_resid_w0.3') and len(S) > 100:   # resíduo da física aprendido com real + sintético
                A = np.r_[Wr, S]; w = np.r_[np.ones(len(Wr)), np.full(len(S), 0.3)]
                _res = HistGradientBoostingRegressor(max_iter=200, random_state=0).fit(feats(A), _y(A) - _phys(A), sample_weight=w)
                class _HR:
                    def predict_windows(self, Wt): return _sc(_phys(Wt) + _res.predict(feats(Wt)))
                run['v']['hyb_resid_w0.3'] = dict(evaluate(_HR()), n_syn=len(S))
            def _hyb_feat(A, w=None):   # previsão física como variável de entrada do modelo de dados
                m = make_model().fit(np.c_[feats(A), _sc(_phys(A))], A[:, -1, 3], sample_weight=w)
                class _HF:
                    def predict_windows(self, Wt): return m.predict(np.c_[feats(Wt), _sc(_phys(Wt))])
                return _HF()
            if want('hyb_feat_real'): run['v']['hyb_feat_real'] = evaluate(_hyb_feat(Wr))
            if want('hyb_feat_w0.3') and len(S) > 100:
                run['v']['hyb_feat_w0.3'] = dict(evaluate(_hyb_feat(np.r_[Wr, S], np.r_[np.ones(len(Wr)), np.full(len(S), 0.3)])), n_syn=len(S))
        if len(syn) > 100 and any(want(f'genphys_{x}') for x in ('r1_w1', 'rfill_w1', 'rfill_w0.3')):
            relabel = phys_labeler(Wr)
            for r_name, n, wv in (('r1', len(Wr), 1.0), ('rfill', n_fill, 1.0), ('rfill', n_fill, 0.3)):
                name = f'genphys_{r_name}_w{wv:g}'
                if not want(name): continue
                S = relabel(syn[:min(n, len(syn))]); w = np.r_[np.ones(len(Wr)), np.full(len(S), wv)]
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
        if AUTO:
            cand = [k for k in ('real', 'physonly', 'gen_rfill_w0.3', 'genphys_rfill_w0.3', 'hyb_resid_w0.3', 'hyb_feat_real', 'hyb_feat_w0.3')
                    if k in run['v'] and run['v'][k].get('val_MAE') is not None]
            ch = min(cand, key=lambda k: run['v'][k]['val_MAE']) if cand else 'real'
            run.update(auto_choice=ch, auto_test_MAE=run['v'][ch]['flow_MAE'], n_val=int(len(VALW)))
        res['runs'].append(run)
        best = min(run['v'].items(), key=lambda kv: kv[1]['flow_MAE'])
        print(f"seed {seed} frac {frac}: real {run['v'].get('real', {}).get('flow_MAE', float('nan')):.3f} | melhor {best[0]} "
              f"{best[1]['flow_MAE']:.3f} | discr gen {run['discr_gen_vs_test']} (real {run['discr_realtrain_vs_test']:.3f}, ok={run['success_fidelity']}) | id: gen {run.get('discr_id_gen')} real {run.get('discr_id_real')} ok={run.get('success_fidelity_id')} | audit {run['audit_pass']:.3f} | "
              f"gen {t_gen:.0f}s | total {time.time()-t0:.0f}s", flush=True)
        json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)
res['meta']['runtime_s'] = time.time() - t0
json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1, default=float)
print('fim', f'{time.time()-t0:.0f}s')
