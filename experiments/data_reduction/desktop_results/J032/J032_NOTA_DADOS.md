# J032–J034 — preparação dos dados BESS (nota do operador do desktop, 04/10/2026)

- Fonte: Zenodo 10.5281/zenodo.20094787 (Qu, CC BY 4.0), 8 arquivos `OperationCondition_AAAAMM_All.mat`, 10 044 400 477 bytes
  no total. Tamanho e MD5 de cada arquivo conferem com os valores da API do Zenodo (SHA-256 no `J032_prep_bess.log`).
- Download: 03/10 19:00 → 04/10 01:25. O Zenodo limitou cada conexão a ~70 KB/s; às 20:30 o download passou a ser feito
  em paralelo (um arquivo por conexão, retomável), sem mudar nenhum arquivo.
- Ambiente: `pip install h5py mat-io==1.0.0` no venv (h5py 3.16.0, mat-io 1.0.0); pandas 3.0.6, numpy 2.5.3.
- Conversor: `tools/convert_bess.py` baixado do servidor (SHA-256 bba2e3c7…, versão com o modo `temp` do d-0020; o modo
  padrão `soc` usado aqui não muda), `python convert_bess.py ../data_bess_raw ../data_bess 5`, prioridade baixa.
- Resultado: `../data_bess/dataset.csv` — SHA-256 sem `\r` = **3732315bcd763c819a5d298221a46d0718dc163bd474abe316ce6208f80c6a66**,
  **igual ao esperado** no J032 (o arquivo gerado no Windows tinha CRLF; o usado nos jobs é a versão LF, como no J013/J020).
  2 263 981 linhas, 1332 segment_file, segmentos por mês [93, 207, 198, 207, 174, 156, 159, 138], meta.json com
  cap_ah = 288,333 (1174 estimativas). Tudo confere com a descrição do job.
- J032–J034 tirados da espera às 01:56; rodam depois do J031.
