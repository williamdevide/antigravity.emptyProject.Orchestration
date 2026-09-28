# Saúde do projeto por evidência

Avaliar por fase e perfil. Cada item tem estado `passed|failed|blocked|not-verified|not-applicable`, evidência, responsável e data; N/A requer justificativa. Não calcular percentual único que permita compensar falha grave de segurança com documentação.

## Planejamento e projeto

- [ ] Ideia, perfil e aplicabilidade específicos do projeto.
- [ ] Requisitos funcionais, não funcionais e `SEC-###` com critérios verificáveis.
- [ ] Modelo de ameaças baseado em fluxos reais, controles, riscos residuais e aprovação humana.

## Desenvolvimento e integração

- [ ] Revisão de código, testes e autorização conforme arquitetura.
- [ ] CI da stack instalada e executada com build, testes e secret scan; SAST/SCA configurados conforme política aprovada.
- [ ] Relatórios de ferramenta reais; falha ou ausência de controle obrigatório bloqueia o gate.

## Liberação e operação

- [ ] Testes negativos e DAST quando pertinente, apenas em ambiente autorizado.
- [ ] Artefato versionado, staging, smoke, aprovação específica de produção e rollback testado.
- [ ] Monitoramento, vulnerabilidades, incidentes, correções e feedback no backlog.

Registrar em cada revisão: commit, ambiente, data, controles aplicáveis, resultado e links para evidências. Não dizer que uma integração está `verified` apenas porque variável ou exemplo aparece no repositório. `phases-gates-reports.md` é a regra de decisão.
