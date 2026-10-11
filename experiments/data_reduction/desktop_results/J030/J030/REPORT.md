# J030 — P3 TRANSFERÊNCIA entre temperaturas: igual ao J029, com o gerador pré-treinado em 10/25/40 °C (ciclos de treino)

Início: 2026-10-03T17:18:40-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J030_frio_transf --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --temps n20degC,n10degC,0degC --pretrain-temps 10degC,25degC,40degC --pretrain-iters 50000 --seeds 0,1,2,3,4 --fracs 0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3` | J030_frio_transf | 0 | 7673 s | `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b` |

## Linhas "seed … frac …" dos logs

```
J030_frio_transf: seed 0 frac 0.02: real 0.217 | melhor physonly 0.052 | discr gen 0.49062499999999987 (real 0.463, ok=True) | id: gen 0.490375 real 0.46461324687355243 ok=True | audit 0.952 | gen 569s | total 701s
J030_frio_transf: seed 0 frac 0.05: real 0.090 | melhor physonly 0.036 | discr gen 0.48387499999999994 (real 0.445, ok=True) | id: gen 0.4710000000000001 real 0.4341294074540347 ok=True | audit 0.986 | gen 283s | total 1116s
J030_frio_transf: seed 0 frac 0.1: real 0.055 | melhor physonly 0.027 | discr gen 0.44362499999999994 (real 0.404, ok=True) | id: gen 0.4481249999999999 real 0.40091706453887244 ok=True | audit 0.969 | gen 283s | total 1529s
J030_frio_transf: seed 1 frac 0.02: real 0.095 | melhor real 0.095 | discr gen 0.49512500000000015 (real 0.477, ok=True) | id: gen 0.4953749999999999 real 0.47339449541284395 ok=True | audit 0.973 | gen 567s | total 2215s
J030_frio_transf: seed 1 frac 0.05: real 0.079 | melhor physonly 0.030 | discr gen 0.46799999999999997 (real 0.453, ok=True) | id: gen 0.4657500000000001 real 0.4537091988130564 ok=True | audit 0.945 | gen 284s | total 2631s
J030_frio_transf: seed 1 frac 0.1: real 0.049 | melhor physonly 0.025 | discr gen 0.4637499999999999 (real 0.413, ok=False) | id: gen 0.4615 real 0.4212123380881163 ok=True | audit 0.981 | gen 284s | total 3045s
J030_frio_transf: seed 2 frac 0.02: real 0.190 | melhor real 0.190 | discr gen 0.49824999999999997 (real 0.484, ok=True) | id: gen 0.498 real 0.48354430379746827 ok=True | audit 0.998 | gen 566s | total 3720s
J030_frio_transf: seed 2 frac 0.05: real 0.092 | melhor hyb_resid_w0.3 0.035 | discr gen 0.478375 (real 0.453, ok=True) | id: gen 0.46950000000000003 real 0.4563906844542245 ok=True | audit 0.982 | gen 284s | total 4136s
J030_frio_transf: seed 2 frac 0.1: real 0.048 | melhor hyb_resid_w0.3 0.025 | discr gen 0.46462500000000007 (real 0.413, ok=False) | id: gen 0.4528749999999999 real 0.4023597723964537 ok=False | audit 0.982 | gen 283s | total 4549s
J030_frio_transf: seed 3 frac 0.02: real 0.180 | melhor physonly 0.047 | discr gen 0.49375 (real 0.459, ok=True) | id: gen 0.48987499999999995 real 0.4620689655172414 ok=True | audit 0.971 | gen 567s | total 5248s
J030_frio_transf: seed 3 frac 0.05: real 0.065 | melhor hyb_resid_w0.3 0.031 | discr gen 0.4797499999999999 (real 0.442, ok=True) | id: gen 0.4786250000000001 real 0.45296167247386754 ok=True | audit 0.979 | gen 292s | total 5677s
J030_frio_transf: seed 3 frac 0.1: real 0.076 | melhor hyb_resid_w0.3 0.026 | discr gen 0.4553750000000001 (real 0.429, ok=True) | id: gen 0.458375 real 0.42503748125937035 ok=True | audit 0.970 | gen 299s | total 6110s
J030_frio_transf: seed 4 frac 0.02: real 0.204 | melhor hyb_resid_w0.3 0.110 | discr gen 0.48687499999999984 (real 0.476, ok=True) | id: gen 0.478375 real 0.4558620689655173 ok=True | audit 0.969 | gen 589s | total 6831s
J030_frio_transf: seed 4 frac 0.05: real 0.084 | melhor hyb_resid_w0.3 0.028 | discr gen 0.4764999999999999 (real 0.450, ok=True) | id: gen 0.47075 real 0.4402298850574713 ok=True | audit 0.967 | gen 291s | total 7254s
J030_frio_transf: seed 4 frac 0.1: real 0.054 | melhor hyb_resid_w0.3 0.023 | discr gen 0.454375 (real 0.392, ok=False) | id: gen 0.44999999999999996 real 0.3938191690143297 ok=False | audit 0.968 | gen 283s | total 7667s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T19:27:08-03:00 — duração do job 7708 s
