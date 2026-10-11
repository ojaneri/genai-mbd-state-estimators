# J016 — Curva de aprendizado ampliada (onde o ganho some; "quanto dado real o sintético vale") — proposto pelo desktop

Início: 2026-10-03T03:03:44-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J016_curva --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.03,0.2,0.3 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3` | J016_curva | 0 | 7416 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J016_curva: seed 0 frac 0.03: real 2.573 | melhor gen_rfill_w0.3 2.399 | discr gen 0.28725 (real 0.167, ok=False) | id: gen 0.21075 real 0.046126760563380165 ok=False | audit 0.978 | gen 303s | total 544s
J016_curva: seed 0 frac 0.2: real 2.236 | melhor gen_rfill_w0.3 2.198 | discr gen 0.22575 (real 0.117, ok=False) | id: gen 0.18212499999999998 real 0.044625000000000026 ok=False | audit 0.956 | gen 293s | total 1031s
J016_curva: seed 0 frac 0.3: real 2.211 | melhor genphys_rfill_w0.3 2.205 | discr gen 0.2333749999999999 (real 0.137, ok=False) | id: gen 0.17562500000000003 real 0.04250000000000009 ok=False | audit 0.933 | gen 285s | total 1497s
J016_curva: seed 1 frac 0.03: real 2.604 | melhor gen_rfill_w0.3 2.398 | discr gen 0.2911250000000001 (real 0.171, ok=False) | id: gen 0.22937499999999988 real 0.05761902197328739 ok=False | audit 0.976 | gen 283s | total 2004s
J016_curva: seed 1 frac 0.2: real 2.236 | melhor genphys_rfill_w0.3 2.215 | discr gen 0.23812499999999992 (real 0.127, ok=False) | id: gen 0.15425 real 0.030500000000000083 ok=False | audit 0.957 | gen 284s | total 2485s
J016_curva: seed 1 frac 0.3: real 2.225 | melhor genphys_rfill_w0.3 2.222 | discr gen 0.27049999999999996 (real 0.130, ok=False) | id: gen 0.19599999999999995 real 0.024375000000000036 ok=False | audit 0.943 | gen 285s | total 2950s
J016_curva: seed 2 frac 0.03: real 2.586 | melhor gen_rfill_w0.3 2.431 | discr gen 0.28475000000000006 (real 0.164, ok=False) | id: gen 0.24075000000000002 real 0.09443207126948772 ok=False | audit 0.984 | gen 283s | total 3455s
J016_curva: seed 2 frac 0.2: real 2.334 | melhor gen_rfill_w0.3 2.267 | discr gen 0.23962499999999998 (real 0.146, ok=False) | id: gen 0.1692499999999999 real 0.039125000000000076 ok=False | audit 0.937 | gen 284s | total 3935s
J016_curva: seed 2 frac 0.3: real 2.250 | melhor gen_rfill_w0.3 2.198 | discr gen 0.23724999999999996 (real 0.131, ok=False) | id: gen 0.16625 real 0.017125000000000057 ok=False | audit 0.940 | gen 282s | total 4395s
J016_curva: seed 3 frac 0.03: real 2.638 | melhor gen_rfill_w0.3 2.429 | discr gen 0.279 (real 0.164, ok=False) | id: gen 0.27374999999999994 real 0.1399178648422328 ok=False | audit 0.987 | gen 301s | total 4928s
J016_curva: seed 3 frac 0.2: real 2.264 | melhor gen_rfill_w0.3 2.222 | discr gen 0.24675000000000002 (real 0.151, ok=False) | id: gen 0.18237499999999995 real 0.04074999999999995 ok=False | audit 0.960 | gen 295s | total 5423s
J016_curva: seed 3 frac 0.3: real 2.234 | melhor genphys_rfill_w0.3 2.204 | discr gen 0.25250000000000006 (real 0.119, ok=False) | id: gen 0.18337499999999995 real 0.02562500000000001 ok=False | audit 0.949 | gen 295s | total 5904s
J016_curva: seed 4 frac 0.03: real 2.578 | melhor gen_rfill_w0.3 2.451 | discr gen 0.33125000000000004 (real 0.198, ok=False) | id: gen 0.27474999999999994 real 0.08824841890069413 ok=False | audit 0.981 | gen 293s | total 6429s
J016_curva: seed 4 frac 0.2: real 2.267 | melhor genphys_rfill_w0.3 2.255 | discr gen 0.275 (real 0.152, ok=False) | id: gen 0.22699999999999998 real 0.04962500000000003 ok=False | audit 0.964 | gen 294s | total 6927s
J016_curva: seed 4 frac 0.3: real 2.219 | melhor genphys_rfill_w0.3 2.195 | discr gen 0.2466250000000001 (real 0.129, ok=False) | id: gen 0.19000000000000006 real 0.04162500000000002 ok=False | audit 0.963 | gen 294s | total 7408s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T05:08:00-03:00 — duração do job 7456 s
