# Antigravity Kit Setup — Setup do AG Kit

## Visão Geral

Este guia define como configurar e usar o **AG Kit** (Antigravity-first agent engineering kit) no seu projeto.

**Repositório:** https://github.com/vudovn/ag-kit

**O que é o AG Kit:**
- Kit de engenharia de agentes com foco em Antigravity
- Regras, skills, agentes especialistas, workflows
- Memória persistente
- MCP guidance
- Orquestração
- Safety hook nativo

---

## Requisitos

- **Node.js:** 22 ou superior (para tooling Antigravity)
- **Python:** 3.10 ou superior (para validadores e utilitários)
- **Google Antigravity:** Workspace confiável
- **Git:** Para atualizações seguras e rollback

---

## Instalação

### Opção 1: Instalação Local (Recomendado)

```bash
# Instalar AG Kit no projeto
npx @vudovn/ag-kit init
```

### Opção 2: Instalação Global

```bash
# Instalar CLI globalmente
npm install -g @vudovn/ag-kit

# Inicializar no projeto
ag-kit init
```

### O que é Instalado

O AG Kit instala um workspace completo `.agents/`:

```text
.agents/
├── rules/           # Regras de workspace
├── skills/          # Skills de domínio
├── workflows/       # Workflows de slash commands
├── agents/          # Definições de agentes especialistas
├── memory/          # Memória persistente
├── hooks/           # Safety hooks
├── antigravity.json # Configuração Antigravity
├── hooks.json       # Configuração de hooks
├── manifest.json    # Manifesto de componentes
└── DEPENDENCY_GRAPH.md # Grafo de dependências
```

### Importante: Git

**NÃO** adicione `.agents/` ao `.gitignore` se o Antigravity precisa indexar regras, skills e workflows.

Para manter local sem desabilitar descoberta:

```bash
# Adicionar ao .git/info/exclude ao invés de .gitignore
echo ".agents/" >> .git/info/exclude
```

---

## Verificação do Workspace

### Comandos de Validação

```bash
# Verificar agentes
npm run check:agents

# Verificar Antigravity (read-only)
npm run check:antigravity

# Testar Antigravity
npm run test:antigravity
```

### Modo Strict

Use modo strict apenas após resolver todos os placeholders:

```bash
node .agents/hooks/antigravity-doctor.mjs --strict
```

---

## Configuração no Antigravity

### 1. Abrir Workspace

Após abrir o repositório como workspace confiável no Antigravity:

### 2. Verificar Slash Commands

Confirmar que os comandos são descobertos:

- `/plan`
- `/coordinate`
- `/orchestrate`
- `/create`
- `/debug`
- `/deploy`
- `/enhance`
- `/test`
- `/verify`

### 3. Verificar Skills

Confirmar que skills relevantes estão selecionadas de `.agents/skills/`.

### 4. Testar Comando Normal

```bash
# Executar comando normal
npm test

# Confirmar que é permitido pelo Antigravity
```

### 5. Verificar Safety Hook

Testar o safety hook com payload mockado:

```bash
# Testar bloqueio de comando destrutivo
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
  | node .agents/hooks/validate-tool-call.mjs
```

**Resultado esperado:**
- Exit code: non-zero
- Output: `BLOCKED by AG Kit`

---

## Safety Hook Nativo

### O que o Hook Bloqueia

O hook nativo é deliberadamente restrito. Bloqueia:

- ❌ Deleção de filesystem root (`rm -rf /`)
- ❌ Formatação de drive
- ❌ Overwrite de disco raw

### O que o Hook Permite

Permite limpeza normal de projeto:

- ✅ Deletar `dist/`
- ✅ Deletar `node_modules/`
- ✅ Comandos de build normais

### Configuração do Hook

O Antigravity carrega `.agents/hooks.json`:

```json
{
  "enabled": true,
  "PreToolUse": [
    {
      "matcher": "run_command",
      "command": "node .agents/hooks/validate-tool-call.mjs",
      "timeout": 10
    }
  ]
}
```

### Desabilitar Temporariamente

Para diagnosticar issues de compatibilidade:

```json
{
  "enabled": false
}
```

Após mudar, reabrir o workspace.

**Importante:** Não deletar os controles de permissão do Antigravity.

---

## MCP Configuration

### Verificar Configuração MCP

Revisar o plano de MCP sem escrever:

```bash
# Check mode
node .agents/hooks/sync-mcp.mjs --check

# Print mode
node .agents/hooks/sync-mcp.mjs --print
```

### Aplicar Configuração

Após substituir placeholders, aplicar explicitamente:

```bash
# Aplicar para suite
node .agents/hooks/sync-mcp.mjs --apply --target suite

# Aplicar para CLI
node .agents/hooks/sync-mcp.mjs --apply --target cli
```

### Segurança

- Servidores existentes com mesmo nome são preservados (a menos que `--force`)
- Backup timestamped é criado antes de mudar arquivo
- **Nunca** commitar credenciais MCP reais

---

## Build e Plugin

### Build do Plugin

```bash
npm run build:antigravity-plugin
```

### Inspecionar Plugin

Revisar `dist/antigravity-plugin/` antes de instalar localmente.

O bundle contém:
- Skills empacotados
- Agentes
- Regras
- Workflow commands convertidos
- Native hook
- MCP example
- `PLUGIN_CONTENTS.json` com SHA-256 entries

### Instalar Plugin (Opcional)

```bash
# Instalar plugin local
agy plugin install ./dist/antigravity-plugin

# Listar plugins
agy plugin list
```

**Nota:** Instalação de plugin é opcional. O workspace `.agents/` nativo do repositório permanece como source of truth.

---

## Componentes Incluídos

| Componente | Count | Propósito |
|---|---|---|
| Agents | 20 | Definições de agentes especialistas e orquestração |
| Skills | 47 | Conhecimento de domínio progressivo e helpers de validação |
| Workflows | 13 | Procedimentos de slash-command repetíveis |
| Rules | 6 | Routing, safety, design e coding constraints |
| Memory Topics | 4+ | Durable project conventions, decisions, preferences, feedback |

### Versionamento

Cada agente, skill, workflow e rule tem contrato SemVer.

```bash
# Gerar agentes
npm run generate:agents

# Check de agentes
npm run check:agents
```

### Manifesto

`.agents/manifest.json`, `.agents/manifest.lock.json` e `.agents/DEPENDENCY_GRAPH.md` tornam o toolkit reprodutível e detectam drift.

---

## Common Workflows

### Comandos Slash

| Comando | Propósito |
|---|---|
| `/brainstorm` | Explorar opções e arquitetura antes de implementar |
| `/coordinate` | Executar tarefas de pesquisa/revisão em paralelo, depois sintetizar |
| `/create` | Criar feature ou aplicação com gates estruturados |
| `/debug` | Análise de root-cause baseada em evidência |
| `/deploy` | Executar pre-flight checks e workflow de deploy |
| `/enhance` | Modificar código existente com segurança |
| `/orchestrate` | Planejar, obter aprovação, delegar para especialistas, verificar |
| `/plan` | Criar plano de implementação detalhado e checklist |
| `/preview` | Gerenciar preview servers locais |
| `/remember` | Salvar informações duráveis do projeto na memória |
| `/status` | Sumarizar trabalho ativo e blockers |
| `/test` | Projetar e executar testes |
| `/verify` | Provar mudanças executando checks ao invés de inspeção |

---

## Safe Updates e Rollback

### Atualizações Merge-Aware

AG Kit updates são merge-aware. Arquivos de usuário e arquivos gerenciados modificados localmente são preservados por padrão.

```bash
# Preview do plano exato
ag-kit update --dry-run

# Merge seguro com backup
ag-kit update

# Substituição completa explícita (ainda com backup)
ag-kit update --strategy replace

# Rollback para backup mais recente
ag-kit rollback
```

### Metadados de Update

- Update metadata: `.agents/.ag-kit/`
- Backups: `.ag-kit-backups/` (fora da árvore gerenciada)

**Importante:** Ler `MIGRATION.md` antes de upgradar para release Antigravity-native.

---

## Runtime Contract

### Configuração Antigravity

`.agents/antigravity.json` declara:

- 6 fases de integração suportadas
- CLI capabilities documentadas do Antigravity usadas pelo AG Kit

Evita inventar semantic version mínimo quando upstream não define.

---

## Production Gates

### Validações Obrigatórias

Um release candidate não é aprovado para produção até:

1. **Toolkit validation**
2. **CLI tests e package validation**
3. **Web lint, typecheck, build, audit**
4. **Antigravity native contract**
5. **Dependency Review**

### Smoke Test Manual

AG Kit nunca requer:
- Merge automático
- Deploy automático
- Sincronização MCP automática

Mudanças de produção devem permanecer reviewáveis e reversíveis.

---

## Troubleshooting

### Erro: Agents Não São Descobertos

**Sintoma:** Slash commands não aparecem no Antigravity.

**Solução:**
```bash
# Verificar se .agents/ está no .gitignore
cat .gitignore

# Se estiver, remover ou mover para .git/info/exclude
echo ".agents/" >> .git/info/exclude
git reset .agents/

# Reabrir workspace no Antigravity
```

---

### Erro: Safety Hook Falha

**Sintoma:** Comandos normais são bloqueados.

**Solução:**
```bash
# Verificar se hook está habilitado
cat .agents/hooks.json

# Se necessário, desabilitar temporariamente
# Editar .agents/hooks.json: "enabled": false

# Reabrir workspace no Antigravity

# Reportar payload shape se contiver dados sensíveis
```

---

### Erro: MCP Sync Falha

**Sintoma:** Erro ao sincronizar MCP.

**Solução:**
```bash
# Verificar configuração atual
node .agents/hooks/sync-mcp.mjs --check

# Verificar se há placeholders
node .agents/hooks/sync-mcp.mjs --print

# Substituir placeholders e tentar novamente
node .agents/hooks/sync-mcp.mjs --apply --target suite
```

---

## Documentação Oficial

- [AG Kit Repository](https://github.com/vudovn/ag-kit)
- [Migration Guide](https://github.com/vudovn/ag-kit/blob/main/MIGRATION.md)
- [Production Checklist](https://github.com/vudovn/ag-kit/blob/main/PRODUCTION_CHECKLIST.md)
- [Security Policy](https://github.com/vudovn/ag-kit/blob/main/SECURITY.md)
- [Agent Flow Architecture](https://github.com/vudovn/ag-kit/blob/main/AGENT_FLOW.md)
- [Toolkit Architecture](https://github.com/vudovn/ag-kit/blob/main/TOOLKIT_ARCHITECTURE.md)
- [Changelog](https://github.com/vudovn/ag-kit/blob/main/CHANGELOG.md)

---

## Referências

- `GLOBAL-RULES.md` — Regras globais
- `GLOBAL-WORKFLOW.md` — Workflow global
- `mcp-servers.md` — MCP servers
- `ai-agents-integration.md` — Integração com agentes de IA