# J035c — REFAZ J035b (mesma causa)

Início: 2026-10-04T21:57:16-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_besstemp out/J035c_besstemp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3` | J035c_besstemp | 0 | 21290 s | `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310` |

## Linhas "seed … frac …" dos logs

```
J035c_besstemp: seed 0 frac 0.01: real 0.418 | melhor hyb_feat_real 0.415 | discr gen 0.486375 (real 0.440, ok=True) | id: gen 0.4832500000000002 real 0.42037499999999994 ok=False | audit 0.859 | gen 286s | total 1107s
J035c_besstemp: seed 0 frac 0.02: real 0.417 | melhor genphys_rfill_w0.3 0.406 | discr gen 0.4867500000000001 (real 0.398, ok=False) | id: gen 0.48512500000000003 real 0.34887499999999994 ok=False | audit 0.842 | gen 284s | total 2183s
J035c_besstemp: seed 0 frac 0.05: real 0.425 | melhor gen_rfill_w0.3 0.413 | discr gen 0.4876250000000001 (real 0.342, ok=False) | id: gen 0.48375 real 0.23249999999999993 ok=False | audit 0.830 | gen 286s | total 3234s
J035c_besstemp: seed 0 frac 0.1: real 0.384 | melhor hyb_feat_w0.3 0.379 | discr gen 0.48987499999999995 (real 0.287, ok=False) | id: gen 0.4883750000000001 real 0.13987499999999997 ok=False | audit 0.834 | gen 289s | total 4283s
J035c_besstemp: seed 1 frac 0.01: real 0.508 | melhor genphys_rfill_w0.3 0.433 | discr gen 0.4897499999999999 (real 0.439, ok=False) | id: gen 0.49 real 0.4026249999999999 ok=False | audit 0.836 | gen 301s | total 5386s
J035c_besstemp: seed 1 frac 0.02: real 0.413 | melhor hyb_resid_w0.3 0.395 | discr gen 0.4877499999999999 (real 0.388, ok=False) | id: gen 0.486 real 0.3264999999999999 ok=False | audit 0.846 | gen 288s | total 6466s
J035c_besstemp: seed 1 frac 0.05: real 0.389 | melhor genphys_rfill_w0.3 0.381 | discr gen 0.4891249999999999 (real 0.327, ok=False) | id: gen 0.485 real 0.25224999999999986 ok=False | audit 0.842 | gen 285s | total 7523s
J035c_besstemp: seed 1 frac 0.1: real 0.397 | melhor hyb_resid_w0.3 0.392 | discr gen 0.48812500000000014 (real 0.287, ok=False) | id: gen 0.48849999999999993 real 0.170875 ok=False | audit 0.826 | gen 285s | total 8548s
J035c_besstemp: seed 2 frac 0.01: real 0.470 | melhor genphys_rfill_w0.3 0.450 | discr gen 0.48887499999999995 (real 0.449, ok=True) | id: gen 0.4901249999999999 real 0.4233091601990603 ok=False | audit 0.868 | gen 285s | total 9636s
J035c_besstemp: seed 2 frac 0.02: real 0.481 | melhor hyb_resid_w0.3 0.432 | discr gen 0.4911249999999999 (real 0.421, ok=False) | id: gen 0.4901249999999999 real 0.3563749999999999 ok=False | audit 0.821 | gen 285s | total 10719s
J035c_besstemp: seed 2 frac 0.05: real 0.410 | melhor gen_rfill_w0.3 0.406 | discr gen 0.4899999999999999 (real 0.338, ok=False) | id: gen 0.48575 real 0.22362499999999996 ok=False | audit 0.818 | gen 284s | total 11773s
J035c_besstemp: seed 2 frac 0.1: real 0.388 | melhor hyb_feat_w0.3 0.382 | discr gen 0.49049999999999994 (real 0.286, ok=False) | id: gen 0.484375 real 0.169875 ok=False | audit 0.813 | gen 284s | total 12789s
J035c_besstemp: seed 3 frac 0.01: real 0.463 | melhor genphys_rfill_w0.3 0.433 | discr gen 0.493 (real 0.452, ok=True) | id: gen 0.48262499999999997 real 0.4099999999999999 ok=False | audit 0.839 | gen 284s | total 13878s
J035c_besstemp: seed 3 frac 0.02: real 0.400 | melhor hyb_feat_real 0.399 | discr gen 0.48987499999999995 (real 0.388, ok=False) | id: gen 0.48987499999999995 real 0.3385 ok=False | audit 0.845 | gen 284s | total 14954s
J035c_besstemp: seed 3 frac 0.05: real 0.394 | melhor genphys_rfill_w0.3 0.390 | discr gen 0.48875000000000013 (real 0.331, ok=False) | id: gen 0.486 real 0.23512500000000003 ok=False | audit 0.847 | gen 283s | total 16009s
J035c_besstemp: seed 3 frac 0.1: real 0.399 | melhor hyb_resid_w0.3 0.389 | discr gen 0.491625 (real 0.293, ok=False) | id: gen 0.490375 real 0.16225 ok=False | audit 0.843 | gen 284s | total 17030s
J035c_besstemp: seed 4 frac 0.01: real 0.418 | melhor real 0.418 | discr gen 0.48687500000000006 (real 0.424, ok=False) | id: gen 0.483125 real 0.39323308270676693 ok=False | audit 0.832 | gen 285s | total 18118s
J035c_besstemp: seed 4 frac 0.02: real 0.416 | melhor hyb_resid_w0.3 0.396 | discr gen 0.48324999999999996 (real 0.404, ok=False) | id: gen 0.47787500000000005 real 0.34450000000000003 ok=False | audit 0.848 | gen 283s | total 19196s
J035c_besstemp: seed 4 frac 0.05: real 0.416 | melhor genphys_rfill_w0.3 0.409 | discr gen 0.48987499999999995 (real 0.313, ok=False) | id: gen 0.48550000000000004 real 0.20537499999999997 ok=False | audit 0.845 | gen 283s | total 20253s
J035c_besstemp: seed 4 frac 0.1: real 0.380 | melhor gen_rfill_w0.3 0.364 | discr gen 0.4907499999999999 (real 0.287, ok=False) | id: gen 0.4897499999999999 real 0.17725000000000002 ok=False | audit 0.846 | gen 282s | total 21274s
```

## Falhas

Nenhuma.

Fim: 2026-10-05T03:52:31-03:00 — duração do job 21315 s
