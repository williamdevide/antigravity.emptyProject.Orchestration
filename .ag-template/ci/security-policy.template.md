# Política de verificações de CI — [projeto]

Preencher após definir a stack; não confundir este modelo com uma esteira já ativa. Referenciar o workflow real, trigger, branch protegida, responsável e data da última execução bem-sucedida.

| Controle | Ferramenta e versão | Gatilho | Limiar de falha | Evidência | Exceção e prazo |
|---|---|---|---|---|---|
| Build e testes | [stack] | PR/push | [definir] | [run] | [decisão] |
| Busca de segredos | [ferramenta] | PR/push | [definir] | [run] | [decisão] |
| SAST | [ferramenta] | PR/push | [definir] | [run] | [decisão] |
| SCA | [ferramenta] | PR/push/agendado | [definir] | [run] | [decisão] |
| DAST, se aplicável | [ferramenta] | staging autorizado | [definir] | [run] | [decisão] |

Falha de execução, configuração ausente ou relatório inválido bloqueia gate obrigatório. Revisar permissões de tokens, dependências da própria CI, proteção de branch, retenção de artefatos e exposição de logs. Justificar N/A pelo perfil/ameaça e registrar aceitação excepcional de achado com dono, mitigação e data de expiração; não desabilitar controles silenciosamente.
