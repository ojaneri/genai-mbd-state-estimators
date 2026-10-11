# J012 — Rodada 6: a melhor configuração até agora (J009_A: DDPM v1 50k h128, dequant + quant) medida pela meta

Início: 2026-10-01T22:10:14-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `d322907e17bebeb51efff8e4f8136bcaaf472069f039063d72c93395aba45232`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J012 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1` | J012 | 0 (reaproveitado) | — | `d322907e17bebeb51efff8e4f8136bcaaf472069f039063d72c93395aba45232` |

## Linhas "seed … frac …" dos logs

```
J012: seed 5 frac 0.01: real 2.839 | melhor gen_rfill_w0.3 2.554 | discr gen 0.367625 (real 0.109, ok=False) | id: gen 0.36225000000000007 real 0.09746042363433671 ok=False | audit 0.990 | gen 304s | total 630s
J012: seed 5 frac 0.02: real 2.821 | melhor gen_rfill_w0.3 2.563 | discr gen 0.3204999999999998 (real 0.116, ok=False) | id: gen 0.32237499999999986 real 0.10841510090466255 ok=False | audit 0.991 | gen 300s | total 1252s
J012: seed 5 frac 0.05: real 2.479 | melhor genphys_rfill_w0.3 2.387 | discr gen 0.268 (real 0.161, ok=False) | id: gen 0.23375 real 0.09950000000000003 ok=False | audit 0.969 | gen 298s | total 1854s
J012: seed 5 frac 0.1: real 2.330 | melhor genphys_rfill_w0.3 2.272 | discr gen 0.26149999999999995 (real 0.153, ok=False) | id: gen 0.1855 real 0.05524999999999991 ok=False | audit 0.955 | gen 299s | total 2435s
J012: seed 6 frac 0.01: real 2.980 | melhor gen_pretrain 2.702 | discr gen 0.38375000000000004 (real 0.171, ok=False) | id: gen 0.375625 real 0.09756680731364276 ok=False | audit 0.983 | gen 299s | total 3059s
J012: seed 6 frac 0.02: real 2.732 | melhor gen_rfill_w0.3 2.528 | discr gen 0.296625 (real 0.086, ok=False) | id: gen 0.3091250000000001 real 0.07199636939117482 ok=False | audit 0.980 | gen 298s | total 3677s
J012: seed 6 frac 0.05: real 2.505 | melhor gen_rfill_w0.3 2.393 | discr gen 0.2446250000000001 (real 0.138, ok=False) | id: gen 0.20937499999999998 real 0.050565383864459745 ok=False | audit 0.966 | gen 297s | total 4281s
J012: seed 6 frac 0.1: real 2.378 | melhor gen_rfill_w0.3 2.308 | discr gen 0.251625 (real 0.140, ok=False) | id: gen 0.18987500000000002 real 0.06262500000000004 ok=False | audit 0.949 | gen 299s | total 4860s
J012: seed 7 frac 0.01: real 3.151 | melhor gen_rfill_w1 2.596 | discr gen 0.39137500000000003 (real 0.165, ok=False) | id: gen 0.36475000000000013 real 0.08387096774193548 ok=False | audit 0.993 | gen 298s | total 5486s
J012: seed 7 frac 0.02: real 2.917 | melhor gen_rfill_w0.3 2.466 | discr gen 0.3317500000000001 (real 0.145, ok=False) | id: gen 0.30574999999999997 real 0.08643485777149151 ok=False | audit 0.981 | gen 298s | total 6104s
J012: seed 7 frac 0.05: real 2.471 | melhor gen_rfill_w0.3 2.363 | discr gen 0.27612500000000006 (real 0.154, ok=False) | id: gen 0.22099999999999997 real 0.05913840208173482 ok=False | audit 0.959 | gen 297s | total 6711s
J012: seed 7 frac 0.1: real 2.346 | melhor genphys_rfill_w0.3 2.284 | discr gen 0.265875 (real 0.148, ok=False) | id: gen 0.2061249999999999 real 0.048374999999999946 ok=False | audit 0.944 | gen 298s | total 7292s
J012: seed 8 frac 0.01: real 3.231 | melhor gen_pretrain 3.014 | discr gen 0.411875 (real 0.203, ok=False) | id: gen 0.3949999999999999 real 0.14474721261053447 ok=False | audit 0.995 | gen 298s | total 7915s
J012: seed 8 frac 0.02: real 3.147 | melhor gen_pretrain 2.895 | discr gen 0.36850000000000005 (real 0.142, ok=False) | id: gen 0.35687499999999994 real 0.11592532467532468 ok=False | audit 0.994 | gen 298s | total 8534s
J012: seed 8 frac 0.05: real 2.466 | melhor gen_rfill_w0.3 2.357 | discr gen 0.2765000000000001 (real 0.169, ok=False) | id: gen 0.22787500000000005 real 0.07952829249249405 ok=False | audit 0.984 | gen 298s | total 9142s
J012: seed 8 frac 0.1: real 2.328 | melhor gen_dfilt_q0.5 2.287 | discr gen 0.23062500000000008 (real 0.106, ok=False) | id: gen 0.1947500000000001 real 0.04600000000000004 ok=False | audit 0.976 | gen 298s | total 9724s
J012: seed 9 frac 0.01: real 3.230 | melhor gen_rfill_w0.3 2.614 | discr gen 0.3739999999999999 (real 0.164, ok=False) | id: gen 0.3526250000000001 real 0.10394712894712899 ok=False | audit 0.995 | gen 299s | total 10344s
J012: seed 9 frac 0.02: real 2.889 | melhor gen_rfill_w0.3 2.466 | discr gen 0.28837500000000005 (real 0.151, ok=False) | id: gen 0.263625 real 0.06466323342822711 ok=False | audit 0.972 | gen 297s | total 10963s
J012: seed 9 frac 0.05: real 2.468 | melhor gen_rfill_w0.3 2.367 | discr gen 0.24387499999999995 (real 0.136, ok=False) | id: gen 0.2313750000000001 real 0.10037499999999999 ok=False | audit 0.958 | gen 298s | total 11568s
J012: seed 9 frac 0.1: real 2.351 | melhor gen_pretrain 2.322 | discr gen 0.22249999999999992 (real 0.162, ok=False) | id: gen 0.20987499999999992 real 0.06549999999999989 ok=False | audit 0.959 | gen 297s | total 12150s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T01:30:15-03:00 — duração do job 12001 s
