# J020–J022 — preparação dos dados de bateria (nota do operador do desktop)

- `convert_lghg2.py` (copiado de tools/, sem alteração) baixou 556 MB do Mendeley (cp3473x7xv v3) em ../data_lghg2_raw e gerou
  ../data_lghg2/dataset.csv: 449 474 linhas, 70 ciclos (6 temperaturas). Log em `J020_prep_lghg2.log`.
- O hash do arquivo gerado no Windows foi `f7a4bff5e22cbecee54411e7cd0ca2e24510cc8d23a9b6936c375b18fa4b3e89`, diferente do esperado,
  porque o pandas no Windows grava fim de linha CRLF. Removendo só os `\r`, o hash é exatamente o esperado
  `2fd898df640fd93d410ea4774708a7ee81f8ac8392e72d90315a7db910e5228b`. Os jobs J020–J022 usam a versão LF (hash idêntico ao do servidor);
  nenhum valor foi alterado. (Mesmo caso do Itabira, ver J013_NOTA_DADOS.md.)
