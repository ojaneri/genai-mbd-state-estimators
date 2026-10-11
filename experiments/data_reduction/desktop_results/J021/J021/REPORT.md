# J021 — Caso B, controle: bootstrap de dados reais como gerador (mesma pergunta do J014, outro domínio)

Início: 2026-10-02T09:29:12-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J021_boot --domain battery --gen bootstrap --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly` | J021_boot | 0 | 1977 s | `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1` |

## Linhas "seed … frac …" dos logs

```
J021_boot: seed 0 frac 0.01: real 0.121 | melhor physonly 0.044 | discr gen 0.4956250000000001 (real 0.476, ok=True) | id: gen 0.492625 real 0.4735632183908045 ok=True | audit 0.696 | gen 0s | total 105s
J021_boot: seed 0 frac 0.02: real 0.114 | melhor physonly 0.040 | discr gen 0.49424999999999986 (real 0.487, ok=True) | id: gen 0.493375 real 0.4828897338403042 ok=True | audit 0.598 | gen 0s | total 201s
J021_boot: seed 0 frac 0.05: real 0.063 | melhor physonly 0.027 | discr gen 0.46562499999999996 (real 0.452, ok=True) | id: gen 0.4564999999999999 real 0.4388119056565234 ok=True | audit 0.292 | gen 0s | total 301s
J021_boot: seed 0 frac 0.1: real 0.046 | melhor physonly 0.025 | discr gen 0.4417500000000001 (real 0.391, ok=False) | id: gen 0.42400000000000004 real 0.380625 ok=True | audit 0.223 | gen 0s | total 397s
J021_boot: seed 1 frac 0.01: real 0.103 | melhor physonly 0.046 | discr gen 0.48975000000000013 (real 0.465, ok=True) | id: gen 0.49087499999999995 real 0.46609195402298853 ok=True | audit 0.638 | gen 0s | total 491s
J021_boot: seed 1 frac 0.02: real 0.088 | melhor physonly 0.058 | discr gen 0.49024999999999996 (real 0.479, ok=True) | id: gen 0.48449999999999993 real 0.4631041899681666 ok=True | audit 0.517 | gen 0s | total 582s
J021_boot: seed 1 frac 0.05: real 0.047 | melhor physonly 0.022 | discr gen 0.451125 (real 0.433, ok=True) | id: gen 0.44999999999999996 real 0.4273663957874485 ok=True | audit 0.277 | gen 0s | total 687s
J021_boot: seed 1 frac 0.1: real 0.037 | melhor physonly 0.020 | discr gen 0.429125 (real 0.373, ok=False) | id: gen 0.40775000000000006 real 0.35425000000000006 ok=False | audit 0.211 | gen 0s | total 783s
J021_boot: seed 2 frac 0.01: real 0.110 | melhor physonly 0.040 | discr gen 0.491375 (real 0.469, ok=True) | id: gen 0.49350000000000005 real 0.48160919540229885 ok=True | audit 0.646 | gen 0s | total 876s
J021_boot: seed 2 frac 0.02: real 0.078 | melhor physonly 0.038 | discr gen 0.4882500000000001 (real 0.474, ok=True) | id: gen 0.48187499999999994 real 0.4549959204167451 ok=True | audit 0.475 | gen 0s | total 971s
J021_boot: seed 2 frac 0.05: real 0.058 | melhor physonly 0.031 | discr gen 0.46287500000000004 (real 0.452, ok=True) | id: gen 0.4501250000000001 real 0.43362357080035174 ok=True | audit 0.333 | gen 0s | total 1070s
J021_boot: seed 2 frac 0.1: real 0.032 | melhor physonly 0.018 | discr gen 0.4397500000000001 (real 0.401, ok=True) | id: gen 0.407875 real 0.35350000000000004 ok=False | audit 0.213 | gen 0s | total 1165s
J021_boot: seed 3 frac 0.01: real 0.124 | melhor physonly 0.076 | discr gen 0.48887499999999995 (real 0.467, ok=True) | id: gen 0.49175 real 0.4768440016956337 ok=True | audit 0.588 | gen 0s | total 1262s
J021_boot: seed 3 frac 0.02: real 0.088 | melhor physonly 0.035 | discr gen 0.48524999999999996 (real 0.466, ok=True) | id: gen 0.476125 real 0.4597121490889666 ok=True | audit 0.457 | gen 0s | total 1364s
J021_boot: seed 3 frac 0.05: real 0.058 | melhor physonly 0.027 | discr gen 0.46087500000000003 (real 0.441, ok=True) | id: gen 0.45487500000000003 real 0.4411311053984577 ok=True | audit 0.298 | gen 0s | total 1463s
J021_boot: seed 3 frac 0.1: real 0.033 | melhor physonly 0.020 | discr gen 0.43025 (real 0.379, ok=False) | id: gen 0.41999999999999993 real 0.36150000000000004 ok=False | audit 0.214 | gen 0s | total 1558s
J021_boot: seed 4 frac 0.01: real 0.121 | melhor physonly 0.098 | discr gen 0.492 (real 0.466, ok=True) | id: gen 0.49512500000000004 real 0.47690569566007857 ok=True | audit 0.524 | gen 0s | total 1646s
J021_boot: seed 4 frac 0.02: real 0.104 | melhor physonly 0.062 | discr gen 0.49 (real 0.476, ok=True) | id: gen 0.48124999999999996 real 0.4576802507836991 ok=True | audit 0.399 | gen 0s | total 1746s
J021_boot: seed 4 frac 0.05: real 0.054 | melhor physonly 0.032 | discr gen 0.475375 (real 0.458, ok=True) | id: gen 0.453125 real 0.430968130659917 ok=True | audit 0.292 | gen 0s | total 1862s
J021_boot: seed 4 frac 0.1: real 0.038 | melhor physonly 0.021 | discr gen 0.4365 (real 0.385, ok=False) | id: gen 0.41212499999999996 real 0.35024999999999995 ok=False | audit 0.194 | gen 0s | total 1972s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T10:02:33-03:00 — duração do job 2001 s
