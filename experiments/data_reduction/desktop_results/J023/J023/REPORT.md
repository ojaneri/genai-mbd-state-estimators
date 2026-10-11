# J023 — HÍBRIDO física + IA generativa (d-0017), caso B (bateria): o sintético do DDPM treina o RESÍDUO do modelo físico

Início: 2026-10-02T15:49:39-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `7e6d22971cb280aa72cd6fa74817b7cb2729bb918e0f295a435f41571589bd97`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J023_bat --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3` | J023_bat | 0 | 12295 s | `7e6d22971cb280aa72cd6fa74817b7cb2729bb918e0f295a435f41571589bd97` |

## Linhas "seed … frac …" dos logs

```
J023_bat: seed 0 frac 0.01: real 0.121 | melhor physonly 0.044 | discr gen 0.4882500000000001 (real 0.476, ok=True) | id: gen 0.48624999999999985 real 0.4735632183908045 ok=True | audit 0.998 | gen 322s | total 580s
J023_bat: seed 0 frac 0.02: real 0.114 | melhor hyb_resid_w0.3 0.035 | discr gen 0.4883749999999999 (real 0.487, ok=True) | id: gen 0.48762499999999986 real 0.4828897338403042 ok=True | audit 0.953 | gen 300s | total 1120s
J023_bat: seed 0 frac 0.05: real 0.063 | melhor hyb_resid_w0.3 0.024 | discr gen 0.44699999999999984 (real 0.452, ok=True) | id: gen 0.43674999999999997 real 0.4388119056565234 ok=True | audit 0.952 | gen 293s | total 1655s
J023_bat: seed 0 frac 0.1: real 0.046 | melhor hyb_resid_w0.3 0.023 | discr gen 0.42737499999999995 (real 0.391, ok=True) | id: gen 0.42225 real 0.380625 ok=True | audit 0.960 | gen 308s | total 2207s
J023_bat: seed 1 frac 0.01: real 0.103 | melhor physonly 0.046 | discr gen 0.48249999999999993 (real 0.465, ok=True) | id: gen 0.483375 real 0.46609195402298853 ok=True | audit 0.987 | gen 304s | total 2751s
J023_bat: seed 1 frac 0.02: real 0.088 | melhor physonly 0.058 | discr gen 0.48762499999999986 (real 0.479, ok=True) | id: gen 0.484375 real 0.4631041899681666 ok=True | audit 0.971 | gen 300s | total 3295s
J023_bat: seed 1 frac 0.05: real 0.047 | melhor physonly 0.022 | discr gen 0.4455 (real 0.433, ok=True) | id: gen 0.4338749999999999 real 0.4273663957874485 ok=True | audit 0.974 | gen 298s | total 3859s
J023_bat: seed 1 frac 0.1: real 0.037 | melhor hyb_resid_w0.3 0.020 | discr gen 0.43337500000000007 (real 0.373, ok=False) | id: gen 0.4205 real 0.35425000000000006 ok=False | audit 0.963 | gen 306s | total 4406s
J023_bat: seed 2 frac 0.01: real 0.110 | melhor physonly 0.040 | discr gen 0.48625000000000007 (real 0.469, ok=True) | id: gen 0.48612500000000003 real 0.48160919540229885 ok=True | audit 0.982 | gen 304s | total 4953s
J023_bat: seed 2 frac 0.02: real 0.078 | melhor hyb_resid_w0.3 0.037 | discr gen 0.48324999999999996 (real 0.474, ok=True) | id: gen 0.47887500000000005 real 0.4549959204167451 ok=True | audit 0.971 | gen 299s | total 5504s
J023_bat: seed 2 frac 0.05: real 0.058 | melhor hyb_resid_w0.3 0.030 | discr gen 0.46075 (real 0.452, ok=True) | id: gen 0.4504999999999999 real 0.43362357080035174 ok=True | audit 0.989 | gen 299s | total 6056s
J023_bat: seed 2 frac 0.1: real 0.032 | melhor physonly 0.018 | discr gen 0.4336249999999999 (real 0.401, ok=True) | id: gen 0.419875 real 0.35350000000000004 ok=False | audit 0.976 | gen 308s | total 6614s
J023_bat: seed 3 frac 0.01: real 0.124 | melhor physonly 0.076 | discr gen 0.48425000000000007 (real 0.467, ok=True) | id: gen 0.48524999999999996 real 0.4768440016956337 ok=True | audit 0.993 | gen 296s | total 7151s
J023_bat: seed 3 frac 0.02: real 0.088 | melhor hyb_resid_w0.3 0.031 | discr gen 0.4804999999999999 (real 0.466, ok=True) | id: gen 0.47825000000000006 real 0.4597121490889666 ok=True | audit 0.948 | gen 299s | total 7698s
J023_bat: seed 3 frac 0.05: real 0.058 | melhor hyb_resid_w0.3 0.024 | discr gen 0.4445 (real 0.441, ok=True) | id: gen 0.443875 real 0.4411311053984577 ok=True | audit 0.980 | gen 298s | total 8242s
J023_bat: seed 3 frac 0.1: real 0.033 | melhor hyb_resid_w0.3 0.019 | discr gen 0.4421250000000001 (real 0.379, ok=False) | id: gen 0.42337500000000006 real 0.36150000000000004 ok=False | audit 0.959 | gen 302s | total 8784s
J023_bat: seed 4 frac 0.01: real 0.121 | melhor hyb_resid_w0.3 0.093 | discr gen 0.4882500000000001 (real 0.466, ok=True) | id: gen 0.49012500000000014 real 0.47690569566007857 ok=True | audit 0.939 | gen 307s | total 9344s
J023_bat: seed 4 frac 0.02: real 0.104 | melhor hyb_resid_w0.3 0.062 | discr gen 0.486375 (real 0.476, ok=True) | id: gen 0.477 real 0.4576802507836991 ok=True | audit 0.960 | gen 329s | total 9982s
J023_bat: seed 4 frac 0.05: real 0.054 | melhor hyb_resid_w0.3 0.027 | discr gen 0.45887500000000014 (real 0.458, ok=True) | id: gen 0.45137499999999997 real 0.430968130659917 ok=True | audit 0.985 | gen 335s | total 10584s
J023_bat: seed 4 frac 0.1: real 0.038 | melhor hyb_resid_w0.3 0.017 | discr gen 0.42925 (real 0.385, ok=True) | id: gen 0.41862500000000014 real 0.35024999999999995 ok=False | audit 0.966 | gen 1092s | total 12279s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T19:15:21-03:00 — duração do job 12343 s
