# J001 — anomalias observadas nos arquivos (registro factual, código não alterado)

Escrito pelo operador do desktop após o job; valores lidos de `J001/results.json`.

1. **`gen_pretrain` com erro ~10x maior que as demais variantes.** `v.gen_pretrain.flow_MAE` nas 20 combinações
   semente×fração: 32.93, 33.07, 31.77, 28.46, 29.85, 29.86, 31.79, 29.22, 27.26, 29.74, 28.79, 31.88, 30.68, 30.4,
   28.2, 31.1, 28.92, 33.8, 31.43, 30.61 (vs. `real` ≈ 2.3–3.2 e `gen_rfill_w1` 2.45–4.23). O comportamento é
   compatível com um problema na função `fit_pretrain` (HistGradientBoostingRegressor com `warm_start` re-ajustado
   em outro conjunto), mas isso não foi investigado nem corrigido aqui.
2. **`gen_dfilt_q0.2` e `gen_dfilt_q0.5` são idênticos em 20/20 combinações** (mesmo `flow_MAE`, mesmo `n_syn`,
   p.ex. 815/815, 1301/1301, 5579/5579, 6702/6702). Em `run2.py`, `S = syn[np.argsort(-pr)[:k]][:len(Wr)]` corta
   para `len(Wr)` janelas; como `k = q·len(syn)` (≈ 24 mil a 120 mil) é sempre maior que `len(Wr)`, os dois filtros
   selecionam o mesmo conjunto (as `len(Wr)` janelas com maior prob. de "real").
