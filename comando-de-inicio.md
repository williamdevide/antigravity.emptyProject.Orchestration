# Comando de início

Preencha `0.ideia-inicial.md` na raiz com conteúdo real. A skill está em `.agents/skills/project-orchestrator/SKILL.md`; as parciais e especificações permanecem em `.ag-template/documentation/directives/`. Então envie:

> Use a skill project-orchestrator para iniciar este projeto pela ideia inicial e parar no gate de aprovação da especificação.

A skill deve primeiro verificar conteúdo e iniciar `/grill-me` (entrevista). Depois, `/goal` tem escopo somente documental até `5.projeto.md` e `5.design.md`; ambos são apresentados para aprovação, com pré-checagem de variáveis do `.env` necessárias às integrações aplicáveis. Se o agente não puder disparar slash commands, ele deve pedir que você execute `/grill-me` e depois `/goal` no chat, sem declarar uso fictício. Não gerar documentos sem ideia suficiente; não criar código, telas no Stitch ou fazer deploy apenas com esse comando.
