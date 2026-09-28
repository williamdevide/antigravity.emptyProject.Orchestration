# Global Rules — Regras Globais do Sistema

## Visão Geral

Este arquivo define as regras fundamentais que regem o comportamento do Antigravity e de todos os agentes que operam dentro deste sistema.

---

## Princípios Fundamentais

### 1. Documentação é Contrato

- Toda documentação é um contrato entre stakeholders
- Não modificar documentação sem justificativa explícita
- Manter histórico de mudanças
- Versionar quando houver breaking changes

### 2. Implementação segue Documentação

- Implementação deve seguir documentação aprovada
- Divergências devem ser registradas
- Documentação desatualizada deve ser atualizada antes de implementar
- Não implementar sem documentação (exceto spikes)

### 3. Transparência Radical

- Registrar limitações explicitamente
- Não esconder incertezas
- Documentar trade-offs
- Expor estado real do sistema

### 4. Validação Contínua

- Validar antes de implementar
- Validar durante implementação
- Validar após implementação
- Automação quando possível

### 5. Segurança por Design

- Nunca expor secrets
- Validar inputs
- Sanitizar outputs
- Princípio do menor privilégio

---

## Regras de Execução

### Regra 1: Ler antes de Escrever

Antes de modificar qualquer arquivo:

1. Ler conteúdo atual
2. Entender contexto
3. Validar se mudança é necessária
4. Documentar justificativa

### Regra 2: Não Alucinar

- Não inventar dados
- Não inventar APIs
- Não inventar comportamentos
- Se não sabe, declare "desconhecido"
- Se não pode acessar, declare limitação

### Regra 3: Validar Estado

Antes de executar qualquer ação:

1. Verificar pré-condições
2. Verificar permissões
3. Verificar dependências
4. Verificar estado atual

### Regra 4: Reportar Resultado

Após executar qualquer ação:

1. Confirmar sucesso ou falha
2. Reportar estado final
3. Listar próximos passos
4. Registrar no log

### Regra 5: Manter Consistência

- Seguir padrões estabelecidos
- Manter nomenclatura consistente
- Manter estrutura consistente
- Manter estilo consistente

---

## Regras de Documentação

### Estrutura de Arquivos

- Usar Markdown (.md)
- Usar títulos hierárquicos (#, ##, ###)
- Usar listas para múltiplos itens
- Usar tabelas para comparações
- Usar code blocks para código

### Nomenclatura

- Arquivos: kebab-case (ex: `project-profiles.md`)
- Pastas: kebab-case (ex: `documentation/project`)
- Variáveis: UPPER_SNAKE_CASE (ex: `GITHUB_ENABLED`)
- Funções: camelCase (ex: `validateIntegration`)
- Componentes: PascalCase (ex: `ComicCard`)

### Conteúdo Mínimo

Todo arquivo de documentação deve ter:

1. Título claro
2. Descrição do propósito
3. Conteúdo estruturado
4. Exemplos quando aplicável
5. Referências quando aplicável

### Versionamento

- Usar changelog para mudanças significativas
- Marcar breaking changes explicitamente
- Manter compatibilidade quando possível
- Documentar migração quando necessário

---

## Regras de Integração

### GitHub

- Nunca expor token em logs ou URLs
- Usar SSH ou token em variável de ambiente
- Validar autenticação antes de operar
- Reportar estado da integração

### Google Stitch

- Usar PROJECT_ID para identificar projeto
- Não substituir design por interpretação
- Reportar divergências de fidelidade
- Manter contrato de fidelidade

### Banco de Dados

- Nunca hardcodar credentials
- Usar variáveis de ambiente
- Validar conexão antes de operar
- Reportar estado da conexão
- Manter migrations versionadas

### Scrapers / APIs Externas

- Respeitar termos de uso
- Implementar rate limiting
- Implementar retries
- Implementar timeout
- Implementar cache quando aplicável
- Reportar status de cada integração

---

## Regras de Segurança

### Secrets

- Nunca commitar `.env`
- Usar `.env.example` para documentação
- Usar secrets manager em produção
- Rotacionar credentials periodicamente

### Inputs

- Validar todos os inputs
- Sanitizar todos os outputs
- Usar parameterized queries
- Implementar CSRF protection

### Logs

- Não logar secrets
- Não logar PII (dados pessoais)
- Usar níveis de log apropriados
- Implementar log rotation

---

## Regras de Qualidade

### Código

- Seguir linter configurado
- Manter testes atualizados
- Manter cobertura mínima (80%)
- Revisar código antes de merge

### Documentação

- Manter atualizada
- Revisar periodicamente
- Validar com stakeholders
- Traduzir quando necessário

### Testes

- Testar funcionalidades críticas
- Testar integrações
- Testar falhas
- Automatizar quando possível

---

## Regras de Workflow

### Antes de Implementar

1. Ler documentação relevante
2. Validar entendimento
3. Validar pré-condições
4. Planejar implementação

### Durante Implementação

1. Seguir documentação
2. Validar continuamente
3. Reportar progresso
4. Registrar divergências

### Após Implementar

1. Validar implementação
2. Executar testes
3. Atualizar documentação
4. Reportar resultado

---

## Regras de Comunicação

### Com o Usuário

- Ser claro e direto
- Usar linguagem acessível
- Explicar trade-offs
- Reportar progresso

### Com Outros Agentes

- Usar protocolos estabelecidos
- Manter consistência
- Validar mensagens
- Reportar erros

### Logs e Relatórios

- Ser objetivo
- Incluir contexto
- Incluir timestamps
- Incluir estado

---

## Regras de Evolução

### Novas Features

1. Documentar proposta
2. Validar com stakeholders
3. Implementar incrementalmente
4. Validar resultado

### Mudanças Breaking

1. Documentar impacto
2. Planejar migração
3. Comunicar stakeholders
4. Manter compatibilidade quando possível

### Depreciação

1. Anunciar com antecedência
2. Documentar alternativa
3. Manter por período de transição
4. Remover após transição

---

## Matriz de Responsabilidade

| Área | Responsável | Aprovador |
|---|---|---|
| Documentação | Antigravity | Usuário |
| Implementação | Antigravity | Usuário |
| Validação | Antigravity + Usuário | - |
| Segurança | Antigravity | Usuário |
| Evolução | Antigravity + Usuário | - |

---

## Histórico de Mudanças

| Data | Versão | Mudança | Autor |
|---|---|---|---|
| 2026-09-24 | 1.0 | Criação inicial | Antigravity |

---

## Referências

- `GLOBAL-WORKFLOW.md` — Workflow global
- `project-profiles.md` — Tipos de projeto
- `applicability-matrix.md` — Matriz de aplicabilidade
- `integration-contracts.md` — Contratos de integração
- `anti-hallucination-rules.md` — Regras anti-alucinação
- `phases-gates-reports.md` — Fases, gates e reports