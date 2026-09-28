# Documentação mínima por projeto

Aplique `applicability-matrix.md` antes de gerar artefatos. O obrigatório universal é: ideia substantiva em `documentation/directives/0.ideia-inicial.md`, perfil/escopo, especificação `project/5.projeto.md` revisada, riscos e critérios de aceite, matriz requisito → controle → teste → evidência, gate de aprovação e registros de execução. Todos esses caminhos de diretivas são relativos a `.ag-template/` no projeto gerado.

Se houver UI, preencher e aprovar `design/5.design.md`; caso contrário justificar N/A. Se houver dados pessoais, integrações, autenticação, pagamentos ou implantação, documentar fluxos de dados, ameaças, controles, tratamento de incidentes e operação adequados ao risco. Para cada integração declarar `configured`, `verified`, `blocked`, `not-verified` ou `not-applicable` com evidência; arquivo de exemplo não configura serviço.

Documentação derivada pode ser criada em `documentation/` (ADRs, backlog, relatórios e runbooks), com referências para as diretivas canônicas. Não exigir um README por diretório, número fixo de registros, formato JSON com comentários, design ou stack web em projetos que não se aplicam. Documentar comandos reais do projeto em README, inclusive como rodar build, testes, verificações e rollback quando disponíveis. Segredos nunca entram em exemplos.
