# Base de Orquestração para Novos Projetos (Antigravity v2)

Esta base fornece um framework robusto e disciplinado para criar, especificar e gerenciar o ciclo de vida completo de novos projetos no **Google Antigravity IDE**.

A estrutura combina governança de engenharia de software (gates G0 a G4, rastreabilidade de requisitos, modelagem de ameaças e mitigação de alucinação) com uma raiz 100% limpa e experiência de início direto no chat.

---

## Como Iniciar um Novo Projeto

1. **Preencha a Ideia Inicial**:
   Abra e preencha [`0.ideia-inicial.md`](file:///f:/antigravity/projetos/antigravity.emptyProject.Orchestration/0.ideia-inicial.md) na raiz do projeto com o objetivo real do produto.
2. **Envie o Comando no Chat**:
   > `/project-orchestrator inicie o projeto`
3. **Responda à Entrevista Interativa**:
   O agente conduzirá uma entrevista rápida com cards de múltipla escolha para definir o perfil, a stack tecnológica, as integrações e a abordagem de design.
4. **Revise a Especificação (Gate G1)**:
   A documentação viva do projeto será gerada na pasta [`docs/`](file:///f:/antigravity/projetos/antigravity.emptyProject.Orchestration/docs/):
   - `docs/projeto.md`: Visão e requisitos (`RF-###`, `RNF-###`).
   - `docs/arquitetura.md`: Modelo de dados e integrações.
   - `docs/design.md`: Design system, UI/UX e acessibilidade.
   - `docs/seguranca.md`: Controles (`SEC-###`) e modelo de ameaças.
   - `docs/diagramas/`: Fluxogramas e diagramas visuais de arquitetura.
5. **Aprovação Expressa**:
   O agente roda a auditoria de ambiente sem vazar segredos (`python .ag-template/scripts/ag-gate.py gate --id g1`) e para obrigatoriamente no Gate G1 para sua aprovação antes de qualquer escrita de código.

---

## Estrutura Canônica da Raiz (Limpa)

```text
projeto/
├── 0.ideia-inicial.md        # Entrada única de produto
├── comando-de-inicio.md      # Instruções diretas de início
├── .env-example              # Dicionário de variáveis de ambiente
├── README.md                 # Visão geral da base
├── .gitignore
├── docs/                     # DOCUMENTAÇÃO VIVA DO PROJETO
│   ├── projeto.md            # Especificação funcional e requisitos
│   ├── arquitetura.md        # Modelo técnico e dados
│   ├── design.md             # Especificação visual e UI
│   ├── seguranca.md          # Controles SEC e ameaças
│   └── diagramas/            # Diagramas Mermaid e fluxogramas
├── .agents/skills/project-orchestrator/SKILL.md # Skill orquestradora
└── .ag-template/             # MOTOR DE GOVERNANÇA (Organizado por Gates)
    ├── 00.governanca/        # Regras globais, ciclo de vida e perfis
    ├── 01.G0_pre-voo/        # Diretrizes da ideia inicial
    ├── 02.G1_especificacao/  # Requisitos, contratos, UI patterns e design
    ├── 03.G2_implementacao/  # SOPs de dev, setup, segurança e testes
    ├── 04.G3_release/        # CI/CD, deploy SOP e templates de release
    ├── 05.G4_operacao/       # Manutenção, telemetria e troubleshooting
    ├── github/               # Templates de workflows para GitHub Actions
    └── scripts/              # ag-gate.py e validate_template.py
```

---

*Consulte [`.ag-template/00.governanca/03.orquestracao-ciclo-vida.md`](file:///f:/antigravity/projetos/antigravity.emptyProject.Orchestration/.ag-template/00.governanca/03.orquestracao-ciclo-vida.md) para detalhes completos sobre as fases, gates e evidências de entrega.*
