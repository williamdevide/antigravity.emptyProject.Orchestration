# Modelo de ameaças por projeto

Criar um modelo específico ao concluir a arquitetura e revisar quando fluxos, integrações ou dados mudarem. Se não houver dados suficientes, marcar `not-verified` e bloquear a aprovação correspondente.

| Campo | Preenchimento obrigatório |
|---|---|
| Escopo e versão | Sistema, ambiente, commit/data |
| Ativos e dados | Informação sensível, disponibilidade e integridade |
| Diagrama | Fluxos, origens, destinos, armazenamento e limites de confiança |
| Agentes e superfícies | Usuários, terceiros, APIs, dependências, CI/CD e agentes de IA |
| Ameaças | ID, cenário concreto, pré-condição, impacto e probabilidade justificada |
| Tratamento | Controle preventivo/detectivo, responsável, teste e evidência |
| Resíduo | Risco residual, aceitação explícita, prazo de revisão |

Verificar conforme aplicável: controle de acesso por objeto e função, autenticação e sessão, exposição de segredos, validação de entrada e saída, injeção, SSRF, upload, isolamento multi-tenant, criptografia, logs e privacidade, cadeia de suprimentos, integridade do build e permissões da esteira. Evitar checklist sem cenário específico. Registrar requisitos `SEC-###`, riscos `RISK-###`, testes `TEST-###` e rastreá-los até o gate de release. Não executar testes ofensivos fora de ambiente e escopo autorizados.
