# J008 — Rodada 4: variações do DDPM (hold só nas entradas, mais treino, rede maior), VALIDAÇÃO 15–17

Início: 2026-10-01T07:27:25-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `9fab12e388fca2190c56d4e433dbdef5247c2adc7bc70ce33cbc442a097942eb`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J008_q20k --val --gen ddpm --iters 20000 --dequant --post quant --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1` | J008_q20k | 0 (reaproveitado) | — | `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0` |
| 2 | `python -u run3.py ../data out/J008_qhin20k --val --gen ddpm --iters 20000 --dequant --post quantholdin --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1` | J008_qhin20k | 0 | 387 s | `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0` |
| 3 | `python -u run3.py ../data out/J008_qhin50k --val --gen ddpm --iters 50000 --dequant --post quantholdin --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1` | J008_qhin50k | 0 | 680 s | `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0` |
| 4 | `python -u run3.py ../data out/J008_qhin50k_h128 --val --gen ddpm --iters 50000 --hidden 128 --dequant --post quantholdin --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1` | J008_qhin50k_h128 | 0 | 906 s | `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0` |
| 5 | `python -u run3.py ../data out/J008_q50k_h128 --val --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1` | J008_q50k_h128 | 0 | 902 s | `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0` |
| 6 | `python -u run3.py ../data out/J008_raw50k_h128 --val --gen ddpm --iters 50000 --hidden 128 --post none --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1` | J008_raw50k_h128 | 0 | 917 s | `9e73246b29471afa66347b6fa9d0e093464331787a84e89eb45a76c1332d76e0` |

## Escolha

Regra: `# Escolha: os 2 com menor média de runs[].discr_dq_gen_vs_test ENTRE os que têm média de (v.gen_r1_w1.flow_MAE − v.real.flow_MAE) ≤ 0,05; se menos de 2 cumprirem, complete pelos menores discr_dq. Registre a escolha e os argumentos.`

| saída | gerador | média runs[].discr_dq_gen_vs_test (por semente) | média (v.gen_r1_w1.flow_MAE − v.real.flow_MAE) | cumpre ≤ 0,05? |
|---|---|---|---|---|
| J008_q20k | ddpm | 0.30925 [0.29275000000000007, 0.32575] | 0.02499261491602578 | sim |
| J008_qhin20k | ddpm | 0.3311875000000001 [0.3233750000000001, 0.3390000000000001] | 0.5082926460712327 | não |
| J008_qhin50k | ddpm | 0.3085 [0.3112499999999999, 0.3057500000000001] | 0.4998082258592387 | não |
| J008_qhin50k_h128 | ddpm | 0.27462500000000006 [0.2782500000000001, 0.271] | 0.4202921447768986 | não |
| J008_q50k_h128 | ddpm | 0.2508125 [0.25475000000000003, 0.24687499999999996] | -0.05164021530367546 | sim |
| J008_raw50k_h128 | ddpm | 0.2540625 [0.25275000000000003, 0.255375] | -0.09060009738433683 | sim |

Ordem dos que cumprem (empate até 1e-9 → desempate): ['J008_q50k_h128', 'J008_raw50k_h128', 'J008_q20k'].

**1º escolhido: `J008_q50k_h128`** — argumentos para reuso: `--gen ddpm --iters 50000 --hidden 128 --dequant --post quant`
**2º escolhido: `J008_raw50k_h128`** — argumentos para reuso: `--gen ddpm --iters 50000 --hidden 128 --post none`

## Linhas "seed … frac …" dos logs

```
J008_q20k: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.294875 (real 0.133, ok=False) | audit 0.967 | gen 103s | total 197s
J008_q20k: seed 1 frac 0.05: real 2.721 | melhor gen_rfill_w1 2.690 | discr gen 0.328375 (real 0.158, ok=False) | audit 0.944 | gen 98s | total 388s
J008_qhin20k: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.3258749999999999 (real 0.133, ok=False) | audit 0.903 | gen 99s | total 193s
J008_qhin20k: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.34087499999999993 (real 0.158, ok=False) | audit 0.888 | gen 98s | total 383s
J008_qhin50k: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.31437500000000007 (real 0.133, ok=False) | audit 0.905 | gen 246s | total 340s
J008_qhin50k: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.3065 (real 0.158, ok=False) | audit 0.918 | gen 244s | total 675s
J008_qhin50k_h128: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.280875 (real 0.133, ok=False) | audit 0.897 | gen 309s | total 453s
J008_qhin50k_h128: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.26875000000000004 (real 0.158, ok=False) | audit 0.910 | gen 306s | total 901s
J008_q50k_h128: seed 0 frac 0.05: real 2.601 | melhor gen_r1_w1 2.593 | discr gen 0.252 (real 0.133, ok=False) | audit 0.972 | gen 308s | total 453s
J008_q50k_h128: seed 1 frac 0.05: real 2.721 | melhor gen_rfill_w1 2.526 | discr gen 0.25012499999999993 (real 0.158, ok=False) | audit 0.964 | gen 306s | total 898s
J008_raw50k_h128: seed 0 frac 0.05: real 2.601 | melhor gen_rfill_w1 2.522 | discr gen 0.48849999999999993 (real 0.133, ok=False) | audit 0.974 | gen 306s | total 461s
J008_raw50k_h128: seed 1 frac 0.05: real 2.721 | melhor gen_rfill_w1 2.495 | discr gen 0.476125 (real 0.158, ok=False) | audit 0.964 | gen 308s | total 912s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T08:36:28-03:00 — duração do job 4144 s
