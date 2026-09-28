# SOP — Operação e manutenção

## Gatilhos

Início da operação, alertas, incidente, nova vulnerabilidade, falha de backup, degradação, atualização de dependência ou mudança de arquitetura.

## Procedimento

1. Identificar ambiente, versão, dono do serviço, fluxo afetado, impacto e fonte do alerta sem registrar segredos ou dados pessoais.
2. Fazer triagem por severidade definida pelo projeto; escalar incidentes críticos; registrar horário, responsável e comunicação.
3. Preservar evidências, correlacionar logs/métricas, distinguir fato de hipótese e avaliar contenção reversível.
4. Corrigir em branch revisada; executar testes de regressão e segurança correspondentes ao risco; seguir CI e gate de release.
5. Para vulnerabilidade, rastrear componente/versão afetados, explorabilidade contextual, mitigação, prazo e risco residual; verificar correção em produção.
6. Verificar health e métricas após liberação, avaliar rollback, revisar causa raiz e adicionar ações ao backlog/modelo de ameaças.
7. Testar periodicamente restauração de backup e disponibilidade de plano de resposta, conforme criticidade.

## Relatório

Registrar incidente/achado, ambiente, versão, impacto, cronologia, decisão, aprovador, evidência de correção, validação pós-deploy, necessidade de notificação aplicável e ações preventivas com responsáveis e prazo. Não declarar resolvido sem confirmação do serviço em operação.
