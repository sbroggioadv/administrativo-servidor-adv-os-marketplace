# Administrativo do Servidor e Concursos

`administrativo-servidor-adv-os` · versão 0.1.0 · IA Combativa

Plugin para o advogado que atua em **direito administrativo do servidor público e concursos federais**, em duas trilhas separadas: **PARTICULAR** (servidor, candidato ou administrado) **ou ENTE federal** (defesa da Administração nos mesmos eixos). Um caso, um polo, confirmado pelo advogado e fixo até o fim; pedido para atuar pelos dois lados no mesmo caso é bloqueado.

Duas portas: **`/administrativo-servidor-install`** (pasta privada e polo do caso, com botões nas escolhas fechadas) e **`/administrativo-servidor-master`** (tria, pergunta o que falta, propõe estratégias e fecha pela revisão final). São 25 skills.

> **Não é parecer jurídico e não substitui o advogado.** Toda saída é minuta, mapa ou conta aberta para revisão humana. A verificação desta versão foi feita por casos de teste e por casos reais julgados pelo STJ e pelo STF, não por uso no Cowork nativo.

## Instalação pelo marketplace

No Claude Desktop: Personalização → Plugins → + Adicionar → Adicionar marketplace → Adicionar de um repositório. Cole a URL pública do marketplace indicada no manual, sincronize e instale `administrativo-servidor-adv-os`. Depois, escolha uma pasta privada por cliente e caso e rode `/administrativo-servidor-install`.

No Claude Code (linha de comando), em um passo:

```
/plugin install administrativo-servidor-adv-os --marketplace sbroggioadv/administrativo-servidor-adv-os-marketplace
```

A interface e a linha de comando guardam marketplaces em caches separados: quem usa o Cowork instala pela interface.

## O que faz

- **Concursos federais:** edital, retificações e eliminação; recurso de concurso; nomeação, cadastro de reserva e preterição; posse e exercício. Sem substituir a banca (Tema 485/STF) e sem prometer nomeação (Temas 161 e 784/STF).
- **PAD federal:** matriz de fatos, imputação, prova e defesa; defesa, recurso e revisão; parecer de legalidade pelo ente. Sem nulidade automática (SV 5/STF; Súmulas 592, 611, 641, 650 e 665/STJ).
- **Direitos funcionais em atividade:** requerimento ou resposta da Administração; rubricas e diferenças nominais condicionadas; gratificação natalina.
- **Via administrativa:** reconsideração e recurso estatutário, autotutela (art. 54 da Lei 9.784) e prescrição quinquenal (Decreto 20.910), como conta aberta.
- **Via judicial:** mandado de segurança ou informações da autoridade, ação funcional ou contestação, apelação, agravos e embargos.
- **Prazos e contas** com marco e calendário confirmados, sempre com a operação à vista.

## O que não faz

Regime estadual ou municipal sem material próprio, RPPS e aposentadoria, abono e CTC, vínculo CLT, servidor militar, improbidade, matéria criminal e sanção a empresas ficam fora do recorte e são encaminhados. Cotas e exames de concurso só recebem triagem. Não há motor de atualização de crédito contra a Fazenda.

## Como evita inventar

Lei, súmula, tema e julgado só entram com arquivo e linha do material capturado em `context/` (captura de 25/10/2026, com data e hash no índice). Aspas apenas com trecho idêntico. Toda entrega passa uma vez pela revisão final; o pedido de pulá-la é recusado. A última linha diz o estado: MINUTA PARA REVISÃO HUMANA, PENDENTE DE PROVA, PENDENTE DE FONTE, FORA DO RECORTE ou BLOQUEADO.

---
© IA Combativa. Uso profissional. Não substitui a análise do advogado responsável.
