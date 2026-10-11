# J028 — por que ainda não rodou (nota do operador do desktop, 03/10/2026)

**Situação:** não executado até agora; **não é falha do experimento**. Será executado logo após o J030 e antes do
J031, com o comando exatamente como está na fila. O relatório da execução sairá nesta mesma pasta como
`REPORT_EXECUCAO.md` (este arquivo fica como registro do atraso).

**Motivo (regra do driver do desktop, não erro nem falta de dado):**

- O driver da fila só executa comandos que casam com uma lista de formatos permitidos (expressão regular `CMD_RE`),
  sem shell. Essa lista aceitava como valor de flag apenas `[A-Za-z0-9_.,-]`, sem barra.
- O J028 tem `--pretrain-src ../data`; o valor `../data` contém `/` e o comando seria rejeitado como "fora do
  padrão permitido", sem ser executado.
- Os dados existem: `../data/dataset.csv` (Opel) e `../data_itabira/dataset.csv` (Itabira) estão no lugar e com os
  hashes já conferidos (J001, J013). O código (`run3.py` d-0018/d-0019) aceita `--pretrain-src`.

**Linha do tempo:**

- 03/10 00:51 — fila passou a ter J026–J031; o teste do driver mostrou que só o J028 não passava no `CMD_RE`.
- 03/10 ~00:55 — `loop_driver.py` corrigido em disco (o valor pode ser `../data` ou `../data_<nome>`; backup da
  versão anterior em `review/loop_driver.v6.py`). A correção só vale após reiniciar o driver, e o reinício (encerrar
  o processo do driver em execução) não foi autorizado no desktop na ocasião.
- 03/10 15:23 — para não registrar uma falha falsa no `done.txt`, o J028 foi posto em espera (`out/hold.txt`); o
  driver então seguiu J027 → J029 → J030, como registrado em `loop_driver.log` ("EM ESPERA ... J028").

**Execução prevista:** ao terminar o J030, o J028 roda por um executor avulso que usa as mesmas funções do driver
(baixa `run3.py` e `gens.py` de novo, registra hashes, gera o relatório e envia), já com a lista de formatos
corrigida. O J031 fica em espera até o J028 terminar e depois volta à fila normal.

— operador do desktop
