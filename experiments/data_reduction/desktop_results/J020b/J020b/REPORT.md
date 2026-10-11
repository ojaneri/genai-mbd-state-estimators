# J020b — Caso B: REFAZ o J020 com a auditoria corrigida (d-0016). O J020 original rejeitou 100 % do sintético (alerta do

Início: 2026-10-02T06:30:20-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J020b --domain battery --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly` | J020b | 0 | 10674 s | `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1` |

## Linhas "seed … frac …" dos logs

```
J020b: seed 0 frac 0.01: real 0.121 | melhor physonly 0.044 | discr gen 0.48775000000000013 (real 0.476, ok=True) | id: gen 0.48424999999999996 real 0.4735632183908045 ok=True | audit 0.998 | gen 299s | total 536s
J020b: seed 0 frac 0.02: real 0.114 | melhor physonly 0.040 | discr gen 0.48750000000000004 (real 0.487, ok=True) | id: gen 0.48725000000000007 real 0.4828897338403042 ok=True | audit 0.953 | gen 302s | total 1071s
J020b: seed 0 frac 0.05: real 0.063 | melhor physonly 0.027 | discr gen 0.44575 (real 0.452, ok=True) | id: gen 0.43974999999999986 real 0.4388119056565234 ok=True | audit 0.951 | gen 302s | total 1607s
J020b: seed 0 frac 0.1: real 0.046 | melhor physonly 0.025 | discr gen 0.430125 (real 0.391, ok=True) | id: gen 0.4255000000000001 real 0.380625 ok=True | audit 0.960 | gen 303s | total 2135s
J020b: seed 1 frac 0.01: real 0.103 | melhor physonly 0.046 | discr gen 0.48275 (real 0.465, ok=True) | id: gen 0.48487499999999994 real 0.46609195402298853 ok=True | audit 0.987 | gen 303s | total 2670s
J020b: seed 1 frac 0.02: real 0.088 | melhor physonly 0.058 | discr gen 0.4877499999999999 (real 0.479, ok=True) | id: gen 0.484 real 0.4631041899681666 ok=True | audit 0.971 | gen 300s | total 3203s
J020b: seed 1 frac 0.05: real 0.047 | melhor physonly 0.022 | discr gen 0.44499999999999995 (real 0.433, ok=True) | id: gen 0.43775 real 0.4273663957874485 ok=True | audit 0.974 | gen 299s | total 3735s
J020b: seed 1 frac 0.1: real 0.037 | melhor physonly 0.020 | discr gen 0.4355 (real 0.373, ok=False) | id: gen 0.420875 real 0.35425000000000006 ok=False | audit 0.963 | gen 299s | total 4266s
J020b: seed 2 frac 0.01: real 0.110 | melhor physonly 0.040 | discr gen 0.4870000000000001 (real 0.469, ok=True) | id: gen 0.48512500000000003 real 0.48160919540229885 ok=True | audit 0.982 | gen 298s | total 4801s
J020b: seed 2 frac 0.02: real 0.078 | melhor physonly 0.038 | discr gen 0.48149999999999993 (real 0.474, ok=True) | id: gen 0.476 real 0.4549959204167451 ok=True | audit 0.971 | gen 299s | total 5336s
J020b: seed 2 frac 0.05: real 0.058 | melhor physonly 0.031 | discr gen 0.46362499999999984 (real 0.452, ok=True) | id: gen 0.4525 real 0.43362357080035174 ok=True | audit 0.989 | gen 303s | total 5872s
J020b: seed 2 frac 0.1: real 0.032 | melhor physonly 0.018 | discr gen 0.43412499999999987 (real 0.401, ok=True) | id: gen 0.4255000000000001 real 0.35350000000000004 ok=False | audit 0.976 | gen 304s | total 6401s
J020b: seed 3 frac 0.01: real 0.124 | melhor physonly 0.076 | discr gen 0.48375 (real 0.467, ok=True) | id: gen 0.48612500000000003 real 0.4768440016956337 ok=True | audit 0.993 | gen 303s | total 6936s
J020b: seed 3 frac 0.02: real 0.088 | melhor physonly 0.035 | discr gen 0.47987500000000005 (real 0.466, ok=True) | id: gen 0.4776250000000001 real 0.4597121490889666 ok=True | audit 0.948 | gen 303s | total 7475s
J020b: seed 3 frac 0.05: real 0.058 | melhor physonly 0.027 | discr gen 0.44762500000000005 (real 0.441, ok=True) | id: gen 0.4385 real 0.4411311053984577 ok=True | audit 0.980 | gen 302s | total 8006s
J020b: seed 3 frac 0.1: real 0.033 | melhor physonly 0.020 | discr gen 0.44562500000000005 (real 0.379, ok=False) | id: gen 0.42462500000000003 real 0.36150000000000004 ok=False | audit 0.959 | gen 298s | total 8530s
J020b: seed 4 frac 0.01: real 0.121 | melhor physonly 0.098 | discr gen 0.4886250000000001 (real 0.466, ok=True) | id: gen 0.491375 real 0.47690569566007857 ok=True | audit 0.939 | gen 299s | total 9066s
J020b: seed 4 frac 0.02: real 0.104 | melhor physonly 0.062 | discr gen 0.486 (real 0.476, ok=True) | id: gen 0.4783750000000001 real 0.4576802507836991 ok=True | audit 0.960 | gen 298s | total 9607s
J020b: seed 4 frac 0.05: real 0.054 | melhor physonly 0.032 | discr gen 0.454125 (real 0.458, ok=True) | id: gen 0.45137499999999997 real 0.430968130659917 ok=True | audit 0.985 | gen 300s | total 10141s
J020b: seed 4 frac 0.1: real 0.038 | melhor physonly 0.021 | discr gen 0.43162500000000004 (real 0.385, ok=True) | id: gen 0.414875 real 0.35024999999999995 ok=False | audit 0.966 | gen 303s | total 10669s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T09:28:38-03:00 — duração do job 10698 s
