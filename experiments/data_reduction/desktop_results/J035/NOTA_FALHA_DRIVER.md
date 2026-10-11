# J035 — o "falhou" no done.txt é falso: o comando não foi executado (nota do operador do desktop, 03/10/2026 21:55)

- O driver em execução leu o J035 às 21:45 e o rejeitou **antes de rodar qualquer coisa**: a lista de formatos
  permitidos do driver aceitava pastas de dados `../data` ou `../data_<nome>` com **um** sufixo; `../data_bess_temp`
  tem dois. Nenhum processo foi iniciado, nenhum dado foi gerado, a GPU não foi usada.
- Além disso, os dados do J035 ainda não existem neste desktop: os 8 `.mat` do Zenodo estão sendo baixados
  (previsão de término ~06:00 de 04/10) e o `../data_bess_temp` depende deles.
- Correção: `loop_driver.py` v8 em disco aceita `../data_<a>_<b>` (backup da v7 em `review/loop_driver.v7.py`).
- O que será feito: quando os `.mat` estiverem completos, `convert_bess.py ../data_bess_raw ../data_bess_temp 5 temp`
  (baixado de novo), conferência do hash/contagens do J035, e execução do J035 com o comando exatamente como na fila,
  pelo executor avulso (mesmas funções do driver). O resultado será registrado como nova linha `J035 ok …` no
  `done.txt` (nenhuma linha existente é apagada) e o relatório sairá em `J035/J035/REPORT_EXECUCAO.md`.
- Revisão do `run3.py` d-0020 (domínio `bess_temp`): mudança aditiva; para `fuel` e `battery` o comportamento é o mesmo.

— operador do desktop
