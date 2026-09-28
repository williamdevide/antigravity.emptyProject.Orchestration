#!/usr/bin/env python3
"""Valida estrutura e caminhos da base; não valida credenciais nem execução do IDE."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    '0.ideia-inicial.md', '.ag-template/agent/GLOBAL-RULES.md',
    '.ag-template/agent/GLOBAL-WORKFLOW.md', '.ag-template/lifecycle-orchestration.md',
    '.ag-template/phases-gates-reports.md', '.ag-template/security/threat-model.md',
    '.ag-template/security/secure-development.md',
    '.ag-template/ci/security-policy.template.md',
    '.ag-template/release/release-record.template.md',
    '.agents/skills/project-orchestrator/SKILL.md', 'comando-de-inicio.md',
]
DIRECTIVES = {
    '0.prompt-iaexterna-inicial.md',
    'project/1.ideia-projeto.md', 'project/2.instrucao-projeto.md',
    'project/3.prompt-iaexterna-projeto.md', 'project/4.prompt-antigravity.md',
    'project/5.projeto.md',
    'design/1.ideia-design.md', 'design/2.instrucao-design.md',
    'design/3.prompt-iaexterna-design.md', 'design/4.prompt-stitch-design.md',
    'design/5.design.md',
}


def check(root=ROOT):
    errors = []
    for name in REQUIRED:
        path = root / name
        if not path.is_file() or not path.stat().st_size:
            errors.append(f'Ausente ou vazio: {name}')
    base = root / '.ag-template'
    if (root / 'ag-template').exists():
        errors.append('Pasta legada ag-template/ ainda existe.')
    if (base / 'documentation/directives/0.ideia-inicial.md').exists():
        errors.append('Ideia duplicada nas diretivas: a entrada é 0.ideia-inicial.md na raiz.')
    folder = base / 'documentation/directives'
    if folder.is_dir():
        found = {p.relative_to(folder).as_posix() for p in folder.rglob('*.md')}
        errors += [f'Diretiva ausente: {n}' for n in sorted(DIRECTIVES - found)]
        errors += [f'Diretiva inesperada: {n}' for n in sorted(found - DIRECTIVES)]
    else:
        errors.append('Diretório de diretivas ausente.')
    for n in ('rules.md', 'workflows.md', 'agent-orchestration.md'):
        if (base / 'agent' / n).exists():
            errors.append(f'Agente legado presente: {n}')
    skill = root / '.agents/skills/project-orchestrator/SKILL.md'
    if skill.is_file() and not re.search(r'(?m)^name:\s*project-orchestrator\s*$', skill.read_text(encoding='utf-8')):
        errors.append('SKILL.md sem name: project-orchestrator.')
    return errors


if __name__ == '__main__':
    problems = check()
    for problem in problems:
        print('ERRO:', problem, file=sys.stderr)
    if problems:
        sys.exit(1)
    print('Estrutura validada; conteúdo, comandos e integrações não foram testados.')
