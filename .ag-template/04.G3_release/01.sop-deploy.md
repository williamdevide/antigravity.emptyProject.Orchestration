# SOP — Deploy and Release

## Objetivo

Publicar uma versão validada de forma segura, observável e reversível.

## Pré-requisitos

- Gate de testes aprovado.
- Branch e commit identificados.
- Variáveis de produção configuradas no provedor seguro.
- Plano de rollback conhecido.
- Aprovação exigida pelo projeto registrada.

## Pre-flight

- [ ] Working tree e branch verificados.
- [ ] Changelog atualizado.
- [ ] Dependências auditadas.
- [ ] Typecheck, lint, testes e build passando.
- [ ] Migrations revisadas.
- [ ] Backups verificados quando aplicável.
- [ ] Health check e monitoramento preparados.

## Procedimento

1. Gerar artefato de release a partir de commit imutável.
2. Executar deploy em staging.
3. Validar smoke tests em staging.
4. Obter aprovação para produção.
5. Executar deploy usando o pipeline oficial.
6. Executar health check imediatamente.
7. Verificar logs, erros e métricas.
8. Validar fluxos críticos.
9. Comunicar resultado e registrar a versão.

## Pós-deploy

Monitorar o período definido pelo projeto. Se houver regressão crítica, interromper mudanças e executar rollback.

## Rollback

1. Identificar a última versão saudável.
2. Confirmar impacto e aprovação operacional.
3. Executar rollback pelo mecanismo oficial.
4. Validar health check e fluxos críticos.
5. Registrar causa, duração e ações corretivas.

## Relatório

```md
# Relatório — Deploy

**Projeto:** [nome]
**Versão:** [tag/commit]
**Ambiente:** staging/production
**Data:** YYYY-MM-DD
**Resultado:** sucesso/rollback/falha

## Checks
- [ ] Pre-flight
- [ ] Staging
- [ ] Health check
- [ ] Smoke tests
- [ ] Monitoramento

## Alterações
- [item]

## Riscos e incidentes
- Nenhum / [descrição]

## Rollback
- Não necessário / executado para [versão]
```

## Regras de Segurança

- Nunca colocar secrets em logs, commits ou URLs.
- Não executar deploy destrutivo sem aprovação.
- Não afirmar que o deploy ocorreu sem verificar o provedor e o health check.

## Referências

- `phases-gates-reports.md`
- `risk-catalogue.md`
- `integration-contracts.md`