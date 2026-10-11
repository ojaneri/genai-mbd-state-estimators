# J005 — Refaz no TimeGAN as variantes com defeito no J001 (filtro estatístico e pré-treino), código corrigido em 01/10 00:3x

Início: 2026-10-01T02:03:07-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `9fab12e388fca2190c56d4e433dbdef5247c2adc7bc70ce33cbc442a097942eb`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run2.py ../data out/J005 --gen timegan --iters 6000 --hidden 24 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --no-ceiling --variants real,gen_dfilt_q0.5,gen_dfilt_q0.2,gen_pretrain` | J005 | 0 | 5341 s | `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56` |

## Linhas "seed … frac …" dos logs

```
J005: seed 0 frac 0.01: real 2.983 | melhor real 2.983 | discr gen 0.4922500000000001 | audit 0.875 | gen 224s | total 271s
J005: seed 0 frac 0.02: real 2.909 | melhor real 2.909 | discr gen 0.4901249999999999 | audit 0.866 | gen 222s | total 540s
J005: seed 0 frac 0.05: real 2.427 | melhor real 2.427 | discr gen 0.49475 | audit 0.998 | gen 220s | total 805s
J005: seed 0 frac 0.1: real 2.329 | melhor real 2.329 | discr gen 0.49412500000000004 | audit 0.985 | gen 220s | total 1072s
J005: seed 1 frac 0.01: real 3.151 | melhor real 3.151 | discr gen 0.49687499999999996 | audit 0.827 | gen 220s | total 1336s
J005: seed 1 frac 0.02: real 2.695 | melhor gen_dfilt_q0.2 2.694 | discr gen 0.4891249999999999 | audit 0.987 | gen 220s | total 1604s
J005: seed 1 frac 0.05: real 2.551 | melhor real 2.551 | discr gen 0.4973749999999999 | audit 0.991 | gen 221s | total 1873s
J005: seed 1 frac 0.1: real 2.362 | melhor real 2.362 | discr gen 0.4952500000000001 | audit 0.949 | gen 221s | total 2140s
J005: seed 2 frac 0.01: real 3.063 | melhor gen_dfilt_q0.2 2.874 | discr gen 0.4879999999999999 | audit 0.812 | gen 220s | total 2405s
J005: seed 2 frac 0.02: real 2.834 | melhor real 2.834 | discr gen 0.4963749999999999 | audit 0.959 | gen 222s | total 2670s
J005: seed 2 frac 0.05: real 2.513 | melhor real 2.513 | discr gen 0.4956250000000001 | audit 0.999 | gen 219s | total 2937s
J005: seed 2 frac 0.1: real 2.322 | melhor real 2.322 | discr gen 0.49212500000000003 | audit 0.836 | gen 221s | total 3205s
J005: seed 3 frac 0.01: real 3.017 | melhor gen_dfilt_q0.2 2.869 | discr gen 0.49212500000000003 | audit 0.991 | gen 219s | total 3468s
J005: seed 3 frac 0.02: real 2.977 | melhor real 2.977 | discr gen 0.49287500000000006 | audit 0.958 | gen 222s | total 3735s
J005: seed 3 frac 0.05: real 2.461 | melhor real 2.461 | discr gen 0.491625 | audit 0.986 | gen 221s | total 4005s
J005: seed 3 frac 0.1: real 2.320 | melhor real 2.320 | discr gen 0.49450000000000005 | audit 0.932 | gen 219s | total 4269s
J005: seed 4 frac 0.01: real 3.109 | melhor gen_dfilt_q0.2 3.079 | discr gen 0.49649999999999994 | audit 0.887 | gen 219s | total 4532s
J005: seed 4 frac 0.02: real 2.856 | melhor gen_dfilt_q0.2 2.760 | discr gen 0.4963749999999999 | audit 0.968 | gen 219s | total 4799s
J005: seed 4 frac 0.05: real 2.463 | melhor real 2.463 | discr gen 0.4956250000000001 | audit 0.990 | gen 220s | total 5068s
J005: seed 4 frac 0.1: real 2.304 | melhor real 2.304 | discr gen 0.492 | audit 0.988 | gen 221s | total 5336s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T03:32:33-03:00 — duração do job 5366 s
