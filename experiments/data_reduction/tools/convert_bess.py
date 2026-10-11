#!/usr/bin/env python3
"""Caso C (BESS estacionário): converte o dataset de campo de um BESS em contêiner (Qu, Zenodo 10.5281/zenodo.20094787,
CC BY 4.0; 8 meses, 1 cluster, 9 racks, ~400 operações de carga/descarga) para o formato de run3.py --domain battery:
timestamp, CURRENT [A, carga > 0], VOLTAGE [V do rack], TEMP [°C, média de 8 pontos do rack], SOC [0–1, estimativa do BMS,
passo de 1 %], segment_id (mês 1..8: 2024-10..2025-05), segment_file (<mês>_<operação>_R<rack>).
- Séries registradas por evento: reamostradas em grade de DT s com retenção do último valor (zero-order hold).
- Racks usados: 1, 5 e 9 (os 9 racks do cluster têm a mesma corrente); temperatura = média dos sensores 1, 28, 55, ..., 190.
- Grava meta.json com dt_s e a capacidade efetiva estimada (mínimos quadrados de ΔSOC contra a carga acumulada), usada pela
  auditoria física de run3.py. O SOC é a estimativa do BMS (não é medida de laboratório): o sensor virtual reproduz o BMS.
Modo 'temp' (d-0020, caso C2): em vez do SOC, grava TCELL = sensor de temperatura 109 do rack (meio) e TREF = média dos
outros 7 sensores (1, 28, 55, 82, 136, 163, 190) — sensor virtual de temperatura com verdade MEDIDA.
Requer h5py e mat-io (pip install h5py mat-io). Uso: python convert_bess.py <pasta_com_.mat> <pasta_saida> [DT=5] [temp]"""
import sys, os, glob, json, time
import numpy as np, pandas as pd, h5py
from matio.v7.matreader7 import read_subsystem
from matio.utils.converters.mattimes import mat_to_datetime
import warnings; warnings.filterwarnings('ignore')
src, out = sys.argv[1], sys.argv[2]; DT = float(sys.argv[3]) if len(sys.argv) > 3 else 5.0
TEMP_MODE = len(sys.argv) > 4 and sys.argv[4] == 'temp'; TGT_PT = 109
os.makedirs(out, exist_ok=True)
RACKS = (1, 5, 9); TPTS = list(range(1, 217, 27))
files = sorted(glob.glob(f'{src}/OperationCondition_*_All.mat'))
rows = []; caps = []
for mi, fn in enumerate(files, 1):
    month = os.path.basename(fn).split('_')[1]; t0 = time.time()
    f = h5py.File(fn, 'r'); ss = read_subsystem(f, '<', False, False)
    top = f[f'OperationCondition_{month}_All']
    def tt(ref): return mat_to_datetime(ss.get_properties(int(np.array(ref).ravel()[-2]))).ravel().astype('datetime64[ms]').astype(np.int64) / 1000.0
    def series(ts, vs, grid):   # retenção do último valor (o valor vale até o próximo evento)
        idx = np.searchsorted(ts, grid, side='right') - 1
        return np.where(idx >= 0, vs[np.clip(idx, 0, None)], np.nan)
    for op in sorted(top.keys(), key=lambda s: int(s.replace('Operation', ''))):
        o = top[op]
        for r in RACKS:
            try:
                tc, ic = tt(o[f'Rack{r}CurrentTime']), np.array(o[f'Rack{r}CurrentValue']).ravel()
                tv, vv = tt(o[f'Rack{r}VoltageTime']), np.array(o[f'Rack{r}VoltageValue']).ravel()
                tsoc, sv = tt(o[f'Rack{r}SOCTime']), np.array(o[f'Rack{r}SOCValue']).ravel()
                temps = []
                for k in TPTS:
                    g = o[f'Rack{r}'][f'Temperature{k}']
                    temps.append((tt(g['t']), np.array(g['value']).ravel()))
            except KeyError:
                continue
            grid = np.arange(tc[0], tc[-1], DT)
            if len(grid) < 60: continue
            TS = np.stack([series(a, b, grid) for a, b in temps])
            T = np.nanmean(TS, 0)
            if TEMP_MODE:
                k = TPTS.index(TGT_PT); TCELL = TS[k]; TREF = np.nanmean(np.delete(TS, k, 0), 0)
            d = pd.DataFrame({'timestamp': pd.to_datetime(grid, unit='s'), 'CURRENT': -series(tc, ic, grid),   # carga > 0
                              'VOLTAGE': series(tv, vv, grid), 'TEMP': T, 'SOC': series(tsoc, sv, grid) / 100.0,
                              'segment_id': mi, 'segment_file': f'{month}_{op}_R{r}'})
            if TEMP_MODE:
                d = d.drop(columns=['TEMP', 'SOC']).assign(TREF=TREF, TCELL=TCELL)[['timestamp', 'CURRENT', 'VOLTAGE', 'TREF', 'TCELL', 'segment_id', 'segment_file']]
                d = d.dropna()
                if len(d) >= 60: rows.append(d)
                continue
            d = d.dropna()
            if len(d) < 60: continue
            ah = d.CURRENT.values * DT / 3600.0
            if np.ptp(d.SOC) > 0.3: caps.append(np.sum(ah) / (d.SOC.iloc[-1] - d.SOC.iloc[0]))
            rows.append(d)
    f.close(); print(month, 'ok', round(time.time() - t0), 's', flush=True)
o = pd.concat(rows).reset_index(drop=True); o.to_csv(f'{out}/dataset.csv', index=False)
cap = float(np.median(caps)) if caps else None
json.dump(dict(mode='temp' if TEMP_MODE else 'soc', target_point=TGT_PT if TEMP_MODE else None, dt_s=DT, cap_ah=cap, cells_series=396,   # 396 células por rack (descrição do dataset); run3 usa V/célula
 n_cap_estimates=len(caps), racks=RACKS, temp_points=TPTS, source='zenodo.20094787'),
          open(f'{out}/meta.json', 'w'), indent=1)
print('linhas', len(o), 'segmentos', o.segment_file.nunique(), 'capacidade efetiva (Ah)', cap)
