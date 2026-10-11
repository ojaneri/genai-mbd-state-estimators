# J027 — P1 PORTÃO DE UTILIDADE, caso B (bateria); sementes 5–9

Início: 2026-10-03T12:42:10-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J027_auto_bat --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --auto-select --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3` | J027_auto_bat | 0 | 10215 s | `dc9fffcd4313acf059e698aa29e543369e57d8cf7ed40c029b60b0e2cdc0c80b` |

## Linhas "seed … frac …" dos logs

```
J027_auto_bat: seed 5 frac 0.01: real 0.125 | melhor physonly 0.059 | discr gen 0.49187499999999995 (real 0.476, ok=True) | id: gen 0.48762499999999986 real 0.4746376811594203 ok=True | audit 0.991 | gen 296s | total 525s
J027_auto_bat: seed 5 frac 0.02: real 0.082 | melhor hyb_resid_w0.3 0.031 | discr gen 0.48124999999999996 (real 0.476, ok=True) | id: gen 0.4766250000000001 real 0.4667999999999999 ok=True | audit 0.993 | gen 301s | total 1069s
J027_auto_bat: seed 5 frac 0.05: real 0.059 | melhor hyb_resid_w0.3 0.032 | discr gen 0.46824999999999994 (real 0.447, ok=True) | id: gen 0.45587500000000003 real 0.4384437822534182 ok=True | audit 0.978 | gen 290s | total 1584s
J027_auto_bat: seed 5 frac 0.1: real 0.040 | melhor hyb_resid_w0.3 0.018 | discr gen 0.43125 (real 0.403, ok=True) | id: gen 0.4096249999999999 real 0.36975 ok=True | audit 0.967 | gen 283s | total 2090s
J027_auto_bat: seed 6 frac 0.01: real 0.126 | melhor physonly 0.054 | discr gen 0.491375 (real 0.469, ok=True) | id: gen 0.48887499999999995 real 0.4572463768115942 ok=True | audit 0.970 | gen 282s | total 2594s
J027_auto_bat: seed 6 frac 0.02: real 0.083 | melhor physonly 0.040 | discr gen 0.4804999999999999 (real 0.435, ok=True) | id: gen 0.4806250000000001 real 0.452608695652174 ok=True | audit 0.998 | gen 282s | total 3107s
J027_auto_bat: seed 6 frac 0.05: real 0.052 | melhor hyb_resid_w0.3 0.026 | discr gen 0.4493750000000001 (real 0.447, ok=True) | id: gen 0.4328749999999999 real 0.4372597299444003 ok=True | audit 0.974 | gen 283s | total 3616s
J027_auto_bat: seed 6 frac 0.1: real 0.054 | melhor hyb_resid_w0.3 0.020 | discr gen 0.4337500000000001 (real 0.408, ok=True) | id: gen 0.42274999999999996 real 0.38049999999999995 ok=True | audit 0.962 | gen 284s | total 4122s
J027_auto_bat: seed 7 frac 0.01: real 0.239 | melhor physonly 0.063 | discr gen 0.49224999999999997 (real 0.480, ok=True) | id: gen 0.4881249999999999 real 0.47208395909318457 ok=True | audit 0.966 | gen 285s | total 4621s
J027_auto_bat: seed 7 frac 0.02: real 0.116 | melhor physonly 0.034 | discr gen 0.4800000000000001 (real 0.465, ok=True) | id: gen 0.47625000000000006 real 0.4582967084787324 ok=True | audit 0.966 | gen 285s | total 5135s
J027_auto_bat: seed 7 frac 0.05: real 0.061 | melhor hyb_resid_w0.3 0.029 | discr gen 0.46287500000000004 (real 0.456, ok=True) | id: gen 0.458375 real 0.4520500273163124 ok=True | audit 0.977 | gen 285s | total 5647s
J027_auto_bat: seed 7 frac 0.1: real 0.046 | melhor hyb_resid_w0.3 0.018 | discr gen 0.4229999999999998 (real 0.416, ok=True) | id: gen 0.40625 real 0.3838750000000001 ok=True | audit 0.925 | gen 283s | total 6151s
J027_auto_bat: seed 8 frac 0.01: real 0.113 | melhor physonly 0.046 | discr gen 0.4880000000000001 (real 0.478, ok=True) | id: gen 0.492625 real 0.4826086956521738 ok=True | audit 0.966 | gen 284s | total 6656s
J027_auto_bat: seed 8 frac 0.02: real 0.096 | melhor hyb_resid_w0.3 0.061 | discr gen 0.491625 (real 0.483, ok=True) | id: gen 0.484375 real 0.468671657305579 ok=True | audit 0.976 | gen 284s | total 7164s
J027_auto_bat: seed 8 frac 0.05: real 0.058 | melhor hyb_resid_w0.3 0.028 | discr gen 0.46125000000000005 (real 0.447, ok=True) | id: gen 0.45137499999999997 real 0.43531563208828117 ok=True | audit 0.964 | gen 284s | total 7675s
J027_auto_bat: seed 8 frac 0.1: real 0.032 | melhor hyb_resid_w0.3 0.020 | discr gen 0.44562500000000005 (real 0.393, ok=False) | id: gen 0.43537499999999996 real 0.37812500000000004 ok=False | audit 0.971 | gen 284s | total 8182s
J027_auto_bat: seed 9 frac 0.01: real 0.214 | melhor hyb_feat_w0.3 0.169 | discr gen 0.49387500000000006 (real 0.480, ok=True) | id: gen 0.48875000000000013 real 0.47608695652173905 ok=True | audit 0.990 | gen 283s | total 8683s
J027_auto_bat: seed 9 frac 0.02: real 0.080 | melhor physonly 0.032 | discr gen 0.477125 (real 0.468, ok=True) | id: gen 0.47062499999999985 real 0.4616600790513834 ok=True | audit 0.954 | gen 282s | total 9195s
J027_auto_bat: seed 9 frac 0.05: real 0.048 | melhor hyb_resid_w0.3 0.022 | discr gen 0.4508749999999999 (real 0.445, ok=True) | id: gen 0.4413750000000001 real 0.43496462638440325 ok=True | audit 0.968 | gen 282s | total 9706s
J027_auto_bat: seed 9 frac 0.1: real 0.043 | melhor hyb_resid_w0.3 0.021 | discr gen 0.4391250000000001 (real 0.424, ok=True) | id: gen 0.41437500000000005 real 0.38987499999999997 ok=True | audit 0.944 | gen 282s | total 10210s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T15:32:51-03:00 — duração do job 10240 s
