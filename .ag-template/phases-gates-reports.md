# Fases, gates e relatórios

`0.ideia-inicial.md` na raiz é entrada obrigatória e única; `.ag-template/documentation/directives/` guarda as 11 diretivas de transformação e especificação. A skill e as regras globais determinam pré-condições e precedência.

| Gate | Entrega | Evidência | Aprovação |
|---|---|---|---|
| G0 | Conteúdo inicial suficiente e entrevista `/grill-me` antes da escrita | Respostas e lacunas; sem inventar execução do slash command | Prosseguir ou parar |
| G1 | `/goal` documental, `5.projeto.md` e `5.design.md` se aplicável | Requisitos, ameaças, riscos, testes, diff e checagem de NOMES de variáveis `.env` necessárias | Expressa para especificação e riscos |
| G2 | Código incremental | Revisão, testes e controles de segurança aplicáveis | Conforme risco aprovado |
| G3 | Release | Artefato, staging, checks, smoke, rollback e decisão | Expressa para produção |
| G4 | Operação | Health, alertas, vulnerabilidades e retorno ao backlog | Conforme política |

Na apresentação de G1, variável presente significa apenas configuração observada, não integração verificada; ausência bloqueia ação dependente. Cada relatório inclui commit, ambiente, responsável, comandos realmente executados, resultados `passed|failed|blocked|not-verified|not-applicable`, evidências, riscos residuais e próximos passos. Não iniciar código, Stitch ou deploy só pela chamada inicial nem promover gate obrigatório sem evidências.
