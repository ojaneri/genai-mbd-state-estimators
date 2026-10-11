# J018 — Baseline estatístico clássico: VAR(3) como gerador no teste — proposto pelo desktop

Início: 2026-10-03T06:36:49-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J018_var --gen var --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J018_var | 0 | 4500 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J018_var: seed 0 frac 0.01: real 2.983 | melhor genphys_rfill_w0.3 2.888 | discr gen 0.49187499999999995 (real 0.177, ok=False) | id: gen 0.490625 real 0.1202453987730061 ok=False | audit 0.873 | gen 0s | total 233s
J018_var: seed 0 frac 0.02: real 2.909 | melhor genphys_rfill_w1 2.729 | discr gen 0.48787500000000006 (real 0.147, ok=False) | id: gen 0.48475 real 0.09070943451941538 ok=False | audit 0.852 | gen 0s | total 462s
J018_var: seed 0 frac 0.05: real 2.427 | melhor genphys_rfill_w1 2.376 | discr gen 0.485 (real 0.226, ok=False) | id: gen 0.485375 real 0.13937500000000003 ok=False | audit 0.880 | gen 0s | total 675s
J018_var: seed 0 frac 0.1: real 2.329 | melhor genphys_rfill_w0.3 2.292 | discr gen 0.486 (real 0.130, ok=False) | id: gen 0.48787500000000006 real 0.051875000000000115 ok=False | audit 0.869 | gen 0s | total 885s
J018_var: seed 1 frac 0.01: real 3.151 | melhor real 3.151 | discr gen 0.48725000000000007 (real 0.182, ok=False) | id: gen 0.48587500000000006 real 0.1528475327752934 ok=False | audit 0.874 | gen 0s | total 1114s
J018_var: seed 1 frac 0.02: real 2.695 | melhor genphys_rfill_w1 2.537 | discr gen 0.491375 (real 0.114, ok=False) | id: gen 0.489625 real 0.0906507692307692 ok=False | audit 0.863 | gen 0s | total 1346s
J018_var: seed 1 frac 0.05: real 2.551 | melhor genphys_rfill_w0.3 2.474 | discr gen 0.48550000000000004 (real 0.169, ok=False) | id: gen 0.48712500000000003 real 0.08446194225721781 ok=False | audit 0.878 | gen 0s | total 1573s
J018_var: seed 1 frac 0.1: real 2.362 | melhor genphys_rfill_w1 2.362 | discr gen 0.48350000000000004 (real 0.144, ok=False) | id: gen 0.48724999999999985 real 0.050000000000000044 ok=False | audit 0.888 | gen 0s | total 1790s
J018_var: seed 2 frac 0.01: real 3.063 | melhor genphys_rfill_w0.3 2.812 | discr gen 0.4873749999999999 (real 0.142, ok=False) | id: gen 0.4883749999999999 real 0.10604026845637582 ok=False | audit 0.899 | gen 0s | total 2026s
J018_var: seed 2 frac 0.02: real 2.834 | melhor genphys_rfill_w1 2.599 | discr gen 0.48550000000000004 (real 0.145, ok=False) | id: gen 0.48687500000000006 real 0.061003093414764065 ok=False | audit 0.884 | gen 0s | total 2258s
J018_var: seed 2 frac 0.05: real 2.513 | melhor genphys_rfill_w0.3 2.480 | discr gen 0.48725000000000007 (real 0.164, ok=False) | id: gen 0.48575 real 0.08074999999999999 ok=False | audit 0.889 | gen 0s | total 2489s
J018_var: seed 2 frac 0.1: real 2.322 | melhor genphys_rfill_w0.3 2.309 | discr gen 0.48550000000000004 (real 0.158, ok=False) | id: gen 0.48612500000000003 real 0.055499999999999994 ok=False | audit 0.905 | gen 0s | total 2703s
J018_var: seed 3 frac 0.01: real 3.017 | melhor genphys_rfill_w0.3 2.901 | discr gen 0.4880000000000001 (real 0.193, ok=False) | id: gen 0.48424999999999996 real 0.13445712182554304 ok=False | audit 0.913 | gen 0s | total 2937s
J018_var: seed 3 frac 0.02: real 2.977 | melhor genphys_rfill_w0.3 2.788 | discr gen 0.48849999999999993 (real 0.191, ok=False) | id: gen 0.4883749999999999 real 0.11971987144400942 ok=False | audit 0.839 | gen 0s | total 3172s
J018_var: seed 3 frac 0.05: real 2.461 | melhor genphys_rfill_w0.3 2.386 | discr gen 0.4876250000000001 (real 0.190, ok=False) | id: gen 0.486375 real 0.09550000000000003 ok=False | audit 0.911 | gen 0s | total 3402s
J018_var: seed 3 frac 0.1: real 2.320 | melhor genphys_rfill_w1 2.295 | discr gen 0.48762499999999986 (real 0.118, ok=False) | id: gen 0.4873749999999999 real 0.049000000000000044 ok=False | audit 0.887 | gen 0s | total 3610s
J018_var: seed 4 frac 0.01: real 3.109 | melhor genphys_r1_w1 2.989 | discr gen 0.48787500000000006 (real 0.124, ok=False) | id: gen 0.4877499999999999 real 0.07631485541288241 ok=False | audit 0.884 | gen 0s | total 3840s
J018_var: seed 4 frac 0.02: real 2.856 | melhor genphys_rfill_w0.3 2.773 | discr gen 0.48849999999999993 (real 0.144, ok=False) | id: gen 0.48650000000000004 real 0.1001595811179502 ok=False | audit 0.848 | gen 0s | total 4064s
J018_var: seed 4 frac 0.05: real 2.463 | melhor genphys_rfill_w0.3 2.404 | discr gen 0.48650000000000004 (real 0.136, ok=False) | id: gen 0.48587499999999983 real 0.05431329449596434 ok=False | audit 0.881 | gen 0s | total 4289s
J018_var: seed 4 frac 0.1: real 2.304 | melhor genphys_rfill_w1 2.297 | discr gen 0.48975000000000013 (real 0.161, ok=False) | id: gen 0.4886250000000001 real 0.05712499999999998 ok=False | audit 0.848 | gen 0s | total 4496s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T07:52:14-03:00 — duração do job 4525 s
