# J035 — preparação dos dados (caso C2, temperatura de célula; nota do operador do desktop, 04/10/2026)

- Mesmos 8 `.mat` do J032 (Zenodo 20094787; tamanho e MD5 conferidos — ver `J032_NOTA_DADOS.md`).
- `tools/convert_bess.py` baixado de novo (SHA-256 bba2e3c7…), `python convert_bess.py ../data_bess_raw ../data_bess_temp 5 temp`,
  prioridade baixa, 01:58 → 02:27.
- `../data_bess_temp/dataset.csv` — SHA-256 sem `\r` = **7249bace12866f6f460e5553a229c9e18f061d15ca87e680cd709b613573b38e**,
  **igual ao esperado**; 2 264 252 linhas, 1332 segment_file, meta.json com mode=temp e target_point=109.
- O J035 roda pelo executor avulso (mesmas funções do driver, comando exatamente como na fila) depois do J034, com a GPU livre;
  ver `NOTA_FALHA_DRIVER.md` sobre o "falhou" falso das 21:47 de 03/10.
