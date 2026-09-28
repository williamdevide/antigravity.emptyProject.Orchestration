---
name: project-orchestrator
description: Conduz novos projetos a partir de 0.ideia-inicial.md na raiz, entrevista requisitos via ask_question, gera especificações vivas desacopladas em docs/ (projeto.md, arquitetura.md, design.md, seguranca.md e diagramas/) e valida o Gate G1 com auditoria determinística de ambiente.
---

# Skill de Orquestração v2 — Project Orchestrator

Esta skill é ativada quando o usuário envia `/project-orchestrator inicie o projeto` (ou comandos equivalentes de inicialização).

## Entrada obrigatória e pré-condições (Gate G0)

1. Leia `0.ideia-inicial.md` na raiz do workspace (única fonte de entrada de produto).
2. Valide deterministicamente a presença de conteúdo real e substantivo além de placeholders com:
   `python .ag-template/scripts/ag-gate.py gate --id g0`
3. Se o arquivo estiver vazio, contiver apenas títulos/placeholders ou faltar problema e público compreensíveis, interrompa a execução, explique o bloqueio de forma construtiva e solicite as definições necessárias ao usuário. Não crie especificações fictícias.

## Entrevista Interativa Contínua (ask_question)

1. Antes de redigir qualquer documento de especificação, inicie imediatamente a entrevista estruturada utilizando a ferramenta nativa `ask_question`.
2. Conduza perguntas objetivas e uma por vez para resolver:
   - Perfil do projeto (1 a 6 conforme `.ag-template/00.governanca/06.perfis-de-projeto.md`) e complexidade.
   - Stack tecnológica e plataforma alvo (Web mobile-first, desktop, API backend, automação, etc.).
   - Abordagem de Design de UI/UX (quando aplicável): Design System em código puro com tokens modernos, prototipação com mockups, ou Google Stitch via MCP/link.
   - Integrações externas estritamente necessárias ao MVP.
   - Riscos, requisitos de segurança (`SEC-###`) e regras de negócio críticas.

## Geração Desacoplada de Especificação (Gate G1)

Após a entrevista estar concluída e alinhada:
1. Consolide as especificações diretamente na pasta viva `docs/` na raiz do workspace (mantendo `.ag-template/` estritamente como base de suporte, normas e templates):
   - `docs/projeto.md`: Visão do produto, requisitos funcionais (`RF-###`), não-funcionais (`RNF-###`) e critérios de aceite verificáveis.
   - `docs/arquitetura.md`: Modelo de dados, arquitetura em camadas, endpoints e contratos de integração.
   - `docs/design.md`: Tokens visuais, layout responsivo, acessibilidade e componentes (ou contrato com Stitch se adotado).
   - `docs/seguranca.md`: Modelo de ameaças, controles de segurança (`SEC-###`), tratamento de segredos e logs.
   - `docs/diagramas/`: Fluxos, diagramas Mermaid (.mmd ou .md) e arquiteturas visuais geradas.
2. Caso o usuário solicite expressamente prompts para consultar modelos fora do IDE, utilize os moldes em `.ag-template/02.G1_especificacao/07.templates-exportacao/`.

## Verificação de Ambiente e Gate G1

1. Execute a validação determinística de ambiente e requisitos:
   `python .ag-template/scripts/ag-gate.py gate --id g1`
2. Verifique a presença das variáveis necessárias no `.env` com base no `.env-example`. Nunca imprima nem leia segredos na resposta.
3. Classifique o status de cada integração conforme a matriz (`configured`, `not-verified`, `blocked` ou `not-applicable`). A presença de variável indica apenas configuração, não conexão funcional testada.
4. **Parada Obrigatória de Gate G1**: Apresente o resumo da especificação, tabela de requisitos, pendências de ambiente e riscos residuais.
5. Solicite aprovação expressa do usuário para o Gate G1. Não avance para implementação de código (G2), criação externa ou deploy sem essa autorização prévia.
