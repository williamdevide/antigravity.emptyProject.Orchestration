# Uso opcional de kits para Antigravity

Este template não depende de kit, CLI ou plugin para iniciar. A entrada é o comando em `comando-de-inicio.md`, e as regras globais são instaladas pelo usuário nas customizações do IDE. Não presumir que `ag-kit create`, `sync`, `validate` ou `/goal` e `/grill-me` existam.

Se o projeto optar por um kit de terceiros, identificar pacote, mantenedor, versão, documentação oficial, permissões, arquivos criados e comando de instalação confirmado na máquina. Executar primeiro em workspace isolado; revisar alterações em regras, hooks e MCP antes de habilitar, especialmente comandos que executam programas ou acessam segredos. Não instalar via `npx` ou globalmente apenas por constar neste guia. Registrar o kit como `not-verified` até prova no ambiente do projeto. Nenhum hook substitui revisão, proteção de branch e aprovações para produção.
