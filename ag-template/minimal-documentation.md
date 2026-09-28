# Minimal Documentation — Documentação Mínima por Pasta

## Visão Geral

Este arquivo define a documentação mínima necessária para cada pasta do projeto.

---

## `documentation/project/`

### Documentação Mínima

| Arquivo | Conteúdo Mínimo |
|---|---|
| `0.project-profile.md` | Tipo de projeto, dimensão, integrações (REQUIRED/OPTIONAL/N/A) |
| `1.visao.md` | Problema, solução, público-alvo, objetivos |
| `2.requisitos.md` | Lista de requisitos funcionais principais |
| `3.regras-negocio.md` | Regras de negócio críticas |
| `4.arquitetura.md` | Componentes principais, integrações, fluxos |
| `5.design.md` | Referência de design ou contrato Stitch |
| `6.modelo-dados.md` | Entidades principais e relacionamentos |
| `7.backlog.md` | Histórias priorizadas com critérios de aceite |
| `applicability.md` | Matriz de aplicabilidade do projeto |

### Template Mínimo

```md
# [Nome do Arquivo]

## Visão Geral

[1-2 parágrafos]

## [Seção Principal]

[Conteúdo estruturado]

## Referências

- [Link para documento relacionado]
```

---

## `documentation/architecture/`

### Documentação Mínima

| Arquivo/Pasta | Conteúdo Mínimo |
|---|---|
| `decisions/` | ADRs para decisões arquiteturais críticas |
| `diagrams/` | Diagrama de arquitetura principal |
| `adr-template.md` | Template para ADRs |

### Template de ADR

```md
# ADR-XXX: [Título]

## Status

[proposed | accepted | deprecated | superseded]

## Contexto

[Descrição do contexto]

## Decisão

[Descrição da decisão]

## Consequências

### Positivas
- Consequência 1

### Negativas
- Consequência 1

## Referências

- [Link]
```

---

## `documentation/design/`

### Documentação Mínima

| Arquivo/Pasta | Conteúdo Mínimo |
|---|---|
| `assets/` | Assets essenciais (logo, ícones principais) |
| `screens/` | Screenshots das telas principais |
| `tokens/` | Tokens de design (cores, fonts, spacing) |

---

## `documentation/guides/`

### Documentação Mínima

| Arquivo | Conteúdo Mínimo |
|---|---|
| `onboarding.md` | Passos para configurar ambiente de desenvolvimento |
| `development.md` | Comandos de desenvolvimento (dev, build, test) |
| `deployment.md` | Passos para deploy em produção |
| `troubleshooting.md` | Problemas comuns e soluções |

---

## `src/`

### Documentação Mínima

| Pasta | Documentação Mínima |
|---|---|
| `app/` | README com estrutura de rotas |
| `components/` | README com lista de componentes e exemplos |
| `lib/` | README com descrição de utilitários |
| `hooks/` | README com lista de hooks e exemplos |
| `types/` | README com descrição de types principais |
| `styles/` | README com tokens e temas |

### Template de README de Pasta

```md
# [Nome da Pasta]

## Propósito

[1-2 parágrafos]

## Estrutura

```text
[pasta]/
├── arquivo1.ts
└── arquivo2.ts
```

## Uso

```ts
// Exemplo de uso
```

## Referências

- [Link para documentação relacionada]
```

---

## `functions/`

### Documentação Mínima

| Pasta | Documentação Mínima |
|---|---|
| `api/` | README com lista de endpoints e schemas |
| `scrapers/` | README por scraper com fonte, campos, seletores |
| `jobs/` | README com descrição de jobs e gatilhos |

### Template de README de Scraper

```md
# Scraper [Nome]

**Fonte:** [URL]

**Status:** [configured | verified | blocked]

**Campos Extraídos:**
- campo1 (tipo)
- campo2 (tipo)

**Campos Ausentes:**
- campo3 (motivo)

**Seletores:**
- Card: `.selector`
- Título: `.title`

**Rate Limit:**
- 1 req/3s

**Última Verificação:** YYYY-MM-DD

**Testes:**
- [x] Parser com fixture
- [x] Validação de schema
```

---

## `tests/`

### Documentação Mínima

| Pasta | Documentação Mínima |
|---|---|
| `unit/` | README com exemplos de testes unitários |
| `integration/` | README com exemplos de testes de integração |
| `e2e/` | README com cenários de testes E2E |

---

## `scripts/`

### Documentação Mínima

| Arquivo | Documentação Mínima |
|---|---|
| `*.ts` | Comentários de cabeçalho com propósito e uso |

### Template de Script

```ts
/**
 * [Nome do Script]
 * 
 * Propósito: [Descrição]
 * 
 * Uso:
 *   npx tsx scripts/[nome].ts
 * 
 * Variáveis de Ambiente:
 *   - [VARIAVEL]: [Descrição]
 */
```

---

## `fixtures/`

### Documentação Mínima

| Arquivo | Documentação Mínima |
|---|---|
| `*.example.json` | Comentários com descrição da estrutura |
| `*.fixture.html` | Comentários com origem e data |

### Template de Fixture

```json
{
  "//": "Fixture de comics para desenvolvimento",
  "//": "Origem: Scraper Panini",
  "//": "Data: YYYY-MM-DD",
  "comics": [
    {
      "titulo": "Exemplo",
      // ...
    }
  ]
}
```

---

## `public/`

### Documentação Mínima

| Arquivo/Pasta | Documentação Mínima |
|---|---|
| `images/` | README com lista de assets |
| `fonts/` | README com lista de fontes e licenças |
| `manifest.json` | Comentários com descrição |

---

## Arquivos de Configuração

### Documentação Mínima

| Arquivo | Documentação Mínima |
|---|---|
| `package.json` | Scripts e dependências principais no README |
| `.env.example` | Variáveis documentadas com comentários |
| `README.md` (root) | Visão, setup, desenvolvimento, deploy |

### Template de `.env.example`

```env
# GitHub Integration
GITHUB_ENABLED=true
GITHUB_TOKEN=github_pat_...
GITHUB_OWNER=seu-usuario
GITHUB_REPOSITORY=seu-repo

# Google Stitch
GOOGLE_STITCH_ENABLED=true
GOOGLE_STITCH_API_KEY=AIza...
GOOGLE_STITCH_PROJECT_ID=seu-project-id
```

---

## Regras de Documentação

### Regra 1: README em Cada Pasta

Toda pasta principal deve ter um `README.md`.

### Regra 2: Documentação Viva

Documentação deve ser atualizada junto com o código.

### Regra 3: Exemplos Reais

Sempre incluir exemplos reais de uso.

### Regra 4: Links Cruzados

Documentação deve linkar para documentos relacionados.

### Regra 5: Versão e Data

Documentar versão e data de última atualização quando relevante.

---

## Checklist de Documentação

### Setup do Projeto

- [ ] `documentation/project/` completo
- [ ] `README.md` root com visão e setup
- [ ] `.env.example` documentado

### Desenvolvimento

- [ ] READMEs de pastas principais
- [ ] Exemplos de uso
- [ ] Guias de desenvolvimento

### Produção

- [ ] Guia de deploy
- [ ] Documentação de operação
- [ ] Troubleshooting

---

## Referências

- `folder-structure.md` — Estrutura de pastas
- `project-health-checklist.md` — Checklist de saúde
- `GLOBAL-RULES.md` — Regras globais