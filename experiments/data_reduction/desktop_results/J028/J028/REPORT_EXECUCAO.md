# J028 — P2 TRANSFERÊNCIA entre carros: DDPM pré-treinado no Opel inteiro (../data) e ajustado na fração do Itabira; compara com J013

Início: 2026-10-03T19:30:09-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_itabira out/J028_transf_ita --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --res-auto --pretrain-src ../data --pretrain-iters 50000 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,aug_rfill_w0.3` | J028_transf_ita | 0 | 9089 s | `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b` |

## Linhas "seed … frac …" dos logs

```
J028_transf_ita: seed 0 frac 0.01: real 27.301 | melhor gen_rfill_w0.3 22.822 | discr gen 0.498375 (real 0.246, ok=False) | id: gen 0.49787499999999996 real 0.26866096866096867 ok=False | audit 0.826 | gen 567s | total 641s
J028_transf_ita: seed 0 frac 0.02: real 37.612 | melhor aug_rfill_w0.3 37.585 | discr gen 0.49987500000000007 (real 0.487, ok=True) | id: gen 0.47187500000000004 real 0.3228785315079732 ok=False | audit 0.989 | gen 283s | total 1012s
J028_transf_ita: seed 0 frac 0.05: real 26.636 | melhor aug_rfill_w0.3 26.278 | discr gen 0.48387499999999994 (real 0.289, ok=False) | id: gen 0.47125000000000006 real 0.24185747209003017 ok=False | audit 0.984 | gen 282s | total 1390s
J028_transf_ita: seed 0 frac 0.1: real 30.092 | melhor aug_rfill_w0.3 29.854 | discr gen 0.47550000000000003 (real 0.358, ok=False) | id: gen 0.4262499999999999 real 0.15461823138171693 ok=False | audit 0.997 | gen 282s | total 1770s
J028_transf_ita: seed 1 frac 0.01: real 34.530 | melhor real 34.530 | discr gen 0.49912500000000004 (real 0.416, ok=False) | id: gen 0.4903749999999999 real 0.2390865384615385 ok=False | audit 0.994 | gen 566s | total 2418s
J028_transf_ita: seed 1 frac 0.02: real 39.062 | melhor gen_rfill_w0.3 37.997 | discr gen 0.499375 (real 0.448, ok=False) | id: gen 0.491625 real 0.2834567901234568 ok=False | audit 0.987 | gen 283s | total 2778s
J028_transf_ita: seed 1 frac 0.05: real 33.361 | melhor real 33.361 | discr gen 0.49512500000000004 (real 0.447, ok=True) | id: gen 0.46175 real 0.20012492831981654 ok=False | audit 0.995 | gen 296s | total 3168s
J028_transf_ita: seed 1 frac 0.1: real 20.068 | melhor gen_rfill_w0.3 18.356 | discr gen 0.4248749999999999 (real 0.162, ok=False) | id: gen 0.4355 real 0.21324041811846695 ok=False | audit 0.994 | gen 293s | total 3554s
J028_transf_ita: seed 2 frac 0.01: real 30.632 | melhor aug_rfill_w0.3 26.812 | discr gen 0.499 (real 0.433, ok=False) | id: gen 0.49824999999999997 real 0.29943019943019933 ok=False | audit 1.000 | gen 595s | total 4214s
J028_transf_ita: seed 2 frac 0.02: real 21.596 | melhor aug_rfill_w0.3 20.778 | discr gen 0.4963749999999999 (real 0.090, ok=False) | id: gen 0.4967499999999999 real 0.2906462585034013 ok=False | audit 0.930 | gen 293s | total 4589s
J028_transf_ita: seed 2 frac 0.05: real 27.149 | melhor aug_rfill_w0.3 25.889 | discr gen 0.482 (real 0.315, ok=False) | id: gen 0.46775 real 0.14992397957194648 ok=False | audit 0.992 | gen 299s | total 4985s
J028_transf_ita: seed 2 frac 0.1: real 25.602 | melhor real 25.602 | discr gen 0.44537499999999997 (real 0.228, ok=False) | id: gen 0.428875 real 0.15141890688979887 ok=False | audit 0.996 | gen 299s | total 5380s
J028_transf_ita: seed 3 frac 0.01: real 32.400 | melhor gen_rfill_w0.3 29.250 | discr gen 0.499375 (real 0.482, ok=True) | id: gen 0.49775000000000014 real 0.3683794466403162 ok=False | audit 1.000 | gen 599s | total 6044s
J028_transf_ita: seed 3 frac 0.02: real 20.124 | melhor gen_rfill_w0.3 19.008 | discr gen 0.46624999999999994 (real 0.214, ok=False) | id: gen 0.47387499999999994 real 0.32217688782876164 ok=False | audit 0.997 | gen 294s | total 6433s
J028_transf_ita: seed 3 frac 0.05: real 27.556 | melhor aug_rfill_w0.3 25.625 | discr gen 0.4813750000000001 (real 0.323, ok=False) | id: gen 0.4515 real 0.13697223139283232 ok=False | audit 0.994 | gen 299s | total 6832s
J028_transf_ita: seed 3 frac 0.1: real 31.397 | melhor gen_rfill_w0.3 31.301 | discr gen 0.48099999999999987 (real 0.378, ok=False) | id: gen 0.438875 real 0.15035172906400385 ok=False | audit 0.994 | gen 300s | total 7230s
J028_transf_ita: seed 4 frac 0.01: real 36.693 | melhor gen_rfill_w0.3 35.823 | discr gen 0.49975 (real 0.449, ok=False) | id: gen 0.49687499999999996 real 0.28051282051282045 ok=False | audit 0.912 | gen 601s | total 7903s
J028_transf_ita: seed 4 frac 0.02: real 33.185 | melhor aug_rfill_w0.3 32.246 | discr gen 0.49950000000000006 (real 0.411, ok=False) | id: gen 0.494 real 0.32236734693877556 ok=False | audit 0.970 | gen 301s | total 8279s
J028_transf_ita: seed 4 frac 0.05: real 28.900 | melhor gen_rfill_w0.3 28.597 | discr gen 0.484 (real 0.370, ok=False) | id: gen 0.4358749999999999 real 0.1400282624723519 ok=False | audit 0.995 | gen 300s | total 8679s
J028_transf_ita: seed 4 frac 0.1: real 24.055 | melhor gen_rfill_w0.3 23.865 | discr gen 0.4421250000000001 (real 0.245, ok=False) | id: gen 0.405 real 0.15733247276356432 ok=False | audit 0.991 | gen 300s | total 9075s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T22:02:20-03:00 — duração do job 9131 s
