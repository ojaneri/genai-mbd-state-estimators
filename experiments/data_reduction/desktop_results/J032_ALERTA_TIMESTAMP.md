# ALERTA — J032/J033 (e, previsivelmente, J034 e J035b) falham ao ler as datas do dataset BESS (nota do operador do desktop, 04/10/2026 05:40)

**Sintoma:** `run3.py` termina com rc=1 em ~40 s, antes de qualquer treino, na linha 82:
`df['dt'] = df.groupby('segment_file').timestamp.diff()...` → `TypeError: unsupported operand type(s) for -: 'str' and 'str'`.

**Causa (verificada):** a coluna `timestamp` de `../data_bess/dataset.csv` (hash 3732315b…, **igual ao esperado**) mistura dois formatos:
- 2 121 131 linhas no formato `2024-10-05 10:30:00` (19 caracteres);
- 142 850 linhas no formato `2024-11-17 04:45:35.000000000` (29 caracteres), em 101 segment_file (ex.: `202411_Operation32_R1`).
Com formatos mistos, `pd.read_csv(..., parse_dates=['timestamp'])` (pandas 3.0.6 neste desktop) não converte a coluna e a deixa como texto;
o `diff()` então falha. O `../data_besstemp` do J035b tem a mesma mistura (mesmo conversor), então o J035b deve falhar igual.
Teste: `pd.to_datetime(col, format='ISO8601')` converte as duas formas sem erro.

**O que o desktop fez:** nada no código nem nos dados (regra do DESKTOP-LOOP). O driver marcou J032/J033 como falhos e segue a fila;
J034 e J035b devem falhar igual em ~1 min cada. Os dados (`../data_bess`, `../data_besstemp`) e os 8 `.mat` continuam no desktop.

**Sugestão para o servidor (decisão de vocês):** (a) no `convert_bess.py`, gravar o timestamp num formato único
(p.ex. `d['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')`), ou (b) no `run3.py`, ler com `pd.to_datetime(..., format='ISO8601')`/`'mixed'`.
Com (a), o hash esperado muda; com (b), os dados atuais servem como estão. Em seguida, J032b–J035c na fila.
