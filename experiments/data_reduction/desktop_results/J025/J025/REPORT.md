# J025 — HÍBRIDO, caso A' (Itabira, veículo 2)

Início: 2026-10-03T00:51:34-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_itabira out/J025_ita --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --res-auto --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3` | J025_ita | 0 | 7836 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J025_ita: seed 0 frac 0.01: real 27.301 | melhor aug_rfill_w0.3 23.547 | discr gen 0.499 (real 0.246, ok=False) | id: gen 0.49812500000000015 real 0.26866096866096867 ok=False | audit 0.795 | gen 308s | total 401s
J025_ita: seed 0 frac 0.02: real 37.612 | melhor aug_rfill_w0.3 37.585 | discr gen 0.49975 (real 0.487, ok=True) | id: gen 0.4752500000000002 real 0.3228785315079732 ok=False | audit 0.994 | gen 300s | total 801s
J025_ita: seed 0 frac 0.05: real 26.636 | melhor hyb_resid_w0.3 25.320 | discr gen 0.47825000000000006 (real 0.289, ok=False) | id: gen 0.46524999999999994 real 0.24185747209003017 ok=False | audit 0.993 | gen 300s | total 1208s
J025_ita: seed 0 frac 0.1: real 30.092 | melhor hyb_resid_w0.3 29.242 | discr gen 0.4734999999999999 (real 0.358, ok=False) | id: gen 0.42037500000000017 real 0.15461823138171693 ok=False | audit 0.999 | gen 300s | total 1617s
J025_ita: seed 1 frac 0.01: real 34.530 | melhor hyb_resid_w0.3 32.424 | discr gen 0.499 (real 0.416, ok=False) | id: gen 0.491 real 0.2390865384615385 ok=False | audit 0.998 | gen 300s | total 2006s
J025_ita: seed 1 frac 0.02: real 39.062 | melhor physonly 34.637 | discr gen 0.49924999999999997 (real 0.448, ok=False) | id: gen 0.490375 real 0.2834567901234568 ok=False | audit 0.991 | gen 300s | total 2394s
J025_ita: seed 1 frac 0.05: real 33.361 | melhor gen_rfill_w0.3 32.691 | discr gen 0.49424999999999986 (real 0.447, ok=True) | id: gen 0.46299999999999986 real 0.20012492831981654 ok=False | audit 0.996 | gen 286s | total 2783s
J025_ita: seed 1 frac 0.1: real 20.068 | melhor gen_rfill_w0.3 18.910 | discr gen 0.4225 (real 0.162, ok=False) | id: gen 0.4332499999999999 real 0.21324041811846695 ok=False | audit 0.998 | gen 283s | total 3167s
J025_ita: seed 2 frac 0.01: real 30.632 | melhor aug_rfill_w0.3 26.812 | discr gen 0.499 (real 0.433, ok=False) | id: gen 0.4982500000000002 real 0.29943019943019933 ok=False | audit 1.000 | gen 281s | total 3519s
J025_ita: seed 2 frac 0.02: real 21.596 | melhor aug_rfill_w0.3 20.778 | discr gen 0.49487500000000006 (real 0.090, ok=False) | id: gen 0.49587500000000007 real 0.2906462585034013 ok=False | audit 0.942 | gen 281s | total 3891s
J025_ita: seed 2 frac 0.05: real 27.149 | melhor hyb_feat_w0.3 25.592 | discr gen 0.48187499999999994 (real 0.315, ok=False) | id: gen 0.4647499999999999 real 0.14992397957194648 ok=False | audit 0.996 | gen 281s | total 4273s
J025_ita: seed 2 frac 0.1: real 25.602 | melhor hyb_resid_w0.3 24.367 | discr gen 0.46425000000000005 (real 0.228, ok=False) | id: gen 0.4537500000000001 real 0.15141890688979887 ok=False | audit 0.998 | gen 283s | total 4659s
J025_ita: seed 3 frac 0.01: real 32.400 | melhor gen_rfill_w0.3 27.028 | discr gen 0.49924999999999997 (real 0.482, ok=True) | id: gen 0.49824999999999997 real 0.3683794466403162 ok=False | audit 1.000 | gen 289s | total 5018s
J025_ita: seed 3 frac 0.02: real 20.124 | melhor gen_rfill_w0.3 18.730 | discr gen 0.4651250000000001 (real 0.214, ok=False) | id: gen 0.47424999999999995 real 0.32217688782876164 ok=False | audit 0.998 | gen 298s | total 5424s
J025_ita: seed 3 frac 0.05: real 27.556 | melhor aug_rfill_w0.3 25.625 | discr gen 0.47787500000000005 (real 0.323, ok=False) | id: gen 0.44874999999999987 real 0.13697223139283232 ok=False | audit 0.997 | gen 302s | total 5833s
J025_ita: seed 3 frac 0.1: real 31.397 | melhor hyb_resid_w0.3 30.680 | discr gen 0.478125 (real 0.378, ok=False) | id: gen 0.4192500000000001 real 0.15035172906400385 ok=False | audit 0.993 | gen 297s | total 6241s
J025_ita: seed 4 frac 0.01: real 36.693 | melhor physonly 33.932 | discr gen 0.49950000000000006 (real 0.449, ok=False) | id: gen 0.49849999999999994 real 0.28051282051282045 ok=False | audit 0.891 | gen 296s | total 6619s
J025_ita: seed 4 frac 0.02: real 33.185 | melhor aug_rfill_w0.3 32.246 | discr gen 0.49924999999999997 (real 0.411, ok=False) | id: gen 0.49287500000000006 real 0.32236734693877556 ok=False | audit 0.958 | gen 296s | total 6998s
J025_ita: seed 4 frac 0.05: real 28.900 | melhor hyb_feat_w0.3 28.037 | discr gen 0.485375 (real 0.370, ok=False) | id: gen 0.45062500000000016 real 0.1400282624723519 ok=False | audit 0.997 | gen 294s | total 7400s
J025_ita: seed 4 frac 0.1: real 24.055 | melhor hyb_feat_w0.3 23.511 | discr gen 0.45124999999999993 (real 0.245, ok=False) | id: gen 0.43162500000000004 real 0.15733247276356432 ok=False | audit 0.993 | gen 304s | total 7816s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T03:02:50-03:00 — duração do job 7876 s
