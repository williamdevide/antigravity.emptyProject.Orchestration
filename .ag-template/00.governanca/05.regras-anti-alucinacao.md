# Anti-Hallucination Rules — Regras para Evitar Alucinações

## Visão Geral

Este arquivo define as regras e práticas para evitar alucinações (informações inventadas) durante a execução de tarefas pelo Antigravity.

---

## O que é Alucinação

Alucinação é quando o agente:

- Inventa dados que não existem
- Inventa APIs que não foram documentadas
- Inventa comportamentos de sistemas
- Inventa resultados de operações
- Inventa integrações não configuradas
- Inventa design não especificado
- Inventa requisitos não documentados

---

## Princípios Anti-Alucinação

### 1. Fonte da Verdade

Todo dado deve vir de uma fonte verificável:

- Documentação do projeto
- APIs configuradas
- Bancos de dados conectados
- Arquivos de configuração
- Inputs do usuário
- Ferramentas executadas

### 2. Validação

Antes de usar qualquer dado:

- Verificar se a fonte existe
- Verificar se o dado está atualizado
- Verificar se o dado é consistente
- Validar schema quando aplicável

### 3. Transparência

Quando não houver dados:

- Declarar "desconhecido" explicitamente
- Declarar "não verificado" quando aplicável
- Declarar limitações de acesso
- Não inventar para preencher lacunas

### 4. Fallback Explícito

Quando usar dados de fallback:

- Declarar que é fallback
- Documentar origem do fallback
- Validar fallback quando possível
- Planejar substituição por dados reais

---

## Regras por Categoria

### Dados de Projeto

✅ Permitido:
- Ler de `documentation/project/`
- Ler de `README.md`
- Ler de variáveis de ambiente
- Perguntar ao usuário

❌ Proibido:
- Inventar nome de projeto
- Inventar descrição
- Inventar requisitos
- Inventar integrações

### Dados de Integração

✅ Permitido:
- Ler estado de variáveis de ambiente
- Executar comandos de verificação
- Ler logs de integração
- Perguntar ao usuário

❌ Proibido:
- Dizer que integração está configurada sem verificar
- Inventar resultados de API
- Inventar dados de scraper
- Fingir que sincronizou sem executar

### Dados de Design

✅ Permitido:
- Importar do Google Stitch
- Ler de `5.design.md`
- Ler de especificações
- Usar fallback explícito

❌ Proibido:
- Inventar design não especificado
- Substituir Stitch por interpretação
- Inventar cores, fonts, spacing
- Inventar layouts não documentados

### Dados de Banco

✅ Permitido:
- Ler de banco conectado
- Usar seeds documentados
- Usar fixtures explícitas
- Declarar "sem dados" quando vazio

❌ Proibido:
- Inventar registros
- Inventar schemas
- Dizer que tem dados quando não tem
- Mock silencioso

### Dados de Scraper

✅ Permitido:
- Executar scraper em fonte real
- Usar fixtures documentadas
- Usar dados cacheados (com timestamp)
- Declarar "não verificado" quando bloqueado

❌ Proibido:
- Inventar resultados de scraper
- Inventar seletores CSS
- Inventar campos extraídos
- Dizer que scrapeou sem executar

---

## Padrões de Validação

### Validação de Integração

```md
## Validação: GitHub

**Verificação:**
- [x] GITHUB_ENABLED = true
- [x] GITHUB_OWNER definido
- [x] GITHUB_REPOSITORY definido
- [x] gh auth status = OK
- [x] gh repo view = OK

**Estado:** `verified`
```

### Validação de Dados

```md
## Validação: Dados de Comics

**Fonte:** Firestore (comics collection)

**Verificação:**
- [x] Conexão estabelecida
- [x] Collection existe
- [x] Registros presentes (150)
- [x] Schema válido
- [x] Seeds executados

**Estado:** `verified`
```

### Validação de Design

```md
## Validação: Design Stitch

**Fonte:** Google Stitch (comixflix-design-123)

**Verificação:**
- [x] Projeto encontrado
- [x] Telas importadas (4/4)
- [x] Assets importados (12/12)
- [x] Fidelidade verificada (95%)

**Divergências:**
- Botão de ação: 5px de diferença

**Estado:** `verified`
```

---

## Padrões de Fallback

### Fallback de Dados

```md
## Dados de Comics

**Fonte Primária:** Firestore

**Status:** `not-configured`

**Fallback:**
- Usando 10 comics de exemplo (fixtures)
- Origem: `fixtures/comics.example.json`
- Válido até: configuração do banco

**Próximos Passos:**
- Configurar Firebase
- Executar seeds
- Substituir fixtures por dados reais
```

### Fallback de Design

```md
## Design

**Fonte Primária:** Google Stitch

**Status:** `not-configured`

**Fallback:**
- Usando especificação de `5.design.md`
- Origem: documento de design
- Válido até: configuração do Stitch

**Próximos Passos:**
- Configurar Google Stitch
- Importar telas
- Validar fidelidade
```

### Fallback de Integração

```md
## Integração: Scrapers

**Status:** `partially-implemented`

**Implementado:**
- Scraper Panini (funcional)

**Não Implementado:**
- Scraper Mythos (site em manutenção)

**Fallback:**
- Usando fixtures para Mythos
- Origem: `fixtures/mythos.example.json`
- Válido até: site disponível

**Próximos Passos:**
- Reexecutar scraper Mythos em 2026-09-25
```

---

## Checklist Anti-Alucinação

### Antes de Executar

- [ ] Li a documentação relevante
- [ ] Verifiquei as variáveis de ambiente
- [ ] Verifiquei o estado das integrações
- [ ] Validei pré-condições
- [ ] Planejei fallback quando necessário

### Durante Execução

- [ ] Estou usando dados de fontes verificáveis
- [ ] Estou validando resultados
- [ ] Estou registrando limitações
- [ ] Estou reportando progresso

### Após Execução

- [ ] Validei o resultado
- [ ] Reportei estado final
- [ ] Registreiro limitações
- [ ] Documentei próximos passos

---

## Exemplos de Boas Práticas

### Exemplo 1: Dados de Projeto

✅ Correto:
```md
**Nome do Projeto:** ComixFlix

**Fonte:** `documentation/project/vision.md`

**Descrição:**
Plataforma de descoberta e acompanhamento de quadrinhos.

**Validação:**
- [x] Arquivo lido
- [x] Conteúdo verificado
```

❌ Incorreto:
```md
**Nome do Projeto:** ComixFlix
**Descrição:** Uma plataforma incrível de quadrinhos...
```
(Inventou descrição sem fonte)

### Exemplo 2: Integração GitHub

✅ Correto:
```md
## GitHub Integration

**Estado:** `verified`

**Verificação:**
- GITHUB_ENABLED: true
- GITHUB_OWNER: comixflix
- GITHUB_REPOSITORY: comixflix-app
- gh auth status: OK
- gh repo view: OK

**Ações:**
- [x] Verificar autenticação
- [x] Verificar repositório
- [x] Configurar remote
```

❌ Incorreto:
```md
## GitHub Integration

**Estado:** configurado

(Observação: não verificou, apenas assumiu)
```

### Exemplo 3: Dados de Scraper

✅ Correto:
```md
## Scraper Panini

**Status:** `verified`

**Fonte:** https://paninibooks.com.br/quadrinhos

**Última Execução:**
- Data: 2026-09-20
- Registros: 150
- Duplicados: 0
- Erros: 0

**Campos Extraídos:**
- titulo, editora, preco_normal, preco_promocional

**Campos Ausentes:**
- isbn, autores (não disponíveis na listagem)
```

❌ Incorreto:
```md
## Scraper Panini

**Status:** funcional

Scrapeou 150 quadrinhos com todos os campos.

(Observação: inventou que tem todos os campos)
```

### Exemplo 4: Design Stitch

✅ Correto:
```md
## Design

**Fonte:** Google Stitch (comixflix-design-123)

**Telas Importadas:**
- Home (100%)
- Explorar (100%)
- Detalhes (95%)
- Coleção (100%)

**Divergências:**
- Detalhes: botão de ação com 5px de diferença

**Estado:** `verified`
```

❌ Incorreto:
```md
## Design

Design importado do Stitch com 100% de fidelidade.

(Observação: não verificou fidelidade, inventou 100%)
```

---

## Regras de Reporte

### Reporte de Sucesso

```md
## Resultado

**Status:** `success`

**Ações Executadas:**
- [x] Ação 1
- [x] Ação 2
- [x] Ação 3

**Validações:**
- [x] Validação 1
- [x] Validação 2

**Próximos Passos:**
- Próximo passo 1
- Próximo passo 2
```

### Reporte com Limitações

```md
## Resultado

**Status:** `partial-success`

**Ações Executadas:**
- [x] Ação 1
- [x] Ação 2
- [ ] Ação 3 (bloqueada)

**Limitações:**
- Ação 3 bloqueada por dependência X

**Fallback:**
- Usando Y como fallback

**Próximos Passos:**
- Resolver dependência X
- Reexecutar Ação 3
```

### Reporte de Falha

```md
## Resultado

**Status:** `failed`

**Erro:**
- Mensagem de erro

**Causa:**
- Análise da causa

**Próximos Passos:**
- Ação corretiva 1
- Ação corretiva 2
```

---

## Referências

- `GLOBAL-RULES.md` — Regras globais
- `integration-contracts.md` — Contratos de integração
- `phases-gates-reports.md` — Fases, gates e reports