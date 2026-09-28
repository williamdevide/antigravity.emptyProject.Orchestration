# Fases, gates e relatórios

A fonte canônica do fluxo é `lifecycle-orchestration.md`. Este documento define a evidência mínima e não substitui aprovação humana. Não impor frontend, banco ou design a projeto que não os exige.

| Gate | Entrega | Evidência mínima | Decisão |
|---|---|---|---|
| G0 Entrada | Ideia real, perfil e aplicabilidade | Arquivo de ideia não vazio; escopo, premissas e N/A justificados | Prosseguir ou pedir informação |
| G1 Especificação | `5.projeto.md` e `5.design.md` se aplicável | Requisitos `RF/RNF/SEC`, critérios, riscos, ameaças, controles e rastreabilidade | Aprovação expressa antes do código |
| G2 Incremento | Código e documentação alinhados | PR/diff, testes, revisão, resultados de lint/build/SAST/SCA/segredos conforme política | Aprovado ou bloqueado |
| G3 Liberação | Artefato imutável e staging validado | Versão, checks, achados, DAST quando aplicável, smoke, rollback e aprovação | Autorizar promoção específica |
| G4 Operação | Serviço observado | Health, alertas, vulnerabilidades, incidentes, correções e retroalimentação | Manter ou acionar resposta |

Cada relatório deve indicar: gate, commit/versão, ambiente, data, responsável, tabela de requisitos e riscos com teste/evidência, controles aplicáveis e N/A justificados, resultados `passed|failed|blocked|not-verified|not-applicable`, exceções com prazo/mitigação/aprovador e decisão assinada. Um gate obrigatório `failed`, `blocked` ou `not-verified` não é aprovado por omissão. A exceção exige decisão humana explícita, com registro; nunca é implícita.
