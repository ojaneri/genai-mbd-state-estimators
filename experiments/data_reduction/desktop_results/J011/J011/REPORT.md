# J011 — Rodada 5: grade completa no TESTE com os 2 escolhidos no J010 (mesmos argumentos, sem --val)

Início: 2026-10-01T17:02:15-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `8b1a63f0f7d783786b73b7e8a19d7d3528f70e22264b356fe569cd8eac601fb5`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J011_A --gen ddpm2 --iters 30000 --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J011_A | 0 | 8816 s | `8b1a63f0f7d783786b73b7e8a19d7d3528f70e22264b356fe569cd8eac601fb5` |
| 2 | `python -u run3.py ../data out/J011_B --gen ddpm2 --iters 30000 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J011_B | 0 | 9396 s | `8b1a63f0f7d783786b73b7e8a19d7d3528f70e22264b356fe569cd8eac601fb5` |

Comando 1: marcador substituído pelos argumentos de `J010_v2_raw` (escolha anterior), sem `--val`; também removidos `--seeds`/`--fracs` (o job define os seus; no script vale a 1ª ocorrência de cada flag) e `--no-ceiling`/`--variants` (grade completa, como J001/J003; inclui as variantes do comando original).
Comando 2: marcador substituído pelos argumentos de `J010_v2_quant` (escolha anterior), sem `--val`; também removidos `--seeds`/`--fracs` (o job define os seus; no script vale a 1ª ocorrência de cada flag) e `--no-ceiling`/`--variants` (grade completa, como J001/J003; inclui as variantes do comando original).

## Linhas "seed … frac …" dos logs

```
J011_A: seed 0 frac 0.01: real 2.983 | melhor gen_rfill_w0.3 2.821 | discr gen 0.48712500000000003 (real 0.177, ok=False) | id: gen 0.4866250000000001 real 0.1202453987730061 ok=False | audit 0.994 | gen 210s | total 440s
J011_A: seed 0 frac 0.02: real 2.909 | melhor genphys_rfill_w0.3 2.687 | discr gen 0.4899999999999999 (real 0.147, ok=False) | id: gen 0.4883750000000001 real 0.09070943451941538 ok=False | audit 0.985 | gen 207s | total 873s
J011_A: seed 0 frac 0.05: real 2.427 | melhor genphys_rfill_w0.3 2.378 | discr gen 0.477125 (real 0.226, ok=False) | id: gen 0.48350000000000004 real 0.13937500000000003 ok=False | audit 0.987 | gen 224s | total 1303s
J011_A: seed 0 frac 0.1: real 2.329 | melhor genphys_rfill_w0.3 2.274 | discr gen 0.4876250000000001 (real 0.130, ok=False) | id: gen 0.491625 real 0.051875000000000115 ok=False | audit 0.971 | gen 225s | total 1730s
J011_A: seed 1 frac 0.01: real 3.151 | melhor gen_dfilt_q0.5 3.010 | discr gen 0.47650000000000003 (real 0.182, ok=False) | id: gen 0.48062499999999986 real 0.1528475327752934 ok=False | audit 0.984 | gen 210s | total 2173s
J011_A: seed 1 frac 0.02: real 2.695 | melhor gen_rfill_w0.3 2.528 | discr gen 0.4881249999999999 (real 0.114, ok=False) | id: gen 0.4817499999999999 real 0.0906507692307692 ok=False | audit 0.991 | gen 214s | total 2616s
J011_A: seed 1 frac 0.05: real 2.551 | melhor genphys_rfill_w0.3 2.461 | discr gen 0.48650000000000004 (real 0.169, ok=False) | id: gen 0.490625 real 0.08446194225721781 ok=False | audit 0.979 | gen 226s | total 3065s
J011_A: seed 1 frac 0.1: real 2.362 | melhor genphys_rfill_w0.3 2.334 | discr gen 0.48350000000000004 (real 0.144, ok=False) | id: gen 0.485 real 0.050000000000000044 ok=False | audit 0.982 | gen 232s | total 3502s
J011_A: seed 2 frac 0.01: real 3.063 | melhor genphys_r1_w1 2.881 | discr gen 0.484125 (real 0.142, ok=False) | id: gen 0.482 real 0.10604026845637582 ok=False | audit 0.989 | gen 207s | total 3941s
J011_A: seed 2 frac 0.02: real 2.834 | melhor genphys_rfill_w0.3 2.705 | discr gen 0.48625000000000007 (real 0.145, ok=False) | id: gen 0.48612500000000003 real 0.061003093414764065 ok=False | audit 0.989 | gen 212s | total 4384s
J011_A: seed 2 frac 0.05: real 2.513 | melhor genphys_rfill_w0.3 2.430 | discr gen 0.484625 (real 0.164, ok=False) | id: gen 0.49024999999999996 real 0.08074999999999999 ok=False | audit 0.981 | gen 230s | total 4831s
J011_A: seed 2 frac 0.1: real 2.322 | melhor genphys_rfill_w0.3 2.293 | discr gen 0.48750000000000004 (real 0.158, ok=False) | id: gen 0.48675 real 0.055499999999999994 ok=False | audit 0.982 | gen 234s | total 5267s
J011_A: seed 3 frac 0.01: real 3.017 | melhor gen_dfilt_q0.2 2.855 | discr gen 0.4857500000000001 (real 0.193, ok=False) | id: gen 0.48450000000000004 real 0.13445712182554304 ok=False | audit 0.984 | gen 208s | total 5702s
J011_A: seed 3 frac 0.02: real 2.977 | melhor genphys_rfill_w0.3 2.819 | discr gen 0.48224999999999996 (real 0.191, ok=False) | id: gen 0.48362499999999997 real 0.11971987144400942 ok=False | audit 0.973 | gen 212s | total 6147s
J011_A: seed 3 frac 0.05: real 2.461 | melhor genphys_rfill_w0.3 2.377 | discr gen 0.4826250000000002 (real 0.190, ok=False) | id: gen 0.4889999999999999 real 0.09550000000000003 ok=False | audit 0.992 | gen 230s | total 6599s
J011_A: seed 3 frac 0.1: real 2.320 | melhor genphys_rfill_w0.3 2.288 | discr gen 0.48924999999999996 (real 0.118, ok=False) | id: gen 0.48875000000000013 real 0.049000000000000044 ok=False | audit 0.993 | gen 234s | total 7036s
J011_A: seed 4 frac 0.01: real 3.109 | melhor gen_dfilt_q0.5 2.882 | discr gen 0.485 (real 0.124, ok=False) | id: gen 0.48262499999999997 real 0.07631485541288241 ok=False | audit 0.993 | gen 210s | total 7478s
J011_A: seed 4 frac 0.02: real 2.856 | melhor genphys_rfill_w0.3 2.792 | discr gen 0.4873750000000001 (real 0.144, ok=False) | id: gen 0.4876250000000001 real 0.1001595811179502 ok=False | audit 0.981 | gen 215s | total 7922s
J011_A: seed 4 frac 0.05: real 2.463 | melhor genphys_rfill_w0.3 2.379 | discr gen 0.48662499999999986 (real 0.136, ok=False) | id: gen 0.49 real 0.05431329449596434 ok=False | audit 0.983 | gen 228s | total 8372s
J011_A: seed 4 frac 0.1: real 2.304 | melhor genphys_rfill_w1 2.269 | discr gen 0.48862499999999986 (real 0.161, ok=False) | id: gen 0.490625 real 0.05712499999999998 ok=False | audit 0.980 | gen 233s | total 8811s
J011_B: seed 0 frac 0.01: real 2.983 | melhor gen_rfill_w0.3 2.817 | discr gen 0.405875 (real 0.177, ok=False) | id: gen 0.39350000000000007 real 0.1202453987730061 ok=False | audit 0.995 | gen 211s | total 429s
J011_B: seed 0 frac 0.02: real 2.909 | melhor genphys_rfill_w0.3 2.690 | discr gen 0.3629999999999999 (real 0.147, ok=False) | id: gen 0.3707499999999999 real 0.09070943451941538 ok=False | audit 0.989 | gen 213s | total 851s
J011_B: seed 0 frac 0.05: real 2.427 | melhor genphys_rfill_w0.3 2.366 | discr gen 0.3346250000000002 (real 0.226, ok=False) | id: gen 0.29975000000000007 real 0.13937500000000003 ok=False | audit 0.988 | gen 226s | total 1262s
J011_B: seed 0 frac 0.1: real 2.329 | melhor genphys_rfill_w0.3 2.256 | discr gen 0.29537500000000005 (real 0.130, ok=False) | id: gen 0.26925 real 0.051875000000000115 ok=False | audit 0.972 | gen 222s | total 1787s
J011_B: seed 1 frac 0.01: real 3.151 | melhor genphys_rfill_w0.3 3.029 | discr gen 0.43412499999999987 (real 0.182, ok=False) | id: gen 0.4221250000000001 real 0.1528475327752934 ok=False | audit 0.983 | gen 1118s | total 3399s
J011_B: seed 1 frac 0.02: real 2.695 | melhor gen_dfilt_q0.5 2.562 | discr gen 0.35287500000000005 (real 0.114, ok=False) | id: gen 0.35562499999999986 real 0.0906507692307692 ok=False | audit 0.992 | gen 221s | total 3848s
J011_B: seed 1 frac 0.05: real 2.551 | melhor genphys_rfill_w0.3 2.454 | discr gen 0.32862499999999994 (real 0.169, ok=False) | id: gen 0.30174999999999996 real 0.08446194225721781 ok=False | audit 0.981 | gen 213s | total 4258s
J011_B: seed 1 frac 0.1: real 2.362 | melhor genphys_rfill_w0.3 2.308 | discr gen 0.3007500000000001 (real 0.144, ok=False) | id: gen 0.27225 real 0.050000000000000044 ok=False | audit 0.983 | gen 212s | total 4643s
J011_B: seed 2 frac 0.01: real 3.063 | melhor gen_r1_w0.3 2.855 | discr gen 0.4039999999999999 (real 0.142, ok=False) | id: gen 0.39349999999999985 real 0.10604026845637582 ok=False | audit 0.989 | gen 188s | total 5035s
J011_B: seed 2 frac 0.02: real 2.834 | melhor genphys_rfill_w0.3 2.665 | discr gen 0.360375 (real 0.145, ok=False) | id: gen 0.35250000000000004 real 0.061003093414764065 ok=False | audit 0.986 | gen 189s | total 5423s
J011_B: seed 2 frac 0.05: real 2.513 | melhor genphys_rfill_w0.3 2.420 | discr gen 0.3095000000000001 (real 0.164, ok=False) | id: gen 0.2858750000000001 real 0.08074999999999999 ok=False | audit 0.982 | gen 203s | total 5816s
J011_B: seed 2 frac 0.1: real 2.322 | melhor genphys_rfill_w0.3 2.272 | discr gen 0.3011250000000001 (real 0.158, ok=False) | id: gen 0.2782500000000001 real 0.055499999999999994 ok=False | audit 0.985 | gen 208s | total 6193s
J011_B: seed 3 frac 0.01: real 3.017 | melhor genphys_r1_w1 2.781 | discr gen 0.41874999999999996 (real 0.193, ok=False) | id: gen 0.4108750000000001 real 0.13445712182554304 ok=False | audit 0.985 | gen 186s | total 6579s
J011_B: seed 3 frac 0.02: real 2.977 | melhor genphys_rfill_w0.3 2.820 | discr gen 0.4181250000000001 (real 0.191, ok=False) | id: gen 0.39837500000000003 real 0.11971987144400942 ok=False | audit 0.980 | gen 188s | total 6969s
J011_B: seed 3 frac 0.05: real 2.461 | melhor genphys_rfill_w0.3 2.361 | discr gen 0.32562499999999994 (real 0.190, ok=False) | id: gen 0.27774999999999994 real 0.09550000000000003 ok=False | audit 0.992 | gen 205s | total 7365s
J011_B: seed 3 frac 0.1: real 2.320 | melhor genphys_rfill_w0.3 2.262 | discr gen 0.28012499999999996 (real 0.118, ok=False) | id: gen 0.26412500000000005 real 0.049000000000000044 ok=False | audit 0.981 | gen 213s | total 7758s
J011_B: seed 4 frac 0.01: real 3.109 | melhor gen_dfilt_q0.5 2.901 | discr gen 0.40425 (real 0.124, ok=False) | id: gen 0.40075000000000005 real 0.07631485541288241 ok=False | audit 0.994 | gen 198s | total 8163s
J011_B: seed 4 frac 0.02: real 2.856 | melhor gen_r1_w0.3 2.758 | discr gen 0.3711249999999999 (real 0.144, ok=False) | id: gen 0.36349999999999993 real 0.1001595811179502 ok=False | audit 0.983 | gen 207s | total 8575s
J011_B: seed 4 frac 0.05: real 2.463 | melhor genphys_rfill_w0.3 2.383 | discr gen 0.29075000000000006 (real 0.136, ok=False) | id: gen 0.284875 real 0.05431329449596434 ok=False | audit 0.983 | gen 215s | total 8995s
J011_B: seed 4 frac 0.1: real 2.304 | melhor genphys_rfill_w0.3 2.252 | discr gen 0.30700000000000005 (real 0.161, ok=False) | id: gen 0.27212500000000006 real 0.05712499999999998 ok=False | audit 0.975 | gen 214s | total 9382s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T22:06:18-03:00 — duração do job 18242 s
