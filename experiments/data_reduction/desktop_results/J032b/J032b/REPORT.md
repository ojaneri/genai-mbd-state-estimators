# J032b — REFAZ J032 (falhou rc=1: coluna timestamp do BESS com dois formatos ISO; pandas 3 não convertia — alerta do desktop

Início: 2026-10-04T06:38:24-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_bess out/J032b_bess --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --test-segs 7-8 --pool-segs 1-6 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3` | J032b_bess | 0 | 25557 s | `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310` |

## Linhas "seed … frac …" dos logs

```
J032b_bess: seed 0 frac 0.01: real 0.083 | melhor hyb_feat_w0.3 0.049 | discr gen 0.3959999999999999 (real 0.446, ok=True) | id: gen 0.37812500000000004 real 0.42974999999999997 ok=True | audit 0.951 | gen 301s | total 1185s
J032b_bess: seed 0 frac 0.02: real 0.065 | melhor hyb_feat_real 0.050 | discr gen 0.359 (real 0.405, ok=True) | id: gen 0.335375 real 0.35024999999999995 ok=True | audit 0.951 | gen 299s | total 2329s
J032b_bess: seed 0 frac 0.05: real 0.050 | melhor hyb_feat_w0.3 0.037 | discr gen 0.29112499999999997 (real 0.347, ok=True) | id: gen 0.24987500000000007 real 0.23875000000000002 ok=True | audit 0.960 | gen 299s | total 3453s
J032b_bess: seed 0 frac 0.1: real 0.043 | melhor hyb_feat_w0.3 0.035 | discr gen 0.2875 (real 0.286, ok=True) | id: gen 0.24787499999999996 real 0.16425 ok=False | audit 0.971 | gen 299s | total 4540s
J032b_bess: seed 1 frac 0.01: real 0.082 | melhor hyb_feat_w0.3 0.046 | discr gen 0.406875 (real 0.445, ok=True) | id: gen 0.3699999999999999 real 0.4225 ok=True | audit 0.960 | gen 299s | total 5698s
J032b_bess: seed 1 frac 0.02: real 0.051 | melhor hyb_feat_real 0.045 | discr gen 0.343375 (real 0.407, ok=True) | id: gen 0.31100000000000017 real 0.35050000000000003 ok=True | audit 0.955 | gen 300s | total 6835s
J032b_bess: seed 1 frac 0.05: real 0.046 | melhor hyb_feat_w0.3 0.037 | discr gen 0.3061250000000001 (real 0.341, ok=True) | id: gen 0.27725 real 0.253625 ok=True | audit 0.951 | gen 297s | total 7945s
J032b_bess: seed 1 frac 0.1: real 0.040 | melhor hyb_feat_w0.3 0.034 | discr gen 0.28074999999999994 (real 0.292, ok=True) | id: gen 0.23912500000000003 real 0.17162499999999992 ok=False | audit 0.955 | gen 298s | total 9022s
J032b_bess: seed 2 frac 0.01: real 0.088 | melhor hyb_feat_real 0.056 | discr gen 0.41662500000000013 (real 0.462, ok=True) | id: gen 0.3869999999999999 real 0.4366785079222375 ok=True | audit 0.966 | gen 297s | total 10167s
J032b_bess: seed 2 frac 0.02: real 0.068 | melhor hyb_feat_w0.3 0.040 | discr gen 0.35787499999999994 (real 0.421, ok=True) | id: gen 0.32162500000000005 real 0.36 ok=True | audit 0.945 | gen 297s | total 11301s
J032b_bess: seed 2 frac 0.05: real 0.050 | melhor hyb_feat_w0.3 0.037 | discr gen 0.334375 (real 0.337, ok=True) | id: gen 0.28937500000000005 real 0.240375 ok=True | audit 0.939 | gen 297s | total 12412s
J032b_bess: seed 2 frac 0.1: real 0.042 | melhor hyb_feat_w0.3 0.035 | discr gen 0.29737499999999994 (real 0.311, ok=True) | id: gen 0.244375 real 0.15550000000000008 ok=False | audit 0.962 | gen 297s | total 13486s
J032b_bess: seed 3 frac 0.01: real 0.109 | melhor hyb_feat_w0.3 0.056 | discr gen 0.3945000000000001 (real 0.455, ok=True) | id: gen 0.37450000000000006 real 0.4188750000000001 ok=True | audit 0.961 | gen 284s | total 14576s
J032b_bess: seed 3 frac 0.02: real 0.059 | melhor hyb_feat_w0.3 0.041 | discr gen 0.350375 (real 0.410, ok=True) | id: gen 0.31037499999999996 real 0.35287500000000005 ok=True | audit 0.957 | gen 284s | total 15658s
J032b_bess: seed 3 frac 0.05: real 0.048 | melhor hyb_feat_w0.3 0.034 | discr gen 0.29100000000000004 (real 0.330, ok=True) | id: gen 0.25 real 0.23387500000000006 ok=True | audit 0.961 | gen 287s | total 16719s
J032b_bess: seed 3 frac 0.1: real 0.041 | melhor hyb_feat_w0.3 0.033 | discr gen 0.2891250000000001 (real 0.288, ok=True) | id: gen 0.26237500000000014 real 0.17362499999999992 ok=False | audit 0.951 | gen 286s | total 17774s
J032b_bess: seed 4 frac 0.01: real 0.080 | melhor hyb_feat_w0.3 0.045 | discr gen 0.38125 (real 0.441, ok=True) | id: gen 0.359375 real 0.4229323308270677 ok=True | audit 0.957 | gen 301s | total 18927s
J032b_bess: seed 4 frac 0.02: real 0.068 | melhor hyb_feat_w0.3 0.044 | discr gen 0.359125 (real 0.404, ok=True) | id: gen 0.3185 real 0.34625000000000006 ok=True | audit 0.966 | gen 299s | total 20061s
J032b_bess: seed 4 frac 0.05: real 0.051 | melhor hyb_feat_w0.3 0.038 | discr gen 0.3165000000000001 (real 0.337, ok=True) | id: gen 0.278 real 0.24012499999999992 ok=True | audit 0.961 | gen 291s | total 23526s
J032b_bess: seed 4 frac 0.1: real 0.046 | melhor hyb_feat_w0.3 0.036 | discr gen 0.29975000000000007 (real 0.303, ok=True) | id: gen 0.2542500000000001 real 0.17025 ok=False | audit 0.966 | gen 610s | total 25514s
```

## Falhas

Nenhuma.

Fim: 2026-10-04T13:44:45-03:00 — duração do job 25581 s
