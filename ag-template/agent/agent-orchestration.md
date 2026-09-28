# Agent Orchestration — Orquestração de Agentes

## Agentes Disponíveis

### 1. Antigravity Kit (CLI)

- **Tipo:** Ferramenta de linha de comando
- **Função:** Inicialização, estrutura, validação
- **Comandos:** `ag-kit init`, `ag-kit create`, `ag-kit add`, `ag-kit sync`, `ag-kit validate`
- **Uso:** Via terminal

### 2. Agente Orquestrador (Antigravity)

- **Tipo:** Agente principal no Antigravity IDE
- **Função:** Orquestrar fluxo do projeto
- **Comandos:** `/goal`, `/grill-me`
- **Uso:** Via chat no Antigravity

### 3. Sub-agentes (Antigravity)

- **Tipo:** Agentes especializados
- **Função:** Tarefas específicas (código, testes, docs)
- **Uso:** Chamados pelo agente orquestrador

### 4. Claude Code

- **Tipo:** Agente de código
- **Função:** Geração de código complexo, arquitetura
- **Uso:** Claude Desktop App, API, MCP

### 5. Codex (GitHub Copilot)

- **Tipo:** Autocomplete e geração de código
- **Função:** Código rotineiro, testes, docs
- **Uso:** VS Code extension, API

### 6. GitHub Agents

- **Tipo:** Automação no GitHub
- **Função:** CI/CD, code review, automação
- **Uso:** GitHub Actions, API

## Fluxo de Orquestração

```
Usuário
  ↓
Antigravity Kit (CLI)
  ↓ ag-kit init
Projeto Inicializado
  ↓
Agente Orquestrador (Antigravity)
  ↓ /goal, /grill-me
Especificação
  ↓
Sub-agentes + Claude Code + Codex
  ↓
Implementação
  ↓
GitHub Agents
  ↓
CI/CD, Deploy
```

## Como Usar

### 1. Inicializar Projeto

```bash
ag-kit create meu-projeto
cd meu-projeto
```

### 2. Chamar Agente Orquestrador

No chat do Antigravity:

```
/agente-orquestrador /goal Iniciar projeto ComixFlix
/grill-me Quais são os requisitos principais?
```

### 3. Agente Lê Especificações

- `documentation/directives/0.ideia-inicial.md`
- `.ag-template/project-profiles.md`
- `.ag-template/applicability-matrix.md`
- `.ag-template/integration-contracts.md`

### 4. Agente Gera Especificações

- `1.ideia-projeto.md`
- `1.ideia-design.md`
- `5.projeto.md`
- `5.design.md`

### 5. Agente Implementa

- Usa sub-agentes para código
- Usa Claude Code para partes complexas
- Usa Codex para autocomplete
- Usa MCP servers para dados

### 6. GitHub Agents Automatizam

- CI/CD
- Code review
- Deploy

## Configuração

```env
# Antigravity Kit
ANTIGRAVITY_KIT_VERSION=3.0.0

# Antigravity IDE
ANTIGRAVITY_IDE_ENABLED=true

# MCP Servers
MCP_GITHUB_ENABLED=true
MCP_GOOGLE_STITCH_ENABLED=true
MCP_FIREBASE_ENABLED=true

# Claude
ANTHROPIC_API_KEY=

# Codex
OPENAI_API_KEY=

# GitHub
GITHUB_TOKEN=
```

## Regras

1. **Sempre usar Antigravity Kit** para inicializar projetos
2. **Sempre chamar agente orquestrador** via `/goal` e `/grill-me`
3. **Sempre ler especificações** antes de implementar
4. **Sempre usar MCP** quando disponível
5. **Sempre validar** com `ag-kit validate`
6. **Sempre documentar** decisões

## Melhores Práticas

- Manter Antigravity Kit atualizado
- Usar comandos `/goal` e `/grill-me` em todos os chats
- Revisar código gerado por agentes
- Testar rigorosamente
- Documentar decisões arquiteturais
- Sincronizar com template regularmente