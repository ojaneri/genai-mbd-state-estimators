# J013 — Rodada 6: REPLICAÇÃO em outro veículo (Itabira-MG, veículo 2; Kaggle brunops2, CC0), mesma configuração do J012, sem reajuste

Início: 2026-10-02T01:30:49-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `d322907e17bebeb51efff8e4f8136bcaaf472069f039063d72c93395aba45232`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_itabira out/J013 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --res-auto --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J013 | 0 | 8450 s | `d322907e17bebeb51efff8e4f8136bcaaf472069f039063d72c93395aba45232` |

## Linhas "seed … frac …" dos logs

```
J013: seed 0 frac 0.01: real 27.301 | melhor aug_rfill_w1 23.449 | discr gen 0.498625 (real 0.246, ok=False) | id: gen 0.498375 real 0.26866096866096867 ok=False | audit 0.794 | gen 298s | total 388s
J013: seed 0 frac 0.02: real 37.612 | melhor gen_r0.5_w1 37.453 | discr gen 0.49987499999999996 (real 0.487, ok=True) | id: gen 0.4726250000000001 real 0.3228785315079732 ok=False | audit 0.994 | gen 301s | total 822s
J013: seed 0 frac 0.05: real 26.636 | melhor gen_r0.5_w0.3 25.684 | discr gen 0.47850000000000004 (real 0.289, ok=False) | id: gen 0.4650000000000001 real 0.24185747209003017 ok=False | audit 0.993 | gen 300s | total 1264s
J013: seed 0 frac 0.1: real 30.092 | melhor gen_r1_w1 29.455 | discr gen 0.476375 (real 0.358, ok=False) | id: gen 0.42037499999999994 real 0.15461823138171693 ok=False | audit 0.999 | gen 298s | total 1713s
J013: seed 1 frac 0.01: real 34.530 | melhor physonly 32.613 | discr gen 0.49887499999999996 (real 0.416, ok=False) | id: gen 0.492 real 0.2390865384615385 ok=False | audit 0.998 | gen 298s | total 2113s
J013: seed 1 frac 0.02: real 39.062 | melhor physonly 34.637 | discr gen 0.49912500000000004 (real 0.448, ok=False) | id: gen 0.49049999999999994 real 0.2834567901234568 ok=False | audit 0.991 | gen 301s | total 2520s
J013: seed 1 frac 0.05: real 33.361 | melhor gen_rfill_w0.3 32.677 | discr gen 0.4936250000000001 (real 0.447, ok=True) | id: gen 0.461375 real 0.20012492831981654 ok=False | audit 0.996 | gen 298s | total 2966s
J013: seed 1 frac 0.1: real 20.068 | melhor gen_rfill_w1 18.911 | discr gen 0.4225 (real 0.162, ok=False) | id: gen 0.43225 real 0.21324041811846695 ok=False | audit 0.998 | gen 298s | total 3408s
J013: seed 2 frac 0.01: real 30.632 | melhor aug_rfill_w0.3 26.812 | discr gen 0.49912500000000004 (real 0.433, ok=False) | id: gen 0.49812500000000015 real 0.29943019943019933 ok=False | audit 1.000 | gen 300s | total 3788s
J013: seed 2 frac 0.02: real 21.596 | melhor gen_r1_w1 20.099 | discr gen 0.4961249999999999 (real 0.090, ok=False) | id: gen 0.4963750000000001 real 0.2906462585034013 ok=False | audit 0.942 | gen 300s | total 4191s
J013: seed 2 frac 0.05: real 27.149 | melhor aug_r0.5_w1 25.388 | discr gen 0.482 (real 0.315, ok=False) | id: gen 0.46599999999999997 real 0.14992397957194648 ok=False | audit 0.996 | gen 298s | total 4630s
J013: seed 2 frac 0.1: real 25.602 | melhor gen_r0.5_w0.3 23.970 | discr gen 0.4657499999999999 (real 0.228, ok=False) | id: gen 0.455125 real 0.15141890688979887 ok=False | audit 0.998 | gen 301s | total 5076s
J013: seed 3 frac 0.01: real 32.400 | melhor gen_rfill_w1 27.456 | discr gen 0.49924999999999997 (real 0.482, ok=True) | id: gen 0.498375 real 0.3683794466403162 ok=False | audit 1.000 | gen 300s | total 5454s
J013: seed 3 frac 0.02: real 20.124 | melhor gen_rfill_w1 18.718 | discr gen 0.46587499999999993 (real 0.214, ok=False) | id: gen 0.475 real 0.32217688782876164 ok=False | audit 0.998 | gen 298s | total 5889s
J013: seed 3 frac 0.05: real 27.556 | melhor aug_rfill_w0.3 25.625 | discr gen 0.477375 (real 0.323, ok=False) | id: gen 0.4492499999999999 real 0.13697223139283232 ok=False | audit 0.997 | gen 300s | total 6331s
J013: seed 3 frac 0.1: real 31.397 | melhor gen_dfilt_q0.5 30.602 | discr gen 0.47662499999999997 (real 0.378, ok=False) | id: gen 0.420875 real 0.15035172906400385 ok=False | audit 0.993 | gen 301s | total 6778s
J013: seed 4 frac 0.01: real 36.693 | melhor physonly 33.932 | discr gen 0.49950000000000006 (real 0.449, ok=False) | id: gen 0.4978750000000002 real 0.28051282051282045 ok=False | audit 0.890 | gen 298s | total 7163s
J013: seed 4 frac 0.02: real 33.185 | melhor aug_r1_w1 30.804 | discr gen 0.4988750000000002 (real 0.411, ok=False) | id: gen 0.492625 real 0.32236734693877556 ok=False | audit 0.958 | gen 297s | total 7552s
J013: seed 4 frac 0.05: real 28.900 | melhor genphys_rfill_w1 28.283 | discr gen 0.48524999999999996 (real 0.370, ok=False) | id: gen 0.4484999999999999 real 0.1400282624723519 ok=False | audit 0.997 | gen 301s | total 7999s
J013: seed 4 frac 0.1: real 24.055 | melhor gen_r1_w1 23.454 | discr gen 0.44999999999999996 (real 0.245, ok=False) | id: gen 0.4305 real 0.15733247276356432 ok=False | audit 0.993 | gen 299s | total 8446s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T03:52:04-03:00 — duração do job 8475 s
