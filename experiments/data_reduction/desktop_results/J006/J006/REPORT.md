# J006 — Rodada 3: triagem de geradores com camada contra artefatos (desquantização + quantização + sample-and-hold), VALIDAÇÃO 15–17

Início: 2026-10-01T03:33:07-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `9fab12e388fca2190c56d4e433dbdef5247c2adc7bc70ce33cbc442a097942eb`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J006_timegan --val --gen timegan --iters 6000 --hidden 24 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_timegan | 0 | 552 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 2 | `python -u run3.py ../data out/J006_timevae --val --gen timevae --latent 16 --iters 3000 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_timevae | 0 | 118 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 3 | `python -u run3.py ../data out/J006_ddpm6k --val --gen ddpm --iters 6000 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_ddpm6k | 0 | 248 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 4 | `python -u run3.py ../data out/J006_ddpm20k --val --gen ddpm --iters 20000 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_ddpm20k | 0 | 387 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 5 | `python -u run3.py ../data out/J006_ddpm20k_raw --val --gen ddpm --iters 20000 --post none --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_ddpm20k_raw | 0 | 391 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 6 | `python -u run3.py ../data out/J006_var --val --gen var --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_var | 0 | 102 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |
| 7 | `python -u run3.py ../data out/J006_bootstrap --val --gen bootstrap --post none --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1` | J006_bootstrap | 0 | 96 s | `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59` |

## Escolha

Regra: `# Escolha: os 2 geradores (exceto bootstrap, que é referência) com menor média de runs[].discr_dq_gen_vs_test; desempate: menor média de v.gen_r1_w1.flow_MAE. Registre a escolha (nome do job J006_* e seus argumentos).`

| saída | gerador | média runs[].discr_dq_gen_vs_test (por semente) | média v.gen_r1_w1.flow_MAE (por semente) |
|---|---|---|---|
| J006_timegan | timegan | 0.4828125000000001 [0.47650000000000003, 0.48912500000000014] | 3.338516925684776 [3.3637245125676527, 3.3133093388018997] |
| J006_timevae | timevae | 0.4990625 [0.49912500000000004, 0.499] | 2.7050562164651675 [2.6247609202970255, 2.785351512633309] |
| J006_ddpm6k | ddpm | 0.37331250000000005 [0.36550000000000016, 0.38112499999999994] | 3.3159631166983194 [3.3329964366971048, 3.298929796699534] |
| J006_ddpm20k | ddpm | 0.3241875 [0.30925000000000014, 0.3391249999999999] | 3.2094444437110585 [3.1609718005456697, 3.2579170868764478] |
| J006_ddpm20k_raw | ddpm | 0.30906249999999996 [0.29212499999999997, 0.32599999999999996] | 2.6765440300029173 [2.652742527268145, 2.7003455327376895] |
| J006_var | var | 0.48556250000000006 [0.4866250000000001, 0.48450000000000004] | 3.5205652460231396 [3.54815132017153, 3.492979171874749] |
| J006_bootstrap | bootstrap (excluído pela regra) | 0.3018125 [0.30462500000000003, 0.29899999999999993] | 2.6157668160918557 [2.5985458973494424, 2.632987734834269] |

Ordem dos elegíveis: ['J006_ddpm20k_raw', 'J006_ddpm20k', 'J006_ddpm6k', 'J006_timegan', 'J006_var', 'J006_timevae'] (empate até 1e-9 → desempate).

**1º escolhido: `J006_ddpm20k_raw`** — argumentos para reuso: `--gen ddpm --iters 20000 --post none`
**2º escolhido: `J006_ddpm20k`** — argumentos para reuso: `--gen ddpm --iters 20000 --dequant --post quanthold`

## Linhas "seed … frac …" dos logs

```
J006_timegan: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.477125 (real 0.133, ok=False) | audit 0.835 | gen 226s | total 277s
J006_timegan: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.4893750000000001 (real 0.158, ok=False) | audit 0.700 | gen 223s | total 547s
J006_timevae: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.499625 (real 0.133, ok=False) | audit 1.000 | gen 15s | total 58s
J006_timevae: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.499 (real 0.158, ok=False) | audit 1.000 | gen 13s | total 114s
J006_ddpm6k: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.36724999999999997 (real 0.133, ok=False) | audit 0.952 | gen 32s | total 123s
J006_ddpm6k: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.37775000000000003 (real 0.158, ok=False) | audit 0.910 | gen 31s | total 243s
J006_ddpm20k: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.30962500000000015 (real 0.133, ok=False) | audit 0.902 | gen 103s | total 193s
J006_ddpm20k: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.34912500000000013 (real 0.158, ok=False) | audit 0.889 | gen 101s | total 383s
J006_ddpm20k_raw: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.486375 (real 0.133, ok=False) | audit 0.966 | gen 100s | total 195s
J006_ddpm20k_raw: seed 1 frac 0.05: real 2.721 | melhor gen_rfill_w1 2.657 | discr gen 0.4850000000000001 (real 0.158, ok=False) | audit 0.943 | gen 98s | total 386s
J006_var: seed 0 frac 0.05: real 2.601 | melhor real 2.601 | discr gen 0.4870000000000001 (real 0.133, ok=False) | audit 0.855 | gen 0s | total 51s
J006_var: seed 1 frac 0.05: real 2.721 | melhor real 2.721 | discr gen 0.48725000000000007 (real 0.158, ok=False) | audit 0.836 | gen 0s | total 98s
J006_bootstrap: seed 0 frac 0.05: real 2.601 | melhor gen_r1_w1 2.599 | discr gen 0.30425 (real 0.133, ok=False) | audit 0.815 | gen 0s | total 47s
J006_bootstrap: seed 1 frac 0.05: real 2.721 | melhor gen_rfill_w1 2.598 | discr gen 0.3087500000000001 (real 0.158, ok=False) | audit 0.781 | gen 0s | total 92s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T04:05:55-03:00 — duração do job 1969 s
