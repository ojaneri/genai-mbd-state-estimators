#!/usr/bin/env python3
"""Converte o dataset público Itabira-MG (Kaggle brunops2/obd-2-vehicular-dataset-trace, CC0) para o formato
usado por run3.py (o mesmo do Opel): timestamp, SPEED, RPM, THROTTLE_POS, REAL_FUEL_USAGE_ML_MIN,
segment_id, segment_file. Usa só o veículo 2. As viagens (Id) são ordenadas pelo início e agrupadas em 22
blocos cronológicos (segment_id 1..22) para reaproveitar a mesma divisão do Opel (treino 8–17, validação
15–17, teste 18–22). Não há registro de litros na bomba (run3 omite litres_MAE).
Uso: python3 convert_itabira.py <Dataset.csv> <pasta_saida>"""
import sys, os
import numpy as np, pandas as pd
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
d = pd.read_csv(src, sep=';', low_memory=False, na_values=['-'])
d = d[d.Vehicle == 2].copy()
d['timestamp'] = pd.to_datetime(d['DeviceTime'], format='%d/%m/%Y %H:%M:%S', errors='coerce')
d = d.dropna(subset=['timestamp'])
o = pd.DataFrame({'timestamp': d.timestamp, 'SPEED': d['Speed(OBD)(KM/h)'], 'RPM': d['EngineRPM(RPM)'],
                  'THROTTLE_POS': d['ThrottlePosition(Manifold)(%)'], 'REAL_FUEL_USAGE_ML_MIN': d['FuelFlowRate/Minute(cc/min)'],
                  'segment_file': d['Id'].astype(int)})
starts = o.groupby('segment_file').timestamp.min().sort_values()
blocks = np.array_split(starts.index.values, 22)
bmap = {t: i + 1 for i, b in enumerate(blocks) for t in b}
o['segment_id'] = o.segment_file.map(bmap)
o = o.sort_values(['segment_id', 'timestamp']).reset_index(drop=True)
o.to_csv(f'{out}/dataset.csv', index=False)
print('linhas', len(o), 'viagens', o.segment_file.nunique(), 'viagens por bloco', [len(b) for b in blocks])
