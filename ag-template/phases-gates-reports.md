# Phases, Gates & Reports — Fases, Gates e Relatórios

## Visão Geral

Este arquivo define as fases do projeto, os gates de validação entre fases e os relatórios obrigatórios.

---

## Fases do Projeto

### Fase 0: Setup

**Objetivo:** Preparar o ambiente para o projeto.

**Entregáveis:**
- [ ] Repositório criado
- [ ] Estrutura de pastas criada
- [ ] `.env.example` configurado
- [ ] `.gitignore` configurado
- [ ] `README.md` inicial
- [ ] Integrações básicas configuradas (GitHub, etc.)

**Gate de Entrada:**
- [ ] Projeto classificado (tipo, dimensão)
- [ ] Matriz de aplicabilidade gerada
- [ ] Stakeholders identificados

**Gate de Saída:**
- [ ] Todos os entregáveis presentes
- [ ] Validação do usuário
- [ ] Próxima fase planejada

---

### Fase 1: Documentação

**Objetivo:** Criar documentação completa do projeto.

**Entregáveis:**
- [ ] `1.visao.md` — Visão do produto
- [ ] `2.requisitos.md` — Requisitos funcionais
- [ ] `3.regras-negocio.md` — Regras de negócio
- [ ] `4.arquitetura.md` — Arquitetura
- [ ] `5.design.md` — Design (ou contrato Stitch)
- [ ] `6.modelo-dados.md` — Modelo de dados
- [ ] `7.backlog.md` — Backlog

**Gate de Entrada:**
- [ ] Fase 0 completa
- [ ] Validação do usuário

**Gate de Saída:**
- [ ] Todos os documentos criados
- [ ] Documentos validados pelo usuário
- [ ] Backlog priorizado
- [ ] Arquitetura aprovada

---

### Fase 2: Implementação - Fundação

**Objetivo:** Implementar a base do projeto.

**Entregáveis:**
- [ ] Projeto inicializado (Next.js, Vite, etc.)
- [ ] Estrutura de pastas implementada
- [ ] Configurações básicas (ESLint, Prettier, etc.)
- [ ] Integrações configuradas (GitHub, Stitch, etc.)
- [ ] Banco de dados configurado (se aplicável)
- [ ] Migrations criadas
- [ ] Seeds criados

**Gate de Entrada:**
- [ ] Fase 1 completa
- [ ] Validação do usuário
- [ ] Ambiente de desenvolvimento pronto

**Gate de Saída:**
- [ ] Projeto rodando localmente
- [ ] Integrações verificadas
- [ ] Banco conectado e com seeds
- [ ] Health checks passando

---

### Fase 3: Implementação - Core

**Objetivo:** Implementar funcionalidades principais.

**Entregáveis:**
- [ ] Entidades principais implementadas
- [ ] CRUDs implementados
- [ ] Autenticação implementada (se aplicável)
- [ ] Integrações implementadas
- [ ] Scrapers implementados (se aplicável)

**Gate de Entrada:**
- [ ] Fase 2 completa
- [ ] Validação do usuário
- [ ] Backlog priorizado

**Gate de Saída:**
- [ ] Funcionalidades principais implementadas
- [ ] Testes passando
- [ ] Integrações verificadas
- [ ] Validação do usuário

---

### Fase 4: Implementação - UI/UX

**Objetivo:** Implementar interface e experiência do usuário.

**Entregáveis:**
- [ ] Telas principais implementadas
- [ ] Componentes implementados
- [ ] Navegação implementada
- [ ] Responsividade implementada
- [ ] Acessibilidade básica implementada
- [ ] Fidelidade ao design verificada

**Gate de Entrada:**
- [ ] Fase 3 completa
- [ ] Design aprovado
- [ ] Validação do usuário

**Gate de Saída:**
- [ ] Telas implementadas com fidelidade
- [ ] Navegação funcional
- [ ] Responsivo em mobile e desktop
- [ ] Validação do usuário

---

### Fase 5: Integrações e Dados

**Objetivo:** Implementar integrações e fluxos de dados.

**Entregáveis:**
- [ ] Scrapers implementados e testados
- [ ] APIs externas integradas
- [ ] Webhooks configurados
- [ ] Jobs/automações implementados
- [ ] Dados populados
- [ ] Deduplicação implementada

**Gate de Entrada:**
- [ ] Fase 4 completa
- [ ] Integrações documentadas
- [ ] Validação do usuário

**Gate de Saída:**
- [ ] Integrações funcionando
- [ ] Dados populados e validados
- [ ] Scrapers executando
- [ ] Validação do usuário

---

### Fase 6: Testes e Qualidade

**Objetivo:** Garantir qualidade do projeto.

**Entregáveis:**
- [ ] Testes unitários implementados
- [ ] Testes de integração implementados
- [ ] Testes E2E implementados
- [ ] Testes manuais executados
- [ ] Bugs críticos resolvidos
- [ ] Performance otimizada

**Gate de Entrada:**
- [ ] Fase 5 completa
- [ ] Funcionalidades implementadas
- [ ] Validação do usuário

**Gate de Saída:**
- [ ] Cobertura de testes > 80%
- [ ] Testes E2E passando
- [ ] Bugs críticos resolvidos
- [ ] Performance aceitável
- [ ] Validação do usuário

---

### Fase 7: Deploy e Produção

**Objetivo:** Colocar projeto em produção.

**Entregáveis:**
- [ ] Ambiente de produção configurado
- [ ] CI/CD configurado
- [ ] Deploy executado
- [ ] Monitoramento configurado
- [ ] Logs configurados
- [ ] Documentação de operação

**Gate de Entrada:**
- [ ] Fase 6 completa
- [ ] Todos os testes passando
- [ ] Validação do usuário
- [ ] Aprovação para produção

**Gate de Saída:**
- [ ] Projeto em produção
- [ ] Health checks passando
- [ ] Monitoramento ativo
- [ ] Documentação de operação
- [ ] Validação do usuário

---

## Gates de Validação

### Gate Template

```md
## Gate: [Nome do Gate]

**Fase:** [Fase X]

**Data:** YYYY-MM-DD

**Critérios:**
- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

**Resultado:** `aprovado` | `reprovado` | `parcial`

**Observações:**
- Observação 1
- Observação 2

**Próximos Passos:**
- Passo 1
- Passo 2

**Aprovado por:** [Nome]
```

### Gates Obrigatórios

| Gate | Fase | Critérios Mínimos |
|---|---|---|
| Gate 0 | Setup | Estrutura, README, .env |
| Gate 1 | Documentação | Todos os documentos |
| Gate 2 | Fundação | Projeto rodando, integrações |
| Gate 3 | Core | Funcionalidades principais |
| Gate 4 | UI/UX | Telas, navegação, responsivo |
| Gate 5 | Integrações | Scrapers, APIs, dados |
| Gate 6 | Testes | Cobertura > 80%, E2E |
| Gate 7 | Deploy | Produção, monitoramento |

---

## Relatórios Obrigatórios

### Relatório de Fase

```md
# Relatório de Fase: [Nome da Fase]

**Projeto:** [Nome do Projeto]

**Período:** YYYY-MM-DD a YYYY-MM-DD

**Status:** `concluido` | `em-andamento` | `bloqueado`

## Entregáveis

### Concluídos
- [x] Entregável 1
- [x] Entregável 2

### Pendentes
- [ ] Entregável 3
- [ ] Entregável 4

## Métricas

- Progresso: X%
- Bugs: X abertos, Y críticos
- Testes: X% cobertura
- Performance: X ms (p95)

## Riscos

| Risco | Impacto | Probabilidade | Mitigação |
|---|---|---|---|
| Risco 1 | Alto | Média | Mitigação 1 |

## Próximos Passos

1. Passo 1
2. Passo 2
3. Passo 3

## Aprovação

**Aprovado por:** [Nome]
**Data:** YYYY-MM-DD
```

### Relatório de Gate

```md
# Relatório de Gate: [Nome do Gate]

**Projeto:** [Nome do Projeto]

**Fase:** [Fase X → Fase Y]

**Data:** YYYY-MM-DD

## Critérios

| Critério | Status | Observação |
|---|---|---|
| Critério 1 | ✅ | OK |
| Critério 2 | ✅ | OK |
| Critério 3 | ⚠️ | Parcial |

## Resultado

**Decisão:** `aprovado` | `aprovado-com-reservas` | `reprovado`

**Reservas:**
- Reserva 1
- Reserva 2

## Próximos Passos

1. Passo 1
2. Passo 2

## Aprovação

**Aprovado por:** [Nome]
**Data:** YYYY-MM-DD
```

### Relatório de Status (Semanal)

```md
# Relatório de Status — Semana X

**Projeto:** [Nome do Projeto]

**Período:** YYYY-MM-DD a YYYY-MM-DD

**Fase Atual:** [Fase X]

## Progresso

- Fase atual: X% concluída
- Fase anterior: concluída em YYYY-MM-DD
- Próxima fase: prevista para YYYY-MM-DD

## Concluído na Semana

- [x] Tarefa 1
- [x] Tarefa 2

## Pendente

- [ ] Tarefa 3
- [ ] Tarefa 4

## Riscos e Bloqueios

| Tipo | Descrição | Impacto | Ação |
|---|---|---|---|
| Risco | Risco 1 | Alto | Ação 1 |
| Bloqueio | Bloqueio 1 | Crítico | Ação 2 |

## Métricas

- Bugs: X abertos (Y críticos)
- Testes: X% cobertura
- Performance: X ms (p95)
- Deploy: X deploys na semana

## Próximos Passos

1. Passo 1
2. Passo 2
3. Passo 3
```

---

## Templates de Documentação por Fase

### Template: Visão do Produto

```md
# Visão do Produto

## Problema

[Descrição do problema]

## Solução

[Descrição da solução]

## Público-Alvo

[Descrição do público]

## Objetivos

- Objetivo 1
- Objetivo 2
- Objetivo 3

## Métricas de Sucesso

- Métrica 1
- Métrica 2
- Métrica 3

## Escopo

### Incluído
- Feature 1
- Feature 2

### Não Incluído
- Feature 3
- Feature 4
```

### Template: Requisitos Funcionais

```md
# Requisitos Funcionais

## RF001: [Nome do Requisito]

**Descrição:** [Descrição]

**Critérios de Aceite:**
- [ ] Critério 1
- [ ] Critério 2

**Prioridade:** `alta` | `média` | `baixa`

**Dependências:**
- Dependência 1

**Notas:**
- Nota 1
```

### Template: Arquitetura

```md
# Arquitetura

## Visão Geral

[Diagrama ou descrição]

## Componentes

### Frontend

- Tecnologia: [Next.js, React, etc.]
- Estrutura: [Pastas principais]

### Backend

- Tecnologia: [Node.js, FastAPI, etc.]
- Estrutura: [Pastas principais]

### Banco de Dados

- Tecnologia: [Firestore, PostgreSQL, etc.]
- Schema: [Referência]

## Integrações

| Integração | Tipo | Status |
|---|---|---|
| GitHub | REQUIRED | configured |
| Stitch | REQUIRED | configured |

## Fluxos Principais

### Fluxo 1: [Nome]

1. Passo 1
2. Passo 2
3. Passo 3
```

---

## Checklist de Validação por Fase

### Fase 0: Setup

- [ ] Repositório criado
- [ ] Estrutura de pastas criada
- [ ] `.env.example` configurado
- [ ] `.gitignore` configurado
- [ ] `README.md` inicial
- [ ] Integrações básicas configuradas

### Fase 1: Documentação

- [ ] `1.visao.md` criado
- [ ] `2.requisitos.md` criado
- [ ] `3.regras-negocio.md` criado
- [ ] `4.arquitetura.md` criado
- [ ] `5.design.md` criado (ou contrato Stitch)
- [ ] `6.modelo-dados.md` criado
- [ ] `7.backlog.md` criado
- [ ] Documentos validados pelo usuário

### Fase 2: Fundação

- [ ] Projeto inicializado
- [ ] Estrutura de pastas implementada
- [ ] Configurações básicas (ESLint, Prettier)
- [ ] Integrações configuradas
- [ ] Banco configurado (se aplicável)
- [ ] Migrations criadas
- [ ] Seeds criados
- [ ] Projeto rodando localmente

### Fase 3: Core

- [ ] Entidades principais implementadas
- [ ] CRUDs implementados
- [ ] Autenticação implementada (se aplicável)
- [ ] Integrações implementadas
- [ ] Scrapers implementados (se aplicável)
- [ ] Testes unitários passando

### Fase 4: UI/UX

- [ ] Telas principais implementadas
- [ ] Componentes implementados
- [ ] Navegação implementada
- [ ] Responsividade implementada
- [ ] Acessibilidade básica implementada
- [ ] Fidelidade ao design verificada

### Fase 5: Integrações e Dados

- [ ] Scrapers implementados e testados
- [ ] APIs externas integradas
- [ ] Webhooks configurados
- [ ] Jobs/automações implementados
- [ ] Dados populados
- [ ] Deduplicação implementada

### Fase 6: Testes e Qualidade

- [ ] Testes unitários implementados
- [ ] Testes de integração implementados
- [ ] Testes E2E implementados
- [ ] Testes manuais executados
- [ ] Bugs críticos resolvidos
- [ ] Performance otimizada
- [ ] Cobertura > 80%

### Fase 7: Deploy e Produção

- [ ] Ambiente de produção configurado
- [ ] CI/CD configurado
- [ ] Deploy executado
- [ ] Monitoramento configurado
- [ ] Logs configurados
- [ ] Documentação de operação
- [ ] Health checks passando

---

## Referências

- `GLOBAL-RULES.md` — Regras globais
- `GLOBAL-WORKFLOW.md` — Workflow global
- `project-profiles.md` — Tipos de projeto
- `applicability-matrix.md` — Matriz de aplicabilidade
- `integration-contracts.md` — Contratos de integração
- `anti-hallucination-rules.md` — Regras anti-alucinação
- `backlog-guidelines.md` — Diretrizes de backlog