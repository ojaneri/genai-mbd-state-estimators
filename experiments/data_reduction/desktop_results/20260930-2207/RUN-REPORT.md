# RUN-REPORT — redução de dados, caso A (Opel Corsa 2012), execução no desktop com GPU

Data da execução: 2026-09-30. Todos os números deste relatório foram lidos dos `results.json` e logs gerados nesta
execução (tabelas da seção 3 geradas por `make_tables.py` a partir de `out/*/results.json`).

## 1. Ambiente

| item | valor |
|---|---|
| SO | Microsoft Windows 10 Enterprise 10.0.19045 (nativo; comandos via Git Bash) |
| CPU | AMD Ryzen 5 5500 |
| GPU | NVIDIA GeForce RTX 3060, 12 288 MiB, driver 610.88 (nvidia-smi informa CUDA UMD 13.3) |
| Python | 3.12.10 (venv) |
| PyTorch | 2.14.1+cu126 (CUDA 12.6, cuDNN 91002), `torch.cuda.is_available() == True` |
| scikit-learn / numpy / pandas | 1.9.1 / 2.5.3 / 3.0.6 |
| `OMP_NUM_THREADS` | 2 (padrão do `run.py`, não alterado) |

Hashes SHA-256 dos dados (Kaggle `pedro2025/obd2-panel-opel-2012`, baixado em 2026-09-30) — **iguais aos esperados**:
- `dataset.csv` — `27e6b070324dcf5b5600b73710be7763c4dada2e221b91e39128605132eee8b3`
- `refueling_history.csv` — `e0f70623872d730d6ac01cd7adb729a3ec72e43638df991658f3801fc835c70c`

Hashes SHA-256 do código usado (idênticos aos arquivos no servidor, conferido com `sha256sum` nos dois lados):
- `run.py` — `b9ccb8d105ae061a84079cc5051dbfcc33ddb880ce2e456a5f2d8a6ba45d955a`
- `timegan.py` — `d6baf805f9e5d1581cb71f35509a81ec561ad9346e32944b963dbc800e448eea`

## 2. Comandos executados e tempos

Pasta de trabalho: `<workdir>\code` (dados em `..\data`, venv em `..\.venv`).

| etapa | comando | tempo (parede) |
|---|---|---|
| fumaça | `python -u run.py ../data out/smoke --val --seed 0 --iters 20 --fracs 0.25 --no-scenario` | 26 s (`fim 26s`) |
| A h24 it1500 | `python -u run.py ../data out/tune_h24_it1500 --val --seed 0 --iters 1500 --hidden 24 --fracs 0.25 --no-scenario` | 89 s |
| A h24 it3000 | idem, `--iters 3000 --hidden 24` | 139 s |
| A h24 it6000 | idem, `--iters 6000 --hidden 24` | 244 s |
| A h48 it1500 | idem, `--iters 1500 --hidden 48` | 85 s |
| A h48 it3000 | idem, `--iters 3000 --hidden 48` | 139 s |
| A h48 it6000 | idem, `--iters 6000 --hidden 48` | 256 s |
| B seed 0 | `python -u run.py ../data out/final_seed0 --seed 0 --iters 6000 --hidden 24` | 985 s |
| B seed 1 | idem `--seed 1` | 998 s |
| B seed 2 | idem `--seed 2` | 996 s |
| B seed 3 | idem `--seed 3` | 1001 s |
| B seed 4 | idem `--seed 4` | 1005 s |

Smoke test conferido: `meta.cuda == true`, `meta.gpu == "NVIDIA GeForce RTX 3060"`, `meta.mode == "validation"`,
`meta.test_segments == [15, 16, 17]`, `runs[0].tg_log.device == "cuda"`.
Tempos de parede medidos com `date` em volta de cada comando; `runtime_s` interno em cada `results.json` (tabelas abaixo).
Tarefa B: 5 sementes rodadas (tempo por semente ≈ 16–17 min, bem abaixo do limite de ~2 h).

## 3. Escolha da configuração (Tarefa A)

Critério do DESKTOP.md §6: menor `discr_timegan`, desempate por maior `audit.all`, depois menor `tstr_timegan.flow_MAE`.

**Escolhida: `hidden=24`, `iters=6000`** (`discr_timegan` = 0,491250, o menor da grade; o segundo menor foi h48/it6000
com 0,491625). Não houve empate, então os critérios de desempate não foram usados.

**Nenhuma configuração ficou com `discr_timegan` < 0,45** (faixa observada: 0,491250–0,498750). Ou seja, em todas
as configurações um classificador distingue o sintético do real de validação quase perfeitamente. Mais iterações
reduziram o `discr` só marginalmente (≈ 0,007), e ao mesmo tempo pioraram o TSTR `flow_MAE` e o `flow_MAE` de
real+TimeGAN. A escolha segue o critério estabelecido, mas a diferença entre as configurações em `discr` é pequena
demais para ter significado prático. Para comparação, na mesma rodada de validação, `discr_simpleaug` = 0,48075 e
`discr_real_train` = 0,12175.

## 4. Tabelas (geradas por `make_tables.py`)

### Tarefa A — ajuste (validação 15–17, fração 0.25, semente 0)

| hidden | iters | discr_timegan | audit.all | tstr litres_MAE | tstr flow_MAE | real_timegan flow_MAE | real flow_MAE | runtime_s |
|---|---|---|---|---|---|---|---|---|
| 24 | 1500 | 0.498750 | 0.9919 | 0.0299 | 3.2370 | 2.4925 | 2.4109 | 84 |
| 24 | 3000 | 0.495375 | 0.9772 | 0.0794 | 3.8118 | 2.6336 | 2.4109 | 135 |
| 24 | 6000 | 0.491250 | 0.9107 | 0.0958 | 4.2579 | 2.6958 | 2.4109 | 239 |
| 48 | 1500 | 0.497625 | 0.9998 | 1.7113 | 3.6465 | 2.4838 | 2.4109 | 80 |
| 48 | 3000 | 0.495125 | 0.8853 | 1.1045 | 3.4537 | 2.5640 | 2.4109 | 135 |
| 48 | 6000 | 0.491625 | 0.9560 | 1.4125 | 3.8849 | 2.6772 | 2.4109 | 251 |

### Tarefa B — teste 18–22, sementes [0, 1, 2, 3, 4] (média ± desvio-padrão amostral entre sementes)

| fração | condição | flow_MAE | litres_MAE |
|---|---|---|---|
| 0.1 | real | 2.3405 ± 0.0204 | 0.6447 ± 0.0311 |
| 0.1 | real_timegan | 2.6768 ± 0.1532 | 0.6500 ± 0.0383 |
| 0.1 | real_timegan_noaudit | 2.6784 ± 0.1747 | 0.6546 ± 0.0415 |
| 0.1 | real_simpleaug | 3.3191 ± 0.1635 | 0.8131 ± 0.1266 |
| 0.25 | real | 2.2613 ± 0.0309 | 0.6462 ± 0.0233 |
| 0.25 | real_timegan | 2.5072 ± 0.0989 | 0.6280 ± 0.0375 |
| 0.25 | real_timegan_noaudit | 2.5110 ± 0.1016 | 0.6268 ± 0.0387 |
| 0.25 | real_simpleaug | 2.9267 ± 0.0294 | 0.7175 ± 0.0553 |
| 0.5 | real | 2.2089 ± 0.0235 | 0.6456 ± 0.0122 |
| 0.5 | real_timegan | 2.4824 ± 0.1196 | 0.6541 ± 0.0352 |
| 0.5 | real_timegan_noaudit | 2.4751 ± 0.1209 | 0.6582 ± 0.0349 |
| 0.5 | real_simpleaug | 2.6500 ± 0.0497 | 0.6649 ± 0.0151 |
| 1.0 | upper_bound_100pct_real | 2.1488 ± 0.0000 | 0.6285 ± 0.0000 |

| fração | discr_timegan | discr_simpleaug | discr_real_train | audit.all | tstr flow_MAE | tstr litres_MAE |
|---|---|---|---|---|---|---|
| 0.1 | 0.4942 ± 0.0019 | 0.4802 ± 0.0019 | 0.1398 ± 0.0177 | 0.8514 ± 0.1244 | 3.9556 ± 0.4719 | 0.7956 ± 0.2144 |
| 0.25 | 0.4942 ± 0.0031 | 0.4783 ± 0.0019 | 0.1423 ± 0.0076 | 0.9788 ± 0.0190 | 3.8670 ± 0.2839 | 0.7656 ± 0.1129 |
| 0.5 | 0.4956 ± 0.0020 | 0.4789 ± 0.0010 | 0.1308 ± 0.0038 | 0.9246 ± 0.0602 | 4.5634 ± 0.4674 | 0.9462 ± 0.2634 |

### Cenário ausente (treino 25 % sem rodovia >80 km/h; MAE de vazão só em janelas de rodovia)

| métrica | média ± dp |
|---|---|
| hw_MAE_real | 2.7170 ± 0.4188 |
| hw_MAE_real_timegan | 2.7196 ± 0.3363 |
| hw_MAE_real_simpleaug | 5.6038 ± 0.6610 |
| hw_MAE_full_real | 2.0798 ± 0.0000 |
| syn_max_speed | 83.5662 ± 4.4893 |

### Referência MAF × bomba (litres_MAE)

seed 0: 0.4571, seed 1: 0.4571, seed 2: 0.4571, seed 3: 0.4571, seed 4: 0.4571

### Tempo por semente (runtime_s)

seed 0: 964, seed 1: 984, seed 2: 991, seed 3: 996, seed 4: 1001

## 5. Leitura dos resultados

Diferenças pareadas por semente (condição − `real`, mesma semente e fração; 5 sementes por fração), calculadas a
partir dos `results.json`:

| métrica | condição | fração 0.1 | fração 0.25 | fração 0.5 |
|---|---|---|---|---|
| flow_MAE | real_timegan − real | +0,336 ± 0,163 (pior em 5/5) | +0,246 ± 0,075 (5/5) | +0,274 ± 0,118 (5/5) |
| flow_MAE | real_timegan_noaudit − real | +0,338 ± 0,185 (5/5) | +0,250 ± 0,082 (5/5) | +0,266 ± 0,118 (5/5) |
| flow_MAE | real_simpleaug − real | +0,979 ± 0,151 (5/5) | +0,665 ± 0,028 (5/5) | +0,441 ± 0,058 (5/5) |
| litres_MAE | real_timegan − real | +0,005 ± 0,027 (pior em 2/5) | −0,018 ± 0,052 (1/5) | +0,009 ± 0,042 (3/5) |
| litres_MAE | real_timegan_noaudit − real | +0,010 ± 0,022 (3/5) | −0,019 ± 0,055 (1/5) | +0,013 ± 0,041 (4/5) |
| litres_MAE | real_simpleaug − real | +0,168 ± 0,146 (5/5) | +0,071 ± 0,078 (4/5) | +0,019 ± 0,025 (4/5) |

1. **Vazão instantânea (`flow_MAE`) — o TimeGAN não ajudou; piorou.** Em todas as 15 combinações semente × fração,
   adicionar o sintético auditado aumentou o erro em relação a treinar só com a fração real (+0,25 a +0,34 mL/min
   em média, diferença bem maior que o desvio entre sementes da condição `real`, ≈ 0,02–0,03). Nenhuma condição com
   sintético se aproximou do teto de 100 % real (2,149) mais do que a própria fração real sozinha.
2. **Litros por tanque (`litres_MAE`) — sem diferença detectável.** As diferenças médias do TimeGAN (−0,018 a +0,009 L)
   estão dentro do desvio entre sementes, e o sinal muda de fração para fração. Essa métrica tem baixo poder de
   discriminação neste protocolo: são só 5 tanques no teste; a própria vazão-alvo (MAF corrigida) integrada difere da
   bomba em 0,457 L em média (`reference_MAF_vs_pump`); e o teto de 100 % real (0,629 L) não é melhor que a fração 0.25
   real (0,646 ± 0,023) por uma margem significativa — em algumas sementes uma fração real ficou abaixo do teto.
   Não se deve ler as pequenas "vitórias" do TimeGAN em litros (fração 0.25: melhor em 4/5 sementes) como ganho real.
3. **Aumento simples (ruído/escala) foi o pior em vazão** — pior que `real` em 15/15 e pior que `real_timegan` em 15/15
   combinações. Em litros, pior que `real` na maioria dos casos. Ou seja, o TimeGAN não foi pior que o aumento simples,
   mas nenhum dos dois superou o uso apenas da fração real.
4. **Auditoria física: efeito nulo nas métricas.** `real_timegan` e `real_timegan_noaudit` diferem em ≤ 0,01 mL/min
   (média) — dentro do ruído. A auditoria aprovou 85 %, 98 % e 92 % (médias nas frações 0.1/0.25/0.5) das janelas,
   portanto as janelas reprovadas eram poucas; e passar na auditoria não tornou o sintético realista
   (`discr_timegan` ≈ 0,494–0,496 em todas as frações, igual com ou sem auditoria).
5. **Fidelidade:** `discr_timegan` 0,494–0,496 (praticamente 0,5, totalmente distinguível). `discr_simpleaug` ≈ 0,48 —
   o aumento simples também é quase totalmente distinguível do real de teste. `discr_real_train` ≈ 0,13–0,14 (real de
   treino vs real de teste), indicando algum deslocamento de distribuição entre os tanques 8–17 e 18–22.
   TSTR (treinar só no sintético): `flow_MAE` 3,87–4,56, muito pior que qualquer condição com dado real.
6. **Cenário ausente (rodovia):** `hw_MAE_real_timegan` (2,720 ± 0,336) ≈ `hw_MAE_real` (2,717 ± 0,419); o TimeGAN foi
   melhor em 3/5 sementes e pior em 2/5, diferença média +0,003 — **sem efeito**. O sintético excedeu 80 km/h em 4/5
   sementes (máx. 79,8–91,0 km/h), mas isso não se traduziu em melhor previsão em rodovia. O aumento simples quase
   dobrou o erro (5,604 ± 0,661). O teto com 100 % real em rodovia foi 2,080.

**Conclusão honesta:** neste caso (sensor virtual de vazão, Opel Corsa, entradas velocidade/RPM/borboleta), com a
configuração TimeGAN escolhida na validação, o aumento com dados sintéticos — auditados ou não — **não aproximou o
estimador do teto de 100 % real; piorou o erro de vazão de forma consistente** e não teve efeito detectável em litros
por tanque nem no cenário ausente. O TimeGAN não conseguiu imitar o sinal (discriminative ≈ 0,5 em todas as
configurações da grade), o que é coerente com esses resultados.

## 6. Mudanças no código e anomalias

- **Código do experimento: nenhuma alteração.** `run.py` e `timegan.py` usados com hashes idênticos aos do servidor.
  Scripts auxiliares criados no desktop (não alteram a lógica): `run_final.sh` (laço da Tarefa B, retomável, pula
  sementes com `fim` no log) e `make_tables.py` (gera `summary.csv` e `tables.md` a partir dos `results.json`).
- **Python:** o desktop só tinha Python 3.13.14 (fora da faixa 3.10–3.12 pedida). Com autorização do Osvaldo, foi
  instalado o Python 3.12.10 via `winget` (escopo do usuário) e criado o venv com ele. Índice PyTorch usado: `cu126`.
- **Laços:** executados no Git Bash (os laços `for` do DESKTOP.md funcionaram sem reescrita para PowerShell).
- **Queda da máquina durante a Tarefa B:** a primeira tentativa da semente 0 (início 20:35:31) foi interrompida por
  queda da máquina antes de concluir a primeira fração (nenhum `results.json` de execução final foi gravado nessa
  tentativa). O log parcial foi preservado como `final_seed0.crashed.log`. A semente 0 foi relançada do zero às
  20:42:26 e as 5 sementes concluíram sem erro (`rc=0`). O valor de `upper_bound_100pct_real` da tentativa
  interrompida (flow_MAE 2,1488, litres_MAE 0,6285) é idêntico ao da execução completa.
- **`upper_bound_100pct_real` e `reference_MAF_vs_pump` têm desvio 0 entre sementes** — esperado: o teto usa o pool
  inteiro e `HistGradientBoostingRegressor(random_state=0)`, independente da semente.
- **Proporção sintético/real:** o protocolo completa o conjunto até o tamanho do pool (`n_fill = len(Wfull) − len(Wr)`);
  na fração 0.1 isso significa ≈ 7,4–8,6 mil janelas reais para ≈ 76,7–77,9 mil sintéticas (≈ 90 % sintético). Isso
  pode ajudar a explicar por que o sintético degrada a vazão nas frações menores; registro como observação, não alterei.
- Observações menores no código (não alteradas): o docstring de `run.py` menciona "3 sementes" (DESKTOP.md pede 5,
  passadas via `--seed`) e o comentário de `feats()` diz `(n, L, 5)`/"4 canais", mas `CH` tem 4 canais e `feats` usa 3.
- Durante toda a execução, nenhuma ação no servidor além de `cat`, `ls`, `df`, `sha256sum`, `scp` (leitura do código e
  envio dos resultados) e `mkdir` em `desktop_results/`.
