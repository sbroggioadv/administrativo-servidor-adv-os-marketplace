# Conta aberta de prazo

H01: Lei 9.784 arts. 59/66/67/69. H02: Lei 8.112 arts. 13/15/108/161/163/238. H04: CPC arts. 219/220/224/231. Buscar artigo no MD da lei e abrir inteiro. Primeiro selecionar regime, quantidade e marco juridicamente correto; excluir começo. Geral/estatutário: dias contínuos; processual CPC: somente úteis, com suspensão legal 20/12–20/01. Calcular dia a dia, expor incluídos/excluídos, depois conferir ausência de expediente final e prorrogação cabível. Mês/ano da Lei 9.784: data a data; sem dia equivalente, último do mês, ainda conferir expediente. Calendário completo deve ser confirmado pelo advogado, inclusive finais de semana e atos especiais; não embutir feriados por memória. Scripts não decidem cabimento, marco, pluralidade, prorrogação nem aplicação da lei.

Faltou calendário/marco/método: fórmula, data null e pendência. MS, prescrição PAD, H10/H11 não são este script; manter conta aberta com método pendente. Caso sem script: declarar número não conferido por script. Casos didáticos só regressão, aguardam Doc. Prazo do ente e do particular segue sua fonte e hipótese; script não concede prazo em dobro automaticamente.

Exceção: art. 62 da Lei 9.784 prevê cinco dias úteis para alegações dos demais interessados; não é contagem contínua deste script geral nem processo judicial do CPC. Exige conta aberta própria pela fonte e calendário, sem forçar o regime judicial no parser.

## Fórmula com a fonte de cada termo

| Regime | Regra | Fonte |
|---|---|---|
| H01, Lei 9.784, dias | exclui o dia do começo e inclui o do vencimento; dias contínuos; vencimento sem expediente prorroga ao primeiro dia útil seguinte | art. 66, caput e §§1º–2º (`context/A-lei9784.md:950–960`) |
| H01, Lei 9.784, meses ou anos | data a data; sem dia equivalente, último dia do mês | art. 66, §3º (`context/A-lei9784.md:962–965`) |
| H02, Lei 8.112 | dias corridos; exclui o começo e inclui o vencimento; prorroga se vencer sem expediente | art. 238 (`context/A-lei8112.md:6013–6016`) |
| H04, CPC | só dias úteis; suspensão de 20/12 a 20/01; exclui o começo e inclui o vencimento | arts. 219, 220 e 224 (`context/A-cpc.md:2041, 2045, 2077–2079`) |

## Tabela de passos (preencher, uma linha por dia)

| Data | Dia da contagem ou motivo da exclusão | Fonte |
|---|---|---|
| marco | excluído (dia do começo) | regra do regime |
| … | 1, 2, 3 … ou "sem expediente", "fim de semana", "suspensão" | calendário confirmado |
| vencimento | último dia contado; se sem expediente, prorrogar | regra do regime |

## Caso de referência resolvido à mão (dados inventados; aguarda conferência do Doc)

H01, prazo de 10 dias da Lei 9.784, ciência em 03/08/2026 e calendário confirmado sem dia sem expediente no período: exclui 03/08; contam 04, 05, 06, 07, 08, 09, 10, 11, 12 e 13/08; **vencimento em 13/08/2026**, quinta-feira. É o caso `tests/golden/h01-dias-continuos.json`; se este método mudar, o teste muda junto.

**Aviso fixo:** sem o script, escrever na entrega que a data não foi conferida por script.
