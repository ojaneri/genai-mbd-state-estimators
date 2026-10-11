# J007 — Rodada 3: grade completa no TESTE com os 2 geradores escolhidos no J006 (mesmos argumentos, sem --val)

Início: 2026-10-01T04:06:41-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `9fab12e388fca2190c56d4e433dbdef5247c2adc7bc70ce33cbc442a097942eb`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J007_A --gen ddpm --iters 20000 --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J007_A | 0 | 5979 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 2 | `python -u run3.py ../data out/J007_B --gen ddpm --iters 20000 --dequant --post quanthold --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J007_B | 0 | 5753 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |

Comando 1: marcador substituído pelos argumentos de `J006_ddpm20k_raw` (escolha anterior), sem `--val`; também removidos `--seeds`/`--fracs` (o job define os seus; no script vale a 1ª ocorrência de cada flag) e `--no-ceiling`/`--variants` (grade completa, como J001/J003; inclui as variantes do comando original).
Comando 2: marcador substituído pelos argumentos de `J006_ddpm20k` (escolha anterior), sem `--val`; também removidos `--seeds`/`--fracs` (o job define os seus; no script vale a 1ª ocorrência de cada flag) e `--no-ceiling`/`--variants` (grade completa, como J001/J003; inclui as variantes do comando original).

## Linhas "seed … frac …" dos logs

```
J007_A: seed 0 frac 0.01: real 2.983 | melhor gen_rfill_w0.3 2.708 | discr gen 0.47762499999999997 (real 0.177, ok=False) | audit 0.983 | gen 101s | total 316s
J007_A: seed 0 frac 0.02: real 2.909 | melhor gen_rfill_w0.3 2.622 | discr gen 0.4832500000000002 (real 0.147, ok=False) | audit 0.957 | gen 98s | total 621s
J007_A: seed 0 frac 0.05: real 2.427 | melhor real 2.427 | discr gen 0.47999999999999987 (real 0.226, ok=False) | audit 0.969 | gen 99s | total 909s
J007_A: seed 0 frac 0.1: real 2.329 | melhor real 2.329 | discr gen 0.47987500000000005 (real 0.130, ok=False) | audit 0.941 | gen 99s | total 1192s
J007_A: seed 1 frac 0.01: real 3.151 | melhor gen_rfill_w0.3 2.577 | discr gen 0.4801249999999999 (real 0.182, ok=False) | audit 0.973 | gen 98s | total 1498s
J007_A: seed 1 frac 0.02: real 2.695 | melhor gen_rfill_w0.3 2.479 | discr gen 0.48475 (real 0.114, ok=False) | audit 0.970 | gen 98s | total 1803s
J007_A: seed 1 frac 0.05: real 2.551 | melhor gen_rfill_w0.3 2.518 | discr gen 0.48687500000000006 (real 0.169, ok=False) | audit 0.965 | gen 98s | total 2103s
J007_A: seed 1 frac 0.1: real 2.362 | melhor real 2.362 | discr gen 0.47775 (real 0.144, ok=False) | audit 0.947 | gen 98s | total 2387s
J007_A: seed 2 frac 0.01: real 3.063 | melhor gen_rfill_w0.3 2.727 | discr gen 0.48212500000000014 (real 0.142, ok=False) | audit 0.969 | gen 98s | total 2695s
J007_A: seed 2 frac 0.02: real 2.834 | melhor gen_rfill_w0.3 2.582 | discr gen 0.477375 (real 0.145, ok=False) | audit 0.950 | gen 99s | total 3001s
J007_A: seed 2 frac 0.05: real 2.513 | melhor gen_pretrain 2.484 | discr gen 0.48675 (real 0.164, ok=False) | audit 0.957 | gen 98s | total 3300s
J007_A: seed 2 frac 0.1: real 2.322 | melhor real 2.322 | discr gen 0.47962499999999986 (real 0.158, ok=False) | audit 0.939 | gen 98s | total 3581s
J007_A: seed 3 frac 0.01: real 3.017 | melhor gen_rfill_w0.3 2.730 | discr gen 0.48387500000000006 (real 0.193, ok=False) | audit 0.986 | gen 99s | total 3887s
J007_A: seed 3 frac 0.02: real 2.977 | melhor gen_rfill_w0.3 2.674 | discr gen 0.4751249999999999 (real 0.191, ok=False) | audit 0.946 | gen 98s | total 4194s
J007_A: seed 3 frac 0.05: real 2.461 | melhor gen_pretrain 2.439 | discr gen 0.47775 (real 0.190, ok=False) | audit 0.974 | gen 98s | total 4494s
J007_A: seed 3 frac 0.1: real 2.320 | melhor real 2.320 | discr gen 0.48575 (real 0.118, ok=False) | audit 0.962 | gen 99s | total 4776s
J007_A: seed 4 frac 0.01: real 3.109 | melhor gen_rfill_w0.3 2.575 | discr gen 0.48750000000000004 (real 0.124, ok=False) | audit 0.989 | gen 98s | total 5083s
J007_A: seed 4 frac 0.02: real 2.856 | melhor gen_rfill_w0.3 2.625 | discr gen 0.4804999999999999 (real 0.144, ok=False) | audit 0.971 | gen 98s | total 5389s
J007_A: seed 4 frac 0.05: real 2.463 | melhor gen_rfill_w0.3 2.451 | discr gen 0.48124999999999996 (real 0.136, ok=False) | audit 0.973 | gen 98s | total 5691s
J007_A: seed 4 frac 0.1: real 2.304 | melhor gen_pretrain 2.297 | discr gen 0.483 (real 0.161, ok=False) | audit 0.957 | gen 99s | total 5974s
J007_B: seed 0 frac 0.01: real 2.983 | melhor real 2.983 | discr gen 0.38012499999999994 (real 0.177, ok=False) | audit 0.921 | gen 103s | total 304s
J007_B: seed 0 frac 0.02: real 2.909 | melhor real 2.909 | discr gen 0.33125000000000004 (real 0.147, ok=False) | audit 0.894 | gen 100s | total 598s
J007_B: seed 0 frac 0.05: real 2.427 | melhor real 2.427 | discr gen 0.37650000000000006 (real 0.226, ok=False) | audit 0.894 | gen 101s | total 876s
J007_B: seed 0 frac 0.1: real 2.329 | melhor real 2.329 | discr gen 0.346125 (real 0.130, ok=False) | audit 0.887 | gen 101s | total 1147s
J007_B: seed 1 frac 0.01: real 3.151 | melhor real 3.151 | discr gen 0.367 (real 0.182, ok=False) | audit 0.920 | gen 100s | total 1442s
J007_B: seed 1 frac 0.02: real 2.695 | melhor real 2.695 | discr gen 0.34887499999999994 (real 0.114, ok=False) | audit 0.912 | gen 99s | total 1737s
J007_B: seed 1 frac 0.05: real 2.551 | melhor real 2.551 | discr gen 0.32875 (real 0.169, ok=False) | audit 0.927 | gen 99s | total 2024s
J007_B: seed 1 frac 0.1: real 2.362 | melhor real 2.362 | discr gen 0.33162500000000006 (real 0.144, ok=False) | audit 0.869 | gen 100s | total 2296s
J007_B: seed 2 frac 0.01: real 3.063 | melhor real 3.063 | discr gen 0.33462499999999995 (real 0.142, ok=False) | audit 0.895 | gen 99s | total 2594s
J007_B: seed 2 frac 0.02: real 2.834 | melhor real 2.834 | discr gen 0.32899999999999996 (real 0.145, ok=False) | audit 0.839 | gen 100s | total 2887s
J007_B: seed 2 frac 0.05: real 2.513 | melhor real 2.513 | discr gen 0.32225000000000004 (real 0.164, ok=False) | audit 0.893 | gen 99s | total 3175s
J007_B: seed 2 frac 0.1: real 2.322 | melhor real 2.322 | discr gen 0.3318749999999999 (real 0.158, ok=False) | audit 0.844 | gen 99s | total 3444s
J007_B: seed 3 frac 0.01: real 3.017 | melhor real 3.017 | discr gen 0.36675 (real 0.193, ok=False) | audit 0.937 | gen 100s | total 3739s
J007_B: seed 3 frac 0.02: real 2.977 | melhor real 2.977 | discr gen 0.3630000000000001 (real 0.191, ok=False) | audit 0.872 | gen 99s | total 4033s
J007_B: seed 3 frac 0.05: real 2.461 | melhor real 2.461 | discr gen 0.36124999999999985 (real 0.190, ok=False) | audit 0.908 | gen 100s | total 4322s
J007_B: seed 3 frac 0.1: real 2.320 | melhor real 2.320 | discr gen 0.31425000000000003 (real 0.118, ok=False) | audit 0.907 | gen 99s | total 4590s
J007_B: seed 4 frac 0.01: real 3.109 | melhor real 3.109 | discr gen 0.3526250000000001 (real 0.124, ok=False) | audit 0.934 | gen 101s | total 4889s
J007_B: seed 4 frac 0.02: real 2.856 | melhor real 2.856 | discr gen 0.352375 (real 0.144, ok=False) | audit 0.934 | gen 99s | total 5184s
J007_B: seed 4 frac 0.05: real 2.463 | melhor real 2.463 | discr gen 0.342125 (real 0.136, ok=False) | audit 0.948 | gen 101s | total 5476s
J007_B: seed 4 frac 0.1: real 2.304 | melhor real 2.304 | discr gen 0.32987500000000014 (real 0.161, ok=False) | audit 0.907 | gen 101s | total 5748s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T07:22:42-03:00 — duração do job 11762 s
