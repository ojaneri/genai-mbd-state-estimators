# J026 — P1 PORTÃO DE UTILIDADE (d-0018), caso A (Opel): o método é escolhido sozinho pela validação interna (últimos 20 % de

Início: 2026-10-03T09:44:20-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data out/J026_auto_opel --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --auto-select --seeds 15,16,17,18,19 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3` | J026_auto_opel | 0 | 10609 s | `cd2345d1c951144c96182e0766880e30a6fbd2ae9c440eec14becfb965e5364c` |

## Linhas "seed … frac …" dos logs

```
J026_auto_opel: seed 15 frac 0.01: real 3.620 | melhor gen_rfill_w0.3 3.062 | discr gen 0.444875 (real 0.118, ok=False) | id: gen 0.45850000000000013 real 0.13846153846153852 ok=False | audit 0.946 | gen 294s | total 528s
J026_auto_opel: seed 15 frac 0.02: real 2.975 | melhor hyb_resid_w0.3 2.550 | discr gen 0.326875 (real 0.169, ok=False) | id: gen 0.3011250000000001 real 0.11539091073691843 ok=False | audit 0.995 | gen 293s | total 1058s
J026_auto_opel: seed 15 frac 0.05: real 2.804 | melhor gen_rfill_w0.3 2.476 | discr gen 0.26287499999999997 (real 0.137, ok=False) | id: gen 0.24087499999999995 real 0.07787234042553193 ok=False | audit 0.973 | gen 293s | total 1584s
J026_auto_opel: seed 15 frac 0.1: real 2.383 | melhor genphys_rfill_w0.3 2.302 | discr gen 0.24075000000000002 (real 0.171, ok=False) | id: gen 0.1758749999999999 real 0.05587500000000001 ok=False | audit 0.959 | gen 294s | total 2101s
J026_auto_opel: seed 16 frac 0.01: real 3.197 | melhor gen_rfill_w0.3 2.726 | discr gen 0.41225 (real 0.164, ok=False) | id: gen 0.4092499999999999 real 0.13094811401263007 ok=False | audit 0.987 | gen 300s | total 2639s
J026_auto_opel: seed 16 frac 0.02: real 3.099 | melhor gen_rfill_w0.3 2.633 | discr gen 0.34024999999999994 (real 0.246, ok=False) | id: gen 0.3074999999999999 real 0.15993268892106616 ok=False | audit 0.990 | gen 321s | total 3197s
J026_auto_opel: seed 16 frac 0.05: real 2.539 | melhor gen_rfill_w0.3 2.321 | discr gen 0.278 (real 0.179, ok=False) | id: gen 0.24512500000000004 real 0.10743507620145432 ok=False | audit 0.970 | gen 293s | total 3720s
J026_auto_opel: seed 16 frac 0.1: real 2.386 | melhor genphys_rfill_w0.3 2.318 | discr gen 0.26625 (real 0.151, ok=False) | id: gen 0.196125 real 0.03749999999999998 ok=False | audit 0.970 | gen 300s | total 4251s
J026_auto_opel: seed 17 frac 0.01: real 3.267 | melhor gen_rfill_w0.3 2.519 | discr gen 0.36887500000000006 (real 0.129, ok=False) | id: gen 0.37224999999999997 real 0.1336745383257011 ok=False | audit 0.985 | gen 298s | total 4791s
J026_auto_opel: seed 17 frac 0.02: real 2.872 | melhor hyb_resid_w0.3 2.579 | discr gen 0.34175 (real 0.186, ok=False) | id: gen 0.310875 real 0.0886592875221941 ok=False | audit 0.981 | gen 297s | total 5320s
J026_auto_opel: seed 17 frac 0.05: real 2.571 | melhor gen_rfill_w0.3 2.444 | discr gen 0.3162499999999999 (real 0.251, ok=False) | id: gen 0.251625 real 0.1448750000000001 ok=False | audit 0.974 | gen 291s | total 5841s
J026_auto_opel: seed 17 frac 0.1: real 2.443 | melhor gen_rfill_w0.3 2.327 | discr gen 0.23212499999999991 (real 0.203, ok=True) | id: gen 0.17725000000000002 real 0.08187499999999992 ok=False | audit 0.972 | gen 290s | total 6349s
J026_auto_opel: seed 18 frac 0.01: real 3.325 | melhor hyb_resid_w0.3 2.908 | discr gen 0.42400000000000004 (real 0.169, ok=False) | id: gen 0.4248749999999999 real 0.16186813186813187 ok=False | audit 0.994 | gen 283s | total 6859s
J026_auto_opel: seed 18 frac 0.02: real 3.157 | melhor hyb_feat_w0.3 2.773 | discr gen 0.36587499999999995 (real 0.183, ok=False) | id: gen 0.3788750000000001 real 0.14967644333203955 ok=False | audit 0.995 | gen 283s | total 7377s
J026_auto_opel: seed 18 frac 0.05: real 2.623 | melhor gen_rfill_w0.3 2.337 | discr gen 0.30225000000000013 (real 0.176, ok=False) | id: gen 0.269 real 0.10188616676081752 ok=False | audit 0.967 | gen 296s | total 7911s
J026_auto_opel: seed 18 frac 0.1: real 2.438 | melhor genphys_rfill_w0.3 2.372 | discr gen 0.28625 (real 0.202, ok=False) | id: gen 0.19662499999999994 real 0.07075000000000009 ok=False | audit 0.970 | gen 298s | total 8440s
J026_auto_opel: seed 19 frac 0.01: real 3.325 | melhor gen_rfill_w0.3 2.738 | discr gen 0.4332499999999999 (real 0.265, ok=False) | id: gen 0.4125 real 0.1979642066031433 ok=False | audit 0.992 | gen 299s | total 8983s
J026_auto_opel: seed 19 frac 0.02: real 3.115 | melhor hyb_resid_w0.3 2.565 | discr gen 0.3065 (real 0.227, ok=False) | id: gen 0.31525000000000003 real 0.17463126843657817 ok=False | audit 0.975 | gen 302s | total 9530s
J026_auto_opel: seed 19 frac 0.05: real 2.639 | melhor gen_rfill_w0.3 2.399 | discr gen 0.26649999999999996 (real 0.175, ok=False) | id: gen 0.21187500000000004 real 0.09708957454952882 ok=False | audit 0.970 | gen 303s | total 10073s
J026_auto_opel: seed 19 frac 0.1: real 2.386 | melhor gen_rfill_w0.3 2.325 | discr gen 0.24562499999999998 (real 0.182, ok=False) | id: gen 0.17337500000000006 real 0.06774999999999998 ok=False | audit 0.946 | gen 301s | total 10604s
```

## Falhas

Nenhuma.

Fim: 2026-10-03T12:41:34-03:00 — duração do job 10634 s
