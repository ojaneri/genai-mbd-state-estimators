# J033b — REFAZ J033 (mesma causa)

Início: 2026-10-04T13:46:44-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_bess out/J033b_bessboot --gen bootstrap --post none --domain battery --test-segs 7-8 --pool-segs 1-6 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3` | J033b_bessboot | 0 | 2655 s | `f989a1914e9bf8a8658e1576cfc3f45756d1cb16029fd22fa850db1c088e3310` |

## Linhas "seed … frac …" dos logs

```
J033b_bessboot: seed 0 frac 0.01: real 0.083 | melhor hyb_resid_w0.3 0.066 | discr gen 0.45862499999999995 (real 0.446, ok=True) | id: gen 0.44575 real 0.42974999999999997 ok=True | audit 0.158 | gen 0s | total 208s
J033b_bessboot: seed 0 frac 0.02: real 0.065 | melhor hyb_resid_w0.3 0.059 | discr gen 0.42974999999999997 (real 0.405, ok=True) | id: gen 0.391625 real 0.35024999999999995 ok=True | audit 0.096 | gen 0s | total 330s
J033b_bessboot: seed 0 frac 0.05: real 0.050 | melhor physonly 0.048 | discr gen 0.41225 (real 0.347, ok=False) | id: gen 0.35325000000000006 real 0.23875000000000002 ok=False | audit 0.068 | gen 0s | total 453s
J033b_bessboot: seed 0 frac 0.1: real 0.043 | melhor physonly 0.043 | discr gen 0.38775000000000015 (real 0.286, ok=False) | id: gen 0.34662499999999985 real 0.16425 ok=False | audit 0.060 | gen 0s | total 576s
J033b_bessboot: seed 1 frac 0.01: real 0.082 | melhor physonly 0.069 | discr gen 0.4557500000000001 (real 0.445, ok=True) | id: gen 0.43725 real 0.4225 ok=True | audit 0.171 | gen 0s | total 706s
J033b_bessboot: seed 1 frac 0.02: real 0.051 | melhor hyb_resid_w0.3 0.050 | discr gen 0.4265000000000001 (real 0.407, ok=True) | id: gen 0.4015000000000001 real 0.35050000000000003 ok=False | audit 0.091 | gen 0s | total 828s
J033b_bessboot: seed 1 frac 0.05: real 0.046 | melhor physonly 0.046 | discr gen 0.390875 (real 0.341, ok=True) | id: gen 0.35324999999999984 real 0.253625 ok=False | audit 0.059 | gen 0s | total 948s
J033b_bessboot: seed 1 frac 0.1: real 0.040 | melhor real 0.040 | discr gen 0.3863749999999999 (real 0.292, ok=False) | id: gen 0.334375 real 0.17162499999999992 ok=False | audit 0.054 | gen 0s | total 1073s
J033b_bessboot: seed 2 frac 0.01: real 0.088 | melhor physonly 0.061 | discr gen 0.466375 (real 0.462, ok=True) | id: gen 0.44725000000000004 real 0.4366785079222375 ok=True | audit 0.137 | gen 0s | total 1207s
J033b_bessboot: seed 2 frac 0.02: real 0.068 | melhor physonly 0.056 | discr gen 0.439125 (real 0.421, ok=True) | id: gen 0.399625 real 0.36 ok=True | audit 0.099 | gen 0s | total 1333s
J033b_bessboot: seed 2 frac 0.05: real 0.050 | melhor physonly 0.045 | discr gen 0.39574999999999994 (real 0.337, ok=False) | id: gen 0.36750000000000005 real 0.240375 ok=False | audit 0.076 | gen 0s | total 1456s
J033b_bessboot: seed 2 frac 0.1: real 0.042 | melhor real 0.042 | discr gen 0.39725 (real 0.311, ok=False) | id: gen 0.34862499999999996 real 0.15550000000000008 ok=False | audit 0.061 | gen 0s | total 1581s
J033b_bessboot: seed 3 frac 0.01: real 0.109 | melhor physonly 0.084 | discr gen 0.45875 (real 0.455, ok=True) | id: gen 0.43312499999999987 real 0.4188750000000001 ok=True | audit 0.158 | gen 0s | total 1716s
J033b_bessboot: seed 3 frac 0.02: real 0.059 | melhor hyb_resid_w0.3 0.052 | discr gen 0.43875 (real 0.410, ok=True) | id: gen 0.4032499999999999 real 0.35287500000000005 ok=False | audit 0.113 | gen 0s | total 1845s
J033b_bessboot: seed 3 frac 0.05: real 0.048 | melhor physonly 0.046 | discr gen 0.3918750000000001 (real 0.330, ok=False) | id: gen 0.3391249999999999 real 0.23387500000000006 ok=False | audit 0.070 | gen 0s | total 1972s
J033b_bessboot: seed 3 frac 0.1: real 0.041 | melhor gen_rfill_w0.3 0.041 | discr gen 0.390375 (real 0.288, ok=False) | id: gen 0.343375 real 0.17362499999999992 ok=False | audit 0.058 | gen 0s | total 2100s
J033b_bessboot: seed 4 frac 0.01: real 0.080 | melhor gen_rfill_w0.3 0.062 | discr gen 0.4487500000000001 (real 0.441, ok=True) | id: gen 0.42925 real 0.4229323308270677 ok=True | audit 0.142 | gen 0s | total 2242s
J033b_bessboot: seed 4 frac 0.02: real 0.068 | melhor physonly 0.061 | discr gen 0.43062500000000004 (real 0.404, ok=True) | id: gen 0.40312499999999996 real 0.34625000000000006 ok=False | audit 0.113 | gen 0s | total 2378s
J033b_bessboot: seed 4 frac 0.05: real 0.051 | melhor gen_rfill_w0.3 0.049 | discr gen 0.40087499999999987 (real 0.337, ok=False) | id: gen 0.35762499999999997 real 0.24012499999999992 ok=False | audit 0.071 | gen 0s | total 2504s
J033b_bessboot: seed 4 frac 0.1: real 0.046 | melhor gen_rfill_w0.3 0.045 | discr gen 0.3859999999999999 (real 0.303, ok=False) | id: gen 0.33787500000000004 real 0.17025 ok=False | audit 0.060 | gen 0s | total 2631s
```

## Falhas

Nenhuma.

Fim: 2026-10-04T14:31:55-03:00 — duração do job 2711 s
