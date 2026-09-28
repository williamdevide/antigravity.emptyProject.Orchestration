# SOP — Feature Implementation

## Objetivo

Implementar uma feature de forma rastreável, incremental e alinhada à documentação aprovada.

## Escopo

Features, correções e mudanças técnicas que alterem código, dados, UI ou integrações.

## Entradas

- Requisito ou história do backlog.
- Critérios de aceite.
- Documentação de arquitetura e design.
- Dependências e riscos conhecidos.

## Procedimento

1. Ler os documentos relevantes e confirmar o escopo.
2. Verificar pré-condições, branch e estado do repositório.
3. Quebrar a tarefa em passos pequenos.
4. Identificar impactos em dados, segurança, acessibilidade e integrações.
5. Implementar a menor mudança suficiente.
6. Criar ou atualizar testes.
7. Validar localmente após cada unidade relevante.
8. Comparar a implementação com o design e os critérios de aceite.
9. Atualizar documentação, backlog e changelog.
10. Produzir o relatório de implementação.

## Regras

- Não inventar requisitos, APIs ou dados.
- Não substituir integração real por mock silencioso.
- Não misturar refatorações não relacionadas.
- Não commitar secrets.
- Registrar toda divergência e limitação.

## Critérios de Sucesso

- [ ] Critérios de aceite atendidos.
- [ ] Testes adicionados ou atualizados.
- [ ] Typecheck e lint passando.
- [ ] Estados loading, error e empty tratados quando aplicável.
- [ ] Acessibilidade básica verificada.
- [ ] Documentação atualizada.

## Evidências

```md
# Relatório — Feature Implementation

**Feature:** [nome]
**Backlog:** [ID]
**Status:** passed/partial/failed

## Alterações
- [arquivo ou módulo]

## Validações
- [ ] Testes
- [ ] Lint
- [ ] Typecheck
- [ ] Build
- [ ] Validação manual

## Divergências e riscos
- Nenhum / [descrição]

## Próximos passos
- [ação]
```

## Rollback

Se a mudança quebrar o fluxo principal, interromper, preservar logs, reverter somente a alteração relacionada e registrar o motivo.

## Referências

- `backlog-guidelines.md`
- `phases-gates-reports.md`
- `GLOBAL-RULES.md`