# Seleção de bibliotecas frontend

Este guia é opcional e só se aplica quando o projeto tem frontend. Não impor Next.js, React, Tailwind ou versões fixas a todos os projetos; avaliar framework, suporte, compatibilidade, acessibilidade, licença, manutenção, custo e segurança da cadeia de suprimentos. Escolher bibliotecas após requisitos e design aprovados; registrar ADR quando a escolha tiver impacto arquitetural.

## Validação antes do uso

1. Confirmar a versão na documentação e no registry, a compatibilidade com a stack real e o lockfile.
2. Registrar justificativa e alternativas; reduzir dependências desnecessárias.
3. Auditar dependências e revisar avisos de segurança, manutenção, licença e permissões.
4. Testar instalação, build, acessibilidade e uso real em incremento pequeno.
5. Não copiar snippets de autenticação deste ou de outros guias: seguir `ui-patterns/auth-flows.md` e `security/secure-development.md`. Tokens sensíveis em armazenamento legível por JavaScript não devem ser adotados como padrão.

Listas de ferramentas são candidatos, não aprovações ou comandos de instalação. Quando não houver interface, registrar `not-applicable`.
