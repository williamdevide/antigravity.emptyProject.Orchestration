# Índice da base

O repositório modelo guarda `ag-template/`; cada projeto novo usa `.ag-template/`. O ponto de entrada executável pelo agente é a skill de workspace `.agents/skills/project-orchestrator/SKILL.md` na raiz do projeto, instalada conforme `activation/README.md`. A ideia inicial fica em `.ag-template/documentation/directives/0.ideia-inicial.md`. Instale as regras globais do diretório `agent/` nas customizações do Antigravity; a cópia local só versiona a origem.

## Mapa

- `lifecycle-orchestration.md` e `phases-gates-reports.md`: fases e critérios de gate.
- `documentation/directives/`: os 12 nomes canônicos, entrada, projeto e design.
- `security/` e `risk-catalogue.md`: ameaças, controles, verificações e riscos.
- `sop-templates/`: setup, implementação, integração, validação, segurança, deploy, troubleshooting e operação.
- `ci/`: orientação e exemplo não executado; CI real depende da stack e vai ao caminho de workflows do projeto.
- `guides/`, `ui-patterns/`: material opcional a revisar conforme perfil; não instalar como regra global nem copiar snippets automaticamente.
- `project-profiles.md`, `applicability-matrix.md`, `minimal-documentation.md`, `folder-structure.md`: classificação, decisões e estrutura.

Os arquivos de diretivas vazios são placeholders; não equivalem a especificações aprovadas. `documentation/` na raiz do projeto pode receber documentação derivada, mas não substitui `.ag-template/documentation/directives/`. Na falta de evidência, declarar `not-verified`.
