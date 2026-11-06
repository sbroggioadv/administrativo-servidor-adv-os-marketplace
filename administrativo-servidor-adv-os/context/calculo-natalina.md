# Conta aberta de natalina federal

Lei 8.112 arts. 63/65 em A-lei8112.md:1707 e seguintes, redação NÃO-tachada. Definir hipótese: exercício/ dezembro ou exoneração e remuneração daquele mês, sem presumir líquido ou rubrica. Meses de exercício mais fração adicional >=15 dias (somente quando esse mês ainda não estiver contado) formam avos, até 12. Dividir remuneração por 12, multiplicar pelos avos e arredondar Decimal ROUND_HALF_UP somente ao final. Exibir base, avos e cada operação; pagamentos/descontos não informados não são deduzidos. Sem base/exercício comprovados, fórmula/null; zero é valor conhecido, não dado ausente. Script não decide direito a rubrica nem conta períodos de afastamento juridicamente controvertidos. Conta sem script deve avisar número não conferido por script. Testes aguardam conferência do Doc.

## Fórmula com a fonte de cada termo

- `avos = meses de exercício no ano + 1, se houver fração adicional igual ou superior a 15 dias em mês ainda não contado` — Lei 8.112, art. 63, parágrafo único (`context/A-lei8112.md:1711–1712`); máximo de 12.
- `natalina bruta = base ÷ 12 × avos`, arredondada só ao final, em centavos, Decimal ROUND_HALF_UP — art. 63, caput (`context/A-lei8112.md:1707–1709`): base é a remuneração de dezembro na hipótese de exercício; na exoneração, a do mês da exoneração (art. 65), sempre a da hipótese confirmada.

## Tabela de passos (preencher)

| # | Operação | Valor | Fonte |
|---|---|---|---|
| 1 | Base da hipótese confirmada | R$ … | documento do caso + art. 63, caput |
| 2 | Meses integrais de exercício | … | ficha funcional |
| 3 | Fração adicional ≥ 15 dias? | sim/não | art. 63, parágrafo único |
| 4 | Avos = linha 2 + (1 se linha 3 = sim) | … | art. 63, parágrafo único |
| 5 | Base ÷ 12 | R$ … | art. 63, caput |
| 6 | Linha 5 × avos, arredondada ao final | R$ … | art. 63, caput |

## Caso de referência resolvido à mão (dados inventados; aguarda conferência do Doc)

Base confirmada de R$ 3.600,00; cinco meses integrais e uma fração adicional de 15 dias em outro mês. Avos: 5 + 1 = 6. R$ 3.600,00 ÷ 12 = R$ 300,00. R$ 300,00 × 6 = **R$ 1.800,00 brutos**. Nenhum pagamento ou desconto foi informado, e nenhum foi deduzido. É o mesmo caso do teste `tests/golden/h07-natalina-fracao.json`; se este método mudar, o teste muda junto.

**Aviso fixo:** sem o script, escrever na entrega que o número não foi conferido por script.
