# J024 — HÍBRIDO, caso A (Opel), sementes NOVAS 10–14

Início: 2026-10-02T19:16:32-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J024_opel --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 10,11,12,13,14 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3` | J024_opel | 0 | 20000 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J024_opel: seed 10 frac 0.01: real 3.328 | melhor gen_rfill_w0.3 2.888 | discr gen 0.42974999999999997 (real 0.149, ok=False) | id: gen 0.4262499999999999 real 0.11910154372095505 ok=False | audit 0.994 | gen 9188s | total 9456s
J024_opel: seed 10 frac 0.02: real 2.710 | melhor gen_rfill_w0.3 2.527 | discr gen 0.3431249999999999 (real 0.156, ok=False) | id: gen 0.3151249999999999 real 0.06778701228963013 ok=False | audit 0.991 | gen 331s | total 10037s
J024_opel: seed 10 frac 0.05: real 2.459 | melhor hyb_feat_w0.3 2.337 | discr gen 0.27674999999999994 (real 0.147, ok=False) | id: gen 0.23212500000000014 real 0.10425000000000006 ok=False | audit 0.953 | gen 307s | total 10604s
J024_opel: seed 10 frac 0.1: real 2.296 | melhor genphys_rfill_w0.3 2.239 | discr gen 0.277 (real 0.172, ok=False) | id: gen 0.190125 real 0.05400000000000005 ok=False | audit 0.945 | gen 337s | total 11178s
J024_opel: seed 11 frac 0.01: real 3.685 | melhor gen_rfill_w0.3 2.965 | discr gen 0.40512499999999996 (real 0.130, ok=False) | id: gen 0.4126249999999999 real 0.11426553672316386 ok=False | audit 0.964 | gen 309s | total 11735s
J024_opel: seed 11 frac 0.02: real 2.756 | melhor gen_rfill_w0.3 2.413 | discr gen 0.30337499999999995 (real 0.174, ok=False) | id: gen 0.26525 real 0.10222877621634985 ok=False | audit 0.977 | gen 307s | total 12288s
J024_opel: seed 11 frac 0.05: real 2.421 | melhor gen_rfill_w0.3 2.289 | discr gen 0.26812500000000006 (real 0.156, ok=False) | id: gen 0.21350000000000002 real 0.07047234816550607 ok=False | audit 0.973 | gen 300s | total 12830s
J024_opel: seed 11 frac 0.1: real 2.312 | melhor gen_rfill_w0.3 2.264 | discr gen 0.22912500000000002 (real 0.168, ok=False) | id: gen 0.18200000000000005 real 0.04512499999999997 ok=False | audit 0.951 | gen 301s | total 13363s
J024_opel: seed 12 frac 0.01: real 2.948 | melhor gen_rfill_w0.3 2.530 | discr gen 0.36512500000000014 (real 0.095, ok=False) | id: gen 0.36187500000000006 real 0.08185753550160324 ok=False | audit 0.989 | gen 300s | total 13914s
J024_opel: seed 12 frac 0.02: real 2.827 | melhor gen_rfill_w0.3 2.500 | discr gen 0.34550000000000003 (real 0.159, ok=False) | id: gen 0.33575 real 0.11700404858299596 ok=False | audit 0.972 | gen 300s | total 14464s
J024_opel: seed 12 frac 0.05: real 2.481 | melhor gen_rfill_w0.3 2.315 | discr gen 0.2582500000000001 (real 0.156, ok=False) | id: gen 0.20237499999999986 real 0.07174999999999998 ok=False | audit 0.962 | gen 301s | total 15008s
J024_opel: seed 12 frac 0.1: real 2.335 | melhor genphys_rfill_w0.3 2.269 | discr gen 0.24625000000000008 (real 0.165, ok=False) | id: gen 0.18837500000000007 real 0.0316249999999999 ok=False | audit 0.941 | gen 303s | total 15552s
J024_opel: seed 13 frac 0.01: real 3.790 | melhor hyb_resid_w0.3 2.950 | discr gen 0.444125 (real 0.223, ok=False) | id: gen 0.44000000000000006 real 0.1803973509933774 ok=False | audit 0.982 | gen 301s | total 16095s
J024_opel: seed 13 frac 0.02: real 2.803 | melhor hyb_resid_w0.3 2.538 | discr gen 0.31799999999999995 (real 0.142, ok=False) | id: gen 0.32362500000000005 real 0.12326388888888895 ok=False | audit 0.996 | gen 299s | total 16644s
J024_opel: seed 13 frac 0.05: real 2.409 | melhor gen_rfill_w0.3 2.306 | discr gen 0.25612499999999994 (real 0.165, ok=False) | id: gen 0.194125 real 0.0615 ok=False | audit 0.980 | gen 297s | total 17225s
J024_opel: seed 13 frac 0.1: real 2.351 | melhor genphys_rfill_w0.3 2.283 | discr gen 0.2397499999999999 (real 0.128, ok=False) | id: gen 0.19400000000000006 real 0.07300000000000006 ok=False | audit 0.963 | gen 303s | total 17767s
J024_opel: seed 14 frac 0.01: real 3.076 | melhor gen_rfill_w0.3 2.590 | discr gen 0.39175000000000004 (real 0.174, ok=False) | id: gen 0.3647499999999999 real 0.10372122581556276 ok=False | audit 0.986 | gen 321s | total 18349s
J024_opel: seed 14 frac 0.02: real 2.708 | melhor genphys_rfill_w0.3 2.531 | discr gen 0.3147500000000001 (real 0.192, ok=False) | id: gen 0.3157500000000001 real 0.13772668412419786 ok=False | audit 0.982 | gen 302s | total 18905s
J024_opel: seed 14 frac 0.05: real 2.456 | melhor gen_rfill_w0.3 2.323 | discr gen 0.26 (real 0.154, ok=False) | id: gen 0.21675 real 0.10787500000000005 ok=False | audit 0.983 | gen 304s | total 19449s
J024_opel: seed 14 frac 0.1: real 2.309 | melhor gen_rfill_w0.3 2.247 | discr gen 0.2300000000000001 (real 0.133, ok=False) | id: gen 0.16625000000000012 real 0.03862500000000002 ok=False | audit 0.956 | gen 301s | total 19986s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T00:50:42-03:00 — duração do job 20050 s
