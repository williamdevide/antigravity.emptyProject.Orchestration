# Project Profiles — Tipos de Projeto e Dimensões

## Tipos de Projeto (6 principais)

### 1. Landing Page / Site Institucional

**Características:**
- Foco em conversão
- Conteúdo estático ou semi-dinâmico
- SEO crítico
- Performance essencial

**Tecnologias Típicas:**
- Next.js, Vite, Astro
- Tailwind CSS, Framer Motion
- CMS headless (Sanity, Contentful)

**Documentação Mínima:**
- README
- Visão do produto
- Requisitos funcionais básicos
- Design (Stitch ou especificação)
- Deploy

---

### 2. Produto Web com Backend e Banco

**Características:**
- CRUD completo
- Autenticação e autorização
- Banco de dados
- API backend

**Tecnologias Típicas:**
- Frontend: Next.js, React, Tailwind
- Backend: Node.js, FastAPI, Firebase Functions
- Banco: Firestore, Supabase, PostgreSQL

**Documentação Mínima:**
- README completo
- PRD / Visão
- Requisitos funcionais
- Regras de negócio
- Arquitetura
- Modelo de dados
- Backlog
- Estratégia de testes
- Deploy

---

### 3. Produto com Integrações Externas (APIs, Scrapers)

**Características:**
- Integração com APIs de terceiros
- Scrapers de dados
- Webhooks
- Rate limiting

**Tecnologias Típicas:**
- Axios, Fetch
- Puppeteer, Playwright (scrapers)
- Zod, Pydantic (validação)

**Documentação Mínima:**
- Tudo do tipo 2 +
- Documentação de cada integração
- Contratos de API
- Scrapers: fontes, legalidade, seletores, tratamento de erro

---

### 4. Produto com Design vindo do Google Stitch

**Características:**
- Design principal no Stitch
- Fidelidade visual crítica
- Assets e telas no Stitch

**Tecnologias Típicas:**
- React, Tailwind
- Framer Motion
- Stitch import

**Documentação Mínima:**
- Tudo do tipo 2 +
- Contrato de fidelidade Stitch
- Projeto Stitch (ID, nome)
- Relatório de divergências

---

### 5. Automação / Job / Pipeline de Dados

**Características:**
- Processamento em batch
- Jobs agendados
- Pipelines de dados
- Logs e métricas

**Tecnologias Típicas:**
- Node.js, Python
- Cloud Functions, Cron
- Message queues

**Documentação Mínima:**
- Descrição do propósito
- Gatilhos
- Entradas e saídas
- Dependências
- Tratamento de erro
- Runbooks

---

### 6. Biblioteca / Pacote de Código

**Características:**
- Código reutilizável
- NPM package ou similar
- Documentação de API

**Tecnologias Típicas:**
- TypeScript
- Jest, Vitest
- tsup, rollup

**Documentação Mínima:**
- README com instalação e uso
- Exemplos
- API docs
- Guia de contribuição

---

## Dimensões de Plataforma

### Web Desktop

- Foco em telas grandes
- Navegação por mouse/teclado
- Top nav comum
- Menos restrições de espaço

### Web Mobile-First (Padrão)

- Responsivo, mobile-first
- Touch-friendly
- Bottom nav comum
- Performance crítica
- PWA quando aplicável

### Mobile App (Futuro)

- Nativo ou híbrido
- App stores
- Recursos nativos
- Offline-first

---

## Projetos Híbridos

Um projeto pode combinar múltiplos tipos:

**Exemplo:** ComixFlix
- Tipo principal: Produto web com backend e banco
- Tipos secundários:
  - Produto com integrações (scrapers de editoras)
  - Produto com Stitch (design)
- Dimensão: Web mobile-first

---

## Classificação de Projetos

Ao classificar um projeto, definir:

### Tipo(s)

```md
Tipos:
- Principal: Produto web com backend e banco
- Secundários:
  - Produto com integrações (scrapers)
  - Produto com Stitch
```

### Dimensão

```md
Dimensão: web-mobile-first
```

### Integrações

```md
Integrações:
- GitHub (REQUIRED)
- Google Stitch (REQUIRED)
- Firebase (REQUIRED)
- Scrapers (REQUIRED)
```

### Complexidade

```md
Complexidade: média
- Frontend: média
- Backend: média
- Integrações: alta
- Dados: média
```

---

## Matriz de Decisão

| Pergunta | Sim → | Não → |
|---|---|---|
| Tem backend e banco? | Tipo 2 | Próxima pergunta |
| Tem integrações externas? | Tipo 3 | Próxima pergunta |
| Design no Stitch? | Tipo 4 | Próxima pergunta |
| É automação/job? | Tipo 5 | Próxima pergunta |
| É biblioteca? | Tipo 6 | Tipo 1 (Landing) |
| Foco mobile? | Mobile-first | Desktop |