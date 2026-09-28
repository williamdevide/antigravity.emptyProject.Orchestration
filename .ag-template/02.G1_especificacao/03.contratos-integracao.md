# Contratos de integração

Integrações não são presumidas pelo template. Para cada serviço, registrar: propósito, dono, ambiente, permissões mínimas, origem da documentação, variáveis necessárias sem valores, esquema de entrada/saída, tratamento de erros, rate limit, dados pessoais, fallback, monitoramento e procedimento de revogação/rollback.

## Estados

- `not-configured`: não habilitado.
- `configured`: configuração presente, sem execução de verificação suficiente.
- `not-verified`: implementação declarada, mas comportamento ainda sem prova.
- `verified`: chamada ou teste real passou, com data, ambiente e evidência.
- `blocked`: necessário e bloqueado, com causa e responsável.
- `not-applicable`: não é usado, com justificativa.

Não usar arquivo `.env-example` como evidência de configuração, nem sinalizar `verified` apenas por variável definida. Nunca registrar o valor de segredo. Fixtures devem ser identificadas como simulação, não resultado de produção.

## Checklist de aceite

1. Confirmar necessidade e autorização do projeto.
2. Consultar documentação oficial atual da integração; confirmar se SDK, CLI, MCP e métodos existem antes de incluí-los em comandos.
3. Configurar secret manager/variáveis no ambiente autorizado; conferir escopos mínimos e expiração.
4. Executar teste de conectividade e casos de sucesso/falha; guardar evidência sem dados sensíveis.
5. Definir timeout, retry com limites, observabilidade e resposta à indisponibilidade.
6. Se houver escrita externa, deploy ou modificação de dados, pedir aprovação específica antes de executar.
7. Atualizar status, responsável, data da última prova, teste e plano de revogação.

Para scrapers: verificar autorização, termos e acesso permitido; não orientar contorno de bloqueios ou CAPTCHA. Guardar origem e data da amostra, campos efetivamente observados e limites de coleta. Para Google Stitch: ID e telas precisam ser verificados por acesso real; percentual de fidelidade só se houver método de comparação documentado. Para GitHub: jamais embutir token em URL/commit; usar proteção de branch, permissões mínimas e revisões conforme risco. Para dados: validar autorização por recurso, retenção, backup e restore quando aplicável.
