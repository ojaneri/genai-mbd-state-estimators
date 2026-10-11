# J039 — REPORT

Máquina: desktop RTX 3060. Hashes (16 primeiros): run3.py f989a1914e9bf8a8; gens.py 580277d75326c94d; timegan.py d6baf805f9e5d158; timevae.py 8d32542e42a36464; 

## Comandos
    python -u run3.py ../data_itabira out/J039_ita_boot --gen bootstrap --post none --res-auto --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3

## Comando 1: J039_ita_boot
- início: 2026-10-11 10:09:00
- fim: 2026-10-11 10:29:30
- duração: 1230s
- código de saída: 0
- linhas seed/frac do log (20 de 20):
```
seed 0 frac 0.01: real 27.301 | melhor real 27.301 | discr gen 0.499625 (real 0.246, ok=False) | id: gen 0.49912500000000004 real 0.26866096866096867 ok=False | audit 0.831 | gen 0s | total 49s
seed 0 frac 0.02: real 37.612 | melhor real 37.612 | discr gen 0.499625 (real 0.487, ok=True) | id: gen 0.4723749999999999 real 0.3228785315079732 ok=False | audit 0.951 | gen 0s | total 111s
seed 0 frac 0.05: real 26.636 | melhor hyb_resid_w0.3 25.153 | discr gen 0.4846250000000001 (real 0.289, ok=False) | id: gen 0.471125 real 0.24185747209003017 ok=False | audit 0.935 | gen 0s | total 179s
seed 0 frac 0.1: real 30.092 | melhor hyb_resid_w0.3 29.783 | discr gen 0.47625000000000006 (real 0.358, ok=False) | id: gen 0.41475000000000006 real 0.15461823138171693 ok=False | audit 0.933 | gen 0s | total 251s
seed 1 frac 0.01: real 34.530 | melhor physonly 32.613 | discr gen 0.49950000000000006 (real 0.416, ok=False) | id: gen 0.49849999999999994 real 0.2390865384615385 ok=False | audit 0.973 | gen 0s | total 306s
seed 1 frac 0.02: real 39.062 | melhor physonly 34.637 | discr gen 0.49950000000000006 (real 0.448, ok=False) | id: gen 0.494375 real 0.2834567901234568 ok=False | audit 0.991 | gen 0s | total 357s
seed 1 frac 0.05: real 33.361 | melhor physonly 33.291 | discr gen 0.49724999999999997 (real 0.447, ok=False) | id: gen 0.4563750000000001 real 0.20012492831981654 ok=False | audit 0.942 | gen 0s | total 428s
seed 1 frac 0.1: real 20.068 | melhor gen_rfill_w0.3 19.547 | discr gen 0.41700000000000004 (real 0.162, ok=False) | id: gen 0.40075000000000005 real 0.21324041811846695 ok=False | audit 0.941 | gen 0s | total 496s
seed 2 frac 0.01: real 30.632 | melhor real 30.632 | discr gen 0.49924999999999997 (real 0.433, ok=False) | id: gen 0.4961249999999999 real 0.29943019943019933 ok=False | audit 0.999 | gen 0s | total 536s
seed 2 frac 0.02: real 21.596 | melhor real 21.596 | discr gen 0.499625 (real 0.090, ok=False) | id: gen 0.498625 real 0.2906462585034013 ok=False | audit 0.887 | gen 0s | total 594s
seed 2 frac 0.05: real 27.149 | melhor real 27.149 | discr gen 0.4886250000000001 (real 0.315, ok=False) | id: gen 0.4733750000000001 real 0.14992397957194648 ok=False | audit 0.947 | gen 0s | total 662s
seed 2 frac 0.1: real 25.602 | melhor hyb_resid_w0.3 24.763 | discr gen 0.45837499999999987 (real 0.228, ok=False) | id: gen 0.4235 real 0.15141890688979887 ok=False | audit 0.960 | gen 0s | total 732s
seed 3 frac 0.01: real 32.400 | melhor real 32.400 | discr gen 0.49950000000000006 (real 0.482, ok=True) | id: gen 0.49787499999999996 real 0.3683794466403162 ok=False | audit 1.000 | gen 0s | total 770s
seed 3 frac 0.02: real 20.124 | melhor hyb_resid_w0.3 19.583 | discr gen 0.477 (real 0.214, ok=False) | id: gen 0.47050000000000003 real 0.32217688782876164 ok=False | audit 0.940 | gen 0s | total 835s
seed 3 frac 0.05: real 27.556 | melhor gen_rfill_w0.3 27.353 | discr gen 0.492 (real 0.323, ok=False) | id: gen 0.46824999999999994 real 0.13697223139283232 ok=False | audit 0.941 | gen 0s | total 904s
seed 3 frac 0.1: real 31.397 | melhor gen_rfill_w0.3 31.293 | discr gen 0.474 (real 0.378, ok=False) | id: gen 0.40875000000000006 real 0.15035172906400385 ok=False | audit 0.913 | gen 0s | total 976s
seed 4 frac 0.01: real 36.693 | melhor physonly 33.932 | discr gen 0.49987500000000007 (real 0.449, ok=False) | id: gen 0.498625 real 0.28051282051282045 ok=False | audit 0.952 | gen 0s | total 1022s
seed 4 frac 0.02: real 33.185 | melhor real 33.185 | discr gen 0.499625 (real 0.411, ok=False) | id: gen 0.4953749999999999 real 0.32236734693877556 ok=False | audit 0.954 | gen 0s | total 1070s
seed 4 frac 0.05: real 28.900 | melhor real 28.900 | discr gen 0.490375 (real 0.370, ok=False) | id: gen 0.4518749999999999 real 0.1400282624723519 ok=False | audit 0.932 | gen 0s | total 1142s
seed 4 frac 0.1: real 24.055 | melhor real 24.055 | discr gen 0.44275 (real 0.245, ok=False) | id: gen 0.3862500000000001 real 0.15733247276356432 ok=False | audit 0.903 | gen 0s | total 1213s
```

## Total
- início: 2026-10-11 10:09:00
- fim: 2026-10-11 10:29:30
- duração: 1230s
- situação: ok 
