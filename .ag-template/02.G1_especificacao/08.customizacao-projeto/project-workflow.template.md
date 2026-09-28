# Workflow específico — [nome do projeto]

**Status:** rascunho até G1. **Base:** [commit e especificações aprovadas].

## Fases e comandos

| Gate | Entregável | Comando real ou verificação | Evidência | Responsável | Aprovação |
|---|---|---|---|---|---|
| G0 | Ideia, perfil, aplicabilidade | [verificar] | [caminho] | [pessoa] | [decisão] |
| G1 | Projeto, design se aplicável, ameaças | [revisar] | [caminho] | [pessoa] | expressa |
| G2 | Incremento, testes, segurança | [comandos da stack] | [CI/PR] | [pessoa] | [critério] |
| G3 | Artefato, staging, release | [workflow real] | [digest, smoke, rollback] | [pessoa] | expressa para produção |
| G4 | Operação e melhoria | [health, alertas] | [incidente/relatório] | [pessoa] | [critério] |

Comando ausente = `not-verified`, nunca sucesso. Definir quais verificações são obrigatórias conforme risco e registrar N/A. DAST só em ambiente autorizado. A skill pode coordenar, mas não promover gates sem evidência e aprovações.
