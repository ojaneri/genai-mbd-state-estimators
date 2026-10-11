# J009 — Rodada 4: grade completa no TESTE com os 2 escolhidos no J008 (mesmos argumentos, sem --val)

Início: 2026-10-01T12:09:16-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J009_A --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J009_A | 0 (reaproveitado) | 11706 | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |
| 2 | `python -u run3.py ../data out/J009_B --gen ddpm --iters 50000 --hidden 128 --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J009_B | 0 (reaproveitado) | — | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |

Comando 1: marcador substituído pelos argumentos de `J008_q50k_h128` (escolha anterior), sem `--val`; também removidos `--seeds`/`--fracs` (o job define os seus; no script vale a 1ª ocorrência de cada flag) e `--no-ceiling`/`--variants` (grade completa, como J001/J003; inclui as variantes do comando original).
Comando 2: marcador substituído pelos argumentos de `J008_raw50k_h128` (escolha anterior), sem `--val`; também removidos `--seeds`/`--fracs` (o job define os seus; no script vale a 1ª ocorrência de cada flag) e `--no-ceiling`/`--variants` (grade completa, como J001/J003; inclui as variantes do comando original).

## Linhas "seed … frac …" dos logs

```
J009_A: seed 0 frac 0.01: real 2.983 | melhor gen_rfill_w0.3 2.570 | discr gen 0.36549999999999994 (real 0.177, ok=False) | audit 0.994 | gen 317s | total 638s
J009_A: seed 0 frac 0.02: real 2.909 | melhor gen_rfill_w0.3 2.553 | discr gen 0.34024999999999994 (real 0.147, ok=False) | audit 0.993 | gen 324s | total 1276s
J009_A: seed 0 frac 0.05: real 2.427 | melhor gen_rfill_w0.3 2.311 | discr gen 0.27212499999999995 (real 0.226, ok=True) | audit 0.964 | gen 313s | total 1854s
J009_A: seed 0 frac 0.1: real 2.329 | melhor genphys_rfill_w0.3 2.270 | discr gen 0.25012500000000004 (real 0.130, ok=False) | audit 0.948 | gen 294s | total 2401s
J009_A: seed 1 frac 0.01: real 3.151 | melhor gen_rfill_w0.3 2.708 | discr gen 0.39375000000000004 (real 0.182, ok=False) | audit 0.992 | gen 298s | total 2995s
J009_A: seed 1 frac 0.02: real 2.695 | melhor gen_rfill_w0.3 2.387 | discr gen 0.28225 (real 0.114, ok=False) | audit 0.986 | gen 302s | total 3589s
J009_A: seed 1 frac 0.05: real 2.551 | melhor gen_rfill_w0.3 2.415 | discr gen 0.29999999999999993 (real 0.169, ok=False) | audit 0.970 | gen 302s | total 4173s
J009_A: seed 1 frac 0.1: real 2.362 | melhor genphys_rfill_w0.3 2.318 | discr gen 0.23962499999999998 (real 0.144, ok=False) | audit 0.951 | gen 293s | total 4718s
J009_A: seed 2 frac 0.01: real 3.063 | melhor gen_rfill_w1 2.585 | discr gen 0.3553750000000001 (real 0.142, ok=False) | audit 0.988 | gen 293s | total 5307s
J009_A: seed 2 frac 0.02: real 2.834 | melhor gen_rfill_w0.3 2.587 | discr gen 0.303125 (real 0.145, ok=False) | audit 0.985 | gen 292s | total 5889s
J009_A: seed 2 frac 0.05: real 2.513 | melhor genphys_r1_w1 2.445 | discr gen 0.26387499999999997 (real 0.164, ok=False) | audit 0.972 | gen 292s | total 6461s
J009_A: seed 2 frac 0.1: real 2.322 | melhor genphys_rfill_w0.3 2.270 | discr gen 0.2659999999999999 (real 0.158, ok=False) | audit 0.960 | gen 293s | total 7008s
J009_A: seed 3 frac 0.01: real 3.017 | melhor gen_rfill_w0.3 2.641 | discr gen 0.38874999999999993 (real 0.193, ok=False) | audit 0.987 | gen 303s | total 7609s
J009_A: seed 3 frac 0.02: real 2.977 | melhor gen_rfill_w0.3 2.633 | discr gen 0.3501249999999999 (real 0.191, ok=False) | audit 0.979 | gen 299s | total 8205s
J009_A: seed 3 frac 0.05: real 2.461 | melhor gen_rfill_w0.3 2.308 | discr gen 0.28737499999999994 (real 0.190, ok=False) | audit 0.990 | gen 298s | total 8789s
J009_A: seed 3 frac 0.1: real 2.320 | melhor genphys_rfill_w0.3 2.262 | discr gen 0.2310000000000001 (real 0.118, ok=False) | audit 0.965 | gen 305s | total 9349s
J009_A: seed 4 frac 0.01: real 3.109 | melhor gen_rfill_w1 2.639 | discr gen 0.36275000000000013 (real 0.124, ok=False) | audit 0.994 | gen 301s | total 9949s
J009_A: seed 4 frac 0.02: real 2.856 | melhor gen_rfill_w0.3 2.564 | discr gen 0.32400000000000007 (real 0.144, ok=False) | audit 0.981 | gen 301s | total 10549s
J009_A: seed 4 frac 0.05: real 2.463 | melhor gen_rfill_w0.3 2.319 | discr gen 0.26625 (real 0.136, ok=False) | audit 0.967 | gen 303s | total 11136s
J009_A: seed 4 frac 0.1: real 2.304 | melhor genphys_rfill_w0.3 2.248 | discr gen 0.267 (real 0.161, ok=False) | audit 0.953 | gen 305s | total 11700s
J009_B: seed 0 frac 0.01: real 2.983 | melhor gen_rfill_w0.3 2.643 | discr gen 0.47887500000000005 (real 0.177, ok=False) | audit 0.993 | gen 305s | total 631s
J009_B: seed 0 frac 0.02: real 2.909 | melhor gen_rfill_w0.3 2.564 | discr gen 0.48387500000000006 (real 0.147, ok=False) | audit 0.992 | gen 310s | total 1262s
J009_B: seed 0 frac 0.05: real 2.427 | melhor gen_rfill_w0.3 2.328 | discr gen 0.47424999999999995 (real 0.226, ok=False) | audit 0.964 | gen 305s | total 1856s
J009_B: seed 0 frac 0.1: real 2.329 | melhor genphys_rfill_w1 2.273 | discr gen 0.47762499999999997 (real 0.130, ok=False) | audit 0.949 | gen 307s | total 2442s
J009_B: seed 1 frac 0.01: real 3.151 | melhor gen_rfill_w0.3 2.740 | discr gen 0.47775 (real 0.182, ok=False) | audit 0.991 | gen 296s | total 3053s
J009_B: seed 1 frac 0.02: real 2.695 | melhor gen_rfill_w0.3 2.384 | discr gen 0.4806250000000001 (real 0.114, ok=False) | audit 0.985 | gen 294s | total 3660s
J009_B: seed 1 frac 0.05: real 2.551 | melhor gen_rfill_w0.3 2.402 | discr gen 0.4827499999999999 (real 0.169, ok=False) | audit 0.971 | gen 306s | total 4277s
J009_B: seed 1 frac 0.1: real 2.362 | melhor gen_pretrain 2.345 | discr gen 0.4813749999999999 (real 0.144, ok=False) | audit 0.952 | gen 306s | total 4870s
J009_B: seed 2 frac 0.01: real 3.063 | melhor gen_rfill_w0.3 2.611 | discr gen 0.478 (real 0.142, ok=False) | audit 0.989 | gen 301s | total 5486s
J009_B: seed 2 frac 0.02: real 2.834 | melhor gen_rfill_w0.3 2.559 | discr gen 0.48149999999999993 (real 0.145, ok=False) | audit 0.984 | gen 308s | total 6113s
J009_B: seed 2 frac 0.05: real 2.513 | melhor genphys_rfill_w0.3 2.429 | discr gen 0.48224999999999996 (real 0.164, ok=False) | audit 0.974 | gen 307s | total 6729s
J009_B: seed 2 frac 0.1: real 2.322 | melhor genphys_rfill_w1 2.284 | discr gen 0.4796250000000001 (real 0.158, ok=False) | audit 0.960 | gen 308s | total 7320s
J009_B: seed 3 frac 0.01: real 3.017 | melhor gen_rfill_w0.3 2.647 | discr gen 0.47925000000000006 (real 0.193, ok=False) | audit 0.988 | gen 307s | total 7949s
J009_B: seed 3 frac 0.02: real 2.977 | melhor gen_rfill_w0.3 2.668 | discr gen 0.47875 (real 0.191, ok=False) | audit 0.980 | gen 308s | total 8580s
J009_B: seed 3 frac 0.05: real 2.461 | melhor gen_rfill_w0.3 2.309 | discr gen 0.4787500000000001 (real 0.190, ok=False) | audit 0.991 | gen 308s | total 9197s
J009_B: seed 3 frac 0.1: real 2.320 | melhor gen_rfill_w0.3 2.241 | discr gen 0.4793749999999999 (real 0.118, ok=False) | audit 0.965 | gen 308s | total 9786s
J009_B: seed 4 frac 0.01: real 3.109 | melhor gen_rfill_w0.3 2.672 | discr gen 0.48025000000000007 (real 0.124, ok=False) | audit 0.995 | gen 306s | total 10412s
J009_B: seed 4 frac 0.02: real 2.856 | melhor gen_rfill_w0.3 2.561 | discr gen 0.48587499999999983 (real 0.144, ok=False) | audit 0.980 | gen 308s | total 11038s
J009_B: seed 4 frac 0.05: real 2.463 | melhor gen_rfill_w0.3 2.308 | discr gen 0.48162499999999997 (real 0.136, ok=False) | audit 0.968 | gen 308s | total 11658s
J009_B: seed 4 frac 0.1: real 2.304 | melhor genphys_rfill_w0.3 2.263 | discr gen 0.4817500000000001 (real 0.161, ok=False) | audit 0.953 | gen 309s | total 12251s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T15:17:18-03:00 — duração do job 11282 s
