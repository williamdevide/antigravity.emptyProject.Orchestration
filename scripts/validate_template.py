#!/usr/bin/env python3
"""Valida invariantes estruturais da base de orquestração; somente leitura."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.ag-template'
DIRECTIVES = BASE / 'documentation' / 'directives'
REQUIRED = [
    BASE / 'agent' / 'GLOBAL-RULES.md',
    BASE / 'agent' / 'GLOBAL-WORKFLOW.md',
    BASE / 'lifecycle-orchestration.md',
    BASE / 'phases-gates-reports.md',
    BASE / 'security' / 'threat-model.md',
    BASE / 'security' / 'secure-development.md',
    BASE / 'ci' / 'security-policy.template.md',
    BASE / 'release' / 'release-record.template.md',
    ROOT / '.agents' / 'skills' / 'project-orchestrator' / 'SKILL.md',
    ROOT / 'comando-de-inicio.md',
]
EXPECTED = {
    '0.ideia-inicial.md', '0.prompt-iaexterna-inicial.md',
    'project/1.ideia-projeto.md', 'project/2.instrucao-projeto.md',
    'project/3.prompt-iaexterna-projeto.md', 'project/4.prompt-antigravity.md',
    'project/5.projeto.md',
    'design/1.ideia-design.md', 'design/2.instrucao-design.md',
    'design/3.prompt-iaexterna-design.md', 'design/4.prompt-stitch-design.md',
    'design/5.design.md',
}


def check(root=ROOT):
    base = root / '.ag-template'
    directives = base / 'documentation' / 'directives'
    errors = []
    if (root / 'ag-template').exists():
        errors.append('Pasta antiga ag-template/ ainda existe.')
    for path in REQUIRED:
        target = root / path.relative_to(ROOT)
        if not target.is_file() or target.stat().st_size == 0:
            errors.append(f'Ausente ou vazio: {target.relative_to(root)}')
    if directives.is_dir():
        found = {str(p.relative_to(directives)).replace('\\', '/') for p in directives.rglob('*.md')}
        errors.extend(f'Diretiva ausente: {name}' for name in sorted(EXPECTED - found))
        errors.extend(f'Diretiva inesperada: {name}' for name in sorted(found - EXPECTED))
    else:
        errors.append('Diretório de diretivas ausente.')
    for name in ('rules.md', 'workflows.md', 'agent-orchestration.md'):
        if (base / 'agent' / name).exists():
            errors.append(f'Agente legado presente: {name}')
    skill = root / '.agents' / 'skills' / 'project-orchestrator' / 'SKILL.md'
    if skill.is_file():
        text = skill.read_text(encoding='utf-8')
        if not re.match(r'\A---\s*\n(?:.|\n)*?\bname:\s*project-orchestrator\b(?:.|\n)*?\n---\s*\n', text):
            errors.append('SKILL.md sem frontmatter name: project-orchestrator.')
    for path in (root / 'README.md', root / 'comando-de-inicio.md', skill):
        if path.is_file() and '..ag-template/' in path.read_text(encoding='utf-8'):
            errors.append(f'Referência duplicada ..ag-template/: {path.relative_to(root)}')
    return errors


if __name__ == '__main__':
    problems = check()
    for problem in problems:
        print('ERRO:', problem, file=sys.stderr)
    if problems:
        sys.exit(1)
    print('Estrutura do template validada; funcionamento do IDE e segurança do software não foram testados.')
