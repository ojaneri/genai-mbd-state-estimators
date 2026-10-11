# J040 — REPORT

Máquina: desktop RTX 3060. Hashes (16 primeiros): run3.py f989a1914e9bf8a8; gens.py 580277d75326c94d; timegan.py d6baf805f9e5d158; timevae.py 8d32542e42a36464; 

## Comandos
    python -u run3.py ../data_besstemp out/J040_besstemp_boot --gen bootstrap --post none --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3

## Comando 1: J040_besstemp_boot
- início: 2026-10-11 10:30:17
- fim: 2026-10-11 11:07:22
- duração: 2225s
- código de saída: 0
- linhas seed/frac do log (20 de 20):
```
seed 0 frac 0.01: real 0.418 | melhor real 0.418 | discr gen 0.4648749999999999 (real 0.440, ok=True) | id: gen 0.4487500000000001 real 0.42037499999999994 ok=True | audit 0.260 | gen 0s | total 153s
seed 0 frac 0.02: real 0.417 | melhor hyb_resid_w0.3 0.401 | discr gen 0.4375 (real 0.398, ok=True) | id: gen 0.41200000000000014 real 0.34887499999999994 ok=False | audit 0.200 | gen 0s | total 263s
seed 0 frac 0.05: real 0.425 | melhor hyb_resid_w0.3 0.412 | discr gen 0.41974999999999996 (real 0.342, ok=False) | id: gen 0.3787499999999999 real 0.23249999999999993 ok=False | audit 0.145 | gen 0s | total 364s
seed 0 frac 0.1: real 0.384 | melhor gen_rfill_w0.3 0.380 | discr gen 0.3946249999999999 (real 0.287, ok=False) | id: gen 0.359625 real 0.13987499999999997 ok=False | audit 0.107 | gen 0s | total 467s
seed 1 frac 0.01: real 0.508 | melhor physonly 0.445 | discr gen 0.45799999999999996 (real 0.439, ok=True) | id: gen 0.43699999999999994 real 0.4026249999999999 ok=True | audit 0.303 | gen 0s | total 593s
seed 1 frac 0.02: real 0.413 | melhor hyb_resid_w0.3 0.405 | discr gen 0.43700000000000006 (real 0.388, ok=True) | id: gen 0.4105000000000001 real 0.3264999999999999 ok=False | audit 0.189 | gen 0s | total 697s
seed 1 frac 0.05: real 0.389 | melhor hyb_resid_w0.3 0.379 | discr gen 0.4119999999999999 (real 0.327, ok=False) | id: gen 0.37512500000000004 real 0.25224999999999986 ok=False | audit 0.137 | gen 0s | total 797s
seed 1 frac 0.1: real 0.397 | melhor hyb_resid_w0.3 0.389 | discr gen 0.39649999999999996 (real 0.287, ok=False) | id: gen 0.35924999999999996 real 0.170875 ok=False | audit 0.108 | gen 0s | total 902s
seed 2 frac 0.01: real 0.470 | melhor gen_rfill_w0.3 0.467 | discr gen 0.4661250000000001 (real 0.449, ok=True) | id: gen 0.4475 real 0.4233091601990603 ok=True | audit 0.249 | gen 0s | total 1026s
seed 2 frac 0.02: real 0.481 | melhor hyb_resid_w0.3 0.449 | discr gen 0.4467500000000001 (real 0.421, ok=True) | id: gen 0.41937499999999994 real 0.3563749999999999 ok=False | audit 0.205 | gen 0s | total 1134s
seed 2 frac 0.05: real 0.410 | melhor physonly 0.406 | discr gen 0.4028750000000001 (real 0.338, ok=False) | id: gen 0.3607500000000001 real 0.22362499999999996 ok=False | audit 0.130 | gen 0s | total 1234s
seed 2 frac 0.1: real 0.388 | melhor gen_rfill_w0.3 0.385 | discr gen 0.40012499999999984 (real 0.286, ok=False) | id: gen 0.36150000000000004 real 0.169875 ok=False | audit 0.122 | gen 0s | total 1338s
seed 3 frac 0.01: real 0.463 | melhor physonly 0.449 | discr gen 0.4567500000000001 (real 0.452, ok=True) | id: gen 0.43925000000000003 real 0.4099999999999999 ok=True | audit 0.258 | gen 0s | total 1463s
seed 3 frac 0.02: real 0.400 | melhor gen_rfill_w0.3 0.396 | discr gen 0.43225000000000013 (real 0.388, ok=True) | id: gen 0.4092500000000001 real 0.3385 ok=False | audit 0.204 | gen 0s | total 1573s
seed 3 frac 0.05: real 0.394 | melhor gen_rfill_w0.3 0.388 | discr gen 0.407625 (real 0.331, ok=False) | id: gen 0.374625 real 0.23512500000000003 ok=False | audit 0.129 | gen 0s | total 1674s
seed 3 frac 0.1: real 0.399 | melhor hyb_resid_w0.3 0.391 | discr gen 0.40849999999999986 (real 0.293, ok=False) | id: gen 0.3610000000000001 real 0.16225 ok=False | audit 0.124 | gen 0s | total 1776s
seed 4 frac 0.01: real 0.418 | melhor real 0.418 | discr gen 0.4425000000000001 (real 0.424, ok=True) | id: gen 0.420625 real 0.39323308270676693 ok=True | audit 0.221 | gen 0s | total 1895s
seed 4 frac 0.02: real 0.416 | melhor hyb_resid_w0.3 0.396 | discr gen 0.4475000000000001 (real 0.404, ok=True) | id: gen 0.412875 real 0.34450000000000003 ok=False | audit 0.211 | gen 0s | total 2007s
seed 4 frac 0.05: real 0.416 | melhor hyb_resid_w0.3 0.408 | discr gen 0.40312499999999996 (real 0.313, ok=False) | id: gen 0.36750000000000005 real 0.20537499999999997 ok=False | audit 0.124 | gen 0s | total 2107s
seed 4 frac 0.1: real 0.380 | melhor hyb_resid_w0.3 0.376 | discr gen 0.4 (real 0.287, ok=False) | id: gen 0.37187499999999996 real 0.17725000000000002 ok=False | audit 0.127 | gen 0s | total 2213s
```

## Total
- início: 2026-10-11 10:30:17
- fim: 2026-10-11 11:07:22
- duração: 2225s
- situação: ok 
