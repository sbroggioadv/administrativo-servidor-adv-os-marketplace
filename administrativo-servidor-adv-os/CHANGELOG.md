# Changelog

## [0.1.1] — 2026-11-06

### O que muda para quem já instalou

Atualize o marketplace no Cowork (Personalização → Plugins → marketplace → Sincronizar). Nada muda na pasta privada nem nos casos já abertos; os comandos são os mesmos.

### Corrigido

Ajustes na revisão final, depois da confirmação completa dos 24 casos de teste no plugin publicado:

- Toda negativa, marco temporal, órgão ou pessoa jurídica que a entrada não dá entra no crivo como linha própria e é reescrita como "não informado na entrada"; ente federal sem pessoa jurídica informada não vira União.
- A paráfrase da inassiduidade habitual preserva "sem causa justificada" (art. 139 da Lei 8.112).
- Intervalo entre datas é conta: número exato contado data a data, ou só a expressão segura ("mais de N anos").
- A falta da norma material sobre o exercício só pesa no estado quando a entrega conclui sobre o direito; não na reconsideração por erro de fato com documento oficial já juntado.
- A medida da autoridade que impugna a validade do ato (art. 54, §2º, da Lei 9.784) é tratada como exercício do direito de anular, não como interrupção do prazo de decadência.

Scripts de cálculo inalterados (versão 0.1.0).

## [0.1.0] — 2026-11-06

### O que muda para quem já instalou

Primeira versão publicada. Não há instalação anterior a migrar.

### Novo

- Duas trilhas segregadas, um polo por caso: particular (servidor, candidato ou administrado) ou ente federal; pedido pelos dois lados no mesmo caso é bloqueado.
- Concursos federais (edital, eliminação, recurso, nomeação, posse e exercício), processo administrativo disciplinar, direitos funcionais em atividade, recursos administrativos, mandado de segurança, ação funcional e recursos judiciais — 25 skills, portas `/administrativo-servidor-install` e `/administrativo-servidor-master`.
- Revisão final obrigatória e não dispensável, com o estado da entrega na última linha.
- Doze julgados do STJ e do STF conferidos contra a fonte oficial, com trecho literal e limite de uso.
- Cálculo: dois scripts locais (prazos administrativo, estatutário e processual; gratificação natalina), só biblioteca padrão e sem rede, com `--versao` e a regra e a fonte de cada número; conta aberta em toda skill que entrega data ou valor.

### Corrigido antes da publicação

- Prazo do mandado de segurança tratado como decadencial; Lei 14.965 tratada como lei nacional; penalidade aplicada não revela a conclusão do relatório da comissão; ausência de informação não vira fato negativo; paráfrase de hipótese legal conferida condição por condição; cabimento do mandado de segurança condicionado ao art. 5º, I, da Lei 12.016.
- Nomes de pessoas físicas e números de OAB das páginas do STF capturadas foram omitidos do material de referência.
