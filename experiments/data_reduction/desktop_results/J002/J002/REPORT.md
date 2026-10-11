# J002 — TimeVAE, ajuste na VALIDAÇÃO (latent x iters), semente 0, fração 0.05

Início: 2026-10-01T00:21:17-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`

## Comandos

| # | comando executado | saída | rc | tempo |
|---|---|---|---|---|
| 1 | `python -u run2.py ../data out/J002_l8_i2000 --val --gen timevae --latent 8 --iters 2000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J002_l8_i2000 | 0 (reaproveitado) | — |
| 2 | `python -u run2.py ../data out/J002_l8_i5000 --val --gen timevae --latent 8 --iters 5000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J002_l8_i5000 | 0 (reaproveitado) | — |
| 3 | `python -u run2.py ../data out/J002_l16_i2000 --val --gen timevae --latent 16 --iters 2000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J002_l16_i2000 | 0 (reaproveitado) | — |
| 4 | `python -u run2.py ../data out/J002_l16_i5000 --val --gen timevae --latent 16 --iters 5000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J002_l16_i5000 | 0 (reaproveitado) | — |

## Escolha

Regra: `# Escolha: menor runs[0].discr_gen_vs_test (aqui é a validação 15–17); desempate: menor v.gen_r1_w1.flow_MAE. Registre a escolha (L, I).`

| saída | runs[0].discr_gen_vs_test | v.gen_r1_w1.flow_MAE |
|---|---|---|
| J002_l16_i5000 | 0.49875 | 2.8138641026232296 |
| J002_l16_i2000 | 0.49924999999999997 | 2.702115098554394 |
| J002_l8_i2000 | 0.4992500000000002 | 2.704979219069413 |
| J002_l8_i5000 | 0.49924999999999997 | 2.7518574567319285 |

**Escolhida: `J002_l16_i5000` → {'L': 16, 'I': 5000}** (usada nos jobs seguintes)

## Linhas "seed … frac …" dos logs

```
J002_l8_i2000: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.4992500000000002 | audit 1.000 | gen 10s | total 40s
J002_l8_i5000: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.49924999999999997 | audit 1.000 | gen 21s | total 52s
J002_l16_i2000: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.49924999999999997 | audit 1.000 | gen 10s | total 40s
J002_l16_i5000: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.49875 | audit 1.000 | gen 21s | total 53s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T00:21:27-03:00 — duração do job 10 s
