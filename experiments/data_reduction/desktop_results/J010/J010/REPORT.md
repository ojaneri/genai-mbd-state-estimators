# J010 — Rodada 5: DDPM v2 (predição de x0, cosseno, EMA, Fourier, DDIM, checkpoint por fidelidade no treino),

Início: 2026-10-01T15:18:21-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J010_v1_20k_raw --val --gen ddpm --iters 20000 --post none --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3` | J010_v1_20k_raw | 0 | 906 s | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |
| 2 | `python -u run3.py ../data out/J010_v2_raw --val --gen ddpm2 --iters 30000 --post none --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3` | J010_v2_raw | 0 | 1309 s | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |
| 3 | `python -u run3.py ../data out/J010_v2_quant --val --gen ddpm2 --iters 30000 --dequant --post quant --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3` | J010_v2_quant | 0 | 1248 s | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |
| 4 | `python -u run3.py ../data out/J010_v2_cond --val --gen ddpm2 --iters 30000 --cond-speed --post none --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3` | J010_v2_cond | 0 | 1308 s | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |
| 5 | `python -u run3.py ../data out/J010_v2_cond_quant --val --gen ddpm2 --iters 30000 --cond-speed --dequant --post quant --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3` | J010_v2_cond_quant | 0 | 1337 s | `cb17c6c95632c2d207e2ec8b1d0ce558db31c2ad45a5c887fc6f887967480639` |

## Escolha

Regra: `# Escolha: entre as 4 configurações v2, as 2 com menor média de runs[].discr_dq_gen_vs_test dentre as que têm média de (melhor de v.gen_rfill_w0.3 e v.genphys_rfill_w0.3 − v.real, por run) ≤ 0; se menos de 2 cumprirem, complete pelos menores discr_dq. Registre também runs[].discr_boot_ref (referência: bootstrap de dados reais).`

| saída | gerador | média runs[].discr_dq_gen_vs_test (por semente) | média (min(v.gen_rfill_w0.3, v.genphys_rfill_w0.3) − v.real) [flow_MAE] | cumpre ≤ 0? | média runs[].discr_boot_ref |
|---|---|---|---|---|---|
| J010_v1_20k_raw | ddpm (fora de v2: só referência) | 0.3288437500000001 [0.33287500000000014, 0.32125000000000004, 0.3313750000000001, 0.32987500000000003] | -0.1830560744903762 | sim | 0.371625 |
| J010_v2_raw | ddpm2 | 0.35146874999999994 [0.38987499999999997, 0.32575, 0.351125, 0.3391249999999999] | -0.16023727631519347 | sim | 0.371625 |
| J010_v2_quant | ddpm2 | 0.3570312499999999 [0.389625, 0.32575, 0.36262499999999986, 0.3501249999999999] | -0.14646807084294788 | sim | 0.371625 |
| J010_v2_cond | ddpm2 | 0.420375 [0.4397500000000001, 0.407625, 0.41837499999999994, 0.41574999999999984] | -0.17187667445540855 | sim | 0.371625 |
| J010_v2_cond_quant | ddpm2 | 0.41934374999999996 [0.438875, 0.40800000000000003, 0.4188749999999999, 0.4116249999999999] | -0.1814225247377922 | sim | 0.371625 |

Ordem dos que cumprem (empate até 1e-9 → desempate): ['J010_v2_raw', 'J010_v2_quant', 'J010_v2_cond_quant', 'J010_v2_cond'].

**1º escolhido: `J010_v2_raw`** — argumentos para reuso: `--gen ddpm2 --iters 30000 --post none`
**2º escolhido: `J010_v2_quant`** — argumentos para reuso: `--gen ddpm2 --iters 30000 --dequant --post quant`

## Linhas "seed … frac …" dos logs

```
J010_v1_20k_raw: seed 0 frac 0.02: real 3.150 | melhor gen_rfill_w0.3 2.929 | discr gen 0.4803749999999999 (real 0.139, ok=False) | audit 0.981 | gen 103s | total 231s
J010_v1_20k_raw: seed 0 frac 0.05: real 2.692 | melhor genphys_rfill_w1 2.576 | discr gen 0.485 (real 0.184, ok=False) | audit 0.960 | gen 100s | total 453s
J010_v1_20k_raw: seed 1 frac 0.02: real 3.315 | melhor gen_rfill_w0.3 3.050 | discr gen 0.48612500000000003 (real 0.102, ok=False) | audit 0.955 | gen 100s | total 676s
J010_v1_20k_raw: seed 1 frac 0.05: real 2.600 | melhor genphys_rfill_w0.3 2.468 | discr gen 0.48475 (real 0.166, ok=False) | audit 0.953 | gen 101s | total 900s
J010_v2_raw: seed 0 frac 0.02: real 3.150 | melhor gen_rfill_w0.3 2.951 | discr gen 0.48712500000000003 (real 0.139, ok=False) | audit 0.984 | gen 213s | total 321s
J010_v2_raw: seed 0 frac 0.05: real 2.692 | melhor genphys_rfill_w0.3 2.584 | discr gen 0.48712500000000003 (real 0.184, ok=False) | audit 0.986 | gen 227s | total 653s
J010_v2_raw: seed 1 frac 0.02: real 3.315 | melhor gen_rfill_w0.3 3.109 | discr gen 0.4891249999999999 (real 0.102, ok=False) | audit 0.985 | gen 213s | total 970s
J010_v2_raw: seed 1 frac 0.05: real 2.600 | melhor genphys_rfill_w0.3 2.472 | discr gen 0.48424999999999996 (real 0.166, ok=False) | audit 0.985 | gen 228s | total 1304s
J010_v2_quant: seed 0 frac 0.02: real 3.150 | melhor gen_rfill_w0.3 2.989 | discr gen 0.390375 (real 0.139, ok=False) | audit 0.981 | gen 211s | total 307s
J010_v2_quant: seed 0 frac 0.05: real 2.692 | melhor genphys_rfill_w0.3 2.578 | discr gen 0.3314999999999999 (real 0.184, ok=False) | audit 0.985 | gen 224s | total 622s
J010_v2_quant: seed 1 frac 0.02: real 3.315 | melhor genphys_rfill_w1 3.125 | discr gen 0.36087500000000006 (real 0.102, ok=False) | audit 0.984 | gen 213s | total 927s
J010_v2_quant: seed 1 frac 0.05: real 2.600 | melhor genphys_rfill_w0.3 2.477 | discr gen 0.35987499999999994 (real 0.166, ok=False) | audit 0.984 | gen 225s | total 1243s
J010_v2_cond: seed 0 frac 0.02: real 3.150 | melhor gen_rfill_w0.3 2.960 | discr gen 0.4821249999999999 (real 0.139, ok=False) | audit 0.968 | gen 212s | total 314s
J010_v2_cond: seed 0 frac 0.05: real 2.692 | melhor genphys_rfill_w0.3 2.587 | discr gen 0.485 (real 0.184, ok=False) | audit 0.960 | gen 226s | total 641s
J010_v2_cond: seed 1 frac 0.02: real 3.315 | melhor gen_rfill_w0.3 3.045 | discr gen 0.4876250000000001 (real 0.102, ok=False) | audit 0.955 | gen 230s | total 971s
J010_v2_cond: seed 1 frac 0.05: real 2.600 | melhor genphys_rfill_w0.3 2.477 | discr gen 0.48487500000000006 (real 0.166, ok=False) | audit 0.939 | gen 230s | total 1302s
J010_v2_cond_quant: seed 0 frac 0.02: real 3.150 | melhor gen_rfill_w0.3 2.959 | discr gen 0.4443750000000002 (real 0.139, ok=False) | audit 0.968 | gen 212s | total 309s
J010_v2_cond_quant: seed 0 frac 0.05: real 2.692 | melhor genphys_rfill_w0.3 2.580 | discr gen 0.41074999999999995 (real 0.184, ok=False) | audit 0.963 | gen 225s | total 634s
J010_v2_cond_quant: seed 1 frac 0.02: real 3.315 | melhor gen_rfill_w0.3 3.028 | discr gen 0.4262499999999999 (real 0.102, ok=False) | audit 0.954 | gen 240s | total 974s
J010_v2_cond_quant: seed 1 frac 0.05: real 2.600 | melhor genphys_rfill_w0.3 2.464 | discr gen 0.41649999999999987 (real 0.166, ok=False) | audit 0.934 | gen 256s | total 1331s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T17:01:35-03:00 — duração do job 6194 s
