# SOP — Troubleshooting

## Objetivo

Diagnosticar e resolver problemas com base em evidências, minimizando impacto e evitando alterações irreversíveis.

## Escopo

Falhas de ambiente, código, dados, integrações, testes, performance e produção.

## Procedimento

1. Registrar sintoma, horário, ambiente e usuário afetado.
2. Classificar severidade e impacto.
3. Reproduzir com o menor caso possível.
4. Coletar logs, stack trace, métricas e estado da configuração.
5. Separar fato observado de hipótese.
6. Comparar com a última mudança conhecida.
7. Testar uma hipótese por vez.
8. Aplicar a menor correção reversível.
9. Reexecutar os testes que reproduziam o problema.
10. Documentar causa raiz, solução e prevenção.

## Severidade

| Nível | Descrição | Ação |
|---|---|---|
| P0 | Serviço indisponível ou risco crítico | Escalar imediatamente |
| P1 | Fluxo principal quebrado | Priorizar correção |
| P2 | Impacto limitado | Corrigir no ciclo atual |
| P3 | Problema cosmético ou workaround disponível | Backlog |

## Checklist por Área

### Ambiente

- [ ] Versões verificadas.
- [ ] Dependências instaladas.
- [ ] Variáveis presentes sem expor valores.
- [ ] Porta e processos verificados.

### API/Integração

- [ ] URL e método confirmados na documentação.
- [ ] Status code e payload registrados.
- [ ] Timeout, retry e rate limit considerados.
- [ ] Estado classificado como verified, blocked ou not-verified.

### Dados

- [ ] Schema confirmado.
- [ ] Migration identificada.
- [ ] Duplicação e integridade verificadas.
- [ ] Backup considerado antes de alteração.

### UI

- [ ] Loading, error e empty verificados.
- [ ] Reprodução em viewport afetada.
- [ ] Console e network inspecionados.
- [ ] Acessibilidade afetada avaliada.

## Regras

- Não apagar banco ou diretórios sem confirmar impacto.
- Não mascarar erro com fallback silencioso.
- Não alterar múltiplas variáveis ao mesmo tempo.
- Não expor dados pessoais ou secrets em relatórios.

## Relatório

```md
# Relatório — Troubleshooting

**Problema:** [resumo]
**Ambiente:** local/staging/production
**Severidade:** P0/P1/P2/P3
**Data:** YYYY-MM-DD

## Sintoma
[observação verificável]

## Reprodução
1. [passo]
2. [passo]

## Evidências
- Logs: [referência]
- Commit relacionado: [hash]
- Métrica: [valor]

## Hipótese e causa raiz
[confirmada ou ainda não verificada]

## Correção
[alteração executada]

## Validação
[checks executados]

## Prevenção
[teste, alerta ou documentação adicionada]
```

## Referências

- `risk-catalogue.md`
- `anti-hallucination-rules.md`
- `project-health-checklist.md`