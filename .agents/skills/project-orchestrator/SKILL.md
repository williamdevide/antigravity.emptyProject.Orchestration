---
name: project-orchestrator
description: Conduz novos projetos a partir de 0.ideia-inicial.md na raiz, entrevista requisitos, gera projeto e design e para no gate G1 com pré-checagem das integrações aplicáveis.
---

# Skill de orquestração

## Entrada obrigatória e pré-condições

Leia `0.ideia-inicial.md` na raiz do workspace; nunca use a antiga diretiva dentro de `.ag-template/`. Antes de criar ou modificar qualquer arquivo, confirme que a ideia existe, tem conteúdo substantivo além de placeholders e oferece problema, público e objetivo minimamente compreensíveis. Leia `.ag-template/lifecycle-orchestration.md`, regras aplicáveis e os templates necessários. Se a ideia, as fontes ou os comandos indispensáveis não estiverem acessíveis, pare, explique o bloqueio e peça os dados faltantes; não gere especificações fictícias.

## Entrevista e geração

Use `/grill-me` para entrevistar o usuário sobre lacunas e decisões relevantes ANTES de gerar documentos. Depois da entrevista, use `/goal` restrito a produzir e revisar `project/5.projeto.md`, `design/5.design.md` quando houver interface, e suas etapas intermediárias sob `.ag-template/documentation/directives/`; a meta termina em G1, sem código, deploy ou escrita externa. Os slash commands são modos do chat: verifique se podem ser invocados nesta sessão; se a skill não puder acioná-los programaticamente, peça ao usuário para invocar `/grill-me` e depois `/goal` no chat. Nunca afirme que os utilizou apenas por mencionar seus nomes. Não escreva nada antes da entrevista e da entrada suficiente.

## Gate G1 e ambiente

Ao apresentar os dois documentos, classifique integrações realmente necessárias conforme aplicabilidade. Verifique localmente apenas PRESENÇA e formato mínimo das variáveis necessárias no `.env`, sem imprimir valores, sem ler segredo em resposta e sem commitar `.env`. Para Stitch, confirme o método real de autenticação (API key ou OAuth/MCP) antes de exigir uma chave específica; se for chave, verificar `GOOGLE_STITCH_API_KEY`. Para outras integrações, derivar os nomes das variáveis do contrato aprovado e do `.env-example`; não exigir credenciais para itens futuros ou N/A. Presença de variável não prova conexão nem permissão: classifique `configured` ou `not-verified` até testar de modo autorizado. Se faltar credencial necessária ao próximo passo, informe somente nomes de variáveis ausentes, marque `blocked` e solicite configuração; não inicie a integração. Peça aprovação expressa de G1 para conteúdo e riscos; aprovação de G1 não autoriza criar no Stitch ou fazer deploy.
