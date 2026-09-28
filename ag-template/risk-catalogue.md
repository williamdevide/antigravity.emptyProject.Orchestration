# Risk Catalogue — Catálogo de Riscos

## Visão Geral

Este arquivo cataloga riscos comuns em projetos de software, com descrições, impactos, probabilidades e mitigações.

---

## Categorias de Risco

1. **Técnicos** — Relacionados a tecnologia e implementação
2. **Integrações** — Relacionados a APIs e serviços externos
3. **Dados** — Relacionados a dados e banco
4. **Prazo** — Relacionados a tempo e entregas
5. **Escopo** — Relacionados a requisitos e mudanças
6. **Segurança** — Relacionados a segurança e compliance
7. **Operação** — Relacionados a deploy e produção

---

## Riscos Técnicos

### TEC-001: Complexidade Não Estimada

**Descrição:** A complexidade real da implementação é maior que o estimado.

**Impacto:** Alto — Atraso significativo, estouro de orçamento.

**Probabilidade:** Média — Comum em projetos com tecnologia nova.

**Sinais:**
- Tarefas levando 2-3x mais que o estimado
- Múltiplas refatorações necessárias
- Bugs recorrentes na mesma área

**Mitigação:**
- Quebrar tarefas em partes menores
- Fazer spikes de investigação
- Adicionar buffer de 20-30% nas estimativas
- Revisar estimativas semanalmente

**Contingência:**
- Reduzir escopo não essencial
- Adicionar recursos (se possível)
- Estender prazo

---

### TEC-002: Tecnologia Nova ou Não Dominada

**Descrição:** A equipe não tem experiência suficiente com a tecnologia escolhida.

**Impacto:** Alto — Curva de aprendizado, implementação lenta, bugs.

**Probabilidade:** Média — Depende da tecnologia e da equipe.

**Sinais:**
- Múltiplas tentativas para implementar features simples
- Documentação constantemente consultada
- Dependência de tutoriais e exemplos

**Mitigação:**
- Fazer proof of concept antes
- Investir em treinamento
- Pair programming
- Consultar especialistas

**Contingência:**
- Simplificar implementação
- Usar bibliotecas e frameworks maduros
- Postergar features complexas

---

### TEC-003: Dívida Técnica Acumulada

**Descrição:** Código com qualidade insuficiente acumula ao longo do tempo.

**Impacto:** Médio — Velocidade reduzida, bugs frequentes.

**Probabilidade:** Alta — Comum em projetos com pressão de prazo.

**Sinais:**
- Código duplicado
- Funções muito longas
- Testes faltando
- Comentários do tipo "TODO: refatorar"

**Mitigação:**
- Code review rigoroso
- Definir Definition of Done clara
- Alocar tempo para refatoração (20% do sprint)
- Métricas de qualidade (ESLint, cobertura)

**Contingência:**
- Sprint de refatoração
- Reescrever módulos críticos
- Adicionar testes gradualmente

---

### TEC-004: Performance Insuficiente

**Descrição:** A aplicação não atende aos requisitos de performance.

**Impacto:** Alto — Experiência do usuário ruim, abandono.

**Probabilidade:** Média — Depende da complexidade e otimização.

**Sinais:**
- Tempo de carregamento > 3s
- Lags e travamentos
- Métricas de Core Web Vitals ruins

**Mitigação:**
- Profiling desde o início
- Otimizar bundle size
- Lazy loading
- Cache estratégico
- CDN para assets

**Contingência:**
- Reduzir features pesadas
- Otimizar queries de banco
- Escalar infraestrutura

---

## Riscos de Integração

### INT-001: API Externa Instável

**Descrição:** API de terceiro apresenta instabilidade ou indisponibilidade.

**Impacto:** Alto — Features quebradas, experiência do usuário afetada.

**Probabilidade:** Média — Depende do provedor.

**Sinais:**
- Timeouts frequentes
- Erros 5xx recorrentes
- Mudanças não documentadas na API

**Mitigação:**
- Implementar retries com backoff
- Implementar fallback
- Cache de respostas
- Monitorar saúde da API
- Ter provedor alternativo

**Contingência:**
- Usar dados cacheados
- Desabilitar feature temporariamente
- Migrar para provedor alternativo

---

### INT-002: Scraper Bloqueado

**Descrição:** Scraper é bloqueado pelo site alvo (CAPTCHA, IP ban, mudanças no HTML).

**Impacto:** Alto — Dados não atualizados, feature quebrada.

**Probabilidade:** Alta — Sites mudam estrutura frequentemente.

**Sinais:**
- Requests retornando CAPTCHA
- IP bloqueado
- Seletores CSS não funcionam mais
- Dados incompletos

**Mitigação:**
- Respeitar robots.txt
- Rate limiting conservador
- User-Agent rotation
- Proxy rotation
- Monitorar mudanças no HTML
- Testes automatizados com fixtures

**Contingência:**
- Atualizar seletores
- Usar API oficial (se disponível)
- Parceria com provedor de dados
- Dados manuais temporariamente

---

### INT-003: Google Stitch Indisponível

**Descrição:** Google Stitch não está acessível ou tem limitações.

**Impacto:** Médio — Design não pode ser importado, atraso na UI.

**Probabilidade:** Baixa — Serviço gerenciado pelo Google.

**Sinais:**
- API retornando erros
- Assets não carregam
- Timeouts na importação

**Mitigação:**
- Exportar assets localmente
- Ter `5.design.md` como fallback
- Cache de exports
- Monitorar saúde do serviço

**Contingência:**
- Usar especificação de design local
- Implementar UI baseada em documentação
- Aguardar serviço voltar

---

### INT-004: GitHub Issues com Rate Limit

**Descrição:** API do GitHub atinge rate limit ao criar issues automaticamente.

**Impacto:** Baixo — Automação de backlog afetada.

**Probabilidade:** Baixa — Rate limits são generosos.

**Sinais:**
- Erros 403 da API do GitHub
- Issues não sendo criadas

**Mitigação:**
- Respeitar rate limits
- Batch de criação de issues
- Token com limites maiores (se necessário)

**Contingência:**
- Criar issues manualmente
- Postergar automação

---

## Riscos de Dados

### DAT-001: Dados Inconsistentes

**Descrição:** Dados no banco estão inconsistentes ou corrompidos.

**Impacto:** Alto — Features quebradas, dados perdidos.

**Probabilidade:** Baixa — Com validação adequada.

**Sinais:**
- Queries retornando dados inesperados
- Erros de validação
- Relacionamentos quebrados

**Mitigação:**
- Validação de schema (Zod, Pydantic)
- Validação no frontend e backend
- Migrations testadas
- Seeds validados
- Backup regular

**Contingência:**
- Scripts de correção de dados
- Restore de backup
- Re-popular com seeds

---

### DAT-002: Dados Duplicados

**Descrição:** Registros duplicados no banco (especialmente de scrapers).

**Impacto:** Médio — Experiência do usuário ruim, dados inflados.

**Probabilidade:** Média — Scrapers podem pegar dados repetidos.

**Sinais:**
- Mesmos itens aparecendo múltiplas vezes
- Contagem de registros maior que o esperado
- Queries retornando duplicados

**Mitigação:**
- Chaves únicas (UUID, slug)
- Deduplicação no scraper
- Validação antes de insert
- Jobs de deduplicação periódicos

**Contingência:**
- Script de deduplicação
- Remover duplicados manualmente
- Re-executar scraper com deduplicação

---

### DAT-003: Dados Insuficientes

**Descrição:** Banco com poucos dados para desenvolvimento ou teste.

**Impacto:** Médio — Desenvolvimento lento, testes limitados.

**Probabilidade:** Média — Scrapers podem não ter executado.

**Sinais:**
- Listagens vazias ou com poucos itens
- Queries retornando 0 resultados
- Dependência de dados mockados

**Mitigação:**
- Seeds robustos (mínimo 50-100 registros)
- Fixtures realistas
- Scrapers executados cedo
- Dados de exemplo diversificados

**Contingência:**
- Poplar com dados de exemplo
- Usar fixtures
- Desenvolver com dados mockados

---

## Riscos de Prazo

### PRA-001: Escopo Subestimado

**Descrição:** O escopo do projeto é maior que o estimado inicialmente.

**Impacto:** Alto — Atraso significativo, estouro de orçamento.

**Probabilidade:** Alta — Comum em projetos de software.

**Sinais:**
- Novas requirements surgindo
- Tarefas levando mais tempo que o estimado
- Backlog crescendo

**Mitigação:**
- Definir MVP claramente
- Priorizar rigorosamente
- Revisar escopo semanalmente
- Comunicar stakeholders

**Contingência:**
- Reduzir escopo não essencial
- Postergar features para fases futuras
- Negociar prazo com stakeholders

---

### PRA-002: Dependências Externas Atrasam

**Descrição:** Dependências externas (APIs, designers, outros times) atrasam.

**Impacto:** Alto — Bloqueio de tarefas críticas.

**Probabilidade:** Média — Depende de fatores externos.

**Sinais:**
- Tarefas bloqueadas aguardando terceiros
- Prazos de terceiros não cumpridos
- Comunicação lenta

**Mitigação:**
- Identificar dependências cedo
- Ter planos alternativos
- Comunicação frequente
- Buffer de tempo para dependências

**Contingência:**
- Trabalhar em tarefas não bloqueadas
- Implementar mocks/fallbacks
- Escalar para gestão

---

## Riscos de Escopo

### ESC-001: Scope Creep

**Descrição:** Requisitos adicionais são adicionados sem ajuste de prazo.

**Impacto:** Alto — Atraso, estouro de orçamento, qualidade reduzida.

**Probabilidade:** Alta — Comum em projetos ágeis.

**Sinais:**
- "Só mais uma featurezinha"
- Requisitos mudando durante desenvolvimento
- Backlog crescendo sem priorização

**Mitigação:**
- Definir MVP claramente
- Change request formal
- Priorização rigorosa
- Comunicar impacto de mudanças

**Contingência:**
- Negociar prazo
- Reduzir outras features
- Postergar para próxima fase

---

### ESC-002: Requisitos Ambíguos

**Descrição:** Requisitos não são claros ou são interpretados de forma diferente.

**Impacto:** Médio — Retrabalho, bugs, frustração.

**Probabilidade:** Média — Comum em comunicação assíncrona.

**Sinais:**
- Implementação não atende expectativa
- Múltiplas interpretações possíveis
- Perguntas frequentes sobre requisitos

**Mitigação:**
- Requisitos escritos e claros
- Critérios de aceite explícitos
- Exemplos e protótipos
- Validação com stakeholders

**Contingência:**
- Refatorar implementação
- Clarificar requisitos
- Re-validar com stakeholders

---

## Riscos de Segurança

### SEG-001: Secrets Expostos

**Descrição:** Secrets (tokens, senhas, chaves) são expostos acidentalmente.

**Impacto:** Crítico — Comprometimento de contas, vazamento de dados.

**Probabilidade:** Baixa — Com práticas adequadas.

**Sinais:**
- `.env` commitado
- Tokens em logs
- Chaves em código

**Mitigação:**
- `.env` no `.gitignore`
- Usar secrets manager
- Rotacionar secrets periodicamente
- Scanner de secrets (git-secrets, etc.)

**Contingência:**
- Rotacionar secrets imediatamente
- Revogar tokens expostos
- Auditar acesso

---

### SEG-002: Vulnerabilidade em Dependência

**Descrição:** Dependência do projeto tem vulnerabilidade de segurança.

**Impacto:** Alto — Comprometimento da aplicação.

**Probabilidade:** Média — Dependências têm vulnerabilidades frequentemente.

**Sinais:**
- Alertas de segurança (Dependabot, etc.)
- CVEs publicados para dependências
- Versões desatualizadas

**Mitigação:**
- Atualizar dependências regularmente
- Usar Dependabot ou similar
- Auditar dependências (npm audit, etc.)
- Minimizar dependências

**Contingência:**
- Atualizar para versão segura
- Substituir dependência
- Aplicar patch de segurança

---

## Riscos de Operação

### OPE-001: Deploy Falha

**Descrição:** Deploy em produção falha ou introduz bugs.

**Impacto:** Alto — Aplicação indisponível ou quebrada.

**Probabilidade:** Média — Depende da qualidade dos testes.

**Sinais:**
- Testes falhando
- Mudanças grandes sem teste adequado
- Deploy manual sem checklist

**Mitigação:**
- CI/CD automatizado
- Testes automatizados
- Deploy em staging primeiro
- Feature flags
- Rollback automático

**Contingência:**
- Rollback imediato
- Hotfix
- Comunicação transparente

---

### OPE-002: Monitoramento Insuficiente

**Descrição:** Produção sem monitoramento adequado, problemas não são detectados.

**Impacto:** Alto — Problemas persistem sem detecção.

**Probabilidade:** Média — Comum em projetos iniciais.

**Sinais:**
- Sem alertas configurados
- Logs não centralizados
- Métricas não monitoradas

**Mitigação:**
- Health checks
- Logs centralizados
- Métricas de performance
- Alertas configurados
- On-call definido

**Contingência:**
- Implementar monitoramento urgente
- Check manual periódico
- Feedback de usuários

---

## Matriz de Riscos

| Risco | Impacto | Probabilidade | Score | Prioridade |
|---|---|---|---|---|
| TEC-001 | Alto | Média | 6 | Alta |
| TEC-002 | Alto | Média | 6 | Alta |
| INT-001 | Alto | Média | 6 | Alta |
| INT-002 | Alto | Alta | 8 | Crítica |
| DAT-002 | Médio | Média | 4 | Média |
| PRA-001 | Alto | Alta | 8 | Crítica |
| ESC-001 | Alto | Alta | 8 | Crítica |
| SEG-001 | Crítico | Baixa | 4 | Média |

**Score = Impacto (1-4) × Probabilidade (1-4)**

**Prioridade:**
- 12-16: Crítica
- 8-11: Alta
- 4-7: Média
- 1-3: Baixa

---

## Template de Registro de Risco

```md
### [CÓDIGO]: [Nome do Risco]

**Categoria:** [Técnico | Integração | Dados | Prazo | Escopo | Segurança | Operação]

**Descrição:**
[Descrição do risco]

**Impacto:** [Baixo | Médio | Alto | Crítico]

**Probabilidade:** [Baixa | Média | Alta]

**Score:** X

**Prioridade:** [Baixa | Média | Alta | Crítica]

**Sinais:**
- Sinal 1
- Sinal 2

**Mitigação:**
- Mitigação 1
- Mitigação 2

**Contingência:**
- Contingência 1
- Contingência 2

**Responsável:** [Nome]

**Status:** [Identificado | Monitorado | Mitigado | Ocorrido | Fechado]

**Data de Identificação:** YYYY-MM-DD

**Última Atualização:** YYYY-MM-DD
```

---

## Referências

- `project-health-checklist.md` — Checklist de saúde
- `phases-gates-reports.md` — Fases, gates e reports
- `GLOBAL-RULES.md` — Regras globais