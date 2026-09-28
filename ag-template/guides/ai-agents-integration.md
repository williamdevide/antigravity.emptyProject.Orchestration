# Integração de agentes de IA

A skill `project-orchestrator` é o ponto de entrada no workspace. Subagentes e serviços externos são opcionais: não pressupor Claude Code, Codex, GitHub Agents, um MCP ou API específica. Verificar disponibilidade, permissões, custo e escopo antes de delegar; solicitar aprovação específica antes de escritas externas. A documentação e os gates do projeto aprovado têm prioridade sobre sugestões dos agentes.

## Contrato de delegação

Para cada tarefa, definir objetivo e contexto mínimo, arquivos permitidos, dados sensíveis vedados, critérios de aceite, prazo/limite, ferramenta identificada, evidência esperada e responsável pela revisão. Tratar saídas como propostas não confiáveis: revisar diffs, referências e resultados de ferramentas. Nunca usar resultado gerado como prova de teste não executado. Não compartilhar segredos com agente sem avaliação de política, consentimento e controles adequados.

## Ciclo

A ideia produz especificações; após G1 aprovado, cada incremento é implementado, revisado, testado e submetido ao gate. A documentação acompanha o código. A skill reporta o que foi observado, bloqueios e divergências; não realiza deploy por conveniência nem aceita risco em nome do usuário.
