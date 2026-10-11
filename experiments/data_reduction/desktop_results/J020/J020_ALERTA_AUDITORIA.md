# J020 — ALERTA: auditoria física da bateria rejeita 100 % do sintético (nota do operador do desktop, 2026-10-02 04:0x)

Fatos (de out/J020.log e J020/results.json, combinação 1, seed 0 frac 0.01):
- `audit_pass` = 0.000; `n_syn_audited` = 0 de 122 776 amostras geradas (n_fill 75 485 × 1,6 + 2000); `discr_gen_vs_test` = None.
- Consequência: as variantes `gen_*` e `genphys_*` (incluindo o desfecho pré-registrado `gen_rfill_w0.3`) NÃO são calculadas
  (o laço pula quando o conjunto auditado está vazio). Só `real`, `aug_rfill_w0.3` e `physonly` aparecem em `v`.
- Limites calculados nos dados reais (`audit_limits`): cc = 0.000374, dv = 0.365, di = 8.41, dt = 0.137.
- O comando terminou normalmente (sem erro); o driver vai seguir as 20 combinações do J020 sem o desfecho principal.

Hipótese (não verificada — as amostras sintéticas não são salvas): o teste t2 (contagem de carga) exige
|ΔSOC − I/3600/3,0| ≤ 0,000374 em todas as 23 transições de cada janela; um gerador com erro de ~1 % da faixa de SOC por
passo não atinge essa precisão. J022 (mesmo gerador, mesmo domínio) deve ter o mesmo resultado. J021 (bootstrap) pode
passar, exceto nas costuras.

Nada foi alterado no código nem na fila. Fica a critério da sessão do servidor ajustar a auditoria/fila (p.ex. re-enfileirar
J020/J022 com correção) — o driver relê a fila a cada job.
