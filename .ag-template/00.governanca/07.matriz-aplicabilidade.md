# Matriz de Aplicabilidade

## Estados

- **REQUIRED**: Obrigatório para o tipo de projeto
- **OPTIONAL**: Criar apenas se houver valor específico
- **NOT_APPLICABLE**: Não se aplica (requer justificativa)
- **FUTURE**: Planejado, mas fora do MVP
- **BLOCKED**: Necessário, porém bloqueado por dependência
- **NOT_VERIFIED**: Declarado, mas ainda não testado

---

## Documentação por Tipo de Projeto

### Tipo 1: Landing Page

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | Vitrine do projeto |
| PRD/Vision | OPTIONAL | Pode ser simples |
| Requisitos Funcionais | OPTIONAL | Básico |
| Regras de Negócio | NOT_APPLICABLE | Sem lógica complexa |
| Arquitetura | OPTIONAL | Simples |
| Modelo de Dados | NOT_APPLICABLE | Sem banco |
| Backlog | OPTIONAL | Poucas histórias |
| Estratégia de Testes | OPTIONAL | E2E e visual |
| Plano de Deploy | REQUIRED | Essencial |

### Tipo 2: Produto Web com Backend

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | Vitrine |
| PRD/Vision | REQUIRED | Direção clara |
| Requisitos Funcionais | REQUIRED | Essencial |
| Regras de Negócio | REQUIRED | Lógica de negócio |
| Arquitetura | REQUIRED | Múltiplas camadas |
| Modelo de Dados | REQUIRED | Banco presente |
| Backlog | REQUIRED | Guia de implementação |
| Estratégia de Testes | REQUIRED | Qualidade |
| Plano de Deploy | REQUIRED | Produção |

### Tipo 3: Produto com Integrações

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | Vitrine |
| PRD/Vision | REQUIRED | Direção |
| Requisitos Funcionais | REQUIRED | Essencial |
| Regras de Negócio | REQUIRED | Lógica |
| Arquitetura | REQUIRED | Integrações complexas |
| Modelo de Dados | REQUIRED | Banco |
| Backlog | REQUIRED | Guia |
| Documentação de Integrações | REQUIRED | Contratos, APIs |
| Estratégia de Testes | REQUIRED | Integração crítica |
| Plano de Deploy | REQUIRED | Produção |

### Tipo 4: Produto com Stitch

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | Vitrine |
| PRD/Vision | REQUIRED | Direção |
| Requisitos Funcionais | REQUIRED | Essencial |
| Arquitetura | REQUIRED | Múltiplas camadas |
| Modelo de Dados | REQUIRED | Banco |
| Backlog | REQUIRED | Guia |
| Contrato de Fidelidade Stitch | REQUIRED | Crítico |
| Relatório de Divergências | REQUIRED | Transparência |

### Tipo 5: Automação / Job

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | Vitrine |
| Descrição do Propósito | REQUIRED | Essencial |
| Gatilhos | REQUIRED | Quando executa |
| Entradas e Saídas | REQUIRED | Dados |
| Dependências | REQUIRED | Crítico |
| Tratamento de Erro | REQUIRED | Robustez |
| Logs e Métricas | REQUIRED | Operação |
| Runbooks | REQUIRED | Operação |

### Tipo 6: Biblioteca / Pacote

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | Instalação e uso |
| API Docs | REQUIRED | Interface pública |
| Exemplos | REQUIRED | Uso prático |
| Guia de Contribuição | OPTIONAL | Se open source |
| Estratégia de Testes | REQUIRED | Qualidade |

---

## Integrações por Tipo de Projeto

| Integração | Tipo 1 | Tipo 2 | Tipo 3 | Tipo 4 | Tipo 5 | Tipo 6 |
|---|---|---|---|---|---|---|
| GitHub | OPT | REQ | REQ | REQ | REQ | OPT |
| Google Stitch | N/A | OPT | OPT | REQ | N/A | N/A |
| Banco de Dados | N/A | REQ | REQ | REQ | OPT | N/A |
| Scrapers | N/A | OPT | REQ | OPT | REQ | N/A |
| APIs Externas | N/A | OPT | REQ | OPT | REQ | OPT |

**Legenda:**
- REQ: REQUIRED
- OPT: OPTIONAL
- N/A: NOT_APPLICABLE

---

## Dimensões de Plataforma

| Artefato | Web Desktop | Web Mobile-First | Mobile App |
|---|---|---|---|
| Bottom Nav | N/A | REQ | REQ |
| Top Nav | REQ | OPT | N/A |
| Splash Screen | OPT | REQ | REQ |
| PWA | OPT | REQ | N/A |
| Offline Support | N/A | OPT | REQ |

---

## Regras de Aplicação

### Regra 1: Todo REQUIRED deve existir

Todo artefato marcado como REQUIRED deve:
- Existir como arquivo real
- Ter conteúdo inicial
- Ser validado antes da implementação

### Regra 2: Todo N/A deve justificar

Todo artefato marcado como NOT_APPLICABLE deve:
- Ter justificativa de uma linha
- Ser registrado em `documentation/project/applicability.md`

### Regra 3: OPTIONAL é opcional

Artefatos OPTIONAL podem ser omitidos sem justificativa.

### Regra 4: Matriz por projeto

Ao criar um projeto:
1. Classificar tipo(s)
2. Gerar matriz específica
3. Salvar em `documentation/project/applicability.md`

### Regra 5: Validação

O Antigravity deve validar:
- Todos os REQUIRED estão presentes
- N/A tem justificativa
- Conteúdo mínimo está presente

---

## Exemplo de Aplicação

### Projeto: ComixFlix

**Classificação:**
- Tipo principal: Tipo 2 (Produto web com backend)
- Tipos secundários: Tipo 3 (scrapers), Tipo 4 (Stitch)
- Dimensão: Web mobile-first

**Matriz Resultante:**

| Artefato | Status |
|---|---|
| README | REQUIRED |
| PRD/Vision | REQUIRED |
| Requisitos Funcionais | REQUIRED |
| Regras de Negócio | REQUIRED |
| Arquitetura | REQUIRED |
| Modelo de Dados | REQUIRED |
| Backlog | REQUIRED |
| Documentação de Scrapers | REQUIRED |
| Contrato de Fidelidade Stitch | REQUIRED |
| Estratégia de Testes | REQUIRED |
| Plano de Deploy | REQUIRED |
| Bottom Nav | REQUIRED |
| Splash Screen | REQUIRED |
| PWA | REQUIRED |

---

## Template de Applicability.md

```md
# Applicability Matrix — [Nome do Projeto]

## Classificação

- **Tipo Principal:** Tipo 2
- **Tipos Secundários:** Tipo 3, Tipo 4
- **Dimensão:** Web mobile-first

## Matriz

### Documentação

| Artefato | Status | Justificativa |
|---|---|---|
| README | REQUIRED | |
| PRD | REQUIRED | |
| ... | ... | |

### Integrações

| Integração | Status | Justificativa |
|---|---|---|
| GitHub | REQUIRED | |
| Stitch | REQUIRED | |
| ... | ... | |

### Plataforma

| Artefato | Status | Justificativa |
|---|---|---|
| Bottom Nav | REQUIRED | Mobile-first |
| ... | ... | |
```