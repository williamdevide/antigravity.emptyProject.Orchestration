# Folder Structure — Estrutura de Pastas do Projeto

## Visão Geral

Esta estrutura organiza o projeto em áreas de responsabilidade claras, facilitando navegação, manutenção e escalabilidade.

---

## Estrutura Principal

```text
project-root/
├── documentation/
│   ├── project/
│   ├── architecture/
│   ├── design/
│   └── guides/
├── src/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── hooks/
│   ├── types/
│   └── styles/
├── functions/
│   ├── api/
│   ├── scrapers/
│   └── jobs/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
├── fixtures/
├── public/
└── [config files]
```

---

## `documentation/`

Propósito: Toda a documentação do projeto.

### `documentation/project/`

Documentação do produto e negócio.

```text
documentation/project/
├── 0.project-profile.md
├── 1.visao.md
├── 2.requisitos.md
├── 3.regras-negocio.md
├── 4.arquitetura.md
├── 5.design.md
├── 6.modelo-dados.md
├── 7.backlog.md
└── applicability.md
```

| Arquivo | Propósito |
|---|---|
| `0.project-profile.md` | Tipo de projeto, dimensão, integrações |
| `1.visao.md` | Visão do produto, problema, solução |
| `2.requisitos.md` | Requisitos funcionais |
| `3.regras-negocio.md` | Regras de negócio |
| `4.arquitetura.md` | Arquitetura técnica |
| `5.design.md` | Design (ou contrato Stitch) |
| `6.modelo-dados.md` | Modelo de dados |
| `7.backlog.md` | Backlog de histórias |
| `applicability.md` | Matriz de aplicabilidade do projeto |

### `documentation/architecture/`

Documentação técnica e arquitetura.

```text
documentation/architecture/
├── decisions/
├── diagrams/
└── adr-template.md
```

| Arquivo/Pasta | Propósito |
|---|---|
| `decisions/` | ADRs (Architecture Decision Records) |
| `diagrams/` | Diagramas de arquitetura |
| `adr-template.md` | Template para ADRs |

### `documentation/design/`

Assets e especificações de design.

```text
documentation/design/
├── assets/
├── screens/
└── tokens/
```

| Arquivo/Pasta | Propósito |
|---|---|
| `assets/` | Imagens, ícones, logos |
| `screens/` | Screenshots ou exports de telas |
| `tokens/` | Tokens de design (cores, fonts, spacing) |

### `documentation/guides/`

Guias e referências.

```text
documentation/guides/
├── onboarding.md
├── development.md
├── deployment.md
└── troubleshooting.md
```

| Arquivo | Propósito |
|---|---|
| `onboarding.md` | Guia de onboarding |
| `development.md` | Guia de desenvolvimento |
| `deployment.md` | Guia de deploy |
| `troubleshooting.md` | Guia de troubleshooting |

---

## `src/`

Propósito: Código fonte da aplicação.

### `src/app/`

Estrutura da aplicação (Next.js App Router).

```text
src/app/
├── layout.tsx
├── page.tsx
├── globals.css
├── (auth)/
│   ├── login/
│   └── register/
├── (main)/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── explorar/
│   └── colecao/
└── api/
    └── [...routes]/
```

| Arquivo/Pasta | Propósito |
|---|---|
| `layout.tsx` | Layout root |
| `page.tsx` | Página inicial |
| `globals.css` | Estilos globais |
| `(auth)/` | Rotas de autenticação (route group) |
| `(main)/` | Rotas principais (route group) |
| `api/` | API routes |

### `src/components/`

Componentes React reutilizáveis.

```text
src/components/
├── ui/
│   ├── Button.tsx
│   ├── Card.tsx
│   └── Input.tsx
├── features/
│   ├── comics/
│   │   ├── ComicCard.tsx
│   │   ├── ComicList.tsx
│   │   └── ComicDetail.tsx
│   └── series/
├── layout/
│   ├── Header.tsx
│   ├── BottomNav.tsx
│   └── Splash.tsx
└── shared/
    └── Loading.tsx
```

| Pasta | Propósito |
|---|---|
| `ui/` | Componentes de UI genéricos (design system) |
| `features/` | Componentes específicos de features |
| `layout/` | Componentes de layout |
| `shared/` | Componentes compartilhados |

### `src/lib/`

Utilitários, configurações e código de infraestrutura.

```text
src/lib/
├── firebase/
│   ├── client.ts
│   ├── auth.ts
│   └── firestore.ts
├── api/
│   ├── client.ts
│   └── endpoints.ts
├── utils/
│   ├── format.ts
│   └── validate.ts
└── constants/
    └── routes.ts
```

| Pasta | Propósito |
|---|---|
| `firebase/` | Configuração e clientes Firebase |
| `api/` | Clientes de API e endpoints |
| `utils/` | Funções utilitárias |
| `constants/` | Constantes da aplicação |

### `src/hooks/`

Custom React hooks.

```text
src/hooks/
├── useAuth.ts
├── useComics.ts
└── useDebounce.ts
```

| Arquivo | Propósito |
|---|---|
| `useAuth.ts` | Hook de autenticação |
| `useComics.ts` | Hook para buscar comics |
| `useDebounce.ts` | Hook utilitário |

### `src/types/`

TypeScript types e interfaces.

```text
src/types/
├── index.ts
├── comic.ts
├── series.ts
└── user.ts
```

| Arquivo | Propósito |
|---|---|
| `index.ts` | Exports de todos os types |
| `comic.ts` | Types de Comic |
| `series.ts` | Types de Series |
| `user.ts` | Types de User |

### `src/styles/`

Estilos e temas.

```text
src/styles/
├── globals.css
├── theme.ts
└── tokens.css
```

| Arquivo | Propósito |
|---|---|
| `globals.css` | Estilos globais |
| `theme.ts` | Configuração de tema |
| `tokens.css` | Design tokens (CSS variables) |

---

## `functions/`

Propósito: Código de backend (Cloud Functions, serverless).

### `functions/api/`

API endpoints serverless.

```text
functions/api/
├── comics/
│   ├── list.ts
│   ├── get.ts
│   ├── create.ts
│   ├── update.ts
│   └── delete.ts
└── health.ts
```

| Arquivo | Propósito |
|---|---|
| `list.ts` | Listar comics |
| `get.ts` | Obter comic por ID |
| `create.ts` | Criar comic |
| `update.ts` | Atualizar comic |
| `delete.ts` | Deletar comic |
| `health.ts` | Health check |

### `functions/scrapers/`

Scrapers de dados externos.

```text
functions/scrapers/
├── panini/
│   ├── index.ts
│   ├── parser.ts
│   ├── selectors.ts
│   ├── normalizer.ts
│   └── README.md
└── mythos/
    └── ...
```

| Arquivo | Propósito |
|---|---|
| `index.ts` | Entry point do scraper |
| `parser.ts` | Parser de HTML/JSON |
| `selectors.ts` | Seletores CSS/XPath |
| `normalizer.ts` | Normalização de dados |
| `README.md` | Documentação do scraper |

### `functions/jobs/`

Jobs agendados e automações.

```text
functions/jobs/
├── sync-comics.ts
├── deduplicate.ts
└── cleanup.ts
```

| Arquivo | Propósito |
|---|---|
| `sync-comics.ts` | Sincronizar comics dos scrapers |
| `deduplicate.ts` | Remover duplicados |
| `cleanup.ts` | Limpeza de dados antigos |

---

## `tests/`

Propósito: Testes automatizados.

### `tests/unit/`

Testes unitários.

```text
tests/unit/
├── components/
│   └── ComicCard.test.tsx
├── utils/
│   └── format.test.ts
└── hooks/
    └── useAuth.test.ts
```

### `tests/integration/`

Testes de integração.

```text
tests/integration/
├── api/
│   └── comics.test.ts
└── scrapers/
    └── panini.test.ts
```

### `tests/e2e/`

Testes end-to-end.

```text
tests/e2e/
├── auth.spec.ts
├── comics.spec.ts
└── navigation.spec.ts
```

---

## `scripts/`

Propósito: Scripts de desenvolvimento e operação.

```text
scripts/
├── seed-db.ts
├── run-scraper.ts
├── validate-integrations.ts
└── setup.sh
```

| Arquivo | Propósito |
|---|---|
| `seed-db.ts` | Popular banco com seeds |
| `run-scraper.ts` | Executar scraper manualmente |
| `validate-integrations.ts` | Validar integrações |
| `setup.sh` | Setup inicial do projeto |

---

## `fixtures/`

Propósito: Dados de exemplo para desenvolvimento e testes.

```text
fixtures/
├── comics.example.json
├── series.example.json
├── users.example.json
└── scrapers/
    ├── panini.fixture.html
    └── panini.expected.json
```

| Arquivo | Propósito |
|---|---|
| `*.example.json` | Dados de exemplo |
| `*.fixture.html` | HTML de exemplo para scrapers |
| `*.expected.json` | Resultado esperado de scrapers |

---

## `public/`

Propósito: Assets estáticos servidos publicamente.

```text
public/
├── images/
│   ├── logo.svg
│   └── icons/
├── fonts/
└── manifest.json
```

| Arquivo/Pasta | Propósito |
|---|---|
| `images/` | Imagens estáticas |
| `fonts/` | Fontes locais |
| `manifest.json` | PWA manifest |

---

## Arquivos de Configuração

```text
project-root/
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── .eslintrc.json
├── .prettierrc
├── .env.example
├── .gitignore
├── .gitattributes
├── README.md
├── GLOBAL-RULES.md
├── GLOBAL-WORKFLOW.md
└── [outros arquivos do ag-template]
```

| Arquivo | Propósito |
|---|---|
| `package.json` | Dependências e scripts |
| `tsconfig.json` | Configuração TypeScript |
| `tailwind.config.ts` | Configuração Tailwind |
| `.eslintrc.json` | Configuração ESLint |
| `.prettierrc` | Configuração Prettier |
| `.env.example` | Variáveis de ambiente (exemplo) |
| `.gitignore` | Arquivos ignorados pelo Git |
| `.gitattributes` | Configurações do Git |
| `README.md` | Vitrine do projeto |

---

## Regras de Estrutura

### Regra 1: Separação por Responsabilidade

- `documentation/` → Documentação
- `src/` → Código da aplicação
- `functions/` → Backend serverless
- `tests/` → Testes
- `scripts/` → Scripts
- `fixtures/` → Dados de exemplo
- `public/` → Assets estáticos

### Regra 2: Nomenclatura

- Pastas: kebab-case (`comic-cards`)
- Arquivos: kebab-case (`comic-card.tsx`)
- Componentes: PascalCase (`ComicCard.tsx`)
- Utilitários: camelCase (`format.ts`)

### Regra 3: Profundidade Máxima

- Evitar mais de 4 níveis de profundidade
- Quebrar pastas grandes em sub-pastas

### Regra 4: Co-location

- Manter arquivos relacionados próximos
- Ex: Componente + teste + estilos na mesma pasta

### Regra 5: Índices

- Usar `index.ts` para exports
- Facilitar imports limpos

---

## Referências

- `minimal-documentation.md` — Documentação mínima por pasta
- `project-health-checklist.md` — Checklist de saúde do projeto
- `GLOBAL-WORKFLOW.md` — Workflow global