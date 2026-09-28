# Base de Governança e Ciclo de Vida — Antigravity v2

A pasta `.ag-template/` organiza todos os artefatos de engenharia de software, normas e SOPs agrupados estritamente por **Gates do Ciclo de Vida** e numerados na ordem canônica em que são comumente necessários.

## Hierarquia por Gates Estritos

```text
.ag-template/
├── 00.governanca/
│   ├── 01.regras-globais.md          # Regras fundamentais do agente orquestrador
│   ├── 02.workflow-global.md         # Fluxo operacional canônico
│   ├── 03.orquestracao-ciclo-vida.md # Definição dos Gates G0 a G4
│   ├── 04.fases-gates-relatorios.md  # Tabela de evidências e entregáveis
│   ├── 05.regras-anti-alucinacao.md  # Padrões de evidência e checagem real
│   ├── 06.perfis-de-projeto.md       # Perfis 1 a 6 e matriz de decisão
│   ├── 07.matriz-aplicabilidade.md   # Classificação REQUIRED / OPTIONAL / N/A
│   └── 08.estrutura-canonica.md      # Mapa de pastas e arquivos
│
├── 01.G0_pre-voo/
│   ├── 01.diretrizes-ideia-inicial.md# Critérios para validação da ideia
│   └── 02.checklist-pre-voo.md       # Auditoria pré-voo
│
├── 02.G1_especificacao/
│   ├── 01.documentacao-minima.md     # Relação de docs obrigatórios em docs/
│   ├── 02.catalogo-de-riscos.md      # Catálogo estruturado de riscos
│   ├── 03.contratos-integracao.md    # Contratos para APIs, DB e serviços
│   ├── 04.diretrizes-backlog.md      # Padrões para backlog e histórias
│   ├── 05.modelagem-ameacas-ref.md   # Modelo de ameaças de referência
│   ├── 06.design-e-ui/
│   │   ├── 01.padroes-ui/            # 17 bibliotecas de padrões de UI
│   │   └── 02.guias-tecnicos/        # Guias modernos (web, 3D, MCPs)
│   ├── 07.templates-exportacao/      # Moldes para exportar prompts a IAs externas
│   └── 08.customizacao-projeto/      # Modelos de governança pós-G1
│
├── 03.G2_implementacao/
│   ├── 01.sop-setup-ambiente.md      # SOP de configuração de ambiente dev
│   ├── 02.sop-implementacao.md       # SOP de codificação e incrementos atômicos
│   ├── 03.sop-integracoes.md         # SOP de integração com serviços externos
│   ├── 04.desenvolvimento-seguro.md  # Diretrizes de segurança no código
│   ├── 05.sop-validacao-testes.md    # SOP de testes unitários e funcionais
│   └── 06.sop-validacao-seguranca.md # SOP de checagem de vulnerabilidades
│
├── 04.G3_release/
│   ├── 01.sop-deploy.md              # SOP de promoção e deploy
│   ├── 02.politica-seguranca-ci.md   # Políticas de segurança para CI/CD
│   ├── 03.registro-release.template.md # Template de changelog e release record
│   └── 04.github-actions-exemplo.yml # Workflow exemplo para CI
│
├── 05.G4_operacao/
│   ├── 01.sop-operacao-manutencao.md # SOP de sustentação e operação
│   ├── 02.sop-troubleshooting.md     # SOP de resolução de incidentes
│   └── 03.checklist-saude-projeto.md # Checklist de saúde contínua
│
├── github/                           # Template de validação de repositório
└── scripts/                          # ag-gate.py e validate_template.py
```
