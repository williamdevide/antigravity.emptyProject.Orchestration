# Índice da base

A pasta `.ag-template/` é canônica no modelo e nos projetos derivados, mas a entrada de produto `0.ideia-inicial.md` fica na raiz do workspace. A skill `.agents/skills/project-orchestrator/SKILL.md` também fica na raiz. Os dois arquivos em `agent/` definem regras globais configuradas no IDE.

## Mapa

- `documentation/directives/`: 11 arquivos de prompts e especificações; `0.prompt-iaexterna-inicial.md` permanece aqui. A ideia inicial NÃO fica aqui.
- `lifecycle-orchestration.md` e `phases-gates-reports.md`: entrevista, G0–G4 e evidências.
- `security/`, `risk-catalogue.md`, `sop-templates/`: controles e operação por risco.
- `project-customization/`, `ci/`, `release/`: modelos por projeto após G1; exemplos não representam execução.
- `guides/`, `ui-patterns/`: referências condicionais, nunca código pronto sem revisão.

A ordem é: validar ideia raiz e pré-requisitos → entrevistar por `/grill-me` → gerar parciais e `5.projeto.md`/`5.design.md` com `/goal` limitado a G1 → verificar nomes de configurações necessárias no `.env` sem mostrar valores → solicitar aprovação expressa. Se os slash commands não puderem ser chamados pelo agente, pedir invocação ao usuário. Não criar artefatos sem ideia suficiente; não tratar `.env` como prova de integração operacional.
