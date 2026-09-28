# Catálogo e registro de riscos

Este catálogo é um conjunto de hipóteses; nenhum risco do projeto deve receber probabilidade, severidade ou status `verified` por cópia de exemplos. Avaliar cenário real, impacto, exposição, probabilidade justificada, evidência, controle, teste, responsável, prazo e risco residual. Risco crítico não deve ser reduzido a um score numérico que o esconda.

## Categorias

- Produto e requisitos: ambiguidade, alterações de escopo, dependências externas.
- Arquitetura e dados: perda, corrupção, indisponibilidade, falha de backup e recuperação.
- Segurança e privacidade: segredos expostos, autorização incorreta, injeção, dependência vulnerável, dados pessoais e cadeia de suprimentos.
- Integrações: falha de provedor, mudança de API, rate limit e uso sem autorização.
- Entrega: CI não configurado, checks ignorados, artefato não rastreável, deploy sem rollback.
- Operação: alertas ausentes, vulnerabilidades sem triagem, incidente sem resposta.

## Registro obrigatório por risco

| Campo | Valor a preencher no projeto |
|---|---|
| ID e cenário | `RISK-###`, causa, evento e consequência |
| Ativo e exposição | Dado, funcionalidade, usuários e ambiente afetados |
| Severidade e probabilidade | Justificativa e método utilizado; desconhecido se sem evidência |
| Mitigação e detecção | Controles preventivos/detectivos, responsável, prazo |
| Verificação | `SEC-###`, `TEST-###`, resultado e evidência |
| Residual | Decisão de aceitação, aprovador e revisão |

Rever na arquitetura, em alteração de superfície de ataque, em achado SAST/SCA/DAST, em incidente e antes de release. Riscos não tratados e controles obrigatórios ausentes bloqueiam o gate até decisão humana explícita e documentada; nenhuma pontuação isolada é aprovação.
