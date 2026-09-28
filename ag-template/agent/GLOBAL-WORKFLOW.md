# Workflow global do agente

Instale este arquivo nas customizações do Antigravity junto com `GLOBAL-RULES.md`. Uma chamada em linguagem natural inicia a orquestração; slash commands e ferramentas só podem ser usados após verificar sua disponibilidade real.

## Chamada única

`Inicie a orquestração deste projeto conforme as regras globais e .ag-template/lifecycle-orchestration.md, usando .ag-template/documentation/directives/0.ideia-inicial.md como entrada. Trabalhe até o primeiro gate de aprovação, registre evidências e não faça deploy.`

## Fluxo

1. Confirmar workspace, caminho da ideia e se ela contém conteúdo substantivo; se faltar, parar. Inspecionar stack e integrações disponíveis sem pressupor uma CLI.
2. Ler `project-profiles.md`, `applicability-matrix.md`, `risk-catalogue.md` e contratos relevantes. Classificar perfil e marcar N/A com justificativa.
3. Produzir `project/1.ideia-projeto.md` e, se houver UI, `design/1.ideia-design.md`; separar fatos, premissas e lacunas. Não declarar um resultado de ferramenta sem execução.
4. Produzir `project/5.projeto.md`, `design/5.design.md` quando aplicável, requisitos `SEC-###`, critérios de aceite e modelo de ameaças específico do projeto. Relacionar riscos, controles, testes, responsáveis e evidências esperadas.
5. Exibir diff e riscos residuais; solicitar aprovação expressa do usuário antes de implementar. A mesma exigência se aplica a integração externa, exclusão, deploy e aceitação excepcional de risco conforme impacto.
6. Após aprovação, implementar incrementos pequenos conforme SOPs; verificar testes e segurança por PR; bloquear se checks obrigatórios falharem ou não existirem. DAST só em ambiente autorizado.
7. Promover releases apenas após gate de qualidade, aprovação específica de produção e plano de rollback. Em operação, monitorar, corrigir, retestar e alimentar o backlog.

Em cada gate: indicar estado real, arquivos alterados, comandos e resultados, evidências, bloqueios, decisões e próximo passo. `lifecycle-orchestration.md` detalha a execução; não tratar exemplos de guias como obrigatórios.
