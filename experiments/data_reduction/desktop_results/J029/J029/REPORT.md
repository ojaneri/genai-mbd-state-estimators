# J029 — P3 base: bateria SÓ COM FRIO (−20, −10, 0 °C), sem pré-treino

Início: 2026-10-03T15:34:03-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J029_frio_base --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --temps n20degC,n10degC,0degC --seeds 0,1,2,3,4 --fracs 0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3` | J029_frio_base | 0 | 6174 s | `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b` |

## Linhas "seed … frac …" dos logs

```
J029_frio_base: seed 0 frac 0.02: real 0.217 | melhor physonly 0.052 | discr gen 0.49049999999999994 (real 0.463, ok=True) | id: gen 0.4877499999999999 real 0.46461324687355243 ok=True | audit 0.912 | gen 283s | total 414s
J029_frio_base: seed 0 frac 0.05: real 0.090 | melhor physonly 0.036 | discr gen 0.4806250000000001 (real 0.445, ok=True) | id: gen 0.47225000000000006 real 0.4341294074540347 ok=True | audit 0.987 | gen 282s | total 829s
J029_frio_base: seed 0 frac 0.1: real 0.055 | melhor physonly 0.027 | discr gen 0.4424999999999999 (real 0.404, ok=True) | id: gen 0.44700000000000006 real 0.40091706453887244 ok=True | audit 0.962 | gen 282s | total 1241s
J029_frio_base: seed 1 frac 0.02: real 0.095 | melhor real 0.095 | discr gen 0.49512500000000015 (real 0.477, ok=True) | id: gen 0.49524999999999986 real 0.47339449541284395 ok=True | audit 0.986 | gen 282s | total 1643s
J029_frio_base: seed 1 frac 0.05: real 0.079 | melhor hyb_resid_w0.3 0.030 | discr gen 0.47062500000000007 (real 0.453, ok=True) | id: gen 0.469 real 0.4537091988130564 ok=True | audit 0.945 | gen 283s | total 2058s
J029_frio_base: seed 1 frac 0.1: real 0.049 | melhor physonly 0.025 | discr gen 0.46162500000000006 (real 0.413, ok=True) | id: gen 0.4651249999999999 real 0.4212123380881163 ok=True | audit 0.984 | gen 282s | total 2470s
J029_frio_base: seed 2 frac 0.02: real 0.190 | melhor gen_rfill_w0.3 0.170 | discr gen 0.49875 (real 0.484, ok=True) | id: gen 0.497625 real 0.48354430379746827 ok=True | audit 0.997 | gen 282s | total 2862s
J029_frio_base: seed 2 frac 0.05: real 0.092 | melhor hyb_resid_w0.3 0.037 | discr gen 0.4767499999999998 (real 0.453, ok=True) | id: gen 0.47925000000000006 real 0.4563906844542245 ok=True | audit 0.983 | gen 283s | total 3278s
J029_frio_base: seed 2 frac 0.1: real 0.048 | melhor hyb_resid_w0.3 0.025 | discr gen 0.4564999999999999 (real 0.413, ok=True) | id: gen 0.459375 real 0.4023597723964537 ok=False | audit 0.974 | gen 283s | total 3690s
J029_frio_base: seed 3 frac 0.02: real 0.180 | melhor physonly 0.047 | discr gen 0.4943750000000001 (real 0.459, ok=True) | id: gen 0.492375 real 0.4620689655172414 ok=True | audit 0.940 | gen 283s | total 4103s
J029_frio_base: seed 3 frac 0.05: real 0.065 | melhor hyb_resid_w0.3 0.031 | discr gen 0.47824999999999984 (real 0.442, ok=True) | id: gen 0.47687499999999994 real 0.45296167247386754 ok=True | audit 0.968 | gen 283s | total 4518s
J029_frio_base: seed 3 frac 0.1: real 0.076 | melhor hyb_resid_w0.3 0.027 | discr gen 0.45899999999999996 (real 0.429, ok=True) | id: gen 0.4574999999999999 real 0.42503748125937035 ok=True | audit 0.958 | gen 283s | total 4932s
J029_frio_base: seed 4 frac 0.02: real 0.204 | melhor hyb_resid_w0.3 0.107 | discr gen 0.49249999999999994 (real 0.476, ok=True) | id: gen 0.4817499999999999 real 0.4558620689655173 ok=True | audit 0.961 | gen 282s | total 5342s
J029_frio_base: seed 4 frac 0.05: real 0.084 | melhor hyb_resid_w0.3 0.030 | discr gen 0.4811249999999999 (real 0.450, ok=True) | id: gen 0.4685 real 0.4402298850574713 ok=True | audit 0.958 | gen 283s | total 5757s
J029_frio_base: seed 4 frac 0.1: real 0.054 | melhor hyb_resid_w0.3 0.023 | discr gen 0.45225000000000004 (real 0.392, ok=False) | id: gen 0.4455 real 0.3938191690143297 ok=False | audit 0.964 | gen 283s | total 6168s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T17:17:47-03:00 — duração do job 6223 s
