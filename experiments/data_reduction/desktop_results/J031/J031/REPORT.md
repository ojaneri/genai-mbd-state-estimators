# J031 — P4 DDPM MAIOR (h256, 100k iterações), caso A (Opel): última tentativa de fidelidade

Início: 2026-10-03T22:18:27-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `94503586e335c5282fa5968997e6286ef70dc434beb978424b3db93d824f2d72`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J031_ddpm_big --gen ddpm --iters 100000 --hidden 256 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05 --variants real,gen_rfill_w0.3,genphys_rfill_w0.3` | J031_ddpm_big | 0 | 25809 s | `94503586e335c5282fa5968997e6286ef70dc434beb978424b3db93d824f2d72` |

## Linhas "seed … frac …" dos logs

```
J031_ddpm_big: seed 0 frac 0.01: real 2.983 | melhor gen_rfill_w0.3 2.781 | discr gen 0.4036249999999999 (real 0.177, ok=False) | id: gen 0.40012499999999984 real 0.1202453987730061 ok=False | audit 0.980 | gen 1271s | total 1723s
J031_ddpm_big: seed 0 frac 0.02: real 2.909 | melhor genphys_rfill_w0.3 2.664 | discr gen 0.365625 (real 0.147, ok=False) | id: gen 0.35250000000000004 real 0.09070943451941538 ok=False | audit 0.972 | gen 1277s | total 3446s
J031_ddpm_big: seed 0 frac 0.05: real 2.427 | melhor gen_rfill_w0.3 2.317 | discr gen 0.3084999999999999 (real 0.226, ok=False) | id: gen 0.25275000000000003 real 0.13937500000000003 ok=False | audit 0.986 | gen 1277s | total 5148s
J031_ddpm_big: seed 1 frac 0.01: real 3.151 | melhor gen_rfill_w0.3 2.879 | discr gen 0.42900000000000005 (real 0.182, ok=False) | id: gen 0.41337499999999994 real 0.1528475327752934 ok=False | audit 0.976 | gen 1276s | total 6870s
J031_ddpm_big: seed 1 frac 0.02: real 2.695 | melhor gen_rfill_w0.3 2.478 | discr gen 0.34162499999999996 (real 0.114, ok=False) | id: gen 0.35125000000000006 real 0.0906507692307692 ok=False | audit 0.979 | gen 1288s | total 8606s
J031_ddpm_big: seed 1 frac 0.05: real 2.551 | melhor gen_rfill_w0.3 2.396 | discr gen 0.30437499999999995 (real 0.169, ok=False) | id: gen 0.26374999999999993 real 0.08446194225721781 ok=False | audit 0.985 | gen 1283s | total 10327s
J031_ddpm_big: seed 2 frac 0.01: real 3.063 | melhor gen_rfill_w0.3 2.706 | discr gen 0.40337499999999993 (real 0.142, ok=False) | id: gen 0.3953749999999999 real 0.10604026845637582 ok=False | audit 0.953 | gen 1278s | total 12054s
J031_ddpm_big: seed 2 frac 0.02: real 2.834 | melhor genphys_rfill_w0.3 2.611 | discr gen 0.36125000000000007 (real 0.145, ok=False) | id: gen 0.34862499999999996 real 0.061003093414764065 ok=False | audit 0.971 | gen 1283s | total 13783s
J031_ddpm_big: seed 2 frac 0.05: real 2.513 | melhor gen_rfill_w0.3 2.359 | discr gen 0.2775000000000001 (real 0.164, ok=False) | id: gen 0.271625 real 0.08074999999999999 ok=False | audit 0.987 | gen 1276s | total 15492s
J031_ddpm_big: seed 3 frac 0.01: real 3.017 | melhor gen_rfill_w0.3 2.769 | discr gen 0.42462500000000003 (real 0.193, ok=False) | id: gen 0.4188749999999999 real 0.13445712182554304 ok=False | audit 0.947 | gen 1273s | total 17211s
J031_ddpm_big: seed 3 frac 0.02: real 2.977 | melhor gen_rfill_w0.3 2.663 | discr gen 0.398875 (real 0.191, ok=False) | id: gen 0.37487500000000007 real 0.11971987144400942 ok=False | audit 0.933 | gen 1276s | total 18934s
J031_ddpm_big: seed 3 frac 0.05: real 2.461 | melhor gen_rfill_w0.3 2.338 | discr gen 0.3026249999999999 (real 0.190, ok=False) | id: gen 0.25350000000000006 real 0.09550000000000003 ok=False | audit 0.996 | gen 1274s | total 20641s
J031_ddpm_big: seed 4 frac 0.01: real 3.109 | melhor gen_rfill_w0.3 2.709 | discr gen 0.41912499999999997 (real 0.124, ok=False) | id: gen 0.4129999999999999 real 0.07631485541288241 ok=False | audit 0.971 | gen 1274s | total 22368s
J031_ddpm_big: seed 4 frac 0.02: real 2.856 | melhor gen_rfill_w0.3 2.667 | discr gen 0.3631249999999999 (real 0.144, ok=False) | id: gen 0.3657499999999999 real 0.1001595811179502 ok=False | audit 0.972 | gen 1280s | total 24092s
J031_ddpm_big: seed 4 frac 0.05: real 2.463 | melhor gen_rfill_w0.3 2.295 | discr gen 0.26025 (real 0.136, ok=False) | id: gen 0.24162499999999998 real 0.05431329449596434 ok=False | audit 0.985 | gen 1267s | total 25795s
```

## Falhas

Nenhuma.

Fim: 2026-10-04T05:29:29-03:00 — duração do job 25862 s
