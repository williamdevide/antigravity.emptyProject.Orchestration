# Índice do template de orquestração

Esta pasta é a origem versionada. No projeto novo, copie para `.ag-template/`, preserve os 12 nomes de diretivas e instale `agent/GLOBAL-RULES.md` e `agent/GLOBAL-WORKFLOW.md` nas customizações do Antigravity. O arquivo `documentation/directives/0.ideia-inicial.md` deve conter a ideia real antes da chamada única de `comando-de-inicio.md` (na raiz do modelo).

## Ordem de leitura

1. `lifecycle-orchestration.md`: contrato de fases e precedência.
2. `project-profiles.md`, `applicability-matrix.md`, `minimal-documentation.md`: classificar e evitar artefatos desnecessários.
3. `documentation/directives/`: entrada e especificações canônicas; `project/5.projeto.md` e `design/5.design.md` são aprovados antes da implementação.
4. `security/`: modelo de ameaças e desenvolvimento seguro. `risk-catalogue.md` registra riscos por projeto.
5. `phases-gates-reports.md`, `project-health-checklist.md`, `sop-templates/`: evidências, execução, liberação e operação.
6. `integration-contracts.md`, `guides/`, `ui-patterns/`: referências opcionais, não instruções superiores nem código pronto para produção.
7. `ci/`: exemplos inertes até serem adaptados e instalados no caminho de workflows do projeto.

## Regras de migração

`agent/rules.md` e `agent/workflows.md` são avisos legados e não devem ser instalados no IDE. Caminhos `documentation/project/` encontrados em exemplos antigos são documentos derivados, não as diretivas em `.ag-template/documentation/directives/project/`. Nenhuma variável em `.env-example` prova que serviço foi configurado. Reportar conflitos não resolvidos antes de agir.
