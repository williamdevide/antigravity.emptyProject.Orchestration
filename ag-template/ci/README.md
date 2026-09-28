# CI e CD por projeto

`github-actions-example.yml` nesta pasta é ilustrativo e não roda aqui. No projeto gerado, depois de definir stack e política de risco, implementar workflow real em `.github/workflows/`; aplicar menor privilégio às permissões, revisão de mudanças na própria esteira e versões de ações auditadas/pinadas.

Em PR e push protegido: validar documentação aplicável, instalar dependências pelo lockfile, build/lint/typecheck/testes existentes, scan de segredos, SAST e SCA. Cada controle precisa falhar o job quando exceder o limiar aprovado; achados e ausências não viram sucesso silencioso. Publicar evidências sem credenciais. Para DAST: staging autorizado e gatilho controlado.

CD deve promover o mesmo artefato identificado por commit/digest entre ambientes, com aprovação de produção, credenciais restritas, smoke/health, rollback e monitoramento pós-deploy. Não incluir job de produção automático por padrão: provedor e ambientes ainda são desconhecidos. Registre quais jobs existem e uma execução real antes de marcar CI/CD `verified`.
