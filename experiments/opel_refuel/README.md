# Teste externo de detecção de reabastecimento em dados públicos (2026-09-30)

Objetivo: checar, fora dos dados da OEM, a camada de detecção de reabastecimento e de janelas
confiáveis do caso A. **Não** é a árvore de decisão da dissertação (treinada com velocidade, RPM e
inclinação de dados OEM); é uma regra análoga: comparar o nível só em janelas com o veículo parado
(v = 0 por ≥ W) e nível estável (pico-a-pico ≤ P2P).

Dados (não versionados; baixar do Kaggle):
- Opel Corsa 2012 — `pedro2025/obd2-panel-opel-2012`, CC BY 4.0: `dataset.csv`, `refueling_history.csv`.
- Itabira-MG — `brunops2/obd-2-vehicular-dataset-trace`, CC0: `Dataset.csv` (separador `;`, ausentes `-`).

Scripts: `refuel_test.py` (mapeamento, detector ingênuo, litros), `gated_vs_naive.py`,
`window_sweep.py`. Saídas: `results.json`, `gated_vs_naive.json`, `itabira_window_sweep.csv`,
`refuel_truth_mapping.csv`, `level_litres_loo.csv`, figura `Figures/generated/public_refuel_fp.pdf`.

## Resultados
- **Mapeamento Opel:** linha k de `refueling_history.csv` = fim do segmento k do log
  (`Segment_id` do arquivo = k + 2). Datas batem em 21/22; a linha 1 diz 15/05/2025, o log mostra
  o reabastecimento em 12/05/2025 21:41–21:49. O 22º ocorre depois do fim do log → 21 observáveis.
- **Opel, detector ingênuo:** 21/21, 0 FP para qualquer limiar de 1 a 50 pontos. O nível do PID é
  tão filtrado (maior subida dentro de viagem: 0,78 ponto; resolução 1/255) que o teste **não
  discrimina** detectores.
- **Opel, detector supervisionado (W = 20 s, P2P = 3):** os 21 detectados, 0 detecção espúria;
  18 dentro de ±2 h e 3 com atraso de 2,5–9,5 h (a primeira janela confiável após o abastecimento
  só abriu na viagem seguinte) → custo em latência.
- **Opel, litros:** escala ajustada (mínimos quadrados, sem intercepto) = 43,13 L por 100 % de
  leitura do PID — *não* é a capacidade do tanque. Leave-one-out: MAE 0,55 L (1,52 % do volume
  abastecido), máx. 1,66 L. Consumo integrado (MAF, `Trapez_l`) vs. bomba: MAE 0,60 L, máx. 2,04 L,
  viés médio −0,02 L (22 tanques).
- **Itabira (nível quase sem filtro; sem reabastecimento dentro das viagens → toda detecção dentro
  de viagem é FP):** ingênuo com limiar 15 pontos: 20,6 FP/h (veículo 2, 1,07 h) e 51,2 FP/h
  (veículo 3, 4,11 h). Supervisionado: **0 FP em todas as 24 combinações** W ∈ {5,10,20} s ×
  P2P ∈ {3,5,10,20}; disponibilidade de 0,5 a 15,6 janelas/h conforme a configuração.

## Limites
- Nível em % já processado pela ECU; nenhum dos dois datasets tem resistência do sensor.
- Itabira: a ausência de reabastecimento dentro das viagens é suposição (maior subida líquida de
  início a fim de viagem: 9,8 e 9,0 pontos, compatível com ruído); poucas horas de dados.
- Opel: um veículo, reabastecimentos sempre de tanque cheio e com motor desligado.
