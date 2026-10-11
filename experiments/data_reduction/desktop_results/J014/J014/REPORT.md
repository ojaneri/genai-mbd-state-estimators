# J014 — Controle: bootstrap de dados reais COMO GERADOR no teste (o ganho vem do modelo generativo ou de "mais janelas parecidas"?) — proposto pelo desktop

Início: 2026-10-02T11:34:53-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J014_boot --gen bootstrap --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1` | J014_boot | 0 | 3578 s | `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1` |

## Linhas "seed … frac …" dos logs

```
J014_boot: seed 0 frac 0.01: real 2.983 | melhor gen_r1_w0.3 2.891 | discr gen 0.4487500000000001 (real 0.177, ok=False) | id: gen 0.438875 real 0.1202453987730061 ok=False | audit 0.786 | gen 0s | total 187s
J014_boot: seed 0 frac 0.02: real 2.909 | melhor genphys_rfill_w1 2.725 | discr gen 0.40449999999999997 (real 0.147, ok=False) | id: gen 0.3936250000000001 real 0.09070943451941538 ok=False | audit 0.788 | gen 0s | total 376s
J014_boot: seed 0 frac 0.05: real 2.427 | melhor genphys_rfill_w0.3 2.379 | discr gen 0.353 (real 0.226, ok=False) | id: gen 0.28700000000000003 real 0.13937500000000003 ok=False | audit 0.828 | gen 0s | total 545s
J014_boot: seed 0 frac 0.1: real 2.329 | melhor genphys_rfill_w0.3 2.278 | discr gen 0.267625 (real 0.130, ok=False) | id: gen 0.21999999999999997 real 0.051875000000000115 ok=False | audit 0.772 | gen 0s | total 706s
J014_boot: seed 1 frac 0.01: real 3.151 | melhor gen_rfill_w0.3 2.983 | discr gen 0.44900000000000007 (real 0.182, ok=False) | id: gen 0.44000000000000006 real 0.1528475327752934 ok=False | audit 0.816 | gen 0s | total 885s
J014_boot: seed 1 frac 0.02: real 2.695 | melhor genphys_rfill_w1 2.540 | discr gen 0.368 (real 0.114, ok=False) | id: gen 0.369375 real 0.0906507692307692 ok=False | audit 0.769 | gen 0s | total 1081s
J014_boot: seed 1 frac 0.05: real 2.551 | melhor genphys_rfill_w0.3 2.447 | discr gen 0.3278749999999999 (real 0.169, ok=False) | id: gen 0.28800000000000003 real 0.08446194225721781 ok=False | audit 0.783 | gen 0s | total 1261s
J014_boot: seed 1 frac 0.1: real 2.362 | melhor genphys_rfill_w1 2.314 | discr gen 0.2666250000000001 (real 0.144, ok=False) | id: gen 0.228375 real 0.050000000000000044 ok=False | audit 0.791 | gen 0s | total 1426s
J014_boot: seed 2 frac 0.01: real 3.063 | melhor genphys_rfill_w0.3 2.887 | discr gen 0.45162500000000017 (real 0.142, ok=False) | id: gen 0.43875 real 0.10604026845637582 ok=False | audit 0.775 | gen 0s | total 1612s
J014_boot: seed 2 frac 0.02: real 2.834 | melhor genphys_rfill_w1 2.710 | discr gen 0.4012499999999999 (real 0.145, ok=False) | id: gen 0.38737500000000014 real 0.061003093414764065 ok=False | audit 0.813 | gen 0s | total 1793s
J014_boot: seed 2 frac 0.05: real 2.513 | melhor genphys_rfill_w0.3 2.422 | discr gen 0.302125 (real 0.164, ok=False) | id: gen 0.272 real 0.08074999999999999 ok=False | audit 0.797 | gen 0s | total 1965s
J014_boot: seed 2 frac 0.1: real 2.322 | melhor genphys_rfill_w1 2.281 | discr gen 0.26812500000000006 (real 0.158, ok=False) | id: gen 0.21350000000000002 real 0.055499999999999994 ok=False | audit 0.811 | gen 0s | total 2132s
J014_boot: seed 3 frac 0.01: real 3.017 | melhor gen_dfilt_q0.2 2.920 | discr gen 0.47287499999999993 (real 0.193, ok=False) | id: gen 0.4610000000000001 real 0.13445712182554304 ok=False | audit 0.782 | gen 0s | total 2312s
J014_boot: seed 3 frac 0.02: real 2.977 | melhor genphys_rfill_w0.3 2.862 | discr gen 0.44462499999999994 (real 0.191, ok=False) | id: gen 0.42862500000000003 real 0.11971987144400942 ok=False | audit 0.752 | gen 0s | total 2491s
J014_boot: seed 3 frac 0.05: real 2.461 | melhor genphys_rfill_w0.3 2.378 | discr gen 0.320875 (real 0.190, ok=False) | id: gen 0.2663749999999999 real 0.09550000000000003 ok=False | audit 0.824 | gen 0s | total 2664s
J014_boot: seed 3 frac 0.1: real 2.320 | melhor genphys_rfill_w0.3 2.270 | discr gen 0.25275000000000003 (real 0.118, ok=False) | id: gen 0.21875 real 0.049000000000000044 ok=False | audit 0.799 | gen 0s | total 2836s
J014_boot: seed 4 frac 0.01: real 3.109 | melhor genphys_rfill_w0.3 2.880 | discr gen 0.45525000000000004 (real 0.124, ok=False) | id: gen 0.44437499999999996 real 0.07631485541288241 ok=False | audit 0.830 | gen 0s | total 3017s
J014_boot: seed 4 frac 0.02: real 2.856 | melhor gen_rfill_w1 2.799 | discr gen 0.40849999999999986 (real 0.144, ok=False) | id: gen 0.3943749999999999 real 0.1001595811179502 ok=False | audit 0.788 | gen 0s | total 3201s
J014_boot: seed 4 frac 0.05: real 2.463 | melhor genphys_rfill_w0.3 2.370 | discr gen 0.30837500000000007 (real 0.136, ok=False) | id: gen 0.27675000000000005 real 0.05431329449596434 ok=False | audit 0.776 | gen 0s | total 3390s
J014_boot: seed 4 frac 0.1: real 2.304 | melhor genphys_rfill_w0.3 2.274 | discr gen 0.27500000000000013 (real 0.161, ok=False) | id: gen 0.2201249999999999 real 0.05712499999999998 ok=False | audit 0.767 | gen 0s | total 3561s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T12:34:56-03:00 — duração do job 3603 s
