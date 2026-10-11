# J017 — Cenário ausente (sem rodovia >80 km/h no treino real e no gerador); medida principal: flow_MAE_hw (só rodovia)

Início: 2026-10-03T05:08:35-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J017_hw --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --hw-absent --seeds 0,1,2,3,4 --fracs 0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3` | J017_hw | 0 | 5237 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J017_hw: seed 0 frac 0.05: real 2.631 | melhor gen_rfill_w0.3 2.487 | discr gen 0.31300000000000006 (real 0.185, ok=False) | id: gen 0.322875 real 0.1668645525062139 ok=False | audit 0.979 | gen 295s | total 529s
J017_hw: seed 0 frac 0.1: real 2.546 | melhor real 2.546 | discr gen 0.29125 (real 0.191, ok=False) | id: gen 0.2906249999999999 real 0.1735 ok=False | audit 0.962 | gen 294s | total 1049s
J017_hw: seed 1 frac 0.05: real 2.613 | melhor gen_rfill_w0.3 2.397 | discr gen 0.360375 (real 0.187, ok=False) | id: gen 0.34887499999999994 real 0.161274120157204 ok=False | audit 0.963 | gen 293s | total 1575s
J017_hw: seed 1 frac 0.1: real 2.492 | melhor gen_rfill_w1 2.374 | discr gen 0.29725 (real 0.210, ok=False) | id: gen 0.28275000000000006 real 0.17300000000000004 ok=False | audit 0.948 | gen 294s | total 2094s
J017_hw: seed 2 frac 0.05: real 2.919 | melhor gen_rfill_w0.3 2.409 | discr gen 0.3213750000000001 (real 0.193, ok=False) | id: gen 0.32337499999999986 real 0.17578288100208772 ok=False | audit 0.973 | gen 294s | total 2620s
J017_hw: seed 2 frac 0.1: real 2.586 | melhor gen_rfill_w0.3 2.478 | discr gen 0.29775000000000007 (real 0.205, ok=False) | id: gen 0.2896249999999999 real 0.17674999999999996 ok=False | audit 0.964 | gen 293s | total 3135s
J017_hw: seed 3 frac 0.05: real 2.542 | melhor gen_rfill_w0.3 2.509 | discr gen 0.337125 (real 0.188, ok=False) | id: gen 0.32799999999999996 real 0.18516129032258066 ok=False | audit 0.980 | gen 293s | total 3661s
J017_hw: seed 3 frac 0.1: real 2.580 | melhor gen_rfill_w0.3 2.343 | discr gen 0.28737499999999994 (real 0.188, ok=False) | id: gen 0.27412499999999995 real 0.165875 ok=False | audit 0.957 | gen 294s | total 4181s
J017_hw: seed 4 frac 0.05: real 2.591 | melhor gen_rfill_w1 2.465 | discr gen 0.29337500000000005 (real 0.178, ok=False) | id: gen 0.30812499999999987 real 0.1648235240813738 ok=False | audit 0.960 | gen 294s | total 4704s
J017_hw: seed 4 frac 0.1: real 2.742 | melhor gen_rfill_w0.3 2.465 | discr gen 0.3313750000000001 (real 0.189, ok=False) | id: gen 0.30362500000000003 real 0.16912500000000008 ok=False | audit 0.967 | gen 293s | total 5224s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T06:36:16-03:00 — duração do job 5261 s
