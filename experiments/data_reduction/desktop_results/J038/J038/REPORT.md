# J038 — REPORT

Máquina: desktop RTX 3060. Hashes (16 primeiros): run3.py f989a1914e9bf8a8; gens.py 580277d75326c94d; timegan.py d6baf805f9e5d158; timevae.py 8d32542e42a36464; 

## Comandos
    python -u run3.py ../data out/J038_mlp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --model mlp --seeds 3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3

## Comando 1: J038_mlp
- início: 2026-10-11 08:54:44
- fim: 2026-10-11 10:08:13
- duração: 4409s
- código de saída: 0
- linhas seed/frac do log (8 de 8):
```
seed 3 frac 0.01: real 4.716 | melhor gen_rfill_w0.3 2.925 | discr gen 0.38849999999999996 (real 0.193, ok=False) | id: gen 0.37387499999999996 real 0.13445712182554304 ok=False | audit 0.987 | gen 310s | total 579s
seed 3 frac 0.02: real 4.549 | melhor genphys_rfill_w0.3 2.787 | discr gen 0.35250000000000004 (real 0.191, ok=False) | id: gen 0.3365 real 0.11971987144400942 ok=False | audit 0.979 | gen 289s | total 1122s
seed 3 frac 0.05: real 3.053 | melhor gen_rfill_w1 2.475 | discr gen 0.281625 (real 0.190, ok=False) | id: gen 0.21324999999999994 real 0.09550000000000003 ok=False | audit 0.990 | gen 290s | total 1665s
seed 3 frac 0.1: real 2.833 | melhor genphys_rfill_w0.3 2.445 | discr gen 0.22399999999999998 (real 0.118, ok=False) | id: gen 0.18775000000000008 real 0.049000000000000044 ok=False | audit 0.964 | gen 291s | total 2191s
seed 4 frac 0.01: real 5.523 | melhor gen_rfill_w1 2.975 | discr gen 0.3543749999999999 (real 0.124, ok=False) | id: gen 0.35225000000000006 real 0.07631485541288241 ok=False | audit 0.994 | gen 289s | total 2735s
seed 4 frac 0.02: real 3.694 | melhor gen_rfill_w1 2.671 | discr gen 0.31899999999999995 (real 0.144, ok=False) | id: gen 0.3125 real 0.1001595811179502 ok=False | audit 0.981 | gen 289s | total 3286s
seed 4 frac 0.05: real 3.266 | melhor gen_rfill_w0.3 2.444 | discr gen 0.2762499999999999 (real 0.136, ok=False) | id: gen 0.242 real 0.05431329449596434 ok=False | audit 0.967 | gen 288s | total 3848s
seed 4 frac 0.1: real 2.712 | melhor gen_rfill_w0.3 2.440 | discr gen 0.2743749999999999 (real 0.161, ok=False) | id: gen 0.17962500000000003 real 0.05712499999999998 ok=False | audit 0.953 | gen 288s | total 4384s
```

## Total
- início: 2026-10-11 08:54:44
- fim: 2026-10-11 10:08:14
- duração: 4410s
- situação: ok 
