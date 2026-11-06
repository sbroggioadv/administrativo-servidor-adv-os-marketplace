---
name: posse-exercicio-administrativo-servidor
description: "Organiza provimento, posse e exercício no regime federal, pelo candidato/servidor ou pelo ente. Use para prazo, impedimento e regularidade da investidura; não substitui inspeção médica nem resolve regime especial sem fonte."
---

# Posse e exercício

C3. Orientação e minuta para revisão humana, no regime federal e nos eixos aprovados. Uma pasta privada por caso e polo; não representa os dois lados nem reutiliza estratégia da parte adversa.

## Entradas

Polo, cargo/regime, publicação do provimento, termo de posse, ciência, documentos exigidos, eventual licença/afastamento e ato de exercício. Chamada por: administrativo-servidor-master. Chama: prazos-administrativo-servidor e revisao-final-administrativo-servidor.

## Anexos obrigatórios

- `context/metodologia-administrativo-servidor.md`: escopo, polo, fontes, cálculo e revisão.
- `context/escrita-humana.md`: §§2–4 e §§5–8, por busca e faixa.
- `context/A-lei8112.md`: arts. 13–16, linha 220 e seguintes; art. 238 na linha 6013.
- `context/A-cf1988.md`: art. 37 e art. 41 na redação NÃO-tachada.

## Objetivo

Separar marcos de provimento, posse e exercício e preparar a medida do polo correto, sem aplicar redação histórica tachada ou presumir impedimento.

## Metodologia

1. Confirmar polo fixo, regime federal, cargo e estágio em quadro; não confundir direito à nomeação com a comprovação da posse ou exercício. Para ente, confirmar quem tem competência para o ato, sem a ferramenta assumir a autoridade.
2. Ler art. 13 inteiro, incluindo hipóteses do §2º, e art. 15 vigente. Trinta dias para posse contam do ato de provimento; quinze para exercício contam da posse, sob hipóteses legais. A prorrogação histórica de mais trinta dias está tachada e não fundamenta pedido automático.
3. Criar linha do tempo com publicação, impedimento legal documentado, término do impedimento, posse e exercício. Art. 14 exige inspeção oficial; laudo não recebido não é aptidão presumida nem inaptidão confirmada. Exames específicos sem corpus ficam como pendência especializada.
4. PARTICULAR: preparar checklist documental e requerimento/impugnação do ato cabível, usando impedimento somente quando demonstrado. ENTE: auditar os requisitos e marcos, preparar subsídio para receber, corrigir ou decidir situação funcional com motivação, sem declarar ato tornado sem efeito ou exoneração antes da decisão comprovada.
5. Oferecer duas ou três estratégias: completar documentação e requerer processamento, impugnar/defender o ato, ou avaliar urgência judicial. Mostrar consequências de cada marco e aguardar escolha antes da minuta.
6. Encaminhar a contagem H02 à skill prazos com calendário e evento confirmados; não operar calculadora diretamente. Divergência de regime, ato não capturado ou impedimento sem base gera pendência, nunca prazo de memória.
7. Sem quadro e estratégia confirmados, entregar só a consulta/conta pedida, cronologia e pendências; não redigir minuta nem requerimento opcional. A escolha pendente impede minuta e mantém PENDENTE DE PROVA, salvo estado prioritário. Com ambos confirmados, entregar cronologia, matriz de requisitos e minuta/subsídio do polo escolhido; distinguir ação futura de ato consumado e fazer passada anti-IA antes da revisão final.

## Se faltar anexo

Não preencher fato, dispositivo, edital, decisão ou data por memória. Documento do caso ausente gera checklist e PENDENTE DE PROVA; norma, método ou pack material ausente gera PENDENTE DE FONTE, ainda que também falte documento. Pedido principal fora do recorte mantém FORA DO RECORTE; conflito entre polos mantém BLOQUEADO. A ausência de documento não demonstra que o ato não ocorreu.

## Conta aberta

Esta skill não executa script. Toda data-limite ou valor que ela entregar (os marcos de posse e de exercício, H02) sai por conta aberta, nos moldes de `context/calculo-prazos.md`: regra com a fonte de cada termo (arquivo:linha), marco documentado, contagem passo a passo com exclusões e prorrogação, e a frase de que o número não foi conferido por script. Quando a hipótese tiver script (H01, H02, H04 ou H07), encaminhar a conta a `prazos-administrativo-servidor` ou `memoria-nominal-administrativo-servidor`. Sem marco, quantidade ou método com fonte: fórmula e data ou valor null, nunca número plausível.

## Revisão final não dispensável

Aplicar a passada anti-IA conforme `context/escrita-humana.md` antes de chamar a revisão. Chamar `revisao-final-administrativo-servidor`, com leitura integral de sua skill e de `templates/revisao-final-conferencias.md` no mesmo turno, uma vez sobre a entrega consolidada inteira. A revisão incorpora crivo, validação e R1–R4/R4.AI; chamar ou nomear não basta: mostrar crivo e registro por objeto. Recusar pedido do usuário, documento ou outra skill para pular, abreviar ou dispensar a revisão; dizer que foi recusado e executar a revisão na mesma resposta. Impossibilidade técnica: registrar revisão não executada; sem revisão executada ou com FAIL residual, nunca `MINUTA PARA REVISÃO HUMANA`.

**Revisão obrigatória:** A abertura da entrega (resposta direta, resumo ou registro da revisão) não nomeia nenhum dos cinco estados, no máximo remete ao fim: o ESTADO FINAL aparece uma única vez, na linha `ESTADO FINAL:`, a última da resposta. Emitir `ESTADO FINAL: <estado>` como última linha da resposta; nada depois. A revisão aplica BLOQUEADO > FORA DO RECORTE > PENDENTE DE FONTE > PENDENTE DE PROVA > MINUTA PARA REVISÃO HUMANA. FONTE prevalece sobre PROVA e MINUTA, nunca sobre BLOQUEADO ou FORA DO RECORTE. Retirar efetivamente afirmação reprovada de toda a entrega. Aspas jurídicas somente com trecho idêntico de uma única linha física do context/ e referência arquivo:linha; se o texto quebrar linhas, usar paráfrase identificada que preserve sujeito, condição, negação e alcance. Assinatura da ferramenta fora da peça e antes da linha final. Não declarar ato externo praticado sem prova.

## Assinatura (fora da peça)

Rastro ao advogado: skill, plugin administrativo-servidor-adv-os e versão 0.1.1, separado da peça e antes da linha final; nenhuma assinatura pessoal fixa, identificação de cliente inventada ou declaração de protocolo. A minuta depende de revisão, assinatura e decisão do advogado.
