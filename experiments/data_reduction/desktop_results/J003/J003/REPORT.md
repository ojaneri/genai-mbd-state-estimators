# J003 — TimeVAE, grade completa no TESTE com a configuração escolhida no J002

Início: 2026-10-01T00:22:06-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`

## Comandos

| # | comando executado | saída | rc | tempo |
|---|---|---|---|---|
| 1 | `python -u run2.py ../data out/J003 --gen timevae --latent 16 --iters 5000 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J003 | 0 | 2608 s |

## Linhas "seed … frac …" dos logs

```
J003: seed 0 frac 0.01: real 2.983 | melhor real 2.983 | discr gen 0.49924999999999997 | audit 1.000 | gen 21s | total 142s
J003: seed 0 frac 0.02: real 2.909 | melhor real 2.909 | discr gen 0.49875 | audit 1.000 | gen 20s | total 277s
J003: seed 0 frac 0.05: real 2.427 | melhor real 2.427 | discr gen 0.498 | audit 1.000 | gen 20s | total 398s
J003: seed 0 frac 0.1: real 2.329 | melhor real 2.329 | discr gen 0.498375 | audit 1.000 | gen 20s | total 513s
J003: seed 1 frac 0.01: real 3.151 | melhor real 3.151 | discr gen 0.49912500000000004 | audit 1.000 | gen 20s | total 648s
J003: seed 1 frac 0.02: real 2.695 | melhor real 2.695 | discr gen 0.49924999999999997 | audit 1.000 | gen 20s | total 785s
J003: seed 1 frac 0.05: real 2.551 | melhor real 2.551 | discr gen 0.498 | audit 1.000 | gen 20s | total 917s
J003: seed 1 frac 0.1: real 2.362 | melhor real 2.362 | discr gen 0.49812500000000015 | audit 1.000 | gen 20s | total 1033s
J003: seed 2 frac 0.01: real 3.063 | melhor real 3.063 | discr gen 0.498625 | audit 1.000 | gen 20s | total 1168s
J003: seed 2 frac 0.02: real 2.834 | melhor real 2.834 | discr gen 0.4977499999999999 | audit 1.000 | gen 20s | total 1303s
J003: seed 2 frac 0.05: real 2.513 | melhor real 2.513 | discr gen 0.49775000000000014 | audit 1.000 | gen 20s | total 1434s
J003: seed 2 frac 0.1: real 2.322 | melhor real 2.322 | discr gen 0.498 | audit 1.000 | gen 20s | total 1549s
J003: seed 3 frac 0.01: real 3.017 | melhor real 3.017 | discr gen 0.49849999999999994 | audit 1.000 | gen 20s | total 1681s
J003: seed 3 frac 0.02: real 2.977 | melhor real 2.977 | discr gen 0.498625 | audit 1.000 | gen 20s | total 1820s
J003: seed 3 frac 0.05: real 2.461 | melhor real 2.461 | discr gen 0.498 | audit 1.000 | gen 20s | total 1953s
J003: seed 3 frac 0.1: real 2.320 | melhor real 2.320 | discr gen 0.499 | audit 1.000 | gen 21s | total 2070s
J003: seed 4 frac 0.01: real 3.109 | melhor real 3.109 | discr gen 0.49949999999999994 | audit 1.000 | gen 20s | total 2206s
J003: seed 4 frac 0.02: real 2.856 | melhor real 2.856 | discr gen 0.49875 | audit 1.000 | gen 20s | total 2345s
J003: seed 4 frac 0.05: real 2.463 | melhor real 2.463 | discr gen 0.498375 | audit 1.000 | gen 21s | total 2481s
J003: seed 4 frac 0.1: real 2.304 | melhor real 2.304 | discr gen 0.4978750000000002 | audit 1.000 | gen 21s | total 2603s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T01:05:50-03:00 — duração do job 2624 s
