# J020 — CASO B (bateria) — replicação do pipeline em OUTRO DOMÍNIO: sensor virtual de SOC numa célula LG 18650HG2

Início: 2026-10-02T06:23:20-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J020 --domain battery --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly` | J020 | 0 (reaproveitado) | — | `d322907e17bebeb51efff8e4f8136bcaaf472069f039063d72c93395aba45232` |

## Linhas "seed … frac …" dos logs

```
J020: seed 0 frac 0.01: real 0.121 | melhor physonly 0.044 | discr gen None (real 0.476, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 299s | total 463s
J020: seed 0 frac 0.02: real 0.114 | melhor physonly 0.040 | discr gen None (real 0.487, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 299s | total 922s
J020: seed 0 frac 0.05: real 0.063 | melhor physonly 0.027 | discr gen 0.49534883720930234 (real 0.452, ok=True) | id: gen 0.49534883720930234 real 0.4388119056565234 ok=False | audit 0.001 | gen 303s | total 1417s
J020: seed 0 frac 0.1: real 0.046 | melhor physonly 0.025 | discr gen None (real 0.391, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 303s | total 1883s
J020: seed 1 frac 0.01: real 0.103 | melhor physonly 0.046 | discr gen None (real 0.465, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 300s | total 2343s
J020: seed 1 frac 0.02: real 0.088 | melhor physonly 0.058 | discr gen None (real 0.479, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 298s | total 2804s
J020: seed 1 frac 0.05: real 0.047 | melhor physonly 0.022 | discr gen None (real 0.433, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 300s | total 3264s
J020: seed 1 frac 0.1: real 0.037 | melhor physonly 0.020 | discr gen None (real 0.373, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 304s | total 3720s
J020: seed 2 frac 0.01: real 0.110 | melhor physonly 0.040 | discr gen None (real 0.469, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 301s | total 4189s
J020: seed 2 frac 0.02: real 0.078 | melhor physonly 0.038 | discr gen None (real 0.474, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 298s | total 4652s
J020: seed 2 frac 0.05: real 0.058 | melhor physonly 0.031 | discr gen None (real 0.452, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 299s | total 5121s
J020: seed 2 frac 0.1: real 0.032 | melhor physonly 0.018 | discr gen None (real 0.401, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 303s | total 5587s
J020: seed 3 frac 0.01: real 0.124 | melhor physonly 0.076 | discr gen None (real 0.467, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 302s | total 6056s
J020: seed 3 frac 0.02: real 0.088 | melhor physonly 0.035 | discr gen 0.4974025974025974 (real 0.466, ok=True) | id: gen 0.49483849483849485 real 0.4597121490889666 ok=True | audit 0.002 | gen 299s | total 6552s
J020: seed 3 frac 0.05: real 0.058 | melhor physonly 0.027 | discr gen 0.4916666666666668 (real 0.441, ok=False) | id: gen 0.4930555555555556 real 0.4411311053984577 ok=False | audit 0.003 | gen 298s | total 7055s
J020: seed 3 frac 0.1: real 0.033 | melhor physonly 0.020 | discr gen None (real 0.379, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 298s | total 7516s
J020: seed 4 frac 0.01: real 0.121 | melhor physonly 0.098 | discr gen None (real 0.466, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 302s | total 7978s
J020: seed 4 frac 0.02: real 0.104 | melhor physonly 0.062 | discr gen None (real 0.476, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 303s | total 8452s
J020: seed 4 frac 0.05: real 0.054 | melhor physonly 0.032 | discr gen None (real 0.458, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 298s | total 8920s
J020: seed 4 frac 0.1: real 0.038 | melhor physonly 0.021 | discr gen None (real 0.385, ok=False) | id: gen None real None ok=None | audit 0.000 | gen 299s | total 9383s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T06:29:43-03:00 — duração do job 383 s
