# Comando de Início — Antigravity Orchestrator

## 1. Passo Preparatório
Preencha [`0.ideia-inicial.md`](file:///f:/antigravity/projetos/antigravity.emptyProject.Orchestration/0.ideia-inicial.md) na raiz do workspace com uma descrição real do problema, público-alvo, solução e funcionalidades (substituindo os placeholders).

## 2. Disparo no Chat
Envie o comando direto abaixo no chat do Antigravity:

> `/project-orchestrator inicie o projeto`

*(O Antigravity ativará a skill nativamente e dará início ao fluxo imediato de orquestração).*

## 3. Fluxo Automatizado do Agente
1. **Validação Pré-voo (G0)**: Inspeciona deterministicamente o arquivo `0.ideia-inicial.md` (`python .ag-template/scripts/ag-gate.py gate --id g0`). Se houver placeholders vazios, ele pausa e orienta o preenchimento.
2. **Entrevista Interativa (ask_question)**: Conduz uma entrevista estruturada com cards de múltipla escolha para definir o perfil do projeto (1 a 6), stack, integrações e abordagem de design.
3. **Geração Desacoplada (G1)**: Cria a documentação viva em [`docs/`](file:///f:/antigravity/projetos/antigravity.emptyProject.Orchestration/docs/):
   - `docs/projeto.md`: Visão do produto, requisitos funcionais (`RF-###`), requisitos não-funcionais (`RNF-###`) e critérios de aceite.
   - `docs/arquitetura.md`: Modelo de dados, contratos de integração e tecnologias.
   - `docs/design.md`: Tokens visuais, UI/UX, acessibilidade e componentes.
   - `docs/seguranca.md`: Controles de segurança (`SEC-###`), modelagem de ameaças e logs.
   - `docs/diagramas/`: Fluxogramas, diagramas Mermaid e arquiteturas visuais.
4. **Auditoria Determinística de Ambiente**: Executa a verificação de variáveis necessárias (`python .ag-template/scripts/ag-gate.py gate --id g1`) sem vazar credenciais.
5. **Parada Obrigatória de Gate G1**: Apresenta a especificação gerada e os riscos para **aprovação expressa do usuário** antes de iniciar qualquer linha de código (G2).
