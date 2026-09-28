# Estrutura canônica de projeto

## Template e projeto

No repositório base, a origem versionada é `.ag-template/`. No novo projeto, copie-a para `.ag-template/`; mantenha as diretivas em `.ag-template/documentation/directives/`, sem renomear os 12 arquivos canônicos. `GLOBAL-RULES.md` e `GLOBAL-WORKFLOW.md` são copiados manualmente para as customizações do Antigravity; sua cópia em `.ag-template/agent/` é apenas referência versionada.

```text
projeto/
├── .ag-template/
│   ├── agent/
│   ├── documentation/directives/
│   │   ├── 0.ideia-inicial.md
│   │   ├── 0.prompt-iaexterna-inicial.md
│   │   ├── project/1.ideia-projeto.md ... 5.projeto.md
│   │   └── design/1.ideia-design.md ... 5.design.md
│   ├── security/
│   ├── ci/
│   ├── guides/
│   ├── ui-patterns/
│   └── sop-templates/
├── documentation/  # relatórios, decisões e documentação derivada, quando aplicável
├── src/            # somente quando a stack adotada usar esse caminho
├── tests/          # conforme a stack
├── .gitignore
└── README.md
```

Não criar diretórios vazios nem estruturas de Next.js, funções serverless, scrapers, banco, 3D ou UI sem necessidade validada. `documentation/project/` em guias antigos é um exemplo de documentação derivada, não a entrada canônica nem substituto de `documentation/directives/project/`. Gerar CI específico em `.github/workflows/` somente após seleção da stack e definição dos controles; `ci/github-actions-example.yml` é não executável no local atual. Não mover arquivos sem atualizar referências e verificar consumidores.
