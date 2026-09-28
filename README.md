# Base de orquestração para novos projetos

O repositório modelo guarda `ag-template/`. No projeto gerado, a pasta final chama-se `.ag-template/`, e a skill fica na raiz em `.agents/skills/project-orchestrator/SKILL.md`. Consulte `ag-template/activation/README.md` para instalar e testar a descoberta no Antigravity.

## Início

1. Copie `ag-template/` para `.ag-template/` e copie a skill `.agents/skills/project-orchestrator/` para a raiz do novo workspace.
2. Instale `GLOBAL-RULES.md` e `GLOBAL-WORKFLOW.md` nas customizações do Antigravity.
3. Preencha `.ag-template/documentation/directives/0.ideia-inicial.md` com a ideia real.
4. No chat, envie: `Use a skill project-orchestrator para iniciar este projeto pela ideia inicial e parar no gate de aprovação da especificação.`

A skill é um ponto de entrada, não uma autorização irrestrita: a especificação, mudanças externas e produção exigem aprovações próprias. Ela exige requisitos de segurança, ameaças, revisão, testes, CI por stack, promoção controlada e operação com evidências. Exemplos na pasta `ci/` não executam até serem adaptados e instalados; o template não contém CD automático. Consulte `ag-template/lifecycle-orchestration.md` para os gates e `ag-template/README.md` para o mapa de arquivos.
