# J022 — Caso B, cenário ausente: sem frio (<5 °C) no treino real e no gerador; medida = erro só nos trechos frios do teste (flow_MAE_hw)

Início: 2026-10-02T10:03:06-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_lghg2 out/J022_cold --domain battery --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --hw-absent --seeds 0,1,2,3,4 --fracs 0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly` | J022_cold | 0 | 5448 s | `b09e8fc2b8b791e839a54cc9a64590c976f60a129bd7215f2c999f4ab265a5d1` |

## Linhas "seed … frac …" dos logs

```
J022_cold: seed 0 frac 0.05: real 0.083 | melhor physonly 0.051 | discr gen 0.4903749999999999 (real 0.475, ok=True) | id: gen 0.48275 real 0.44396551724137934 ok=True | audit 0.979 | gen 341s | total 607s
J022_cold: seed 0 frac 0.1: real 0.074 | melhor physonly 0.071 | discr gen 0.4886250000000001 (real 0.441, ok=True) | id: gen 0.48124999999999996 real 0.40312499999999996 ok=False | audit 0.959 | gen 339s | total 1210s
J022_cold: seed 1 frac 0.05: real 0.089 | melhor physonly 0.045 | discr gen 0.4886250000000001 (real 0.470, ok=True) | id: gen 0.47675 real 0.4502163781624502 ok=True | audit 0.962 | gen 337s | total 1813s
J022_cold: seed 1 frac 0.1: real 0.082 | melhor physonly 0.060 | discr gen 0.4908750000000002 (real 0.463, ok=True) | id: gen 0.48324999999999996 real 0.42266085558174815 ok=False | audit 0.957 | gen 326s | total 2372s
J022_cold: seed 2 frac 0.05: real 0.087 | melhor physonly 0.057 | discr gen 0.48750000000000004 (real 0.469, ok=True) | id: gen 0.48424999999999996 real 0.44993900533927156 ok=True | audit 0.983 | gen 282s | total 2884s
J022_cold: seed 2 frac 0.1: real 0.101 | melhor physonly 0.056 | discr gen 0.490625 (real 0.470, ok=True) | id: gen 0.4869999999999999 real 0.4337500000000001 ok=False | audit 0.971 | gen 283s | total 3389s
J022_cold: seed 3 frac 0.05: real 0.079 | melhor physonly 0.050 | discr gen 0.4950000000000001 (real 0.456, ok=True) | id: gen 0.4903749999999999 real 0.4419491525423729 ok=True | audit 0.983 | gen 290s | total 3901s
J022_cold: seed 3 frac 0.1: real 0.084 | melhor physonly 0.061 | discr gen 0.4891249999999999 (real 0.466, ok=True) | id: gen 0.47987500000000005 real 0.4336249999999999 ok=True | audit 0.976 | gen 289s | total 4419s
J022_cold: seed 4 frac 0.05: real 0.092 | melhor physonly 0.056 | discr gen 0.491625 (real 0.475, ok=True) | id: gen 0.48625000000000007 real 0.4451865483149311 ok=True | audit 0.966 | gen 291s | total 4929s
J022_cold: seed 4 frac 0.1: real 0.082 | melhor physonly 0.055 | discr gen 0.48524999999999996 (real 0.465, ok=True) | id: gen 0.48249999999999993 real 0.43132110924165623 ok=False | audit 0.959 | gen 286s | total 5442s
```

## Falhas

Nenhuma.

Fim: 2026-10-02T11:34:19-03:00 — duração do job 5473 s
