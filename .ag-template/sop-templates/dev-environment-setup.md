# SOP — Development Environment Setup

## Objetivo

Configurar, validar e registrar um ambiente local reproduzível para qualquer projeto criado a partir do `ag-template`.

## Escopo

Aplica-se a novos desenvolvedores, novos workspaces, reconfiguração de ambiente e onboarding de agentes.

## Responsáveis

- Desenvolvedor: executar os passos e registrar falhas.
- Tech Lead: revisar bloqueios e exceções.
- Antigravity: orientar, validar e nunca inventar credenciais ou resultados.

## Pré-requisitos

- Node.js conforme a versão declarada em `package.json`, `.nvmrc` ou `engines`.
- Git instalado e configurado.
- Gerenciador de pacotes definido pelo lockfile.
- Editor de código.
- Acesso autorizado ao repositório.
- `.env.example` disponível.
- Serviços externos identificados no `project-profile.md` e em `applicability.md`.

## Entradas

- URL do repositório.
- Nome do projeto.
- Lockfile (`package-lock.json`, `pnpm-lock.yaml` ou `yarn.lock`).
- `.env.example`.
- Documentação do projeto.

## Procedimento

### 1. Clonar e selecionar o projeto

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
git status
```

Confirmar branch, remote e estado limpo antes de modificar arquivos.

### 2. Validar versões

```bash
node --version
npm --version
git --version
```

Usar a versão definida pelo projeto. Não atualizar a stack sem registrar a decisão.

### 3. Instalar dependências

Usar o gerenciador correspondente ao lockfile:

```bash
npm ci
# ou
pnpm install --frozen-lockfile
# ou
yarn install --frozen-lockfile
```

### 4. Configurar variáveis locais

```bash
cp .env.example .env
```

Preencher apenas valores autorizados. Nunca copiar secrets de produção para o ambiente local sem autorização explícita. Nunca commitar `.env`.

### 5. Configurar serviços locais

Quando aplicável:

```bash
npm run db:migrate
npm run db:seed
```

Se houver Docker, Firebase, Supabase, PostgreSQL ou outro serviço, seguir o contrato de integração específico. Se a integração não estiver disponível, registrar `blocked` ou `not-verified`; não usar mock silencioso.

### 6. Validar estrutura e documentação

```bash
npm run validate:structure
npm run validate:docs
npm run validate:integrations
```

Executar somente comandos existentes no projeto. Se um script não existir, registrar a ausência em vez de afirmar que foi executado.

### 7. Iniciar a aplicação

```bash
npm run dev
```

Confirmar a URL indicada pelo projeto, por exemplo `http://localhost:3000`.

### 8. Executar validação mínima

```bash
npm run type-check
npm run lint
npm test
npm run build
```

Executar os comandos disponíveis e registrar o resultado de cada um.

## Critérios de Sucesso

- [ ] Repositório clonado e branch confirmada.
- [ ] Versões compatíveis.
- [ ] Dependências instaladas pelo lockfile.
- [ ] `.env` local configurado sem secrets expostos.
- [ ] Banco e serviços necessários acessíveis ou bloqueios documentados.
- [ ] Aplicação iniciada sem erro fatal.
- [ ] Typecheck, lint, testes e build passando quando aplicáveis.
- [ ] Relatório de setup preenchido.

## Tratamento de Falhas

- Dependências: verificar versão do Node e lockfile antes de remover `node_modules`.
- Banco: verificar variáveis, conexão, migrations e permissões.
- Porta ocupada: identificar o processo ou usar uma porta documentada.
- Integração bloqueada: registrar fonte, erro, impacto e próximo passo.
- Falha de build: preservar a mensagem original e reproduzir com comando mínimo.

Não apagar dados, resetar banco ou remover arquivos sem confirmar o impacto.

## Evidências e Registros

Registrar em `documentation/reports/dev-environment-setup.md`:

```md
# Relatório — Development Environment Setup

**Data:** YYYY-MM-DD
**Projeto:** [nome]
**Responsável:** [nome]

## Comandos

| Comando | Resultado | Observação |
|---|---|---|
| `npm ci` | passed/failed | |
| `npm run dev` | passed/failed | |
| `npm run type-check` | passed/failed/not-applicable | |
| `npm run lint` | passed/failed/not-applicable | |
| `npm test` | passed/failed/not-applicable | |
| `npm run build` | passed/failed/not-applicable | |

## Integrações

| Integração | Estado | Observação |
|---|---|---|
| GitHub | configured/verified/blocked | |
| Banco | configured/verified/blocked | |

## Bloqueios

- [ ] Nenhum
- [ ] [Descrição]

## Resultado

`aprovado` | `aprovado-com-reservas` | `reprovado`
```

## Frequência ou Gatilho

- Novo desenvolvedor ou agente.
- Novo projeto.
- Mudança de stack, dependência ou serviço externo.
- Falha de ambiente que exige reconstrução.

## Revisão e Histórico

Revisar quando houver mudança em comandos, versões, serviços ou estrutura. Registrar a alteração no changelog do projeto.

## Referências

- `GLOBAL-RULES.md`
- `integration-contracts.md`
- `anti-hallucination-rules.md`
- `project-health-checklist.md`