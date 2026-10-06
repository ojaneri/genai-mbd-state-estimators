#!/usr/bin/env python3
"""Teste externo de detecção de reabastecimento e de estimativa de litros no dataset público
OBD2_panel_opel_2012 (Kaggle pedro2025, CC BY 4.0).

Entrada: dataset.csv e refueling_history.csv do Kaggle (não versionados; ver README).
Uso: python3 refuel_test.py <pasta_com_csvs> <pasta_saida>
"""
import sys, json
import numpy as np, pandas as pd

src, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(f'{src}/dataset.csv', usecols=['timestamp', 'SPEED', 'FUEL_LEVEL', 'segment_id',
                 'segment_file', 'REAL_FUEL_USED_TOTAL_ML'], parse_dates=['timestamp'])
ref = pd.read_csv(f'{src}/refueling_history.csv')
ref['date'] = pd.to_datetime(ref['Data'], format='%d-%m-%Y')

# --- 1. mapeamento: reabastecimento da linha k = fim do segmento k do log --------------
seg = df.groupby('segment_id').agg(start=('timestamp', 'min'), end=('timestamp', 'max'))
lv = df.dropna(subset=['FUEL_LEVEL']).groupby('segment_id').FUEL_LEVEL.agg(['first', 'last'])
seg = seg.join(lv)
truth = []
for k, r in ref.iterrows():
    sid = int(r['Lp'])  # linha k -> segmento k do log (segment_id do arquivo = k + 2)
    s = seg.loc[sid]
    nxt = seg.loc[sid + 1] if sid + 1 in seg.index else None
    truth.append(dict(lp=int(r['Lp']), file_segment=int(r['Segment_id']), log_segment=sid,
                      pump_L=float(r['Refueling']), trapez_L=float(r['Trapez_l']), file_date=str(r['date'].date()),
                      log_end=str(s['end']), next_start=str(nxt['start']) if nxt is not None else None,
                      date_match=(s['end'].date() == r['date'].date()),
                      level_before=float(s['last']), level_after=float(nxt['first']) if nxt is not None else None,
                      observable=nxt is not None))
T = pd.DataFrame(truth)

# --- 2. detector que só vê FUEL_LEVEL (sem segment_id) ------------------------------------
x = df.dropna(subset=['FUEL_LEVEL'])[['timestamp', 'FUEL_LEVEL']].sort_values('timestamp').reset_index(drop=True)
jump = x.FUEL_LEVEL.diff()
def detect(th):
    idx = np.where(jump > th)[0]
    return x.loc[idx, 'timestamp'].tolist(), jump.iloc[idx].tolist()
obs = T[T.observable]
def evaluate(th, tol=pd.Timedelta('2h')):
    det, dj = detect(th)
    tp, used = 0, set()
    for _, r in obs.iterrows():
        a, b = pd.Timestamp(r.log_end) - tol, pd.Timestamp(r.next_start) + tol
        hit = [i for i, t in enumerate(det) if a <= t <= b and i not in used]
        if hit: tp += 1; used.add(hit[0])
    fp = len(det) - len(used)
    return dict(threshold=th, detections=len(det), TP=tp, FN=len(obs) - tp, FP=fp,
                precision=tp / len(det) if det else None, recall=tp / len(obs))
sweep = [evaluate(th) for th in [1, 2, 3, 5, 8, 10, 15, 20, 30, 40, 50]]
# maior salto positivo dentro de uma viagem (ruído residual, candidato a falso positivo)
x['file'] = df.dropna(subset=['FUEL_LEVEL']).sort_values('timestamp')['segment_file'].values
within = x.groupby('file').FUEL_LEVEL.apply(lambda s: s.diff().max())
quant = float(np.round(np.diff(np.unique(x.FUEL_LEVEL)).min(), 4))

# --- 3. litros a partir do salto de nível: capacidade ajustada com leave-one-out ----------
o = obs.copy(); o['dpct'] = o.level_after - o.level_before
cap_all = float((o.pump_L * o.dpct).sum() / (o.dpct ** 2).sum() * 100)  # L por 100 %, mínimos quadrados sem intercepto
loo = []
for i in o.index:
    tr = o.drop(i); c = (tr.pump_L * tr.dpct).sum() / (tr.dpct ** 2).sum() * 100
    loo.append(c * o.loc[i, 'dpct'] / 100 - o.loc[i, 'pump_L'])
o['level_est_err_L'] = loo
T['trapez_err_L'] = T.trapez_L - T.pump_L

res = dict(
    n_refuels_file=len(T), n_observable=int(T.observable.sum()),
    date_mismatches=T.loc[~T.date_match, ['lp', 'file_date', 'log_end']].to_dict('records'),
    level_quantum_pct=quant, max_within_trip_rise_pct=float(within.max()),
    detector_sweep=sweep,
    capacity_fit_L_per_100pct=round(cap_all, 2),
    level_based_litres_LOO=dict(MAE_L=round(float(np.mean(np.abs(loo))), 2), max_abs_L=round(float(np.max(np.abs(loo))), 2),
                                MAE_pct_of_pump=round(float(np.mean(np.abs(loo) / o.pump_L) * 100), 2)),
    consumption_integration_vs_pump=dict(n=len(T), MAE_L=round(float(T.trapez_err_L.abs().mean()), 2),
                                         max_abs_L=round(float(T.trapez_err_L.abs().max()), 2),
                                         mean_signed_L=round(float(T.trapez_err_L.mean()), 2)),
)
T.to_csv(f'{out}/refuel_truth_mapping.csv', index=False)
o[['lp', 'pump_L', 'level_before', 'level_after', 'dpct', 'level_est_err_L']].to_csv(f'{out}/level_litres_loo.csv', index=False)
json.dump(res, open(f'{out}/results.json', 'w'), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
