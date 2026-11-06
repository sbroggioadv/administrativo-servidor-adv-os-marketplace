# Administrativo do Servidor e Concursos

Apoio ao advogado em direito administrativo do servidor público e concursos federais, em duas trilhas separadas — o particular ou o ente federal, um polo por caso.

**25 skills** · 25 commands · 2 scripts de cálculo · 29 arquivos de referência em `context/` (leis, súmulas, temas e julgados capturados de fonte oficial, mais metodologia e guias de cálculo).

---

## Instalação

> ⚠️ **Instale pela interface**, não pela linha de comando. A interface e a CLI têm caches separados de marketplace — um marketplace adicionado pela CLI **não aparece** na interface.

1. Abra o Claude Desktop
2. **Personalização → Plugins → + Adicionar → Adicionar marketplace → Adicionar de um repositório**
3. Cole a URL deste repositório:
   ```
   https://github.com/sbroggioadv/administrativo-servidor-adv-os-marketplace
   ```
4. **Sincronizar** → instalar `administrativo-servidor-adv-os`
5. Escolha uma pasta privada por cliente e caso e rode `/administrativo-servidor-install`

---

## O que o plugin cobre

- **Concursos federais** — edital, retificações e eliminação, recurso de concurso, nomeação e preterição, posse e exercício, sem substituir a banca nem prometer nomeação.
- **Processo administrativo disciplinar federal** — matriz de fatos, imputação e prova, defesa, recurso e revisão, ou parecer de legalidade pelo ente, sem nulidade automática.
- **Direitos funcionais em atividade** — requerimento ou resposta da Administração, rubricas e diferenças nominais condicionadas, gratificação natalina.
- **Via administrativa e judicial** — reconsideração e recurso estatutário, autotutela e prescrição quinquenal como conta aberta, mandado de segurança ou informações da autoridade, ação funcional e recursos.

## O que o plugin **não** cobre

- Regime estadual ou municipal sem material próprio → encaminhado; a Lei 8.112 não é aplicada como regra universal
- Aposentadoria, RPPS, abono de permanência e CTC → núcleo previdenciário
- Vínculo CLT, servidor militar, improbidade, matéria criminal e sanção a empresas → fora do recorte
- Cotas e exames de concurso → só triagem, com a fonte especializada que falta apontada
- Atualização de crédito contra a Fazenda → diferença nominal e fórmula, sem motor de atualização

---

## Como usar

| Comando | Para quê |
|---|---|
| `/administrativo-servidor-install` | configuração inicial: pasta privada e polo do caso |
| `/administrativo-servidor-master` | porta única — descreva o caso em linguagem natural |
| `/triagem-administrativo-servidor` | classificar um caso novo |
| `/revisao-final-administrativo-servidor` | passar a entrega pela revisão final |

Ou simplesmente **descreva o caso** — a porta única roteia sozinha.

---

## Como o plugin evita inventar

- **Fonte local, com arquivo e linha** — lei, súmula, tema e julgado só entram se estiverem no material capturado em `context/`, com data e hash de captura no índice
- **Aspas só com trecho idêntico** da fonte; o resto é paráfrase identificada
- **Revisão final obrigatória** — conferência de fato, norma, prazo, conta, polo e precedente, depois as rodadas R1–R4; o pedido de pulá-la é recusado
- **Estado na última linha** — MINUTA PARA REVISÃO HUMANA, PENDENTE DE PROVA, PENDENTE DE FONTE, FORA DO RECORTE ou BLOQUEADO

O plugin **declara** o que falta e o que não cobre. Promessa fácil é defeito, não venda.

---

## Requisitos

- Claude Desktop
- Nenhuma chave de API, nenhum serviço externo — o plugin funciona offline

---

## Licença

Ver `LICENSE`, e a licença de uso completa no manual do produto.

---

*IA Combativa*
