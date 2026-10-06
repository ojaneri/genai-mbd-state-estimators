# REPRODUCE — exact command of every job

Commands copied verbatim from the job queue that drove the experiments (comments in Portuguese kept; lines with server
addresses removed). Run from `experiments/data_reduction/` with the converted datasets in `../data*` (see README).
Each job wrote `out/<name>/results.json`, archived here under `desktop_results/<job>/`.


## J001 — TimeGAN, grade completa (variantes de proporção/peso/filtro/pré-treino), frações escassas
    python -u run2.py ../data out/J001 --gen timegan --iters 6000 --hidden 24 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J002 — TimeVAE, ajuste na VALIDAÇÃO (latent x iters), semente 0, fração 0.05
    python -u run2.py ../data out/J002_l8_i2000 --val --gen timevae --latent 8 --iters 2000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run2.py ../data out/J002_l8_i5000 --val --gen timevae --latent 8 --iters 5000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run2.py ../data out/J002_l16_i2000 --val --gen timevae --latent 16 --iters 2000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run2.py ../data out/J002_l16_i5000 --val --gen timevae --latent 16 --iters 5000 --seeds 0 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1

## J003 — TimeVAE, grade completa no TESTE com a configuração escolhida no J002
    python -u run2.py ../data out/J003 --gen timevae --latent L --iters I --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J004 — Rede neural (MLP) como modelo final, gerador TimeGAN (h24, 6000 it), 3 sementes
    python -u run2.py ../data out/J004 --gen timegan --iters 6000 --hidden 24 --model mlp --seeds 0,1,2 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_r1_w1,gen_r1_w0.3,gen_rfill_w1,gen_dfilt_q0.2,gen_pretrain,aug_r1_w1

## J005 — Refaz no TimeGAN as variantes com defeito no J001 (filtro estatístico e pré-treino), código corrigido em 01/10 00:3x
    python -u run2.py ../data out/J005 --gen timegan --iters 6000 --hidden 24 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --no-ceiling --variants real,gen_dfilt_q0.5,gen_dfilt_q0.2,gen_pretrain

## J006 — Rodada 3: triagem de geradores com camada contra artefatos (desquantização + quantização + sample-and-hold), VALIDAÇÃO 15–17
    python -u run3.py ../data out/J006_timegan --val --gen timegan --iters 6000 --hidden 24 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run3.py ../data out/J006_timevae --val --gen timevae --latent 16 --iters 3000 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run3.py ../data out/J006_ddpm6k --val --gen ddpm --iters 6000 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run3.py ../data out/J006_ddpm20k --val --gen ddpm --iters 20000 --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run3.py ../data out/J006_ddpm20k_raw --val --gen ddpm --iters 20000 --post none --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run3.py ../data out/J006_var --val --gen var --dequant --post quanthold --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1
    python -u run3.py ../data out/J006_bootstrap --val --gen bootstrap --post none --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1

## J007 — Rodada 3: grade completa no TESTE com os 2 geradores escolhidos no J006 (mesmos argumentos, sem --val)
    python -u run3.py ../data out/J007_A <argumentos do 1º escolhido, sem --val> --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1
    python -u run3.py ../data out/J007_B <argumentos do 2º escolhido, sem --val> --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J008 — Rodada 4: variações do DDPM (hold só nas entradas, mais treino, rede maior), VALIDAÇÃO 15–17
    python -u run3.py ../data out/J008_q20k --val --gen ddpm --iters 20000 --dequant --post quant --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1
    python -u run3.py ../data out/J008_qhin20k --val --gen ddpm --iters 20000 --dequant --post quantholdin --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1
    python -u run3.py ../data out/J008_qhin50k --val --gen ddpm --iters 50000 --dequant --post quantholdin --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1
    python -u run3.py ../data out/J008_qhin50k_h128 --val --gen ddpm --iters 50000 --hidden 128 --dequant --post quantholdin --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1
    python -u run3.py ../data out/J008_q50k_h128 --val --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1
    python -u run3.py ../data out/J008_raw50k_h128 --val --gen ddpm --iters 50000 --hidden 128 --post none --seeds 0,1 --fracs 0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_r0.5_w1

## J009 — Rodada 4: grade completa no TESTE com os 2 escolhidos no J008 (mesmos argumentos, sem --val)
    python -u run3.py ../data out/J009_A <argumentos do 1º escolhido, sem --val> --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1
    python -u run3.py ../data out/J009_B <argumentos do 2º escolhido, sem --val> --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J010 — Rodada 5: DDPM v2 (predição de x0, cosseno, EMA, Fourier, DDIM, checkpoint por fidelidade no treino),

## condicionamento na velocidade real (inpainting) e rótulo físico de vazão + resíduo (variantes genphys_*). VALIDAÇÃO 15–17.
    python -u run3.py ../data out/J010_v1_20k_raw --val --gen ddpm --iters 20000 --post none --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3
    python -u run3.py ../data out/J010_v2_raw --val --gen ddpm2 --iters 30000 --post none --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3
    python -u run3.py ../data out/J010_v2_quant --val --gen ddpm2 --iters 30000 --dequant --post quant --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3
    python -u run3.py ../data out/J010_v2_cond --val --gen ddpm2 --iters 30000 --cond-speed --post none --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3
    python -u run3.py ../data out/J010_v2_cond_quant --val --gen ddpm2 --iters 30000 --cond-speed --dequant --post quant --seeds 0,1 --fracs 0.02,0.05 --no-ceiling --variants real,gen_r1_w1,gen_rfill_w1,gen_rfill_w0.3,genphys_r1_w1,genphys_rfill_w1,genphys_rfill_w0.3

## J011 — Rodada 5: grade completa no TESTE com os 2 escolhidos no J010 (mesmos argumentos, sem --val)
    python -u run3.py ../data out/J011_A <argumentos do 1º escolhido, sem --val> --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1
    python -u run3.py ../data out/J011_B <argumentos do 2º escolhido, sem --val> --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J012 — Rodada 6: a melhor configuração até agora (J009_A: DDPM v1 50k h128, dequant + quant) medida pela meta

## pré-registrada d-0011 (fidelidade na mesma distribuição), no TESTE. Mesmo comando do J009_A com o run3.py atual.
    python -u run3.py ../data out/J012 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1

## J013 — Rodada 6: REPLICAÇÃO em outro veículo (Itabira-MG, veículo 2; Kaggle brunops2, CC0), mesma configuração do J012, sem reajuste
    mkdir -p ../data_itabira_raw ../data_itabira && cd ../data_itabira_raw
    curl -L -o i.zip https://www.kaggle.com/api/v1/datasets/download/brunops2/obd-2-vehicular-dataset-trace && unzip -o i.zip
    sha256sum Dataset.csv   # esperado: começa com 5d0ced594efcd95e
    cd ../code && python convert_itabira.py ../data_itabira_raw/Dataset.csv ../data_itabira
    sha256sum ../data_itabira/dataset.csv   # esperado: b5a91d90cc2557ce745b5675048f1a0357ef840a2ae4d2fb6620cf0c0c6d391f — se diferir, PARE e avise
    python -u run3.py ../data_itabira out/J013 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --res-auto --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J020 — CASO B (bateria) — replicação do pipeline em OUTRO DOMÍNIO: sensor virtual de SOC numa célula LG 18650HG2
    cd ../code && python convert_lghg2.py ../data_lghg2_raw ../data_lghg2
    sha256sum ../data_lghg2/dataset.csv   # esperado: 2fd898df640fd93d410ea4774708a7ee81f8ac8392e72d90315a7db910e5228b — se diferir, PARE e avise
    python -u run3.py ../data_lghg2 out/J020 --domain battery --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly

## J020b — Caso B: REFAZ o J020 com a auditoria corrigida (d-0016). O J020 original rejeitou 100 % do sintético (alerta do
    python -u run3.py ../data_lghg2 out/J020b --domain battery --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly

## J021 — Caso B, controle: bootstrap de dados reais como gerador (mesma pergunta do J014, outro domínio)
    python -u run3.py ../data_lghg2 out/J021_boot --domain battery --gen bootstrap --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly

## J022 — Caso B, cenário ausente: sem frio (<5 °C) no treino real e no gerador; medida = erro só nos trechos frios do teste (flow_MAE_hw)
    python -u run3.py ../data_lghg2 out/J022_cold --domain battery --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --hw-absent --seeds 0,1,2,3,4 --fracs 0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3,physonly

## J014 — Controle: bootstrap de dados reais COMO GERADOR no teste (o ganho vem do modelo generativo ou de "mais janelas parecidas"?) — proposto pelo desktop
    python -u run3.py ../data out/J014_boot --gen bootstrap --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J023 — HÍBRIDO física + IA generativa (d-0017), caso B (bateria): o sintético do DDPM treina o RESÍDUO do modelo físico
    python -u run3.py ../data_lghg2 out/J023_bat --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J024 — HÍBRIDO, caso A (Opel), sementes NOVAS 10–14
    python -u run3.py ../data out/J024_opel --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 10,11,12,13,14 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J025 — HÍBRIDO, caso A' (Itabira, veículo 2)
    python -u run3.py ../data_itabira out/J025_ita --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --res-auto --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J015 — Validação cruzada por blocos de tanques (o efeito não depende de um único teste); DDPM do J009_A, 3 sementes
    python -u run3.py ../data out/J015_f1 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --test-segs 8-12 --pool-segs 13-22 --seeds 0,1,2 --fracs 0.01,0.02,0.05
    python -u run3.py ../data out/J015_f2 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --test-segs 13-17 --pool-segs 8-12,18-22 --seeds 0,1,2 --fracs 0.01,0.02,0.05

## J016 — Curva de aprendizado ampliada (onde o ganho some; "quanto dado real o sintético vale") — proposto pelo desktop
    python -u run3.py ../data out/J016_curva --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.03,0.2,0.3 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3

## J017 — Cenário ausente (sem rodovia >80 km/h no treino real e no gerador); medida principal: flow_MAE_hw (só rodovia)
    python -u run3.py ../data out/J017_hw --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --hw-absent --seeds 0,1,2,3,4 --fracs 0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3

## J018 — Baseline estatístico clássico: VAR(3) como gerador no teste — proposto pelo desktop
    python -u run3.py ../data out/J018_var --gen var --post none --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1

## J019 — Outra classe de modelo final: MLP com o DDPM do J009_A (3 sementes) — proposto pelo desktop
    python -u run3.py ../data out/J019_mlp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --model mlp --seeds 0,1,2 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,gen_rfill_w1,genphys_rfill_w0.3,aug_rfill_w0.3

## J026 — P1 PORTÃO DE UTILIDADE (d-0018), caso A (Opel): o método é escolhido sozinho pela validação interna (últimos 20 % de
    python -u run3.py ../data out/J026_auto_opel --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --auto-select --seeds 15,16,17,18,19 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3

## J027 — P1 PORTÃO DE UTILIDADE, caso B (bateria); sementes 5–9
    python -u run3.py ../data_lghg2 out/J027_auto_bat --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --auto-select --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3

## J028 — P2 TRANSFERÊNCIA entre carros: DDPM pré-treinado no Opel inteiro (../data) e ajustado na fração do Itabira; compara com J013
    python -u run3.py ../data_itabira out/J028_transf_ita --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --res-auto --pretrain-src ../data --pretrain-iters 50000 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,aug_rfill_w0.3

## J029 — P3 base: bateria SÓ COM FRIO (−20, −10, 0 °C), sem pré-treino
    python -u run3.py ../data_lghg2 out/J029_frio_base --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --temps n20degC,n10degC,0degC --seeds 0,1,2,3,4 --fracs 0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3

## J030 — P3 TRANSFERÊNCIA entre temperaturas: igual ao J029, com o gerador pré-treinado em 10/25/40 °C (ciclos de treino)
    python -u run3.py ../data_lghg2 out/J030_frio_transf --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --temps n20degC,n10degC,0degC --pretrain-temps 10degC,25degC,40degC --pretrain-iters 50000 --seeds 0,1,2,3,4 --fracs 0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3

## J031 — P4 DDPM MAIOR (h256, 100k iterações), caso A (Opel): última tentativa de fidelidade
    python -u run3.py ../data out/J031_ddpm_big --gen ddpm --iters 100000 --hidden 256 --dequant --post quant --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05 --variants real,gen_rfill_w0.3,genphys_rfill_w0.3

## J032 — CASO C (BESS estacionário em contêiner; Qu, Zenodo 10.5281/zenodo.20094787, CC BY 4.0) — d-0019: sensor virtual do
    mkdir ../data_bess_raw ../data_bess
    para M em 202410 202411 202412 202501 202502 202503 202504 202505:
    cd ../code && python convert_bess.py ../data_bess_raw ../data_bess 5
    sha256 de ../data_bess/dataset.csv SEM os \r (como no J013/J020): esperado 3732315bcd763c819a5d298221a46d0718dc163bd474abe316ce6208f80c6a66
    python -u run3.py ../data_bess out/J032_bess --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --test-segs 7-8 --pool-segs 1-6 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J033 — Caso C, controle: bootstrap de dados reais como gerador
    python -u run3.py ../data_bess out/J033_bess_boot --gen bootstrap --post none --domain battery --test-segs 7-8 --pool-segs 1-6 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3

## J034 — Caso C, portão de utilidade (escolha automática pela validação interna); sementes 5–9
    python -u run3.py ../data_bess out/J034_bess_auto --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --test-segs 7-8 --pool-segs 1-6 --auto-select --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3

## J035 — CASO C2 (BESS): sensor virtual de TEMPERATURA de célula (verdade medida) — d-0020; sugestão do desktop
    cd ../code && python convert_bess.py ../data_bess_raw ../data_bess_temp 5 temp
    sha256 (sem \r) esperado 7249bace12866f6f460e5553a229c9e18f061d15ca87e680cd709b613573b38e; se diferir, confira 2 264 252 linhas,
    python -u run3.py ../data_bess_temp out/J035_bess_temp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J035b — REFAZ o J035 (rejeitado pelo driver do desktop: "comando fora do padrão permitido", provável sublinhado duplo em
    cd ../code && python convert_bess.py ../data_bess_raw ../data_besstemp 5 temp   (hash esperado: ver J035)
    python -u run3.py ../data_besstemp out/J035b_besstemp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J032b — REFAZ J032 (falhou rc=1: coluna timestamp do BESS com dois formatos ISO; pandas 3 não convertia — alerta do desktop
    python -u run3.py ../data_bess out/J032b_bess --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --test-segs 7-8 --pool-segs 1-6 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3

## J033b — REFAZ J033 (mesma causa)
    python -u run3.py ../data_bess out/J033b_bessboot --gen bootstrap --post none --domain battery --test-segs 7-8 --pool-segs 1-6 --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,hyb_resid_w0.3

## J034b — REFAZ J034 (mesma causa)
    python -u run3.py ../data_bess out/J034b_bessauto --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain battery --test-segs 7-8 --pool-segs 1-6 --auto-select --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3

## J035c — REFAZ J035b (mesma causa)
    python -u run3.py ../data_besstemp out/J035c_besstemp --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --domain bess_temp --seeds 0,1,2,3,4 --fracs 0.01,0.02,0.05,0.1 --variants real,gen_rfill_w0.3,physonly,genphys_rfill_w0.3,hyb_resid_w0.3,hyb_feat_real,hyb_feat_w0.3,aug_rfill_w0.3
