# Template de orquestração de projetos

Este repositório é uma base para iniciar projetos a partir de `ag-template/documentation/directives/0.ideia-inicial.md`. Ao usar a base em um novo repositório, copie `ag-template/` para `.ag-template/` e preencha `.ag-template/documentation/directives/0.ideia-inicial.md`; não execute prompts de exemplo como scripts.

## Início

1. Cole `ag-template/agent/GLOBAL-RULES.md` e `ag-template/agent/GLOBAL-WORKFLOW.md` nas sessões de customização do Antigravity. Confirme que estão ativos antes de iniciar; a cópia no repositório é a origem versionada, não uma segunda instrução a carregar.
2. Abra o projeto no Antigravity e chame o agente com: `Inicie a orquestração deste projeto conforme as instruções globais e .ag-template/lifecycle-orchestration.md, usando .ag-template/documentation/directives/0.ideia-inicial.md como entrada. Trabalhe até o primeiro gate de aprovação, registre evidências e não faça deploy.`
3. O agente prepara especificações, riscos, requisitos de segurança e plano de validação; aguarda aprovação expressa antes de implementar. A partir daí prossegue por incrementos e gates. Um comando inicia o processo, não autoriza mudanças externas nem elimina aprovações posteriores.

## Contratos

- Caminho canônico das diretivas no projeto gerado: `.ag-template/documentation/directives/`. Documentação derivada da aplicação pode ficar em `documentation/`, mas não substitui as diretivas.
- `GLOBAL-RULES.md` e `GLOBAL-WORKFLOW.md` são configurados pelo usuário no IDE; `lifecycle-orchestration.md` detalha o processo, sem redefinir essas regras.
- SOPs e guias são modelos condicionais à stack e ao perfil. Comandos e integrações não verificados ficam como `not-verified`.
- O repositório fornece documentação e um exemplo de CI; não instala uma CLI, não ativa CD automaticamente e não garante segurança sem execução e evidências.
