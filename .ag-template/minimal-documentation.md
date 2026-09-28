# Documentação mínima por projeto

Antes de escrever, confirmar ideia substantiva em `0.ideia-inicial.md` na raiz, fontes e entrevista `/grill-me`. Não usar placeholder como evidência. O plano documental é G0; `/goal` gera somente especificações até G1.

Em `.ag-template/documentation/directives/`, conservar 11 arquivos: `0.prompt-iaexterna-inicial.md`, cinco de `project/` e cinco de `design/`. Preencher `5.projeto.md` com requisitos, segurança, riscos, critérios e rastreabilidade; preencher `5.design.md` se interface aplicável. Se não houver UI, registrar N/A justificado. O usuário aprova explicitamente antes da implementação.

Em `documentation/` na raiz podem ficar `applicability.md`, ADRs, backlog e relatórios. Não exigir artefatos de UI, banco, scraper ou deploy se não fizerem parte do produto. Antes de pedir aprovação de G1, verificar sem divulgar valores se `.env` possui as variáveis necessárias às integrações realmente previstas para a próxima etapa; ausências bloqueiam apenas ações dependentes e devem ser relatadas.
