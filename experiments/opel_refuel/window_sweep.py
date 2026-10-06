#!/usr/bin/env python3
"""Compromisso disponibilidade x falsos positivos do detector supervisionado em Itabira (veículos 2 e 3):
varia a duração mínima parada (W) e a variação pico-a-pico máxima (P2P) da janela estável."""
import sys, json
import numpy as np, pandas as pd
d = pd.read_csv(f'{sys.argv[1]}/Dataset.csv', sep=';', low_memory=False, na_values=['-'])
d['t'] = pd.to_datetime(d['DeviceTime'], format='%d/%m/%Y %H:%M:%S', errors='coerce')
L, V = 'FuelLevel(FromEngineECU)(%)', 'Speed(OBD)(KM/h)'
out = []
for veh, g in d.dropna(subset=['t']).groupby('Vehicle'):
    g = g.sort_values(['Id', 't']).reset_index(drop=True)
    s = g.dropna(subset=[L])
    if len(s) < 100: continue
    hours = s.groupby('Id').t.agg(lambda z: (z.max() - z.min()).total_seconds()).sum() / 3600
    t, v, lv, tr = g.t.values, g[V].fillna(-1).values, g[L].values, g.Id.values
    for Ws in [5, 10, 20]:
        for P2P in [3, 5, 10, 20]:
            wins = []; i, n = 0, len(t)
            while i < n:
                if v[i] != 0: i += 1; continue
                j = i
                while j + 1 < n and v[j + 1] == 0 and tr[j + 1] == tr[i]: j += 1
                if (t[j] - t[i]) >= np.timedelta64(Ws, 's'):
                    l = lv[i:j + 1]; l = l[~np.isnan(l)]
                    if len(l) and l.max() - l.min() <= P2P: wins.append((np.median(l), tr[i]))
                i = j + 1
            fp = {th: sum(1 for k in range(1, len(wins)) if wins[k][1] == wins[k-1][1] and wins[k][0] - wins[k-1][0] > th) for th in [5, 10, 15]}
            out.append(dict(vehicle=int(veh), min_stop_s=Ws, p2p=P2P, windows=len(wins), windows_per_h=round(len(wins)/hours, 2), FP_th5=fp[5], FP_th10=fp[10], FP_th15=fp[15]))
pd.DataFrame(out).to_csv(sys.argv[2], index=False)
print(pd.DataFrame(out).to_string(index=False))
