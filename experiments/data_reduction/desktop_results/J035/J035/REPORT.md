# J035 — CASO C2 (BESS): sensor virtual de TEMPERATURA de célula (verdade medida) — d-0020; sugestão do desktop

Início: 2026-10-03T21:46:09-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `94503586e335c5282fa5968997e6286ef70dc434beb978424b3db93d824f2d72`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|

## Linhas "seed … frac …" dos logs

```
(nenhuma)
```

## Falhas

comando fora do padrão permitido (não executado): python -u run3.py ../data_bess_temp out/J035_bess_temp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

Fim: 2026-10-03T21:46:47-03:00 — duração do job 38 s
