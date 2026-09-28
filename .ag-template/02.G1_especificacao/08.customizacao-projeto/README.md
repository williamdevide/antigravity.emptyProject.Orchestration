# Customização específica do projeto

Estes modelos não substituem as regras globais do Antigravity nem a skill. Após G1, o agente preenche os arquivos específicos no projeto com base em `docs/prd.md`, `docs/design.md`, aplicabilidade e riscos aprovados. Não sobrescrever decisões já aprovadas sem apresentar diff e obter nova aprovação.

- `project-rules.template.md`: restrições de produto, segurança, dados, arquitetura e testes do projeto.
- `project-workflow.template.md`: fases, responsáveis, comandos reais, gates, evidências, ambientes e rollback.

Manter as referências das especificações aprovadas e o histórico de decisões; segredos e dados pessoais não entram nesses documentos. Se a plataforma exigir outro local para descobrir regras por projeto, verificar documentação e configuração da versão usada antes de mover ou ativar os arquivos.
