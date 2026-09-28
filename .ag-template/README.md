# Índice da base

A pasta `.ag-template/` é canônica no repositório-modelo e nos novos projetos. O ponto de entrada é `.agents/skills/project-orchestrator/SKILL.md` na raiz do workspace. A ideia inicial fica em `.ag-template/documentation/directives/0.ideia-inicial.md`; as regras globais do diretório `agent/` são configuradas separadamente no IDE.

## Mapa

- `lifecycle-orchestration.md` e `phases-gates-reports.md`: fases e gates.
- `documentation/directives/`: 12 diretivas canônicas; não renomear.
- `security/`, `risk-catalogue.md` e `sop-templates/`: ameaças, segurança, execução e operação.
- `project-customization/`: modelos de regras e workflow específicos após G1.
- `ci/`: política por projeto e exemplo inerte; CI de aplicação depende da stack real.
- `release/`: registro de promoção e evidências, não prova de deploy.
- `guides/` e `ui-patterns/`: referências condicionais, nunca código de produção sem revisão.

O workflow `.github/workflows/template-validation.yml` na raiz do repositório-modelo executa `scripts/validate_template.py` e valida apenas estrutura e nomes, não testes de software, scanners ou descoberta da skill no Antigravity. Diretivas placeholder não equivalem a aprovação de G1. Sem evidência de execução, classificar `not-verified`.
