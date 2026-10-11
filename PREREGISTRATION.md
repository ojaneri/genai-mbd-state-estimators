# Pre-registration records (d-0005 – d-0033)

These are the hypotheses, outcomes, decision rules and data checks written **before** each experiment was run, copied
verbatim from the project's internal research log (in Portuguese, as written). Each entry gives the time it was first
committed to the authors' private project repository and the commit id; the results it governs were produced afterwards
(see the job dates in `experiments/data_reduction/desktop_results/*/REPORT.md`). The private repository is not public,
so these timestamps are the authors' record and are not independently verifiable. "status: proposed" is the internal
workflow label of the log; it does not mean the rule was changed later. Amendments are recorded as separate entries
(e.g. d-0016 amends d-0015) and were committed before any affected outcome existed.

Glossary: só-real = real data only; fração = fraction of the real training data; semente = seed; gen_rfill_w0.3 = real
data plus generator windows filling the pool at sample weight 0.3; physonly = physics-structured model plus residual,
real data only; hyb_resid / hyb_feat = hybrids of physics and generative data; portão de utilidade = utility gate;
desktop = the workstation (RTX 3060) that ran the jobs; servidor = the server that prepared jobs and analysed results.

### d-0005 — first committed 2026-09-30T17:22:45-03:00 (commit ebb51dc0de2c)

- **[#d-0005]** date: 2026-09-30 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **Validação do framework por redução de dados com teste reservado: treinar o gerador (e o estimador) com frações dos dados reais (10/25/50/100 %), gerar sintético, e comparar com o uso de 100 % dos dados reais, sempre num conjunto de teste real que nem o gerador nem o estimador viram.**
  Proposto pelo autor humano (reduzir dados, aplicar o framework, comparar com o total) e refinado:
  divisão por viagem/veículo/bloco de tempo (não por linha), várias sementes com intervalo de
  confiança, linhas de base de aumento simples (ruído, time-warping, simulação só física), teste de
  extrapolação de cenário (ex.: sem rodovia no treino) e leave-one-vehicle-out. Rejeitado: comparar
  com o dataset total incluindo a fração de treino (vazamento, resultado otimista).

### d-0006 — first committed 2026-09-30T22:09:39-03:00 (commit 64eede990c76)

- **[#d-0006]** date: 2026-09-30 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **Relatar no artigo o resultado negativo do TimeGAN como achado, não omiti-lo.**
  A validação pré-registrada (d-0005) mostrou que o sintético não ajudou e piorou a vazão; omitir seria
  viés de publicação. Alternativa (testar outros geradores até um "funcionar") só vale se reportada como
  busca, com todos os resultados. O resultado reforça o papel do portão de fidelidade e muda a narrativa:
  o pipeline detecta quando o sintético não serve.

### d-0007 — first committed 2026-10-01T01:04:10-03:00 (commit 85e927861119)

- **[#d-0007]** date: 2026-10-01 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **Rodada 3: buscar dados sintéticos de boa qualidade com (i) camada contra artefatos de medição em todos os geradores (desquantização no treino, quantização na resolução do sensor e emulação de sample-and-hold) e (ii) geradores alternativos (DDPM 1D, VAR(3), bootstrap de blocos como referência), triados na validação e testados na grade completa.**
  Motivo: o sinal real é quantizado (velocidade 1 km/h, borboleta 100/255 %, 46 % e 34 % de repetições) e
  o sintético era contínuo; a literatura (TSGBench; Diffusion-TS; Theis et al. 2016) e o histórico (TimeGAN
  e VAE recorrente falharam) apontam nessa direção. Teste de fumaça no servidor (VAR, 1 semente): a camada
  igualou as repetições mas a distinguibilidade quase não mudou (0,486 → 0,481; desquantizada 0,482 vs 0,184
  real) — indício de que a dinâmica, e não só a quantização, difere. Critério de sucesso fixado antes:
  discr_gen ≤ discr_real + 0,05 e utilidade ≥ só-real. Alternativas seguintes já mapeadas em
  `literature/notes/synthetic_quality_strategies.md` (condicional na velocidade; rótulo físico de vazão).

### d-0008 — first committed 2026-10-01T04:25:43-03:00 (commit 8e86f296b611)

- **[#d-0008]** date: 2026-10-01 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **Rodada 4: concentrar no DDPM (melhor fidelidade no J006) com "hold" só nas entradas (não no alvo), mais treino (50k) e rede maior (128), triado na validação com restrição de utilidade (Δ ≤ 0,05) e testado na grade completa (J008–J009).**
  Motivo: J006 mostrou DDPM 20k com camada discr 0,329 (perto do bootstrap real 0,307), mas utilidade pior
  pelo hold no alvo. Alternativas ainda mapeadas: condicional na velocidade; rótulo físico de vazão.

### d-0009 — first committed 2026-10-01T08:38:12-03:00 (commit d8f4f900fdd5)

- **[#d-0009]** date: 2026-10-01 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **Rodada 5 (aceita pelo usuário em 01/10): DDPM v2 no estilo Diffusion-TS (x0, cosseno, EMA, Fourier, DDIM, checkpoint escolhido por discr num subconjunto reservado do treino), geração condicional na velocidade real por inpainting, rótulo físico de vazão + resíduo (variantes genphys_*), e métrica de referência do bootstrap real (discr_boot_ref).**
  Motivo: J007 mostrou que o DDPM (sem camada) é o único gerador com utilidade (1 % e 2 %, 10/10 sementes),
  mas a fidelidade (desquant. 0,31–0,34) segue acima da meta 0,195 — que nem o bootstrap real (0,307) atinge.
  A meta registrada não muda; discr_boot_ref passa a ser reportado ao lado como teto prático.

### d-0010 — first committed 2026-10-01T09:30:42-03:00 (commit d64dd0851b8c)

- **[#d-0010]** date: 2026-10-01 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **Pré-registro do julgamento do J009 e jobs seguintes (registrado às 09:3x de 01/10, ANTES de o J009 terminar; o servidor ainda não tinha nenhum arquivo do J009): desfecho principal = variante gen_rfill_w0.3 (escolhida pelo J007, concluído antes). Utilidade numa fração = média de flow_MAE nas 5 sementes menor que o só-real, com no máximo 1/5 sementes pior. Fidelidade numa fração = success_fidelity em ≥ 4/5 sementes (reportar também média ± dp do discr e do limite). Objetivo atingido = utilidade E fidelidade na MESMA fração. As demais variantes (inclusive genphys_*) são secundárias/exploratórias e não decidem o objetivo.**
  Motivo: parciais do desktop mostraram ganhos por semente escolhendo a melhor entre ~20 variantes (viés de
  seleção) e um limite de fidelidade que oscila entre sementes (real-treino×teste 0,13–0,23).

### d-0011 — first committed 2026-10-01T15:42:35-03:00 (commit 48213f39471f)

- **[#d-0011]** date: 2026-10-01 · status: accepted · author: janeri (aprovado pelo usuário na conversa, antes do J011) · promoted_by: janeri on 2026-10-06
  **Pré-registro da meta de fidelidade revisada, válida a partir do J011 (inclusive; o J011 ainda não começou no momento deste commit — o desktop roda o J010, só de validação): FIDELIDADE PRINCIPAL = "na mesma distribuição": discr(sintético, janelas de viagens do treino FORA da fração) ≤ discr(fração real, essas mesmas janelas) + 0,05 (success_fidelity_id), em ≥ 4/5 sementes. COMPLEMENTAR = discr_id_gen ≤ discr_id_boot (tão realista quanto dados reais recombinados). A meta original (vs teste, success_fidelity) continua reportada como "generalização para outros tanques". Utilidade e desfecho principal (gen_rfill_w0.3) inalterados (d-0010). Objetivo = utilidade E fidelidade principal na mesma fração.**
  Motivo: a meta vs teste mistura qualidade do gerador com a mudança de distribuição entre tanques (real-treino×teste
  0,13–0,23, oscila entre sementes) e nem dados reais recombinados a cumprem (bootstrap 0,27–0,46 no J009).
  A métrica nova não é mais branda: no teste de fumaça, real×real na mesma distribuição deu 0,094 (vs 0,139 contra o
  teste). J001–J010 não têm essa métrica; o J009 fica como evidência exploratória (só a métrica antiga e o bootstrap).

### d-0012 — first committed 2026-10-01T18:26:22-03:00 (commit 4b6cb3dd34b0)

- **[#d-0012]** date: 2026-10-01 · status: accepted · author: janeri · promoted_by: janeri on 2026-10-06
  **J012: repetir no teste a melhor configuração (DDPM v1 50k h128, dequant + quant; J009_A) com o run3.py que mede a fidelidade na mesma distribuição (d-0011). Desfecho pré-registrado antes de rodar: o mesmo de d-0010/d-0011.**
  Motivo: o J009 rodou antes da métrica nova; esta configuração teve a melhor fidelidade (discr 0,25–0,37 vs teste,
  abaixo do bootstrap real) e utilidade em 1/2/5 %. Mantém o GPU ocupado após o J011.

### d-0013 — first committed 2026-10-01T19:20:07-03:00 (commit 4cad8f00c7f5)

- **[#d-0013]** date: 2026-10-01 · status: accepted · author: janeri (aprovado pelo usuário na conversa) · promoted_by: janeri on 2026-10-06
  **J013: replicação em outro veículo — Itabira-MG, veículo 2 (CC0; 253 viagens, ~1 Hz), mesma tarefa (velocidade, RPM, borboleta → vazão cc/min) e MESMA configuração do J012 (DDPM v1 50k h128, dequant + quant), sem reajuste; viagens em 22 blocos cronológicos para manter a divisão (treino 8–17, teste 18–22); resolução do sensor medida nos dados (--res-auto). Desfecho pré-registrado: o mesmo de d-0010/d-0011.**
  Limitações conhecidas antes de rodar: sem litros da bomba (só flow_MAE); mudança de regime no alvo a partir de
  12/04/2022 (vazão média sobe de ~41–68 para ~70–97 cc/min na mesma faixa de velocidade; provável troca para etanol,
  só registrada no bloco 16 — 70 %), que torna treino (8–17) e teste (18–22) diferentes e afeta todas as condições.
  No teste de fumaça (VAR, 1 semente), o teto com 100 % real (25,4) foi pior que 5 % real (24,6), sinal dessa mudança.

### d-0014 — first committed 2026-10-01T19:47:26-03:00 (commit 6e0ea834704d)

- **[#d-0014]** date: 2026-10-01 · status: accepted · author: janeri (aprovado pelo usuário; propostas da sessão do desktop) · promoted_by: janeri on 2026-10-06
  **Pré-registro (antes de rodar J012 e J014–J019; o desktop roda o J011): (a) EMENDA ao J012 — sementes novas 5–9 (replicação com sementes nunca vistas) e meta d-0011; (b) hipóteses: H1 = gen_rfill_w0.3 melhora sobre só-real (desfecho principal, regra d-0010); H2 = genphys_rfill_w0.3 melhora sobre só-real (mesma regra), secundária, com correção de Holm entre H1 e H2 nos testes pareados; (c) controles: J014 bootstrap e J018 VAR como geradores — comparação pareada por semente do gen_rfill_w0.3 do DDPM (J009_A, sementes 0–4) contra o do controle; o argumento a favor da IA generativa só se sustenta se o DDPM for melhor que o bootstrap; (d) J015 validação cruzada por blocos de tanques (testes 8–12 e 13–17), sucesso = mesma direção do efeito H1 nas frações 1 % e 2 %; (e) J016 curva ampliada (0,03/0,2/0,3); (f) J017 cenário ausente: medida = flow_MAE_hw; sucesso = gen_rfill_w0.3 com flow_MAE_hw menor que só-real (sem rodovia) em ≥4/5 sementes; (g) J019 MLP: mesma regra d-0010, comparando também com o HGB só-real.**
  Motivo: lacunas que um revisor apontaria (controle por recombinação real, sementes novas, dependência de um único teste,
  cenário ausente, classe de modelo), propostas pela sessão do desktop e aceitas.

### d-0015 — first committed 2026-10-01T20:08:40-03:00 (commit df4b15937960)

- **[#d-0015]** date: 2026-10-01 · status: accepted · author: janeri (aprovado pelo usuário: "testes em outros datasets, como de bateria") · promoted_by: janeri on 2026-10-06
  **Caso B (bateria) como replicação do pipeline em outro domínio — J020–J022, pré-registrado antes de rodar.** Dados: LG 18650HG2
  (Kollmeyer et al., McMaster; Mendeley doi:10.17632/cp3473x7xv.3, CC BY 4.0), 70 ciclos de condução (UDDS, HWFET, LA92, US06,
  Mixed1–8; faltam Mixed3 a 0 e 10 °C) em 6 temperaturas, reamostrados a 1 Hz; SOC por contagem de carga do equipamento
  (1 + Ah/3,0). Tarefa: sensor virtual de SOC a partir de corrente, tensão e temperatura (janela de 24 s, mesmas features e
  modelo HGB do caso A). Treino UDDS–Mixed4 (1–8), teste Mixed5–8 (9–12); frações sorteadas em trechos de 10 min (552 no treino).
  Gerador: MESMA configuração do caso A (DDPM v1 50k h128, dequant+quant com resolução medida), sem reajuste.
  Desfechos: H1 = gen_rfill_w0.3 vs só-real (regra d-0010). Fidelidade principal na bateria = success_fidelity_id_dyn (≥4/5
  sementes), porque a métrica d-0011 degenera: no teste de fumaça, até real × real reservado foi separado a ~97 %
  (discr_id_real 0,47) pelo nível de SOC/temperatura de cada trecho; d-0011 continua reportada. H2 = genphys_rfill_w0.3 melhor
  que só-real E que o controle physonly (modelo físico+resíduo usado direto, sem sintético) — só assim o sintético agrega além
  da física. Controles: J021 bootstrap como gerador; J022 cenário ausente (sem <5 °C), medida = erro nos trechos frios.
  Novas medidas para TODOS os jobs a partir daqui (inclusive J012 do caso A): physonly e discr_id_dyn_* (janela menos a média).
  Teste de fumaça (servidor, VAR/bootstrap, semente 0, 1 %; não é resultado): só-real 12,1 % de SOC; physonly 4,4 %;
  teto 100 % real 1,43 %; no Opel, physonly 3,08 vs só-real 2,98 (o modelo físico sozinho não ajuda no caso A).

### d-0016 — first committed 2026-10-02T05:31:39-03:00 (commit 3b3c7950aa5e)

- **[#d-0016]** date: 2026-10-02 · status: accepted · author: janeri (correção de desenho; sessão do servidor) · promoted_by: janeri on 2026-10-06
  **Emenda ao d-0015 antes de existir desfecho do caso B: a auditoria física da bateria passa a avaliar contagem de carga e
  temperatura na JANELA de 24 s, e J020 é refeito como J020b.** O J020 original (desktop, 02/10 04:0x) teve audit_pass = 0:
  os níveis por passo de 1 s exigiam |ΔSOC − I·Δt/3600/3| ≤ 0,00037 e |ΔT| ≤ 0,137 °C a cada segundo (q99,9 dos dados
  reais, que não têm ruído de gerador); num DDPM curto no servidor passaram 1,1 % e 5,1 %. Nova regra: |ΔSOC na janela −
  carga acumulada| ≤ máx(q99,9 real, 0,01) e |T_fim − T_início| ≤ máx(q99,9 real, 1 °C). Os pisos (1 ponto de SOC, 1 °C em
  24 s) são de plausibilidade física, escolhidos SEM ver nenhum desfecho (o J020 não calculou gen_* nem genphys_*). Teste de
  fumaça (DDPM 3k, semente 0, 5 %): passam 67 % do sintético e 96 % do real. Desfechos e regras de d-0015 inalterados.
  J021/J022 já usam o código corrigido (o desktop rebaixa o run3.py a cada job). Novos campos: audit_tiers, audit_pass_real.

### d-0017 — first committed 2026-10-02T12:38:39-03:00 (commit 545dfd7c8b80)

- **[#d-0017]** date: 2026-10-02 · status: accepted · author: janeri (pedido do usuário: "cenário juntando genai e físico") · promoted_by: janeri on 2026-10-06
  **Pré-registro (antes de rodar J023–J025): híbridos física + IA generativa, com o mesmo DDPM (v1 50k h128, dequant + quant).**
  Parte física = a mesma do physonly (regressão nos termos físicos, ajustada só no real da fração). Variantes:
  hyb_resid_w0.3 = física + resíduo (HGB, 200 iterações, como no physonly) treinado em real + sintético (peso 0,3);
  hyb_feat_w0.3 = modelo de dados (HGB 300) com a previsão física como variável extra, treinado em real + sintético;
  hyb_feat_real = o mesmo só com real (controle). Hipóteses, regra d-0010 (média menor e ≤ 1/5 sementes pior), por fração:
  H3 (principal) hyb_resid_w0.3 melhor que physonly — a IA generativa agrega ao modelo físico;
  H4 hyb_feat_w0.3 melhor que hyb_feat_real; H5 o melhor híbrido pré-registrado (H3 ou H4) melhor que só-real E que
  gen_rfill_w0.3. Holm entre H3 e H4 nos testes pareados. Casos: J023 bateria (sementes 0–4), J024 Opel (sementes NOVAS
  10–14), J025 Itabira (0–4). Fidelidade não muda (o gerador é o mesmo); os híbridos testam UTILIDADE.
  Motivo: no caso B o physonly vence o DDPM em 20/20 e o DDPM vence o só-real; no caso A o physonly não ajuda mas o
  genphys sim. Teste de fumaça (geradores baratos, 1 semente; não é resultado): bateria VAR 5 % — physonly 3,57,
  hyb_resid 5,30, hyb_feat_real 4,40; Opel bootstrap 2 % — real 2,812, physonly 2,833, hyb_resid 2,759.

### d-0018 — first committed 2026-10-02T22:52:11-03:00 (commit 2896894e748d)

- **[#d-0018]** date: 2026-10-02 · status: accepted · author: janeri (propostas P1–P4 aprovadas pelo usuário, no fim da fila) · promoted_by: janeri on 2026-10-06
  **Pré-registro (antes de rodar J026–J031).** Regra de utilidade = d-0010 (média menor, ≤ 1/5 sementes pior), por fração.
  P1 portão de utilidade (J026 Opel, sementes 15–19; J027 bateria, 5–9): em cada viagem da fração, janelas dos últimos 20 %
  = validação interna; tudo (gerador incluído) treina nos 80 % restantes; candidatos real, physonly, gen_rfill_w0.3,
  genphys_rfill_w0.3, hyb_resid_w0.3, hyb_feat_real, hyb_feat_w0.3; escolhido = menor erro na validação interna.
  H6: auto_test_MAE melhor que real (dos mesmos 80 %); H6b (bateria): auto não pior que physonly pela mesma regra;
  reportar o arrependimento (auto − melhor candidato no teste).
  P2 transferência entre carros (J028): DDPM pré-treinado 50k no Opel inteiro (escala do alvo) + ajuste fino 50k na fração do
  Itabira. H7: gen_rfill_w0.3 do J028 melhor que o do J013 (mesmas sementes e frações, sem pré-treino; pareado) E que só-real.
  P3 transferência entre temperaturas (J029 base e J030; frio = −20/−10/0 °C; pré-treino em 10/25/40 °C, ciclos 1–8).
  H8: gen_rfill_w0.3 do J030 melhor que o do J029 (pareado) E que só-real; secundário: hyb_resid do J030 vs physonly.
  P4 (J031): DDPM h256, 100k, Opel, sementes 0–4, frações 1/2/5 %. H9 = objetivo d-0011 (utilidade E fidelidade id ≥ 4/5
  na mesma fração); comparação com J009_A (h128 50k) por semente. Se H9 falhar, a busca de fidelidade é encerrada.
  Teste de fumaça (servidor, DDPM curto, 1 semente; não é resultado): auto escolheu genphys (val 2,443), teste 2,741 vs real
  2,830; transferência Opel→Itabira com 137 283 janelas de fonte; frio com 42 463 janelas de fonte e auditoria 0,52.

### d-0019 — first committed 2026-10-03T12:18:08-03:00 (commit 045de0b39c6a)

- **[#d-0019]** date: 2026-10-03 · status: accepted · author: janeri (pedido do usuário: "testes com BESS ... ver se entra ou não no artigo") · promoted_by: janeri on 2026-10-06
  **Caso C (BESS estacionário) — pré-registro antes de rodar J032–J034.** Dados: BESS em contêiner em operação (Qu, Zenodo
  10.5281/zenodo.20094787, CC BY 4.0), 8 meses (out/2024–mai/2025), 1 cluster de 9 racks com 396 células; séries registradas
  por evento, reamostradas a 5 s com retenção do último valor (tools/convert_bess.py); racks 1, 5 e 9; corrente com carga > 0;
  tensão do rack / 396 (V por célula); temperatura = média de 8 sensores do rack; alvo = SOC estimado pelo BMS (passo de 1 %;
  limitação: o sensor virtual reproduz o BMS, não uma referência de laboratório). Capacidade efetiva estimada nos dados (outubro:
  ≈ 289 Ah, mediana de 78 operações) usada na auditoria (contagem de carga) com limite de corrente = 1,2 × q99,9 do treino
  (o limite de 20 A da célula LG rejeitava 90 % das janelas reais do rack — corrigido antes de qualquer desfecho).
  Divisão temporal: treino meses 1–6, teste meses 7–8. Gerador, frações e variantes iguais ao caso B, sem reajuste.
  Hipóteses (regra d-0010): H1 gen_rfill_w0.3 < só-real; H3 hyb_resid_w0.3 < physonly; H5 melhor híbrido < só-real e < gen;
  controle J033 (bootstrap); J034 portão de utilidade (H6 como em d-0018). Fidelidade principal = dinâmica (como d-0015).
  **Regra de inclusão no artigo (decidida agora):** o caso C entra como terceiro domínio se a preparação for válida (auditoria
  aceita ≥ 90 % das janelas reais e o teto com 100 % real < só-real com 1 %); os resultados são reportados qualquer que seja o
  sinal; uma afirmação positiva só se H1 ou H3 passar. Teste de fumaça (servidor, 1 mês, DDPM curto; não é resultado):
  auditoria real 0,966 / sintético 0,476; só-real 10,14; gen 8,24; physonly 5,39; hyb_resid 5,73 (pontos de SOC). Regressão da
  célula LG com o código novo: idêntica (6,25 / 6,19 / 3,57). Conversão completa no servidor (03/10 13:4x): 2 263 981 linhas,
  1332 operações-rack, capacidade efetiva 288,3 Ah (1174 estimativas), sha256 3732315b…; temperatura média 25,8–26,6 °C
  em todos os meses (sem estação marcada).

### d-0020 — first committed 2026-10-03T21:37:32-03:00 (commit 8d56523ec01b)

- **[#d-0020]** date: 2026-10-03 · status: accepted · author: janeri (sugestão do desktop, aprovada pelo usuário: "aplique sua sugestão") · promoted_by: janeri on 2026-10-06
  **Caso C2 (BESS) — sensor virtual de temperatura de célula com verdade MEDIDA; pré-registro antes do J035.** Mesmos dados do
  d-0019 (convert_bess.py modo temp): alvo TCELL = sensor 109 do rack; entradas: corrente, tensão por célula e TREF = média de
  7 outros sensores (1, 28, 55, 82, 136, 163, 190). Divisão temporal: treino meses 1–6, teste 7–8. Física = modelo térmico
  concentrado (T_ref + I² com médias de 8/24 passos + I + V) + resíduo; auditoria térmica de 5 níveis (faixas, deriva da célula
  e da referência na janela, dV/dI, |célula − referência|). Hipóteses e regra iguais a d-0019 (H1, H3, H5; regra d-0010);
  fidelidade dinâmica reportada. **Limitação conhecida antes de rodar:** o sensor tem resolução de 1 °C e a célula difere da
  referência em 0,23 ± 0,58 °C; no teste de fumaça (1 mês, 10 %) o teto com 100 % real foi 0,40 °C contra 0,47 só-real —
  pouca margem; o resultado provável é "sem diferença detectável" e o J035 é verificação, não evidência principal.
  Conversão completa no servidor: 2 264 252 linhas, 1332 operações-rack, sha256 7249bace…

### d-0021 — first committed 2026-10-04T06:29:23-03:00 (commit 384ca6e05c7d)

- **[#d-0021]** date: 2026-10-04 · status: accepted · author: janeri (regra pré-registrada em d-0018) · promoted_by: janeri on 2026-10-06
  **Encerrar a busca de fidelidade estatística: o objetivo d-0011 (utilidade E fidelidade id ≥ 4/5 na mesma fração) é declarado
  não alcançado com os geradores testados.** Tentados: TimeGAN (vários ajustes), VAE recorrente, DDPM v1 (6k–100k iterações,
  h64–h256, desquantização/quantização, retenção), DDPM v2 (predição de x0, cosseno, EMA, Fourier, DDIM, escolha de checkpoint,
  condicionamento), VAR, bootstrap, filtro discriminativo, pré-treino em outra fonte. Nenhum ficou a ≤ 0,05 do real reservado
  em nenhuma fração de nenhum caso, por nenhuma das três medidas. O artigo reporta utilidade (comprovada) e fidelidade (não
  atingida) separadamente. A fila continua só com os jobs do BESS (J032b–J034b, J035c); ao terminar, STATUS: STOP e fechamento.

### d-0030 — first committed 2026-10-11T07:46:17-03:00 (commit 35c047178585)

- **[#d-0030]** date: 2026-10-11 · status: accepted · author: janeri (pedido do usuário: "rode os testes/experimentos que faltam") · promoted_by: janeri on 2026-10-11
  **Pré-registro (antes de rodar J036–J040; nenhum resultado existe): completar a Tabela III nos dois alvos de ganho marginal e
  fechar t-0016.** Configuração idêntica à dos jobs originais (DDPM v1 50k h128, dequant + quant; Itabira com --res-auto).
  J036 portão de utilidade no veículo 2 (Itabira; sementes 5–9) e J037 no BESS temperatura (sementes 5–9), candidatos e
  validação interna como d-0018. Hipóteses por fração: H6 = auto_test_MAE < só-real dos mesmos 80 % (regra d-0010);
  **H6s (principal nestes dois alvos) = portão não pior que só-real em ≥ 4/5 sementes** — testa se o portão é seguro onde o
  sintético quase não ajuda; arrependimento reportado. J038 MLP como modelo final, sementes 3–4 (as 0–2 são do J019): com as
  5 sementes, regra d-0010 para MLP+DDPM vs MLP só-real; secundário: MLP+DDPM vs HGB só-real (J009_A, mesmas sementes).
  J039 (Itabira) e J040 (BESS temperatura): bootstrap de blocos como gerador, sementes 0–4; comparação pareada por semente
  com o gen_rfill_w0.3 do DDPM do J013 e do J035c (mesmas sementes e frações). Regra de uso no artigo: tudo é reportado
  qualquer que seja o sinal; linhas "Gate" e "Bootstrap" da Tabela III passam a cobrir os cinco alvos; se H6s falhar em
  algum alvo, o texto deixa de dizer que o portão "never did worse than real-only training".

### d-0032 — first committed 2026-10-11T13:53:40-03:00 (commit 2835d2abc445)

- **[#d-0032]** date: 2026-10-11 · status: proposed · author: janeri (pedido do usuário: "aplique todos ... E")
  **Pré-registro (antes de rodar J041–J043; nenhum resultado existe).** Código: run3.py ganha `--save-windows` (grava 200
  janelas reais, 200 sintéticas aceitas e 100 rejeitadas por semente×fração; não usa rng nem altera cálculos); novo hash
  23303793b8f977e7. J036/J037, ainda não rodados, usarão este run3.py: sem a opção, o comportamento é idêntico ao da versão
  f989a1914e9bf8a8 (d-0030 vale sem mudança).
  J041 (célula) e J042 (BESS SOC): curva longa, frações 0,2/0,3/0,5, sementes 0–4, variantes real, gen_rfill_w0.3, physonly,
  hyb_resid_w0.3, hyb_feat_w0.3. Medida principal: **equivalência de dados** e(f) = fração de dados reais com a qual o
  só-real (interpolado linearmente no erro, em log da fração, entre frações medidas, juntando J020b/J032b) iguala o erro de
  "real + DDPM" na fração f; reportada como fator e(f)/f, sem teste de hipótese. Secundário: regra d-0010 para DDPM vs
  só-real nas frações novas (expectativa declarada: o ganho diminui com mais dados, como no veículo 1/J016).
  J043: exportação de janelas para a figura (5 domínios, semente 0, fração 5 %, variantes real e gen_rfill_w0.3); não é
  evidência quantitativa, só ilustração.

### d-0033 — first committed 2026-10-11T15:45:01-03:00 (commit 2e887647c4ca)

- **[#d-0033]** date: 2026-10-11 · status: proposed · author: janeri (pedido do usuário: expandir BMS e BESS, "faça isso")
  **Pré-registro (antes de rodar J044; nenhum resultado existe): teto justo para os modelos com física.** Com 100 % do pool
  (fração 1,0; semente 0; sem dados sintéticos, porque o preenchimento é zero), treinar real, physonly e hyb_feat_real na
  célula (J044a) e no BESS SOC (J044b). Medida: erro no teste de cada um. Uso no artigo: a Tabela "gap" passa a ter também o
  teto do modelo com física como entrada; a afirmação "a fração de dados de campo, com física e sintético, igualou o modelo
  só de dados com todos os dados" fica; e se hyb_feat_w0.3 com 5–10 % ficar abaixo do hyb_feat_real com 100 %, isso é
  reportado como tal; se ficar acima, o texto diz que a vantagem vem da entrada física e não supera o teto justo.
  Emenda (11/10 16:08, antes de qualquer resultado): o J044 falhou nos dois comandos (rc=1) — com fração 1,0 o pool de aumento
  simples fica vazio e `discr(Wtest, aug_pool)` quebra antes dos modelos (erro de desenho do pré-registro, não testado).
  run3.py corrigido: esse score só é calculado com > 100 janelas (para todos os jobs anteriores nada muda); novo hash
  cdffce07f3c20f45; teste de fumaça no servidor com dados falsos de bateria em fração 1,0 rodou até o fim. Refeito como J044r,
  mesma regra e mesmas variantes.

## Reproducibility notes (not decisions)

- 2026-10-04 — nota de reprodutibilidade (não é decisão): (1) J032–J034 e J035b falharam antes de treinar porque o
  convert_bess.py gravou `timestamp` em dois formatos ISO e o pandas 3 do desktop não converte a mistura; corrigido na leitura do
  run3.py (`format='ISO8601'`), reenfileirados como J032b–J034b e J035c, sem mudar dados nem pré-registro. (2) O arquivo do Opel
  no Kaggle mudou: sha256 atual 0eaadd171ce10bc1… (o conferido em 30/09 era 27e6b070…); o desktop usa a cópia antiga conferida;
  um teste no servidor com a cópia nova reproduziu os mesmos números (bootstrap 2 %, semente 0: 2,812 / 2,804). Citar a versão
  usada (data e hash) no artigo.

- 2026-10-06 — correção do fechamento de 05/10 (não é decisão nova): o texto do artigo e da apresentação sobre o BESS dizia
  "fidelidade 5/5 a 1–5 %" com a medida degenerada e chamava o BESS de "dados de laboratório"; a citação `zenodo_bess_2024`
  tinha título, autor e ano inventados. Corrigido: fidelidade pela medida dinâmica pré-registrada (0/5), BESS descrito como
  dados de campo com SOC do BMS, citação substituída por Qu_2026_bess (metadados do Zenodo/DataCite). A figura de arquitetura
  original do Overleaf, substituída em 05/10 por um diagrama gerado com entradas erradas, foi restaurada; a curva de geradores
  foi refeita a partir dos results.json (tools/fig_curve.py). A seção pública foi reescrita sem TODOs de jobs já concluídos.
