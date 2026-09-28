Para iniciar a criação do projeto, siga esta sequência:

## 1. Preparação inicial

```bash
# Na raiz do projeto
mkdir -p documentation/directives/project
mkdir -p documentation/directives/design
touch documentation/directives/0.ideia-inicial.md
```

## 2. Preencher a ideia inicial

Edite `documentation/directives/0.ideia-inicial.md` com sua ideia bruta.

## 3. Gerar especificações iniciais

No Antigravity, execute:

```text
Leia documentation/directives/0.ideia-inicial.md e documentation/directives/0.prompt-iaexterna-inicial.md. Gere:
- documentation/directives/project/1.ideia-projeto.md
- documentation/directives/design/1.ideia-design.md
```

## 4. Gerar projeto definitivo

```text
Leia documentation/directives/project/1.ideia-projeto.md e documentation/directives/project/2.instrucao-projeto.md. Gere documentation/directives/project/5.projeto.md.
```

## 5. Gerar design definitivo

```text
Leia documentation/directives/design/1.ideia-design.md e documentation/directives/design/2.instrucao-design.md. Gere documentation/directives/design/5.design.md.
```

## 6. Aprovação e início da implementação

Após revisar e aprovar `5.projeto.md` e `5.design.md`, execute:

```text
/agente-orquestrador /grill-me /goal

Inicie a implementação do projeto utilizando como fontes de verdade:
- documentation/directives/project/5.projeto.md
- documentation/directives/design/5.design.md

Importe e utilize MCPs disponíveis, inclusive integrações de design no Google Stitch quando aplicável.
Priorize o fluxo principal do MVP, mantendo consistência com os dois documentos.
Não altere requisitos sem registrar a decisão e o motivo.

Siga os SOPs em sop-templates/ e execute gates conforme phases-gates-reports.md.
```

Ou, alternativamente, use o prompt direto:

```text
Leia documentation/directives/4.prompt-antigravity.md e execute conforme instruções.
```

## Resumo do comando principal

O comando chave é:

```text
/agente-orquestrador /grill-me /goal

Inicie a implementação do projeto utilizando como fonte de verdade:
`documentation/directives/project/5.projeto.md` (especificação técnica e funcional)
e `documentation/directives/design/5.design.md` (especificação visual e de UI/UX).

Importe e utilize MCPs disponíveis, inclusive integrações de design no Google Stitch quando aplicável.
Priorize o fluxo principal do MVP, mantendo consistência com os dois documentos.
Não altere requisitos sem registrar a decisão e o motivo.
```

**Importante:** Só execute após aprovar explicitamente `5.projeto.md` e `5.design.md`.