# Desenvolvimento e verificação seguros

## Antes do código

Para cada história, definir critérios de aceite e abuso, dados tratados, controles e testes. Verificar bibliotecas e versões na stack real; não copiar exemplos dos guias como código pronto para produção.

## Na implementação

Aplicar menor privilégio, autorização no servidor para cada recurso, validação de entradas, codificação de saída contextual, consultas parametrizadas, gestão de sessão e segredos em serviço apropriado, criptografia e observabilidade sem dados sensíveis. Revisar dependências novas e mudanças de permissões. Não usar tokens sensíveis em `localStorage` como padrão de autenticação; escolher mecanismo conforme modelo de ameaças e arquitetura. Testar caminhos de erro e negação.

## Revisão e evidências

A cada PR: relacionar requisito e risco, apresentar mudanças, testes funcionais e negativos, resultado real de lint/typecheck/build quando aplicável, scan de segredos, SAST e SCA configurados, falsos positivos justificados e achados priorizados. Se uma ferramenta não estiver disponível, registrar `not-verified` e bloquear o gate que a exigir. Não publicar logs de segredos ou dados pessoais. Revisão por outra pessoa quando houver autenticação, pagamentos, autorização, migração destrutiva ou mudanças na esteira.
