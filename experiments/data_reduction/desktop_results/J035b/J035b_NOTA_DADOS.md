# J035b — dados (nota do operador do desktop, 04/10/2026 05:35)

- `../data_besstemp` = cópia byte a byte de `../data_bess_temp`, gerado às 01:58–02:27 por
  `python convert_bess.py ../data_bess_raw ../data_bess_temp 5 temp` (o mesmo comando do J035b, só o nome da pasta de saída muda;
  conversor baixado do servidor, SHA-256 bba2e3c7…). Ver `J035_NOTA_DADOS.md`.
- SHA-256 de `../data_besstemp/dataset.csv` (sem `\r`) = **7249bace12866f6f460e5553a229c9e18f061d15ca87e680cd709b613573b38e**,
  igual ao esperado do J035; 2 264 252 linhas, 1332 segment_file, meta.json idêntico (mode=temp, target_point=109).
- O J035 original (falsa falha do driver) não foi rodado: o J035b o substitui, pela fila normal, depois do J034.
