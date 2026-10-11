# J013 — preparação dos dados (nota do operador do desktop)

- Dataset.csv (Kaggle brunops2, baixado 2026-10-01 22:08): SHA-256 `5d0ced594efcd95ecc1d9a515783ba8385210b49927e8e61fdbbb468ff8b43fe` (começa com 5d0ced594efcd95e, conforme esperado).
- `convert_itabira.py` (copiado de tools/, sem alteração) gerou ../data_itabira/dataset.csv com 125 725 linhas, 253 viagens.
- O hash do arquivo gerado no Windows foi `45a3189b7e99c8fb921997301f96c7f0b1f4ff4ce95db1d0d0abd8f12e96a547`, diferente do esperado,
  porque o pandas no Windows grava fim de linha CRLF. Removendo só os `\r`, o hash é exatamente o esperado
  `b5a91d90cc2557ce745b5675048f1a0357ef840a2ae4d2fb6620cf0c0c6d391f`. O arquivo usado no J013 é a versão LF (hash idêntico ao do servidor);
  nenhum valor foi alterado.
