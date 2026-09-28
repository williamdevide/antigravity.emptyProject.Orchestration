# Registro de release — [projeto]

**Versão/tag:** [valor] **Commit:** [sha] **Artefato/digest:** [valor] **Ambiente:** [staging/produção] **Data:** [ISO] **Responsável:** [nome].

## Gate de liberação

- Especificação e riscos residuais aprovados: [referência].
- Build, testes, secret scan, SAST, SCA e DAST quando aplicável: [links, versões, resultados ou N/A justificado].
- Achados abertos e exceções: [ID, impacto, mitigação, aprovador, validade].
- Artefato de staging corresponde exatamente ao promovido: [digest e evidência].
- Migrações e backup/restore quando aplicável: [evidência].
- Smoke/health em staging: [resultado].
- Plano de rollback e última versão saudável: [referência].
- Aprovação específica para produção: [responsável, data e escopo].

## Pós-deploy

- Execução real e saúde: [logs sem dados sensíveis, métricas, período observado].
- Decisão: `passed|failed|blocked|not-verified`; se houve rollback, registrar versão e causa.
- Ações de operação e backlog: [IDs, donos e prazos].

Sem aprovação e evidências, não promover produção. Este arquivo é um modelo, não prova de deploy.
