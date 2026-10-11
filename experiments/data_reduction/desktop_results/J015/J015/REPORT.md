# J015 — Validação cruzada por blocos de tanques (o efeito não depende de um único teste); DDPM do J009_A, 3 sementes

Início: 2026-10-02T12:35:31-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `7e6d22971cb280aa72cd6fa74817b7cb2729bb918e0f295a435f41571589bd97`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J015_f1 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --test-segs 8-12 --pool-segs 13-22 --seeds 0,1,2 --fracs 0.01,0.02,0.05` | J015_f1 | 0 | 5848 s | `7e6d22971cb280aa72cd6fa74817b7cb2729bb918e0f295a435f41571589bd97` |
| 2 | `python -u run3.py ../data out/J015_f2 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --test-segs 13-17 --pool-segs 8-12,18-22 --seeds 0,1,2 --fracs 0.01,0.02,0.05` | J015_f2 | 0 | 5682 s | `7e6d22971cb280aa72cd6fa74817b7cb2729bb918e0f295a435f41571589bd97` |

## Linhas "seed … frac …" dos logs

```
J015_f1: seed 0 frac 0.01: real 3.930 | melhor gen_rfill_w1 3.303 | discr gen 0.42925 (real 0.170, ok=False) | id: gen 0.40075000000000005 real 0.15157004830917864 ok=False | audit 0.993 | gen 320s | total 675s
J015_f1: seed 0 frac 0.02: real 3.392 | melhor gen_rfill_w0.3 2.905 | discr gen 0.3425 (real 0.171, ok=False) | id: gen 0.279875 real 0.06770329278712595 ok=False | audit 0.994 | gen 319s | total 1344s
J015_f1: seed 0 frac 0.05: real 2.920 | melhor gen_rfill_w1 2.673 | discr gen 0.270875 (real 0.161, ok=False) | id: gen 0.2157500000000001 real 0.0645 ok=False | audit 0.971 | gen 320s | total 2007s
J015_f1: seed 1 frac 0.01: real 4.009 | melhor gen_rfill_w0.3 3.130 | discr gen 0.39925 (real 0.159, ok=False) | id: gen 0.37787500000000007 real 0.13972602739726026 ok=False | audit 0.987 | gen 321s | total 2685s
J015_f1: seed 1 frac 0.02: real 3.245 | melhor hyb_feat_w0.3 2.865 | discr gen 0.320875 (real 0.119, ok=False) | id: gen 0.273625 real 0.0839080459770114 ok=False | audit 0.988 | gen 322s | total 3370s
J015_f1: seed 1 frac 0.05: real 2.895 | melhor gen_rfill_w0.3 2.676 | discr gen 0.25775000000000003 (real 0.164, ok=False) | id: gen 0.21487500000000004 real 0.06912499999999999 ok=False | audit 0.969 | gen 290s | total 3996s
J015_f1: seed 2 frac 0.01: real 4.108 | melhor gen_rfill_w0.3 3.259 | discr gen 0.44000000000000006 (real 0.195, ok=False) | id: gen 0.4265000000000001 real 0.16497633536173084 ok=False | audit 0.955 | gen 282s | total 4610s
J015_f1: seed 2 frac 0.02: real 3.528 | melhor gen_rfill_w1 3.116 | discr gen 0.36024999999999996 (real 0.168, ok=False) | id: gen 0.31737499999999985 real 0.11655172413793102 ok=False | audit 0.979 | gen 283s | total 5233s
J015_f1: seed 2 frac 0.05: real 3.065 | melhor gen_rfill_w0.3 2.862 | discr gen 0.27625 (real 0.198, ok=False) | id: gen 0.21175 real 0.103375 ok=False | audit 0.957 | gen 282s | total 5843s
J015_f2: seed 0 frac 0.01: real 3.347 | melhor gen_rfill_w0.3 2.810 | discr gen 0.33862500000000006 (real 0.188, ok=False) | id: gen 0.326125 real 0.15099835067797351 ok=False | audit 0.989 | gen 284s | total 630s
J015_f2: seed 0 frac 0.02: real 2.897 | melhor gen_rfill_w1 2.618 | discr gen 0.31400000000000006 (real 0.104, ok=False) | id: gen 0.29975000000000007 real 0.0785024110525323 ok=False | audit 0.989 | gen 283s | total 1252s
J015_f2: seed 0 frac 0.05: real 2.593 | melhor genphys_rfill_w0.3 2.498 | discr gen 0.2386250000000001 (real 0.145, ok=False) | id: gen 0.18825000000000003 real 0.074125 ok=False | audit 0.966 | gen 296s | total 1883s
J015_f2: seed 1 frac 0.01: real 3.878 | melhor genphys_rfill_w1 3.550 | discr gen 0.43225 (real 0.220, ok=False) | id: gen 0.4401250000000001 real 0.21942154806613667 ok=False | audit 0.990 | gen 295s | total 2508s
J015_f2: seed 1 frac 0.02: real 2.992 | melhor genphys_rfill_w0.3 2.768 | discr gen 0.32887500000000003 (real 0.187, ok=False) | id: gen 0.3151249999999999 real 0.09931613688675822 ok=False | audit 0.990 | gen 294s | total 3144s
J015_f2: seed 1 frac 0.05: real 2.670 | melhor hyb_feat_w0.3 2.563 | discr gen 0.23350000000000004 (real 0.139, ok=False) | id: gen 0.22599999999999998 real 0.05875000000000008 ok=False | audit 0.970 | gen 293s | total 3760s
J015_f2: seed 2 frac 0.01: real 4.102 | melhor gen_rfill_w1 2.876 | discr gen 0.36175 (real 0.129, ok=False) | id: gen 0.3476250000000001 real 0.062092624356775206 ok=False | audit 0.979 | gen 295s | total 4404s
J015_f2: seed 2 frac 0.02: real 2.948 | melhor gen_rfill_w0.3 2.699 | discr gen 0.3087500000000001 (real 0.125, ok=False) | id: gen 0.30437499999999995 real 0.0950326539557308 ok=False | audit 0.984 | gen 298s | total 5041s
J015_f2: seed 2 frac 0.05: real 2.668 | melhor gen_rfill_w0.3 2.504 | discr gen 0.24025000000000007 (real 0.142, ok=False) | id: gen 0.21000000000000008 real 0.071125 ok=False | audit 0.972 | gen 311s | total 5675s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T15:48:15-03:00 — duração do job 11564 s
