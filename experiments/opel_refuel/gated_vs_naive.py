#!/usr/bin/env python3
"""Detector de reabastecimento ingênuo (salto entre amostras) vs. supervisionado por contexto
(só compara níveis em janelas estacionárias estáveis — análogo à árvore supervisora de
Dominguez 2026: v = 0 e variação pico-a-pico pequena).

Datasets públicos: Opel Corsa (Kaggle pedro2025, CC BY 4.0; 21 reabastecimentos observáveis)
e Itabira-MG (Kaggle brunops2, CC0; sem reabastecimento dentro das viagens -> toda detecção
dentro de viagem é falso positivo).
Uso: python3 gated_vs_naive.py <pasta_opel> <pasta_itabira> <pasta_saida>
"""
import sys, json
import numpy as np, pandas as pd

opel_dir, ita_dir, out = sys.argv[1:4]
W = pd.Timedelta('20s')   # duração mínima parada
P2P = 3.0                 # variação pico-a-pico máxima do nível na janela (pontos %)
TH = [5, 10, 15, 20, 30]

def stable_windows(t, v, lvl, trip):
    """Janelas com v==0 contínuo por >= W, dentro da mesma viagem, com nível estável."""
    wins = []
    stopped = (v == 0).values
    i, n = 0, len(t)
    while i < n:
        if not stopped[i]: i += 1; continue
        j = i
        while j + 1 < n and stopped[j + 1] and trip[j + 1] == trip[i]: j += 1
        if t[j] - t[i] >= W:
            l = lvl[i:j + 1]; l = l[~np.isnan(l)]
            if len(l) and (l.max() - l.min()) <= P2P:
                wins.append((t[i], t[j], float(np.median(l)), trip[i]))
        i = j + 1
    return wins

def gated_events(wins, th):
    return [(wins[k][0], wins[k][2] - wins[k - 1][2], wins[k - 1][3] == wins[k][3])
            for k in range(1, len(wins)) if wins[k][2] - wins[k - 1][2] > th]

res = {}
# ---------------- Opel ----------------
o = pd.read_csv(f'{opel_dir}/dataset.csv', usecols=['timestamp', 'SPEED', 'FUEL_LEVEL', 'segment_id', 'segment_file'],
                parse_dates=['timestamp']).sort_values('timestamp').reset_index(drop=True)
o['FUEL_LEVEL'] = o.FUEL_LEVEL.ffill().where(o.segment_file.eq(o.segment_file.shift()) | o.FUEL_LEVEL.notna())
seg = o.groupby('segment_id').timestamp.agg(['min', 'max'])
bounds = [(seg.loc[k, 'max'], seg.loc[k + 1, 'min']) for k in seg.index if k + 1 in seg.index]  # 21 reabastecimentos
wins = stable_windows(o.timestamp.values, o.SPEED, o.FUEL_LEVEL.values, o.segment_file.values)
x = o.dropna(subset=['FUEL_LEVEL']); jump = x.FUEL_LEVEL.diff().values; tx = x.timestamp.values
tol = np.timedelta64(2, 'h')
def score(times):
    used, tp = set(), 0
    for a, b in bounds:
        h = [i for i, t in enumerate(times) if a - tol <= t <= b + tol and i not in used]
        if h: tp += 1; used.add(h[0])
    return dict(TP=tp, FN=len(bounds) - tp, FP=len(times) - len(used))
res['opel'] = dict(n_refuels=len(bounds), stable_windows=len(wins),
    naive={th: score([tx[i] for i in np.where(jump > th)[0]]) for th in TH},
    gated={th: score([e[0] for e in gated_events(wins, th)]) for th in TH})

# ---------------- Itabira ----------------
d = pd.read_csv(f'{ita_dir}/Dataset.csv', sep=';', low_memory=False, na_values=['-'])
d['t'] = pd.to_datetime(d['DeviceTime'], format='%d/%m/%Y %H:%M:%S', errors='coerce')
L, V = 'FuelLevel(FromEngineECU)(%)', 'Speed(OBD)(KM/h)'
ita = {}
for veh, g in d.dropna(subset=['t']).groupby('Vehicle'):
    g = g.sort_values(['Id', 't']).reset_index(drop=True)
    s = g.dropna(subset=[L])
    if len(s) < 100: continue
    hours = s.groupby('Id').t.agg(lambda z: (z.max() - z.min()).total_seconds()).sum() / 3600
    dj = s.groupby('Id')[L].diff().values
    trip_net = s.groupby('Id')[L].agg(lambda z: z.iloc[-5:].median() - z.iloc[:5].median())
    w = stable_windows(g.t.values, g[V].fillna(-1), g[L].values, g.Id.values)
    ev = [e for th in TH for e in []]
    ita[int(veh)] = dict(level_rows=len(s), trips=int(s.Id.nunique()), hours=round(hours, 2),
        max_trip_net_rise=round(float(trip_net.max()), 1),
        naive_FP={th: int(np.nansum(dj > th)) for th in TH},
        gated_FP_within_trip={th: sum(1 for e in gated_events(w, th) if e[2]) for th in TH},
        stable_windows=len(w))
    for th in TH:
        ita[int(veh)].setdefault('naive_FP_per_h', {})[th] = round(ita[int(veh)]['naive_FP'][th] / hours, 2)
res['itabira'] = ita
res['params'] = dict(min_stop=str(W), p2p_max_pct=P2P, thresholds=TH)
json.dump(res, open(f'{out}/gated_vs_naive.json', 'w'), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
