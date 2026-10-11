# J034b — REFAZ J034 (mesma causa)

Início: 2026-10-04T14:33:26-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_bess out/J034b_bessauto --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --test-segs 7-8 --pool-segs 1-6 --auto-select --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3` | J034b_bessauto | 0 | 26522 s | `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310` |

## Linhas "seed … frac …" dos logs

```
J034b_bessauto: seed 5 frac 0.01: real 0.095 | melhor hyb_feat_w0.3 0.062 | discr gen 0.4261250000000001 (real 0.448, ok=True) | id: gen 0.39875000000000005 real 0.4224590447285468 ok=True | audit 0.946 | gen 624s | total 2162s
J034b_bessauto: seed 5 frac 0.02: real 0.072 | melhor hyb_feat_w0.3 0.043 | discr gen 0.37212500000000015 (real 0.427, ok=True) | id: gen 0.33675 real 0.3858750000000001 ok=True | audit 0.955 | gen 623s | total 4283s
J034b_bessauto: seed 5 frac 0.05: real 0.045 | melhor hyb_feat_w0.3 0.038 | discr gen 0.29075000000000006 (real 0.349, ok=True) | id: gen 0.265625 real 0.273625 ok=True | audit 0.945 | gen 617s | total 6838s
J034b_bessauto: seed 5 frac 0.1: real 0.041 | melhor hyb_feat_w0.3 0.035 | discr gen 0.30299999999999994 (real 0.299, ok=True) | id: gen 0.2536249999999999 real 0.171875 ok=False | audit 0.947 | gen 283s | total 7864s
J034b_bessauto: seed 6 frac 0.01: real 0.087 | melhor hyb_feat_w0.3 0.051 | discr gen 0.412875 (real 0.465, ok=True) | id: gen 0.40449999999999997 real 0.44822804314329745 ok=True | audit 0.958 | gen 285s | total 8942s
J034b_bessauto: seed 6 frac 0.02: real 0.068 | melhor gen_rfill_w0.3 0.052 | discr gen 0.368 (real 0.419, ok=True) | id: gen 0.3323750000000001 real 0.37187499999999996 ok=True | audit 0.961 | gen 282s | total 10007s
J034b_bessauto: seed 6 frac 0.05: real 0.051 | melhor hyb_feat_w0.3 0.039 | discr gen 0.33599999999999997 (real 0.346, ok=True) | id: gen 0.28275000000000006 real 0.26449999999999996 ok=True | audit 0.941 | gen 283s | total 11054s
J034b_bessauto: seed 6 frac 0.1: real 0.043 | melhor hyb_feat_w0.3 0.035 | discr gen 0.3317499999999999 (real 0.312, ok=True) | id: gen 0.2735000000000001 real 0.2017500000000001 ok=False | audit 0.957 | gen 283s | total 12077s
J034b_bessauto: seed 7 frac 0.01: real 0.074 | melhor hyb_feat_w0.3 0.050 | discr gen 0.4355 (real 0.448, ok=True) | id: gen 0.41037499999999993 real 0.415881551709979 ok=True | audit 0.926 | gen 283s | total 13151s
J034b_bessauto: seed 7 frac 0.02: real 0.070 | melhor hyb_feat_w0.3 0.048 | discr gen 0.360375 (real 0.414, ok=True) | id: gen 0.3225 real 0.381375 ok=True | audit 0.946 | gen 281s | total 14211s
J034b_bessauto: seed 7 frac 0.05: real 0.048 | melhor gen_rfill_w0.3 0.040 | discr gen 0.3248749999999999 (real 0.368, ok=True) | id: gen 0.28774999999999995 real 0.2709999999999999 ok=True | audit 0.957 | gen 281s | total 15257s
J034b_bessauto: seed 7 frac 0.1: real 0.046 | melhor hyb_feat_w0.3 0.036 | discr gen 0.314125 (real 0.315, ok=True) | id: gen 0.25849999999999995 real 0.17975000000000008 ok=False | audit 0.951 | gen 280s | total 16274s
J034b_bessauto: seed 8 frac 0.01: real 0.095 | melhor hyb_feat_w0.3 0.055 | discr gen 0.41974999999999996 (real 0.448, ok=True) | id: gen 0.3879999999999999 real 0.4214800689817594 ok=True | audit 0.962 | gen 280s | total 17354s
J034b_bessauto: seed 8 frac 0.02: real 0.058 | melhor hyb_feat_w0.3 0.048 | discr gen 0.389625 (real 0.439, ok=True) | id: gen 0.358 real 0.39674999999999994 ok=True | audit 0.956 | gen 290s | total 20110s
J034b_bessauto: seed 8 frac 0.05: real 0.054 | melhor hyb_feat_w0.3 0.037 | discr gen 0.3084999999999999 (real 0.363, ok=True) | id: gen 0.2732500000000001 real 0.27025 ok=True | audit 0.946 | gen 286s | total 21158s
J034b_bessauto: seed 8 frac 0.1: real 0.045 | melhor gen_rfill_w0.3 0.036 | discr gen 0.3005000000000001 (real 0.316, ok=True) | id: gen 0.25087499999999996 real 0.19900000000000007 ok=False | audit 0.958 | gen 281s | total 22179s
J034b_bessauto: seed 9 frac 0.01: real 0.089 | melhor hyb_feat_w0.3 0.048 | discr gen 0.41575000000000006 (real 0.463, ok=True) | id: gen 0.38624999999999987 real 0.4389012991059864 ok=True | audit 0.960 | gen 282s | total 23264s
J034b_bessauto: seed 9 frac 0.02: real 0.074 | melhor hyb_feat_w0.3 0.046 | discr gen 0.36912500000000004 (real 0.430, ok=True) | id: gen 0.33299999999999996 real 0.38187499999999996 ok=True | audit 0.947 | gen 293s | total 24364s
J034b_bessauto: seed 9 frac 0.05: real 0.052 | melhor hyb_feat_w0.3 0.037 | discr gen 0.3215 (real 0.350, ok=True) | id: gen 0.2692499999999999 real 0.26637500000000003 ok=True | audit 0.944 | gen 302s | total 25451s
J034b_bessauto: seed 9 frac 0.1: real 0.048 | melhor hyb_feat_w0.3 0.038 | discr gen 0.31325000000000003 (real 0.299, ok=True) | id: gen 0.26425 real 0.18762499999999993 ok=False | audit 0.953 | gen 293s | total 26493s
```

## Falhas

Nenhuma.

Fim: 2026-10-04T21:56:42-03:00 — duração do job 26596 s
