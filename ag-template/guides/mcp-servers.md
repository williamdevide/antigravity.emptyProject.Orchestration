# MCP Servers — Servidores MCP Disponíveis

## Visão Geral

Este guia lista os servidores MCP (Model Context Protocol) disponíveis e como configurá-los no projeto.

---

## O que é MCP?

MCP (Model Context Protocol) é um protocolo padrão para conectar IAs a ferramentas e dados externos.

**Benefícios:**
- Padronização de integrações
- Segurança (permissões explícitas)
- Composição de múltiplos servidores
- Ecossistema em crescimento

---

## Servidores Disponíveis

### 1. GitHub

**Propósito:** Acessar repositórios, issues, pull requests, código.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-github
```

**Configuração:**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "github_pat_..."
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `read_file` — Ler arquivo do repositório
- `write_file` — Escrever arquivo no repositório
- `list_files` — Listar arquivos de um diretório
- `search_code` — Buscar código
- `search_issues` — Buscar issues
- `create_issue` — Criar issue
- `get_pull_request` — Obter PR
- `list_branches` — Listar branches

**Exemplo de Uso:**

```ts
// Ler arquivo do repositório
const content = await mcp.github.read_file({
  owner: 'comixflix',
  repo: 'comixflix-app',
  path: 'src/app/page.tsx',
  branch: 'main',
})

// Criar issue
await mcp.github.create_issue({
  owner: 'comixflix',
  repo: 'comixflix-app',
  title: 'Adicionar tela de login',
  body: 'Implementar tela de login com email e senha.',
  labels: ['feature', 'frontend'],
})
```

**Documentação:** [GitHub MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github)

---

### 2. Google Drive

**Propósito:** Acessar arquivos e pastas do Google Drive.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-google-drive
```

**Configuração:**

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-drive"],
      "env": {
        "GOOGLE_DRIVE_API_KEY": "AIza...",
        "GOOGLE_DRIVE_CREDENTIALS": "..."
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `list_files` — Listar arquivos de uma pasta
- `read_file` — Ler conteúdo de arquivo
- `search` — Buscar arquivos
- `get_file_info` — Obter metadados de arquivo

**Exemplo de Uso:**

```ts
// Listar arquivos de uma pasta
const files = await mcp.gdrive.list_files({
  folderId: '1a2b3c4d5e6f',
  pageSize: 50,
})

// Buscar arquivos
const results = await mcp.gdrive.search({
  query: "name contains 'design' and mimeType = 'application/pdf'",
})

// Ler arquivo
const content = await mcp.gdrive.read_file({
  fileId: '1x2y3z4a5b6c',
})
```

**Documentação:** [Google Drive MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)

---

### 3. Google Stitch

**Propósito:** Acessar projetos de design no Google Stitch.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-google-stitch
```

**Configuração:**

```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-stitch"],
      "env": {
        "GOOGLE_STITCH_API_KEY": "AIza...",
        "GOOGLE_STITCH_PROJECT_ID": "comixflix-design-123"
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `get_project` — Obter informações do projeto
- `list_screens` — Listar telas do projeto
- `get_screen` — Obter detalhes de uma tela
- `list_components` — Listar componentes
- `get_component` — Obter detalhes de um componente
- `export_assets` — Exportar assets do projeto

**Exemplo de Uso:**

```ts
// Obter projeto
const project = await mcp.stitch.get_project({
  projectId: 'comixflix-design-123',
})

// Listar telas
const screens = await mcp.stitch.list_screens({
  projectId: 'comixflix-design-123',
})

// Obter tela específica
const screen = await mcp.stitch.get_screen({
  projectId: 'comixflix-design-123',
  screenId: 'home-screen',
})

// Exportar assets
const assets = await mcp.stitch.export_assets({
  projectId: 'comixflix-design-123',
  format: 'svg',
})
```

**Documentação:** [Google Stitch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/stitch)

---

### 4. PostgreSQL

**Propósito:** Acessar banco de dados PostgreSQL.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-postgres
```

**Configuração:**

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/comixflix"
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `query` — Executar query SQL
- `list_tables` — Listar tabelas
- `describe_table` — Descrever estrutura de tabela
- `insert` — Inserir dados
- `update` — Atualizar dados
- `delete` — Deletar dados

**Exemplo de Uso:**

```ts
// Listar tabelas
const tables = await mcp.postgres.list_tables()

// Descrever tabela
const schema = await mcp.postgres.describe_table({
  table: 'comics',
})

// Query
const comics = await mcp.postgres.query({
  query: 'SELECT * FROM comics WHERE editora = $1',
  params: ['Panini'],
})

// Insert
await mcp.postgres.insert({
  table: 'comics',
  data: {
    titulo: 'Batman #1',
    editora: 'Panini',
    preco: 19.90,
  },
})
```

**Documentação:** [PostgreSQL MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)

---

### 5. SQLite

**Propósito:** Acessar banco de dados SQLite (local).

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-sqlite
```

**Configuração:**

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite"],
      "env": {
        "DATABASE_PATH": "./data/comixflix.db"
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `query` — Executar query SQL
- `list_tables` — Listar tabelas
- `describe_table` — Descrever estrutura de tabela
- `insert` — Inserir dados
- `update` — Atualizar dados
- `delete` — Deletar dados

**Exemplo de Uso:**

```ts
// Listar tabelas
const tables = await mcp.sqlite.list_tables()

// Query com join
const results = await mcp.sqlite.query({
  query: `
    SELECT c.titulo, e.nome as editora
    FROM comics c
    JOIN editoras e ON c.editora_id = e.id
    WHERE e.ativa = 1
  `,
})
```

**Documentação:** [SQLite MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)

---

### 6. Filesystem

**Propósito:** Acessar sistema de arquivos local.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Configuração:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "/Users/username/projects/comixflix"
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `read_file` — Ler arquivo
- `write_file` — Escrever arquivo
- `list_directory` — Listar diretório
- `create_directory` — Criar diretório
- `delete_file` — Deletar arquivo
- `move_file` — Mover arquivo
- `search_files` — Buscar arquivos

**Exemplo de Uso:**

```ts
// Listar diretório
const files = await mcp.filesystem.list_directory({
  path: '/projects/comixflix/src',
})

// Ler arquivo
const content = await mcp.filesystem.read_file({
  path: '/projects/comixflix/src/app/page.tsx',
  encoding: 'utf-8',
})

// Escrever arquivo
await mcp.filesystem.write_file({
  path: '/projects/comixflix/src/lib/utils.ts',
  content: 'export function cn(...) {...}',
  encoding: 'utf-8',
})

// Buscar arquivos
const results = await mcp.filesystem.search_files({
  path: '/projects/comixflix',
  pattern: '*.tsx',
})
```

**Documentação:** [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)

---

### 7. Brave Search

**Propósito:** Buscar na web usando Brave Search API.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-brave-search
```

**Configuração:**

```json
{
  "mcpServers": {
    "brave": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "..."
      }
    }
  }
}
```

**Ferramentas Disponíveis:**
- `search_web` — Buscar na web
- `search_local` — Buscar localmente (businesses)
- `search_news` — Buscar notícias

**Exemplo de Uso:**

```ts
// Buscar na web
const results = await mcp.brave.search_web({
  query: 'melhores quadrinhos 2024',
  count: 10,
  offset: 0,
})

// Buscar notícias
const news = await mcp.brave.search_news({
  query: 'Marvel novos lançamentos',
  count: 5,
})
```

**Documentação:** [Brave Search MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)

---

### 8. Fetch

**Propósito:** Fetch de URLs e extração de conteúdo.

**Instalação:**

```bash
npm install -g @modelcontextprotocol/server-fetch
```

**Configuração:**

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

**Ferramentas Disponíveis:**
- `fetch_url` — Fetch de URL
- `extract_content` — Extrair conteúdo de HTML

**Exemplo de Uso:**

```ts
// Fetch de URL
const response = await mcp.fetch.fetch_url({
  url: 'https://paninibooks.com.br/quadrinhos',
  method: 'GET',
  headers: {
    'User-Agent': 'Mozilla/5.0...',
  },
})

// Extrair conteúdo
const content = await mcp.fetch.extract_content({
  url: 'https://paninibooks.com.br/quadrinhos/batman-1',
  selector: '.product-details',
})
```

**Documentação:** [Fetch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)

---

## Configuração Completa

### Exemplo de `mcp.json`

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "github_pat_..."
      }
    },
    "stitch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-stitch"],
      "env": {
        "GOOGLE_STITCH_API_KEY": "AIza...",
        "GOOGLE_STITCH_PROJECT_ID": "comixflix-design-123"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/comixflix"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "/Users/username/projects/comixflix"
      }
    },
    "brave": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "..."
      }
    }
  }
}
```

---

## Segurança

### Melhores Práticas

1. **Tokens em Variáveis de Ambiente**
   - Nunca commitar tokens
   - Usar `.env` com `.gitignore`
   - Rotacionar tokens periodicamente

2. **Permissões Mínimas**
   - Usar tokens com escopo mínimo necessário
   - GitHub: fine-grained PATs
   - Google: service accounts com permissões específicas

3. **Paths Restritos**
   - Filesystem: restringir `ALLOWED_PATHS`
   - Não permitir acesso a paths sensíveis

4. **Auditoria**
   - Log de operações
   - Revisar permissões periodicamente
   - Monitorar uso anômalo

---

## Troubleshooting

### Servidor Não Inicia

**Sintoma:** Erro ao iniciar servidor MCP.

**Solução:**
```bash
# Verificar instalação
npm list -g @modelcontextprotocol/server-github

# Reinstalar
npm install -g @modelcontextprotocol/server-github

# Verificar node version
node --version  # Deve ser >= 18
```

### Timeout nas Requisições

**Sintoma:** Requisições MCP timeout após 30s.

**Solução:**
```json
{
  "mcpServers": {
    "github": {
      "timeout": 60000
    }
  }
}
```

### Permissões Insuficientes

**Sintoma:** Erro 403 ao acessar recursos.

**Solução:**
- Verificar escopo do token
- Regenerar token com permissões adequadas
- Verificar se repositório/banco está acessível

---

## Checklist de Configuração

### Setup

- [ ] Node.js >= 18 instalado
- [ ] npm global path configurado
- [ ] MCP servers instalados

### Configuração

- [ ] `mcp.json` criado
- [ ] Variáveis de ambiente configuradas
- [ ] Tokens em `.env` (não commitado)

### Validação

- [ ] Cada servidor inicia sem erro
- [ ] Ferramentas básicas funcionam
- [ ] Permissões verificadas

### Segurança

- [ ] Tokens com escopo mínimo
- [ ] Paths restritos (filesystem)
- [ ] `.env` no `.gitignore`
- [ ] Logs habilitados

---

## Referências

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [frontend-libraries.md](./frontend-libraries.md)
- [ai-agents-integration.md](./ai-agents-integration.md)