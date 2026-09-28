# Integration Contracts — Contratos de Integração

## Estados de Integração

| Estado | Descrição | Quando Usar |
|---|---|---|
| `configured` | Configurada e operacional | Tudo funcionando |
| `verified` | Configurada, operacional e testada | Com testes passando |
| `partially-implemented` | Parcialmente implementada | Algumas features faltando |
| `not-configured` | Não configurada | Setup pendente |
| `blocked` | Necessária, mas bloqueada | Dependência externa |
| `not-verified` | Implementada, mas não testada | Falta teste |
| `not-applicable` | Não se aplica ao projeto | Justificar |

---

## GitHub

### Variáveis de Ambiente

```env
GITHUB_ENABLED=true
GITHUB_TOKEN=github_pat_...
GITHUB_OWNER=seu-usuario-ou-org
GITHUB_REPOSITORY=nome-do-repositorio
GITHUB_DEFAULT_BRANCH=main
GITHUB_CREATE_REPOSITORY=false
GITHUB_SYNC_DOCUMENTATION=true
GITHUB_CREATE_ISSUES=false
GITHUB_CREATE_PROJECT=false
```

### O que o Antigravity pode fazer

✅ Permitido:
- Ler variáveis de ambiente
- Verificar autenticação (sem exibir token)
- Identificar owner e repository
- Verificar se repositório existe
- Configurar remote (sem token na URL)
- Sincronizar documentação (quando autorizado)
- Criar branch/commit inicial (com autorização)
- Confirmar resultado
- Registrar o que foi feito

❌ Proibido:
- Colocar token na URL do remote
- Fingir que sincronizou sem executar
- Commitar `.env`
- Expor token em logs
- Criar repositório sem `GITHUB_CREATE_REPOSITORY=true`

### Contrato de Execução

1. **Verificar configuração**
   ```bash
   echo $GITHUB_ENABLED
   echo $GITHUB_OWNER
   echo $GITHUB_REPOSITORY
   ```

2. **Verificar autenticação**
   ```bash
   gh auth status
   ```

3. **Verificar repositório**
   ```bash
   gh repo view $GITHUB_OWNER/$GITHUB_REPOSITORY
   ```

4. **Configurar remote** (se necessário)
   ```bash
   git remote add origin git@github.com:$GITHUB_OWNER/$GITHUB_REPOSITORY.git
   ```

5. **Sincronizar** (se autorizado)
   ```bash
   git push -u origin main
   ```

6. **Registrar estado**
   ```md
   Estado: `verified`
   Owner: $GITHUB_OWNER
   Repository: $GITHUB_REPOSITORY
   Remote: configurado
   Sync: executado em YYYY-MM-DD
   ```

### Relatório Obrigatório

```md
## GitHub Integration

**Estado:** `verified`

**Configuração:**
- Owner: seu-usuario
- Repository: seu-repo
- Branch: main

**Ações Executadas:**
- [x] Verificar autenticação
- [x] Verificar repositório
- [x] Configurar remote
- [x] Push inicial

**Limitações:**
- Nenhuma

**Próximos Passos:**
- Criar issues do backlog (quando GITHUB_CREATE_ISSUES=true)
```

---

## Google Stitch

### Variáveis de Ambiente

```env
GOOGLE_STITCH_ENABLED=true
GOOGLE_STITCH_API_KEY=AIza...
GOOGLE_STITCH_PROJECT_ID=comixflix-design-123
GOOGLE_STITCH_PROJECT_NAME=ComixFlix Design
GOOGLE_STITCH_EXPORT_PATH=/exports/comixflix
GOOGLE_STITCH_IMPORT_MODE=source-of-truth
GOOGLE_STITCH_FIDELITY=exact
```

### O que o Antigravity deve fazer

1. **Resolver projeto pelo ID**
   - Usar `GOOGLE_STITCH_PROJECT_ID`
   - Confirmar `GOOGLE_STITCH_PROJECT_NAME`

2. **Importar assets disponíveis**
   - Telas
   - Componentes
   - Tokens de design
   - Assets (imagens, ícones)

3. **Comparar com especificação**
   - Verificar fidelidade visual
   - Identificar divergências
   - Registrar limitações

4. **Não substituir por interpretação**
   - Se não conseguir importar, declarar limitação
   - Não inventar design
   - Usar `5.design.md` como fallback

### Contrato de Fidelidade

| Modo | Descrição | Quando Usar |
|---|---|---|
| `source-of-truth` | Design vem do Stitch | Projeto principal |
| `reference` | Stitch é referência | Design complementar |
| `disabled` | Não usar Stitch | Sem Stitch |

| Fidelidade | Descrição | Tolerância |
|---|---|---|
| `exact` | Réplica exata | 0% divergência |
| `close` | Próximo visual | < 10% divergência |
| `inspired` | Inspirado | < 30% divergência |

### Relatório Obrigatório

```md
## Google Stitch Integration

**Estado:** `verified`

**Configuração:**
- Project ID: comixflix-design-123
- Project Name: ComixFlix Design
- Import Mode: source-of-truth
- Fidelity: exact

**Telas Importadas:**
- Home (100%)
- Explorar (100%)
- Detalhes (95%)
- Coleção (100%)

**Divergências:**
- Detalhes: botão de ação com 5px de diferença

**Limitações:**
- Nenhuma

**Próximos Passos:**
- Ajustar botão de ação na tela de Detalhes
```

---

## Banco de Dados (Firebase/Supabase)

### Variáveis de Ambiente

```env
# Firebase
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=...
NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=...
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
NEXT_PUBLIC_FIREBASE_APP_ID=...

FIREBASE_CLIENT_EMAIL=...
FIREBASE_PRIVATE_KEY=...

# Supabase
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
```

### Contrato Mínimo

✅ Obrigatório:
- Cliente inicializado e conectado
- Entidades principais com repositório
- CRUD básico funcional
- Migrações / schema versionado
- Seeds para desenvolvimento
- Health check
- Estado "sem banco" explícito quando não configurado

❌ Proibido:
- Substituir banco por arrays estáticos no fluxo principal de produção
- Mock silencioso sem indicação visual/textual
- Dizer "usa Firestore" e não usar em nada

### Contrato de Execução

1. **Inicializar cliente**
   ```ts
   import { initializeApp } from 'firebase/app'
   import { getFirestore } from 'firebase/firestore'

   const app = initializeApp(firebaseConfig)
   const db = getFirestore(app)
   ```

2. **Verificar conexão**
   ```ts
   async function healthCheck() {
     try {
       await getDocs(collection(db, 'health'))
       return { status: 'connected' }
     } catch (error) {
       return { status: 'disconnected', error }
     }
   }
   ```

3. **Criar repositórios**
   ```ts
   export const comicsRepository = {
     async findAll() { ... },
     async findById(id) { ... },
     async create(data) { ... },
     async update(id, data) { ... },
     async delete(id) { ... },
   }
   ```

4. **Criar migrations**
   ```ts
   // migrations/001-create-comics.ts
   export async function up(db) {
     await createCollection(db, 'comics', {
       fields: [
         { name: 'titulo', type: 'string' },
         { name: 'editora', type: 'string' },
         // ...
       ]
     })
   }
   ```

5. **Criar seeds**
   ```ts
   // seeds/001-comics.ts
   export async function seed(db) {
     await db.collection('comics').add({
       titulo: 'Batman #1',
       editora: 'Panini',
       // ...
     })
   }
   ```

### Relatório Obrigatório

```md
## Database Integration

**Estado:** `verified`

**Configuração:**
- Provider: Firebase Firestore
- Project: comixflix-prod
- Collections: comics, series, users, user_comics

**Entidades Implementadas:**
- [x] Comic (CRUD completo)
- [x] Series (CRUD completo)
- [x] User (CRUD completo)
- [x] UserComic (CRUD completo)

**Migrations:**
- [x] 001-create-comics
- [x] 001-create-series
- [x] 001-create-users

**Seeds:**
- [x] 10 comics de exemplo
- [x] 5 series de exemplo

**Health Check:**
- Status: connected
- Latência: 45ms

**Próximos Passos:**
- Implementar índices compostos
- Adicionar validações no schema
```

---

## Scrapers / APIs Externas

### Contrato Mínimo

Para cada scraper/API:

1. **URL de origem**
2. **Autorização e termos**
3. **Método de acesso**
4. **Paginação**
5. **Seletores reais**
6. **Campos extraídos**
7. **Campos ausentes**
8. **Normalização**
9. **Deduplicação**
10. **Retries**
11. **Rate limit**
12. **Timeout**
13. **User-Agent**
14. **Cache**
15. **Tratamento de bloqueio**
16. **Logs**
17. **Métricas**
18. **Fixtures**
19. **Teste automatizado**
20. **Data de última verificação**

### Regra de Execução

Para cada scraper:

1. Localizar página real ou fixture autorizada
2. Executar parser
3. Validar payload
4. Persistir no banco
5. Confirmar contagem de registros
6. Verificar duplicação
7. Registrar logs
8. Executar teste de falha
9. Só então marcar como concluído

Se não for possível acessar a fonte:

- Criar adapter com status `blocked` ou `not-verified`
- Criar fixture explícita
- Não inventar resultados
- Não marcar integração como pronta

### Estrutura de Scraper

```text
functions/scrapers/
└── panini/
    ├── index.ts              ← Entry point
    ├── parser.ts             ← Parser HTML/JSON
    ├── selectors.ts          ← Seletores CSS/XPath
    ├── normalizer.ts         ← Normalização de dados
    ├── validator.ts          ← Validação de schema
    ├── fixture.html          ← HTML de exemplo
    ├── fixture.expected.json ← Resultado esperado
    └── README.md             ← Documentação
```

### Documentação de Scraper

```md
# Scraper Panini

**Fonte:** https://paninibooks.com.br/quadrinhos

**Status:** `verified`

**Campos Extraídos:**
- titulo (string)
- editora (string)
- preco_normal (number)
- preco_promocional (number | null)
- url_capa (string)
- url_produto (string)
- personagem_principal (string)

**Campos Ausentes:**
- isbn (não disponível na listagem)
- autores (não disponível na listagem)

**Seletores:**
- Card: `.product-card`
- Título: `.product-title`
- Preço: `.price-regular`
- Capa: `.product-image img`

**Rate Limit:**
- 1 req/3s
- User-Agent rotation

**Cache:**
- TTL: 6h
- Invalidação: manual

**Última Verificação:** 2026-09-20

**Testes:**
- [x] Parser com fixture
- [x] Validação de schema
- [x] Deduplicação
```

### Relatório Obrigatório

```md
## Scrapers Integration

**Estado:** `verified`

### Scraper Panini

**Status:** `verified`

**Fonte:** https://paninibooks.com.br/quadrinhos

**Campos:**
- Extraídos: 8/10
- Ausentes: 2/10 (isbn, autores)

**Última Execução:**
- Data: 2026-09-20
- Registros: 150
- Duplicados: 0
- Erros: 0

**Testes:**
- [x] Parser
- [x] Validação
- [x] Deduplicação

### Scraper Mythos

**Status:** `not-verified`

**Bloqueio:** Site em manutenção

**Próximos Passos:**
- Reexecutar em 2026-09-25
```

---

## Validação de Contratos

### Checklist de Validação

Para cada integração:

- [ ] Variáveis de ambiente configuradas
- [ ] Cliente inicializado
- [ ] Conexão verificada
- [ ] CRUD/operacoes implementadas
- [ ] Testes criados
- [ ] Logs configurados
- [ ] Métricas disponíveis
- [ ] Documentação atualizada
- [ ] Estado registrado

### Comando de Validação

```bash
ag-kit validate integrations
```

Saída esperada:

```text
✓ GitHub: verified
✓ Google Stitch: verified
✓ Firebase: verified
⚠ Scraper Panini: verified (2 campos ausentes)
⚠ Scraper Mythos: not-verified (bloqueado)
```

---

## Matriz de Integrações por Projeto

| Integração | ComixFlix | Landing | SaaS | Automação |
|---|---|---|---|---|
| GitHub | REQ | OPT | REQ | REQ |
| Stitch | REQ | N/A | OPT | N/A |
| Firebase | REQ | N/A | REQ | OPT |
| Scrapers | REQ | N/A | OPT | REQ |

**Legenda:**
- REQ: REQUIRED
- OPT: OPTIONAL
- N/A: NOT_APPLICABLE