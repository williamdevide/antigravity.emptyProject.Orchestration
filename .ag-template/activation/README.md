# Ativação da orquestração

O repositório modelo e o projeto novo usam `.ag-template/`. A skill `.agents/skills/project-orchestrator/SKILL.md` deve permanecer na raiz do workspace. Instale o conteúdo de `.ag-template/agent/GLOBAL-RULES.md` e `GLOBAL-WORKFLOW.md` nas customizações do Antigravity. A entrada de ideia é `0.ideia-inicial.md` na raiz, fora de `.ag-template/`.

Ao abrir novo projeto, copie `.ag-template/`, `.agents/skills/project-orchestrator/` e o template `0.ideia-inicial.md` para a raiz e preencha-o. Faça a chamada em `comando-de-inicio.md`. Verifique no IDE que a skill foi descoberta, `/grill-me` entrevistou antes de qualquer escrita, `/goal` conduziu a geração documental e o agente parou em G1. Se slash commands não puderem ser invocados pela skill, peça execução separada ao usuário. Não considere a presença de `.env` prova de conexão.
