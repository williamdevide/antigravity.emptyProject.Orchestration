# SOP — External Integration

## Objetivo

Configurar, implementar e verificar integrações externas sem inventar capacidades, resultados ou credenciais.

## Escopo

GitHub, bancos, APIs, scrapers, webhooks, serviços de design, storage e provedores de autenticação.

## Entradas

- Contrato da integração.
- Documentação oficial da API.
- Credenciais autorizadas.
- Schema de entrada e saída.
- Rate limits, termos de uso e restrições.
- Estratégia de fallback.

## Procedimento

1. Classificar a integração como `REQUIRED`, `OPTIONAL` ou `NOT_APPLICABLE`.
2. Confirmar a fonte oficial e os termos de uso.
3. Definir variáveis de ambiente sem incluir valores reais no Git.
4. Configurar o cliente com timeout, retries e validação.
5. Implementar adapter/repository isolado do domínio.
6. Criar fixture ou sandbox para testes.
7. Executar health check autenticado sem expor secrets.
8. Validar payload com schema.
9. Implementar logs sem PII e sem credenciais.
10. Testar sucesso, timeout, rate limit, payload inválido e indisponibilidade.
11. Documentar estado, limitações e última verificação.

## Scrapers

Além dos passos acima, registrar fonte, seletores reais, campos ausentes, paginação, cache, deduplicação, User-Agent, rate limit e data de verificação. Se a fonte estiver bloqueada, marcar `blocked` ou `not-verified`.

## Critérios de Sucesso

- [ ] Variáveis configuradas com segurança.
- [ ] Cliente inicializado.
- [ ] Health check confirmado.
- [ ] Schema validado.
- [ ] Retries e timeout configurados.
- [ ] Casos de falha testados.
- [ ] Documentação e relatório atualizados.

## Proibições

- Não colocar token em URL ou log.
- Não afirmar que uma chamada foi executada sem evidência.
- Não inventar campos ou dados extraídos.
- Não substituir integração real por mock silencioso.
- Não contornar bloqueios ou termos de uso.

## Relatório

```md
# Relatório — External Integration

**Integração:** [nome]
**Projeto:** [nome]
**Data:** YYYY-MM-DD
**Estado:** configured/verified/partial/blocked/not-verified

## Configuração
- Provider: [nome]
- Endpoint/projeto: [referência não sensível]
- Modo: [sandbox/production]

## Validações
- [ ] Autenticação
- [ ] Health check
- [ ] Schema
- [ ] Sucesso
- [ ] Falha e timeout
- [ ] Rate limit

## Dados
- Registros/payloads observados: [valor real ou não verificado]
- Campos ausentes: [lista]

## Limitações
- [descrição]

## Próximos passos
- [ação]
```

## Rollback e Desativação

Desabilitar a integração por feature flag ou configuração documentada, preservar dados já persistidos e garantir estado de erro compreensível para o usuário.

## Referências

- `integration-contracts.md`
- `anti-hallucination-rules.md`
- `risk-catalogue.md`