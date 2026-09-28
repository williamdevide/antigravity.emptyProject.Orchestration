# SOP — Validação de segurança

Aplicar conforme ameaças e aplicabilidade; registrar `not-applicable` justificado. Nunca executar testes ofensivos fora do ambiente e escopo autorizados.

1. Revisar modelo de ameaças, requisitos `SEC-###`, critérios e riscos residuais.
2. Em PR, confirmar origem de dependências, verificar segredos, SAST e SCA configurados; preservar resultados e tratar achados por severidade contextual.
3. Exercitar testes de autorização por recurso, entradas inválidas, sessão, rate limit e fluxos de erro quando pertinentes. Não assumir que scanner substitui teste manual.
4. Para DAST, obter autorização, URL de staging isolada, janela, limite de tráfego, credenciais de teste e responsável; evitar produção e dados reais; registrar escopo e versão testada.
5. Retestar correções, relacionar achado → risco → controle → teste → evidência. Não reduzir severidade nem suprimir falha sem justificativa rastreável e aceitação humana.
6. Gate: se controle obrigatório falhar, estiver ausente ou sem prova, bloquear release; exceção exige aprovador, mitigação, prazo e revisão.

Relatório: commit, ambiente, ferramenta/versão, escopo, comandos ou execução, achados, falsos positivos justificados, responsáveis, prazo, resultado e evidências sem payload sensível.
