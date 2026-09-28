# Project Health Checklist — Checklist de Saúde do Projeto

## Visão Geral

Este arquivo define o checklist para avaliar a saúde de um projeto em qualquer ponto do desenvolvimento.

---

## Categorias de Saúde

1. **Documentação** — Documentação completa e atualizada
2. **Código** — Código limpo, testado e mantível
3. **Integrações** — Integrações configuradas e funcionando
4. **Dados** — Dados populados e consistentes
5. **UI/UX** — Interface fiel ao design e usável
6. **Testes** — Testes automatizados com boa cobertura
7. **Deploy** — Deploy configurado e monitorado
8. **Segurança** — Segurança básica implementada

---

## Checklist Completo

### 1. Documentação

#### 1.1. Documentação do Projeto

- [ ] `0.project-profile.md` — Tipo, dimensão, integrações
- [ ] `1.visao.md` — Visão do produto
- [ ] `2.requisitos.md` — Requisitos funcionais
- [ ] `3.regras-negocio.md` — Regras de negócio
- [ ] `4.arquitetura.md` — Arquitetura
- [ ] `5.design.md` — Design (ou contrato Stitch)
- [ ] `6.modelo-dados.md` — Modelo de dados
- [ ] `7.backlog.md` — Backlog

#### 1.2. Documentação Técnica

- [ ] `documentation/architecture/` — ADRs e diagramas
- [ ] `documentation/guides/` — Guias (onboarding, dev, deploy)
- [ ] READMEs de pastas principais

#### 1.3. Documentação de Integrações

- [ ] GitHub: estado e configuração documentados
- [ ] Google Stitch: contrato de fidelidade documentado
- [ ] Banco: schema e migrations documentados
- [ ] Scrapers: fontes, campos, seletores documentados

#### 1.4. Atualização

- [ ] Documentação atualizada nas últimas 2 semanas
- [ ] Changelog atualizado
- [ ] ADRs para decisões recentes

---

### 2. Código

#### 2.1. Estrutura

- [ ] Estrutura de pastas segue `folder-structure.md`
- [ ] Nomenclatura consistente (kebab-case, PascalCase)
- [ ] Profundidade máxima de 4 níveis

#### 2.2. Qualidade

- [ ] ESLint passando sem erros
- [ ] Prettier formatado
- [ ] TypeScript sem erros
- [ ] Sem `any` explícito
- [ ] Sem `console.log` em produção

#### 2.3. Organização

- [ ] Componentes pequenos (< 200 linhas)
- [ ] Funções pequenas (< 50 linhas)
- [ ] Imports organizados
- [ ] Exports claros

#### 2.4. Performance

- [ ] Sem re-renders desnecessários
- [ ] Lazy loading de rotas pesadas
- [ ] Imagens otimizadas
- [ ] Bundle size aceitável (< 500KB inicial)

---

### 3. Integrações

#### 3.1. GitHub

- [ ] `GITHUB_ENABLED = true`
- [ ] `GITHUB_OWNER` definido
- [ ] `GITHUB_REPOSITORY` definido
- [ ] Autenticação verificada (`gh auth status`)
- [ ] Repositório existe
- [ ] Remote configurado
- [ ] Push inicial executado

**Estado:** `configured` | `verified` | `not-configured`

#### 3.2. Google Stitch

- [ ] `GOOGLE_STITCH_ENABLED = true`
- [ ] `GOOGLE_STITCH_API_KEY` definido
- [ ] `GOOGLE_STITCH_PROJECT_ID` definido
- [ ] Projeto encontrado
- [ ] Telas importadas
- [ ] Fidelidade verificada (> 95%)

**Estado:** `configured` | `verified` | `not-configured`

#### 3.3. Banco de Dados

- [ ] Variáveis de ambiente configuradas
- [ ] Cliente inicializado
- [ ] Conexão verificada
- [ ] Collections/tables criadas
- [ ] Migrations versionadas
- [ ] Seeds executados
- [ ] Health check passando

**Estado:** `configured` | `verified` | `not-configured`

#### 3.4. Scrapers

Para cada scraper:

- [ ] Fonte documentada
- [ ] Seletores implementados
- [ ] Parser implementado
- [ ] Normalização implementada
- [ ] Validação de schema
- [ ] Deduplicação implementada
- [ ] Rate limiting implementado
- [ ] Retries implementados
- [ ] Timeout implementado
- [ ] Cache implementado
- [ ] Logs implementados
- [ ] Testes com fixtures
- [ ] Última execução documentada

**Estado:** `verified` | `partially-implemented` | `not-verified` | `blocked`

---

### 4. Dados

#### 4.1. População

- [ ] Seeds executados
- [ ] Dados de exemplo presentes
- [ ] Mínimo de 10 registros por entidade principal

#### 4.2. Consistência

- [ ] Sem dados duplicados
- [ ] Chaves estrangeiras válidas
- [ ] Campos obrigatórios preenchidos
- [ ] Tipos de dados corretos

#### 4.3. Validação

- [ ] Schema validado (Zod, Pydantic, etc.)
- [ ] Validação no frontend
- [ ] Validação no backend
- [ ] Mensagens de erro claras

---

### 5. UI/UX

#### 5.1. Fidelidade ao Design

- [ ] Cores fiéis ao design
- [ ] Fonts fiéis ao design
- [ ] Spacing fiel ao design
- [ ] Componentes fiéis ao design
- [ ] Layout fiel ao design

**Fidelidade:** > 95% | > 90% | > 80% | < 80%

#### 5.2. Responsividade

- [ ] Mobile (< 640px) testado
- [ ] Tablet (640-1024px) testado
- [ ] Desktop (> 1024px) testado
- [ ] Navegação mobile funcional (bottom nav)
- [ ] Navegação desktop funcional (top nav)

#### 5.3. Acessibilidade

- [ ] Contraste adequado
- [ ] Focus states visíveis
- [ ] Labels em inputs
- [ ] Alt text em imagens
- [ ] Navegação por teclado funcional

#### 5.4. Usabilidade

- [ ] Loading states presentes
- [ ] Error states presentes
- [ ] Empty states presentes
- [ ] Feedback de ações
- [ ] Navegação intuitiva

---

### 6. Testes

#### 6.1. Cobertura

- [ ] Cobertura unitária > 80%
- [ ] Componentes críticos testados
- [ ] Utilitários testados
- [ ] Hooks testados

#### 6.2. Tipos de Teste

- [ ] Testes unitários implementados
- [ ] Testes de integração implementados
- [ ] Testes de componentes implementados
- [ ] Testes E2E implementados

#### 6.3. Qualidade

- [ ] Testes descrevem comportamento
- [ ] Testes são independentes
- [ ] Testes são reproduzíveis
- [ ] Testes falham de forma clara

#### 6.4. Execução

- [ ] Testes rodam em CI
- [ ] Testes rodam localmente
- [ ] Testes E2E rodam em staging
- [ ] Relatório de cobertura disponível

---

### 7. Deploy

#### 7.1. Configuração

- [ ] Ambiente de produção configurado
- [ ] Variáveis de ambiente em produção
- [ ] CI/CD configurado
- [ ] Deploy automático em main

#### 7.2. Monitoramento

- [ ] Health checks configurados
- [ ] Logs em produção
- [ ] Métricas de performance
- [ ] Alertas configurados

#### 7.3. Operação

- [ ] Documentação de deploy
- [ ] Runbooks de operação
- [ ] Plano de rollback
- [ ] Backup configurado (se aplicável)

---

### 8. Segurança

#### 8.1. Secrets

- [ ] `.env` não commitado
- [ ] `.env.example` presente
- [ ] Secrets em variáveis de ambiente
- [ ] Secrets rotacionados periodicamente

#### 8.2. Inputs

- [ ] Validação de inputs no frontend
- [ ] Validação de inputs no backend
- [ ] Sanitização de outputs
- [ ] Parameterized queries (SQL injection)

#### 8.3. Autenticação

- [ ] Autenticação implementada
- [ ] Autorização implementada
- [ ] Tokens seguros (JWT, etc.)
- [ ] Refresh tokens implementados
- [ ] Logout seguro

#### 8.4. Proteção

- [ ] CSRF protection
- [ ] XSS protection
- [ ] Rate limiting em APIs
- [ ] CORS configurado

---

## Matriz de Saúde

### Score por Categoria

| Categoria | Score (0-100) | Peso | Weighted |
|---|---|---|---|
| Documentação | | 10% | |
| Código | | 20% | |
| Integrações | | 20% | |
| Dados | | 10% | |
| UI/UX | | 15% | |
| Testes | | 15% | |
| Deploy | | 5% | |
| Segurança | | 5% | |
| **Total** | | **100%** | |

### Cálculo do Score

Para cada categoria:

```
Score = (Itens marcados / Total de itens) * 100
```

Score total:

```
Total = Σ(Score * Peso)
```

### Interpretação

| Score | Saúde | Ação |
|---|---|---|
| 90-100 | Excelente | Manter, melhorar continuamente |
| 75-89 | Boa | Resolver gaps menores |
| 60-74 | Regular | Resolver gaps críticos |
| 40-59 | Ruim | Plano de ação necessário |
| 0-39 | Crítica | Intervenção imediata |

---

## Template de Relatório

```md
# Project Health Report — [Nome do Projeto]

**Data:** YYYY-MM-DD

**Avaliador:** [Nome]

## Score por Categoria

| Categoria | Score | Status |
|---|---|---|
| Documentação | X% | 🟢 |
| Código | X% | 🟢 |
| Integrações | X% | 🟡 |
| Dados | X% | 🟢 |
| UI/UX | X% | 🟡 |
| Testes | X% | 🔴 |
| Deploy | X% | 🟢 |
| Segurança | X% | 🟢 |

## Score Total

**Total:** X%

**Saúde:** [Excelente | Boa | Regular | Ruim | Crítica]

## Gaps Críticos

1. [Gap 1] — Categoria: [Nome] — Impacto: [Alto/Médio/Baixo]
2. [Gap 2] — Categoria: [Nome] — Impacto: [Alto/Médio/Baixo]

## Plano de Ação

| Ação | Categoria | Prioridade | Responsável | Prazo |
|---|---|---|---|---|
| Ação 1 | Testes | Alta | [Nome] | YYYY-MM-DD |
| Ação 2 | Integrações | Média | [Nome] | YYYY-MM-DD |

## Próximos Passos

1. [Passo 1]
2. [Passo 2]
3. [Passo 3]
```

---

## Frequência de Avaliação

| Tipo | Frequência | Responsável |
|---|---|---|
| Auto-avaliação | Diária | Desenvolvedor |
| Avaliação formal | Semanal | Tech Lead |
| Avaliação completa | Mensal | Time |
| Auditoria | Trimestral | Externo |

---

## Referências

- `folder-structure.md` — Estrutura de pastas
- `minimal-documentation.md` — Documentação mínima
- `integration-contracts.md` — Contratos de integração
- `GLOBAL-RULES.md` — Regras globais