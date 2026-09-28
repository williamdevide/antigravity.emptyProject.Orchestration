# Base de orquestração para novos projetos

A estrutura canônica usa `.ag-template/` neste modelo e nos projetos derivados; a entrada de produto fica em `0.ideia-inicial.md` na raiz. A skill está em `.agents/skills/project-orchestrator/SKILL.md`. Instale `GLOBAL-RULES.md` e `GLOBAL-WORKFLOW.md` nas customizações do Antigravity.

## Início

1. Preencha `0.ideia-inicial.md` na raiz com ideia substantiva.
2. Envie: `Use a skill project-orchestrator para iniciar este projeto pela ideia inicial e parar no gate de aprovação da especificação.`
3. O agente confirma os insumos, conduz `/grill-me` antes de escrever e utiliza `/goal` para as especificações finais; se não puder invocar esses comandos no chat, deve pedir sua execução, sem simular que os usou.
4. Revise as parciais e `.ag-template/documentation/directives/project/5.projeto.md` e `design/5.design.md` quando aplicável. Antes de pedir aprovação de G1, o agente verifica apenas presença de configuração necessária no `.env` sem exibir segredos; configuração não prova integração ativa.

Aprovação de G1 não autoriza escrita no Stitch, deploy ou ações externas. Consulte `.ag-template/activation/README.md` e `.ag-template/lifecycle-orchestration.md` para instalação, gates e critérios. O CI do modelo verifica estrutura, não a segurança de aplicações derivadas.
