# J002 — nota do operador do desktop

O driver da fila foi parado às ~00:20 (durante o comando 4) para corrigir a comparação da regra de escolha:
valores do critério principal iguais até 1e-9 passam a contar como empate (antes, um resíduo de ponto flutuante
como 0.49924999999999997 vs 0.4992500000000002 decidiria). O comando 4 continuou rodando e terminou normalmente;
ao relançar, os 4 comandos foram reaproveitados (logs terminados em `fim`), por isso o REPORT.md mostra
"reaproveitado" sem tempo. Tempos medidos na primeira execução (parede, pelo driver): cmd1 45 s, cmd2 57 s,
cmd3 45 s; cmd4 `fim 53s` (tempo interno do run2.py). Neste job a correção não alterou a escolha:
J002_l16_i5000 tem discr 0.49875, estritamente menor que as demais (0.49925).
