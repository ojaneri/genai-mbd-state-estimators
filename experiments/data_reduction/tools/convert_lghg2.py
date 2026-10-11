#!/usr/bin/env python3
"""Caso B (bateria): baixa e converte os ciclos de condução do dataset LG 18650HG2 (McMaster, Kollmeyer et al.,
Mendeley Data doi:10.17632/cp3473x7xv.3, CC BY 4.0) para o formato de run3b.py: timestamp, CURRENT [A],
VOLTAGE [V], TEMP [°C], SOC [0–1], segment_id, segment_file.
- Ciclos: UDDS, HWFET, LA92, US06, Mixed1..Mixed8 em 6 temperaturas (−20, −10, 0, 10, 25, 40 °C).
- Reamostragem: média em janelas de 1 s (dados originais a ~10 Hz).
- SOC = 1 + Ah acumulado / 3,0 Ah (capacidade nominal; cada ciclo começa após carga completa). Documentado como
  referência por contagem de carga do equipamento de laboratório (precisão 0,1 % FS).
- segment_id = índice do ciclo (UDDS=1, HWFET=2, LA92=3, US06=4, Mixed1..8 = 5..12); segment_file = <temp>_<ciclo>.
Uso: python3 convert_lghg2.py <pasta_cache_csv> <pasta_saida>"""
import sys, os, json, re, urllib.request, io
import numpy as np, pandas as pd
cache, out = sys.argv[1], sys.argv[2]; os.makedirs(cache, exist_ok=True); os.makedirs(out, exist_ok=True)
API = 'https://data.mendeley.com/public-api/datasets/cp3473x7xv'
UA = {'User-Agent': 'Mozilla/5.0 (research data download)'}
def _get(url): return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300)
CYC = ['UDDS', 'HWFET', 'LA92', 'US06'] + [f'Mixed{i}' for i in range(1, 9)]
folders = json.load(_get(f'{API}/folders/3'))
rows = []
for fo in folders:
    if not re.fullmatch(r'n?\d+degC', fo['name']): continue
    temp = fo['name']
    files = json.load(_get(f"{API}/files?folder_id={fo['id']}&version=3"))
    for f in files:
        m = re.fullmatch(r'\d+_(\w+)\.csv', f['filename'])
        if not m or m.group(1) not in CYC: continue
        cyc = m.group(1); dst = f'{cache}/{temp}_{cyc}.csv'
        if not os.path.exists(dst):
            open(dst, 'wb').write(_get(f['content_details']['download_url']).read())
        raw = open(dst, encoding='latin-1').read().splitlines()
        h = next(i for i, l in enumerate(raw) if l.startswith('Time Stamp'))
        d = pd.read_csv(io.StringIO('\n'.join([raw[h]] + raw[h + 2:])))
        t = pd.to_timedelta(d['Prog Time']).dt.total_seconds()
        d = pd.DataFrame({'t': (t - t.iloc[0]).astype(int), 'CURRENT': d['Current'], 'VOLTAGE': d['Voltage'],
                          'TEMP': d['Temperature'], 'AH': d['Capacity']})
        g = d.groupby('t').mean().reset_index()
        g['SOC'] = 1 + g.AH / 3.0
        g['timestamp'] = pd.Timestamp('2018-01-01') + pd.to_timedelta(g.t, unit='s')
        g['segment_id'] = CYC.index(cyc) + 1; g['segment_file'] = f'{temp}_{cyc}'
        rows.append(g[['timestamp', 'CURRENT', 'VOLTAGE', 'TEMP', 'SOC', 'segment_id', 'segment_file']])
        print(temp, cyc, len(g), round(g.SOC.min(), 3), flush=True)
o = pd.concat(rows).sort_values(['segment_file', 'timestamp']).reset_index(drop=True)
o.to_csv(f'{out}/dataset.csv', index=False)
print('linhas', len(o), 'ciclos', o.segment_file.nunique())
