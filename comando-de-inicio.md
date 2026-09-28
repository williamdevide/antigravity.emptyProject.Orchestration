# Comando de início pela skill

No repositório modelo, a base está em `.ag-template/`. No projeto novo, copie para `.ag-template/` e mantenha a skill em `.agents/skills/project-orchestrator/SKILL.md` na raiz do workspace; siga `.ag-template/activation/README.md` antes da primeira execução.

Com `GLOBAL-RULES.md` e `GLOBAL-WORKFLOW.md` instalados nas customizações do Antigravity e `.ag-template/documentation/directives/0.ideia-inicial.md` preenchido, envie:

> Use a skill project-orchestrator para iniciar este projeto pela ideia inicial e parar no gate de aprovação da especificação.

Se a skill não for descoberta, use como alternativa explícita: `Inicie pela .ag-template/lifecycle-orchestration.md e pela .ag-template/documentation/directives/0.ideia-inicial.md; pare em G1.` Registre que a descoberta da skill falhou; não declare o mecanismo ativado. A chamada não autoriza implementação anterior ao gate, escrita externa, exclusão nem deploy.
