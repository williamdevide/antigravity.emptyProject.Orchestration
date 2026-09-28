# Ativação da orquestração no Antigravity

No projeto novo, usar `.ag-template/` para os contratos e `.agents/skills/project-orchestrator/SKILL.md` na raiz do workspace para descoberta da skill. O `SKILL.md` versionado no repositório modelo está em `.agents/skills/project-orchestrator/`; copiar junto ao preparar o projeto. A skill não é automaticamente descoberta se estiver apenas dentro de `.ag-template/`.

1. Copiar `.ag-template/` do modelo para `.ag-template/` do novo projeto e versionar a pasta sem segredos.
2. Copiar `.agents/skills/project-orchestrator/SKILL.md` do modelo para o mesmo caminho na raiz do novo projeto.
3. Instalar o conteúdo de `agent/GLOBAL-RULES.md` e `agent/GLOBAL-WORKFLOW.md` nas customizações do Antigravity, sem instalar os antigos `rules.md` e `workflows.md`.
4. Preencher `.ag-template/documentation/directives/0.ideia-inicial.md` com a ideia real.
5. Abrir o workspace e solicitar: `Use a skill project-orchestrator para iniciar este projeto pela ideia inicial e parar no gate de aprovação da especificação.`
6. Confirmar no ambiente que a skill foi descoberta, que a leitura da ideia ocorreu e que o agente parou em G1; se não, diagnosticar descoberta e caminhos antes de dizer que a automação funciona.

Uma skill coordena o trabalho; não substitui configuração real de CI/CD, credenciais, aprovações nem execução de testes. O formato de `SKILL.md` e o caminho de workspace seguem a documentação do Antigravity, mas sua descoberta precisa ser testada na versão efetiva do IDE.
