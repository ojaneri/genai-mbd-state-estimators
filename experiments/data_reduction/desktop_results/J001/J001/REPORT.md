# J001 — TimeGAN, grade completa (variantes de proporção/peso/filtro/pré-treino), frações escassas

Início: 2026-09-30T22:21:55-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `42e9ae46aa0e778a5b448ad72c896f303d556731053e1d17978027632cd40b9e`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`

## Comandos

| # | comando executado | saída | rc | tempo |
|---|---|---|---|---|
| 1 | `python -u run2.py ../data out/J001 --gen timegan --iters 6000 --hidden 24 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J001 | 0 | 6857 s |

## Linhas "seed … frac …" dos logs

```
J001: seed 0 frac 0.01: real 2.983 | melhor real 2.983 | discr gen 0.4922500000000001 | audit 0.875 | gen 226s | total 358s
J001: seed 0 frac 0.02: real 2.909 | melhor real 2.909 | discr gen 0.4901249999999999 | audit 0.866 | gen 223s | total 709s
J001: seed 0 frac 0.05: real 2.427 | melhor real 2.427 | discr gen 0.49475 | audit 0.998 | gen 223s | total 1051s
J001: seed 0 frac 0.1: real 2.329 | melhor real 2.329 | discr gen 0.49412500000000004 | audit 0.985 | gen 222s | total 1388s
J001: seed 1 frac 0.01: real 3.151 | melhor real 3.151 | discr gen 0.49687499999999996 | audit 0.827 | gen 222s | total 1735s
J001: seed 1 frac 0.02: real 2.695 | melhor real 2.695 | discr gen 0.4891249999999999 | audit 0.987 | gen 223s | total 2086s
J001: seed 1 frac 0.05: real 2.551 | melhor real 2.551 | discr gen 0.4973749999999999 | audit 0.991 | gen 223s | total 2433s
J001: seed 1 frac 0.1: real 2.362 | melhor real 2.362 | discr gen 0.4952500000000001 | audit 0.949 | gen 223s | total 2770s
J001: seed 2 frac 0.01: real 3.063 | melhor gen_rfill_w0.3 2.838 | discr gen 0.4879999999999999 | audit 0.812 | gen 223s | total 3121s
J001: seed 2 frac 0.02: real 2.834 | melhor real 2.834 | discr gen 0.4963749999999999 | audit 0.959 | gen 223s | total 3468s
J001: seed 2 frac 0.05: real 2.513 | melhor real 2.513 | discr gen 0.4956250000000001 | audit 0.999 | gen 221s | total 3813s
J001: seed 2 frac 0.1: real 2.322 | melhor real 2.322 | discr gen 0.49212500000000003 | audit 0.836 | gen 221s | total 4146s
J001: seed 3 frac 0.01: real 3.017 | melhor gen_r1_w1 2.877 | discr gen 0.49212500000000003 | audit 0.991 | gen 218s | total 4488s
J001: seed 3 frac 0.02: real 2.977 | melhor gen_r0.5_w1 2.949 | discr gen 0.49287500000000006 | audit 0.958 | gen 218s | total 4833s
J001: seed 3 frac 0.05: real 2.461 | melhor real 2.461 | discr gen 0.491625 | audit 0.986 | gen 218s | total 5172s
J001: seed 3 frac 0.1: real 2.320 | melhor real 2.320 | discr gen 0.49450000000000005 | audit 0.932 | gen 217s | total 5500s
J001: seed 4 frac 0.01: real 3.109 | melhor gen_rfill_w0.3 3.102 | discr gen 0.49649999999999994 | audit 0.887 | gen 217s | total 5843s
J001: seed 4 frac 0.02: real 2.856 | melhor gen_dfilt_q0.5 2.780 | discr gen 0.4963749999999999 | audit 0.968 | gen 215s | total 6183s
J001: seed 4 frac 0.05: real 2.463 | melhor real 2.463 | discr gen 0.4956250000000001 | audit 0.990 | gen 214s | total 6521s
J001: seed 4 frac 0.1: real 2.304 | melhor real 2.304 | discr gen 0.492 | audit 0.988 | gen 218s | total 6852s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T00:16:27-03:00 — duração do job 6872 s
