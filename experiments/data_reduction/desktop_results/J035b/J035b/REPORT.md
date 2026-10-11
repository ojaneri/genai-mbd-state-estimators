# J035b — REFAZ o J035 (rejeitado pelo driver do desktop: "comando fora do padrão permitido", provável sublinhado duplo em

Início: 2026-10-04T05:35:51-03:00

## Código (SHA-256, baixado do servidor no início do job)

- `run2.py` — `d48163c65d58cafe6f45da14b022af72541909d542744ddcf54ce258e916af56`
- `run3.py` — `94503586e335c5282fa5968997e6286ef70dc434beb978424b3db93d824f2d72`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`
- `timevae.py` — `8d32542e42a3646486f99ccf3b92b5185aa19d2f28ac13aa61e1f9c29c8a8bef`
- `gens.py` — `580277d75326c94d3ef9bacba89bc81e40d7fc0a7a97cb1ea7e799b7a1fcf8e9`

## Comandos

| # | comando executado | saída | rc | tempo | SHA-256 do script usado |
|---|---|---|---|---|---|
| 1 | `python -u run3.py ../data_besstemp out/J035b_besstemp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3` | J035b_besstemp | 1 | 9 s | `94503586e335c5282fa5968997e6286ef70dc434beb978424b3db93d824f2d72` |

## Linhas "seed … frac …" dos logs

```
(nenhuma)
```

## Falhas

comando 1 (J035b_besstemp) terminou com rc=1. Final do log:
```
    result = ops.arithmetic_op(lvalues, rvalues, op)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<workdir>\.venv\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
                 ^^^^^^^^^^^^^^^
  File "<workdir>\.venv\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
           ^^^^^^^^^^^^^^^^^^^
  File "<workdir>\.venv\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<workdir>\.venv\Lib\site-packages\pandas\core\arrays\string_.py", line 1233, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

Fim: 2026-10-04T05:36:33-03:00 — duração do job 42 s
