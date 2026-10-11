# J019 — Outra classe de modelo final: MLP com o DDPM do J009_A (3 sementes) — proposto pelo desktop

Início: 2026-10-03T07:52:48-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J019_mlp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --model mlp --seeds 0,1,2 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3` | J019_mlp | 0 | 6633 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J019_mlp: seed 0 frac 0.01: real 4.275 | melhor genphys_rfill_w0.3 2.861 | discr gen 0.36812500000000004 (real 0.177, ok=False) | id: gen 0.35024999999999995 real 0.1202453987730061 ok=False | audit 0.994 | gen 294s | total 576s
J019_mlp: seed 0 frac 0.02: real 4.499 | melhor gen_rfill_w0.3 2.706 | discr gen 0.33575 (real 0.147, ok=False) | id: gen 0.33125000000000004 real 0.09070943451941538 ok=False | audit 0.993 | gen 293s | total 1139s
J019_mlp: seed 0 frac 0.05: real 3.311 | melhor genphys_rfill_w0.3 2.472 | discr gen 0.2798749999999999 (real 0.226, ok=False) | id: gen 0.20300000000000007 real 0.13937500000000003 ok=False | audit 0.964 | gen 294s | total 1688s
J019_mlp: seed 0 frac 0.1: real 3.158 | melhor genphys_rfill_w0.3 2.390 | discr gen 0.243 (real 0.130, ok=False) | id: gen 0.18025000000000002 real 0.051875000000000115 ok=False | audit 0.949 | gen 294s | total 2233s
J019_mlp: seed 1 frac 0.01: real 3.990 | melhor gen_rfill_w1 3.056 | discr gen 0.39512499999999995 (real 0.182, ok=False) | id: gen 0.3723750000000001 real 0.1528475327752934 ok=False | audit 0.992 | gen 293s | total 2791s
J019_mlp: seed 1 frac 0.02: real 4.846 | melhor gen_rfill_w0.3 2.607 | discr gen 0.287875 (real 0.114, ok=False) | id: gen 0.29174999999999995 real 0.0906507692307692 ok=False | audit 0.986 | gen 293s | total 3337s
J019_mlp: seed 1 frac 0.05: real 3.382 | melhor genphys_rfill_w0.3 2.543 | discr gen 0.29737499999999994 (real 0.169, ok=False) | id: gen 0.24499999999999988 real 0.08446194225721781 ok=False | audit 0.970 | gen 293s | total 3883s
J019_mlp: seed 1 frac 0.1: real 2.745 | melhor genphys_rfill_w0.3 2.516 | discr gen 0.2446250000000001 (real 0.144, ok=False) | id: gen 0.19162499999999993 real 0.050000000000000044 ok=False | audit 0.951 | gen 293s | total 4419s
J019_mlp: seed 2 frac 0.01: real 4.433 | melhor gen_rfill_w0.3 2.886 | discr gen 0.35862499999999997 (real 0.142, ok=False) | id: gen 0.34987500000000016 real 0.10604026845637582 ok=False | audit 0.988 | gen 293s | total 4984s
J019_mlp: seed 2 frac 0.02: real 3.772 | melhor genphys_rfill_w0.3 2.672 | discr gen 0.31199999999999994 (real 0.145, ok=False) | id: gen 0.280875 real 0.061003093414764065 ok=False | audit 0.985 | gen 293s | total 5540s
J019_mlp: seed 2 frac 0.05: real 2.888 | melhor gen_rfill_w0.3 2.587 | discr gen 0.2648750000000002 (real 0.164, ok=False) | id: gen 0.21724999999999994 real 0.08074999999999999 ok=False | audit 0.972 | gen 293s | total 6087s
J019_mlp: seed 2 frac 0.1: real 2.867 | melhor genphys_rfill_w0.3 2.484 | discr gen 0.26025 (real 0.158, ok=False) | id: gen 0.20174999999999987 real 0.055499999999999994 ok=False | audit 0.960 | gen 294s | total 6628s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T09:43:45-03:00 — duração do job 6657 s
