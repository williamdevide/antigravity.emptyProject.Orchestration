# Backlog Guidelines — Diretrizes de Backlog

## Visão Geral

Este arquivo define as diretrizes para criação, estruturação e manutenção do backlog de projetos.

---

## Estrutura do Backlog

### Arquivo Principal

O backlog principal deve estar em:

```text
/documentation/project/7.backlog.md
```

### Estrutura do Arquivo

```md
# Backlog — [Nome do Projeto]

## Visão Geral

- **Total de Histórias:** X
- **Concluídas:** Y
- **Em Progresso:** Z
- **Pendentes:** W

## Épicos

### Épico 1: [Nome]

**Descrição:** [Descrição do épico]

**Histórias:**
- [ ] HIST-001
- [ ] HIST-002

### Épico 2: [Nome]

**Descrição:** [Descrição do épico]

**Histórias:**
- [ ] HIST-003
- [ ] HIST-004

## Histórias

### HIST-001: [Nome da História]

**Épico:** [Nome do Épico]

**Descrição:**
Como [persona], quero [ação], para [benefício].

**Critérios de Aceite:**
- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

**Prioridade:** `alta` | `média` | `baixa`

**Estimativa:** X pontos

**Status:** `backlog` | `selected` | `in-progress` | `done`

**Dependências:**
- HIST-XXX
- Integração Y

**Notas:**
- Nota 1
- Nota 2

---

### HIST-002: [Nome da História]

...
```

---

## Tipos de Histórias

### História de Feature

**Propósito:** Implementar funcionalidade para o usuário.

**Template:**
```md
### HIST-XXX: [Nome da Feature]

**Épico:** [Nome do Épico]

**Descrição:**
Como [persona], quero [ação], para [benefício].

**Critérios de Aceite:**
- [ ] Critério 1
- [ ] Critério 2

**Prioridade:** `alta`

**Estimativa:** X pontos

**Status:** `backlog`
```

### História de Integração

**Propósito:** Configurar ou implementar integração.

**Template:**
```md
### HIST-XXX: Integração [Nome]

**Épico:** Integrações

**Descrição:**
Como desenvolvedor, quero [integração], para [benefício].

**Critérios de Aceite:**
- [ ] Variáveis de ambiente configuradas
- [ ] Cliente inicializado
- [ ] Conexão verificada
- [ ] CRUD/operacoes implementadas
- [ ] Testes criados
- [ ] Documentação atualizada

**Prioridade:** `alta`

**Estimativa:** X pontos

**Status:** `backlog`
```

### História de Infraestrutura

**Propósito:** Configurar infraestrutura ou deploy.

**Template:**
```md
### HIST-XXX: [Nome da Infra]

**Épico:** Infraestrutura

**Descrição:**
Como operador, quero [infraestrutura], para [benefício].

**Critérios de Aceite:**
- [ ] Ambiente configurado
- [ ] CI/CD configurado
- [ ] Deploy executado
- [ ] Monitoramento configurado
- [ ] Documentação de operação

**Prioridade:** `alta`

**Estimativa:** X pontos

**Status:** `backlog`
```

### História de Dívida Técnica

**Propósito:** Resolver dívida técnica.

**Template:**
```md
### HIST-XXX: [Nome da Dívida]

**Épico:** Dívida Técnica

**Descrição:**
Como desenvolvedor, quero [refatoração], para [benefício].

**Critérios de Aceite:**
- [ ] Código refatorado
- [ ] Testes passando
- [ ] Documentação atualizada

**Prioridade:** `média`

**Estimativa:** X pontos

**Status:** `backlog`
```

### História de Bug

**Propósito:** Corrigir bug.

**Template:**
```md
### HIST-XXX: Bug [Descrição]

**Épico:** Bugs

**Descrição:**
[Descrição do bug]

**Passos para Reproduzir:**
1. Passo 1
2. Passo 2
3. Passo 3

**Comportamento Esperado:**
[Descrição]

**Comportamento Atual:**
[Descrição]

**Critérios de Aceite:**
- [ ] Bug corrigido
- [ ] Teste adicionado
- [ ] Validação manual

**Prioridade:** `alta` | `crítica`

**Estimativa:** X pontos

**Status:** `backlog`
```

---

## Priorização

### Níveis de Prioridade

| Prioridade | Descrição | Quando Usar |
|---|---|---|
| `crítica` | Bloqueia o projeto | Bugs críticos, segurança |
| `alta` | Essencial para MVP | Features principais |
| `média` | Importante, mas não essencial | Features secundárias |
| `baixa` | Nice to have | Melhorias, otimizações |

### Matriz de Priorização

| Impacto | Esforço | Prioridade |
|---|---|---|
| Alto | Baixo | `alta` |
| Alto | Médio | `alta` |
| Alto | Alto | `média` |
| Médio | Baixo | `média` |
| Médio | Médio | `média` |
| Médio | Alto | `baixa` |
| Baixo | Baixo | `baixa` |
| Baixo | Médio | `baixa` |
| Baixo | Alto | `baixa` |

---

## Estimativa

### Pontos de História

| Pontos | Descrição | Exemplo |
|---|---|---|
| 1 | Muito pequeno | Ajuste de texto |
| 2 | Pequeno | Componente simples |
| 3 | Médio | Feature pequena |
| 5 | Grande | Feature média |
| 8 | Muito grande | Feature complexa |
| 13 | Enorme | Épico, quebrar |

### T-Shirt Sizing

| Tamanho | Pontos | Descrição |
|---|---|---|
| XS | 1-2 | Muito pequeno |
| S | 3 | Pequeno |
| M | 5 | Médio |
| L | 8 | Grande |
| XL | 13 | Muito grande |

---

## Critérios de Aceite

### Padrão GIVEN-WHEN-THEN

```md
**Critérios de Aceite:**

**Cenário 1: [Nome do Cenário]**
- **Dado** [contexto]
- **Quando** [ação]
- **Então** [resultado]

**Cenário 2: [Nome do Cenário]**
- **Dado** [contexto]
- **Quando** [ação]
- **Então** [resultado]
```

### Exemplo

```md
### HIST-001: Listar Comics

**Descrição:**
Como usuário, quero ver uma lista de quadrinhos, para descobrir novos títulos.

**Critérios de Aceite:**

**Cenário 1: Listar todos os comics**
- **Dado** que estou na página inicial
- **Quando** a página carrega
- **Então** vejo uma lista de quadrinhos
- **E** cada item mostra título, editora e capa

**Cenário 2: Paginação**
- **Dado** que há mais de 20 comics
- **Quando** rolo a página
- **Então** novos comics são carregados
- **E** não há duplicação

**Cenário 3: Estado vazio**
- **Dado** que não há comics
- **Quando** a página carrega
- **Então** vejo uma mensagem de "Nenhum quadrinho encontrado"
```

---

## Definição de Pronto (DoD)

### DoD para Features

- [ ] Código implementado
- [ ] Testes unitários passando
- [ ] Testes de integração passando
- [ ] Code review aprovado
- [ ] Documentação atualizada
- [ ] Deploy em staging
- [ ] Validação manual

### DoD para Integrações

- [ ] Variáveis de ambiente configuradas
- [ ] Cliente inicializado
- [ ] Conexão verificada
- [ ] CRUD/operacoes implementadas
- [ ] Testes criados
- [ ] Logs configurados
- [ ] Documentação atualizada
- [ ] Validação manual

### DoD para Bugs

- [ ] Bug corrigido
- [ ] Teste adicionado
- [ ] Validação manual
- [ ] Deploy em staging
- [ ] Validação do usuário (se aplicável)

---

## Backlog por Tipo de Projeto

### Tipo 1: Landing Page

**Épicos Típicos:**
- Setup
- Conteúdo
- SEO
- Deploy

**Histórias Típicas:**
- CONFIG-001: Configurar projeto Next.js
- CONTENT-001: Implementar hero section
- CONTENT-002: Implementar features section
- SEO-001: Configurar meta tags
- DEPLOY-001: Configurar Vercel

### Tipo 2: Produto Web com Backend

**Épicos Típicos:**
- Setup
- Autenticação
- Entidades Principais
- Integrações
- UI/UX
- Deploy

**Histórias Típicas:**
- AUTH-001: Implementar login
- AUTH-002: Implementar registro
- ENT-001: CRUD de [Entidade]
- INT-001: Integração GitHub
- UI-001: Implementar home
- DEPLOY-001: Configurar produção

### Tipo 3: Produto com Integrações

**Épicos Típicos:**
- Setup
- Entidades
- Scrapers
- APIs Externas
- UI/UX
- Deploy

**Histórias Típicas:**
- SCRAP-001: Scraper [Fonte]
- SCRAP-002: Normalização de dados
- SCRAP-003: Deduplicação
- API-001: Integração [API]
- UI-001: Implementar listagem

### Tipo 4: Produto com Stitch

**Épicos Típicos:**
- Setup
- Stitch Import
- Entidades
- UI/UX
- Deploy

**Histórias Típicas:**
- STITCH-001: Configurar Google Stitch
- STITCH-002: Importar telas
- STITCH-003: Validar fidelidade
- ENT-001: CRUD de [Entidade]
- UI-001: Implementar home (fidelidade Stitch)

---

## Template de Backlog

```md
# Backlog — [Nome do Projeto]

## Visão Geral

- **Total de Histórias:** X
- **Concluídas:** Y
- **Em Progresso:** Z
- **Pendentes:** W

## Épicos

### Setup

**Descrição:** Configurar projeto e integrações básicas.

**Histórias:**
- [ ] CONFIG-001
- [ ] CONFIG-002
- [ ] INT-001

### [Épico 2]

**Descrição:** [Descrição]

**Histórias:**
- [ ] HIST-001
- [ ] HIST-002

## Histórias

### CONFIG-001: Configurar Projeto

**Épico:** Setup

**Descrição:**
Como desenvolvedor, quero configurar o projeto, para começar a desenvolver.

**Critérios de Aceite:**
- [ ] Projeto Next.js criado
- [ ] Estrutura de pastas configurada
- [ ] ESLint e Prettier configurados
- [ ] `.env.example` criado
- [ ] `README.md` inicial

**Prioridade:** `alta`

**Estimativa:** 3 pontos

**Status:** `done`

**Dependências:**
- Nenhuma

**Notas:**
- Nenhuma

---

### INT-001: Integração GitHub

**Épico:** Setup

**Descrição:**
Como desenvolvedor, quero configurar GitHub, para versionar código.

**Critérios de Aceite:**
- [ ] Variáveis de ambiente configuradas
- [ ] Autenticação verificada
- [ ] Repositório verificado
- [ ] Remote configurado
- [ ] Push inicial executado

**Prioridade:** `alta`

**Estimativa:** 2 pontos

**Status:** `done`

**Dependências:**
- CONFIG-001

**Notas:**
- Nenhuma

---

### [HIST-XXX: Nome]

...
```

---

## Referências

- `GLOBAL-RULES.md` — Regras globais
- `project-profiles.md` — Tipos de projeto
- `applicability-matrix.md` — Matriz de aplicabilidade
- `phases-gates-reports.md` — Fases, gates e reports