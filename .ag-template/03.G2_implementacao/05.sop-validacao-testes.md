# SOP — Validation and Verification

## Objetivo

Provar, por evidências, que uma mudança atende ao requisito e não introduz regressões conhecidas.

## Escopo

Validações de documentação, código, UI, dados, integrações, segurança e release.

## Procedimento

1. Confirmar o escopo e os critérios de aceite.
2. Verificar se o ambiente e as dependências estão disponíveis.
3. Executar validação estática:
   ```bash
   npm run type-check
   npm run lint
   ```
4. Executar testes unitários e de integração:
   ```bash
   npm test
   ```
5. Executar E2E quando aplicável:
   ```bash
   npm run test:e2e
   ```
6. Executar build:
   ```bash
   npm run build
   ```
7. Validar manualmente os fluxos críticos.
8. Verificar loading, error, empty, responsividade e acessibilidade.
9. Validar integrações usando evidência real, fixture identificada ou estado `blocked`.
10. Registrar resultados e decisão do gate.

## Matriz Mínima

| Área | Evidência | Resultado |
|---|---|---|
| Requisito | Critério de aceite | passed/failed |
| Código | typecheck/lint | passed/failed |
| Testes | relatório | passed/failed |
| UI | validação visual/manual | passed/partial |
| Segurança | secrets e inputs | passed/failed |
| Integrações | health check/log | verified/blocked |

## Critérios de Saída

- [ ] Nenhum bloqueador aberto.
- [ ] Falhas conhecidas têm ticket e mitigação.
- [ ] Testes reproduzíveis.
- [ ] Relatório anexado ao gate ou PR.

## Tratamento de Falhas

Não marcar como aprovado com base em inspeção visual בלבד. Reproduzir a falha, preservar a mensagem original, identificar causa provável e classificar como `failed`, `partial` ou `blocked`.

## Relatório

```md
# Relatório — Validation

**Escopo:** [descrição]
**Data:** YYYY-MM-DD
**Resultado:** aprovado/aprovado-com-reservas/reprovado

## Comandos
- `npm run type-check`: [resultado]
- `npm run lint`: [resultado]
- `npm test`: [resultado]
- `npm run build`: [resultado]

## Fluxos validados
- [ ] [fluxo]

## Falhas e limitações
- Nenhuma / [descrição]

## Decisão
[justificativa]
```

## Referências

- `project-health-checklist.md`
- `phases-gates-reports.md`
- `anti-hallucination-rules.md`