# J004 — Rede neural (MLP) como modelo final, gerador TimeGAN (h24, 6000 it), 3 sementes

Início: 2026-10-01T01:10:09-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `fd1ec8fbd39be4f32d74e9cd21021c552f4014b97bb616f62be12724e9c7ff59`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `9fab12e388fca2190c56d4e433dbdef5247c2adc7bc70ce33cbc442a097942eb`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run2.py ../data out/J004 --gen timegan --iters 6000 --hidden 24 --model mlp --seeds 0,1,2 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_r1_w1,gen_r1_w0.3,gen_rfill_w1,gen_dfilt_q0.2,gen_pretrain,aug_r1_w1` | J004 | 0 (reaproveitado) | — | `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56` |

## Linhas "seed … frac …" dos logs

```
J004: seed 0 frac 0.01: real 4.275 | melhor gen_r1_w1 4.107 | discr gen 0.4922500000000001 | audit 0.875 | gen 228s | total 299s
J004: seed 0 frac 0.02: real 4.499 | melhor gen_rfill_w1 3.583 | discr gen 0.4901249999999999 | audit 0.866 | gen 221s | total 575s
J004: seed 0 frac 0.05: real 3.311 | melhor gen_r1_w0.3 3.071 | discr gen 0.49475 | audit 0.998 | gen 221s | total 853s
J004: seed 0 frac 0.1: real 3.158 | melhor gen_r1_w0.3 2.806 | discr gen 0.49412500000000004 | audit 0.985 | gen 222s | total 1143s
J004: seed 1 frac 0.01: real 3.990 | melhor real 3.990 | discr gen 0.49687499999999996 | audit 0.827 | gen 221s | total 1407s
J004: seed 1 frac 0.02: real 4.846 | melhor gen_rfill_w1 3.021 | discr gen 0.4891249999999999 | audit 0.987 | gen 222s | total 1679s
J004: seed 1 frac 0.05: real 3.382 | melhor gen_r1_w1 3.340 | discr gen 0.4973749999999999 | audit 0.991 | gen 221s | total 1947s
J004: seed 1 frac 0.1: real 2.745 | melhor real 2.745 | discr gen 0.4952500000000001 | audit 0.949 | gen 222s | total 2230s
J004: seed 2 frac 0.01: real 4.433 | melhor gen_rfill_w1 2.904 | discr gen 0.4879999999999999 | audit 0.812 | gen 222s | total 2500s
J004: seed 2 frac 0.02: real 3.772 | melhor gen_rfill_w1 3.305 | discr gen 0.4963749999999999 | audit 0.959 | gen 221s | total 2769s
J004: seed 2 frac 0.05: real 2.888 | melhor gen_r1_w0.3 2.837 | discr gen 0.4956250000000001 | audit 0.999 | gen 221s | total 3048s
J004: seed 2 frac 0.1: real 2.867 | melhor gen_r1_w0.3 2.805 | discr gen 0.49212500000000003 | audit 0.836 | gen 221s | total 3331s
```

## Falhas

Nenhuma.

Fim: 2026-10-01T02:02:33-03:00 — duração do job 3144 s
