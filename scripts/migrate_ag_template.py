#!/usr/bin/env python3
"""Prévia e migração local de ag-template/ para .ag-template/."""
from pathlib import Path
import argparse
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / 'ag-template'
NEW = ROOT / '.ag-template'
TEXT_SUFFIXES = {'.md', '.yml', '.yaml', '.json', '.py', '.txt', '.sh', '.bat'}
ROOT_TEXT = {'.gitignore', '.env-example'}
PATTERN = re.compile(r'(?<![.\w-])ag-template/')


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if not OLD.is_dir() or NEW.exists():
        raise SystemExit('Esperado: ag-template/ existente e .ag-template/ ausente.')
    if git('rev-parse', '--show-toplevel') != str(ROOT):
        raise SystemExit('Execute na raiz do clone Git.')
    if git('status', '--porcelain'):
        raise SystemExit('Working tree não está limpa.')
    edits = []
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.parts or p == Path(__file__).resolve():
            continue
        if p.suffix not in TEXT_SUFFIXES and p.name not in ROOT_TEXT:
            continue
        try:
            text = p.read_text(encoding='utf-8')
        except UnicodeError:
            continue
        updated = PATTERN.sub('.ag-template/', text)
        if updated != text:
            edits.append((p, updated))
    print('Mover ag-template/ -> .ag-template/; referências a editar:', len(edits))
    for p, _ in edits:
        print(p.relative_to(ROOT))
    if not args.apply:
        print('Somente prévia; use --apply para executar.')
        return
    git('mv', '--', 'ag-template', '.ag-template')
    for old, updated in edits:
        dest = NEW / old.relative_to(OLD) if old.is_relative_to(OLD) else old
        dest.write_text(updated, encoding='utf-8')
    print('Revise git diff --check, git diff HEAD e git status antes de commitar.')


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as error:
        print(error.stderr or str(error), file=sys.stderr)
        sys.exit(1)
