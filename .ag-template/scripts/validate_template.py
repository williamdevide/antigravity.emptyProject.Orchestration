#!/usr/bin/env python3
"""Valida estrutura canônica da base organizada por gates estritos."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    '0.ideia-inicial.md',
    'comando-de-inicio.md',
    'README.md',
    '.agents/skills/project-orchestrator/SKILL.md',
    '.ag-template/00.governanca/01.regras-globais.md',
    '.ag-template/00.governanca/02.workflow-global.md',
    '.ag-template/00.governanca/03.orquestracao-ciclo-vida.md',
    '.ag-template/00.governanca/04.fases-gates-relatorios.md',
    '.ag-template/01.G0_pre-voo/01.diretrizes-ideia-inicial.md',
    '.ag-template/02.G1_especificacao/01.documentacao-minima.md',
    '.ag-template/02.G1_especificacao/05.modelagem-ameacas-ref.md',
    '.ag-template/03.G2_implementacao/04.desenvolvimento-seguro.md',
    '.ag-template/04.G3_release/02.politica-seguranca-ci.md',
    '.ag-template/04.G3_release/03.registro-release.template.md',
    '.ag-template/05.G4_operacao/01.sop-operacao-manutencao.md',
    '.ag-template/scripts/ag-gate.py',
    'docs/diagramas/README.md',
]


def check(root=ROOT):
    errors = []
    for name in REQUIRED:
        path = root / name
        if not path.is_file() or not path.stat().st_size:
            errors.append(f'Ausente ou vazio: {name}')
            
    base = root / '.ag-template'
    if (root / 'ag-template').exists():
        errors.append('Pasta legada ag-template/ ainda existe na raiz.')
    if (root / 'scripts').exists():
        errors.append('scripts/ na raiz deve ser mantido dentro de .ag-template/scripts/.')
    if (root / '.github').exists():
        errors.append('.github/ na raiz deve ser mantido em .ag-template/github/.')
        
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
    print('Estrutura canônica validada por gates estritos com sucesso!')
