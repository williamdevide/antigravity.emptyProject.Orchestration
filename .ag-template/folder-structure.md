# Estrutura canônica

```text
projeto/
├── 0.ideia-inicial.md        # única entrada de produto; conteúdo real antes de iniciar
├── .ag-template/
│   ├── agent/                # regras globais para customização do IDE
│   ├── documentation/directives/
│   │   ├── 0.prompt-iaexterna-inicial.md
│   │   ├── project/          # 1 a 5; fonte final 5.projeto.md
│   │   └── design/           # 1 a 5; fonte final 5.design.md se houver UI
│   ├── security/
│   ├── project-customization/
│   ├── ci/
│   ├── release/
│   └── sop-templates/
├── .agents/skills/project-orchestrator/SKILL.md
├── documentation/           # documentação derivada e reports, quando aplicáveis
├── .env                    # local, nunca versionar
└── .env-example            # nomes, sem segredos
```

Não duplicar `0.ideia-inicial.md` sob `.ag-template/`. As parciais e finais ficam sob `.ag-template/documentation/directives/`, enquanto `documentation/` na raiz pode receber material derivado, como `applicability.md`. Estrutura de código, banco, UI e CI de aplicação depende do perfil e stack aprovados. Não gerar diretórios irrelevantes.
