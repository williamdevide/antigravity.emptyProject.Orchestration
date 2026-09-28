# Padrões de autenticação — requisitos, não snippets de produção

Este documento não escolhe um provedor nem entrega código pronto. Defina e aprove a arquitetura de identidade no `docs/architecture.md`, modele ameaças e utilize SDK/mecanismo do provedor comprovado no projeto. Não reutilize exemplos legados com tokens sensíveis em `localStorage` ou proteção de rota apenas no cliente: autorização por recurso deve ocorrer no servidor.

## Fluxos condicionais

- Login: validar dados, responder sem enumerar contas, limitar tentativas, criar sessão de acordo com o modelo de ameaças, garantir logout/invalidação e observar eventos sem registrar senhas.
- Registro: validar identidade e termos quando aplicáveis, impedir enumeração, proteger contra automação e verificar email quando necessário.
- Recuperação: tokens de uso único, expiração, proteção contra replay, confirmação genérica e invalidação de sessões conforme política.
- OAuth: verificar estado, redirecionamentos permitidos, permissões mínimas, vínculo de contas e tratamento de erro; não presumir que um botão implementa o protocolo.

## Critérios de aceite

- Testar acesso negado a recurso de outro usuário e a funções não autorizadas, inclusive requisições diretas à API.
- Testar expiração, logout, revogação, CSRF quando aplicável, mensagens que não revelam se conta existe e limites de tentativa.
- Verificar atributos de sessão e estratégia de armazenamento de credenciais conforme plataforma e ameaça; não copiar estratégia de armazenamento de outros projetos automaticamente.
- Verificar por teste funcional e revisão de segurança, relacionando `SEC-###`, `RISK-###` e `TEST-###`. Se o serviço de identidade estiver ausente, marcar `blocked` ou `not-verified`; não simular autenticação em produção.
