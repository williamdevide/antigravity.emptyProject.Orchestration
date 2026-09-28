#!/usr/bin/env python3
"""
Utilitário de verificação determinística de gates e ambiente para o Antigravity Orchestrator.
Nunca expõe valores de variáveis nem segredos; valida presença e conformidade estrutural.
"""
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[2]


def parse_env_file(file_path: Path) -> dict:
    """Lê um arquivo .env retornando as chaves encontradas sem valores sensíveis."""
    if not file_path.is_file():
        return {}
    keys = {}
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line:
            key, val = line.split('=', 1)
            key = key.strip()
            val = val.strip().strip('"\'')
            keys[key] = bool(val)
    return keys


def check_env(root: Path = ROOT) -> dict:
    """Compara .env-example com .env e classifica presença de variáveis."""
    example_path = root / '.env-example'
    env_path = root / '.env'
    
    if not example_path.is_file():
        return {'status': 'error', 'message': '.env-example não encontrado.'}
    
    example_keys = parse_env_file(example_path)
    actual_keys = parse_env_file(env_path) if env_path.is_file() else {}
    
    configured = []
    empty_or_missing = []
    
    for k in sorted(example_keys.keys()):
        if k in actual_keys and actual_keys[k]:
            configured.append(k)
        else:
            empty_or_missing.append(k)
            
    return {
        'status': 'ok',
        'has_env': env_path.is_file(),
        'configured_count': len(configured),
        'missing_count': len(empty_or_missing),
        'configured': configured,
        'missing': empty_or_missing,
    }


def check_docs(root: Path = ROOT) -> dict:
    """Verifica presença dos documentos do projeto e conformidade dos identificadores de requisitos."""
    docs_dir = root / 'docs'
    if not docs_dir.is_dir():
        # Fallback para checar diretivas do template caso legado ainda esteja em uso
        alt_dir = root / '.ag-template' / 'documentation' / 'directives'
        if not alt_dir.is_dir():
            return {'status': 'not_found', 'message': 'Pasta docs/ não encontrada.'}
        docs_dir = alt_dir

    findings = []
    rf_count = 0
    rnf_count = 0
    sec_count = 0

    for doc in docs_dir.rglob('*.md'):
        text = doc.read_text(encoding='utf-8', errors='ignore')
        rf_matches = re.findall(r'\bRF-\d{3}\b', text)
        rnf_matches = re.findall(r'\bRNF-\d{3}\b', text)
        sec_matches = re.findall(r'\bSEC-\d{3}\b', text)
        
        rf_count += len(rf_matches)
        rnf_count += len(rnf_matches)
        sec_count += len(sec_matches)

        if '[Digite' in text or '[Qual problema' in text:
            findings.append(f'Placeholders não preenchidos detectados em {doc.name}')

    return {
        'status': 'ok',
        'rf_count': rf_count,
        'rnf_count': rnf_count,
        'sec_count': sec_count,
        'findings': findings
    }


def verify_gate(gate_id: str, root: Path = ROOT) -> int:
    """Verifica as pré-condições do gate especificado."""
    gate = gate_id.lower()
    print(f"=== Verificando Gate: {gate.upper()} ===")
    
    if gate in ('g0', '0'):
        idea = root / '0.ideia-inicial.md'
        if not idea.is_file() or not idea.stat().st_size:
            print("STATUS: FAILED - 0.ideia-inicial.md não existe ou está vazio.")
            return 1
        content = idea.read_text(encoding='utf-8')
        if '[Digite o nome do projeto]' in content:
            print("STATUS: BLOCKED - 0.ideia-inicial.md ainda contém placeholders vazios. Preencha com a ideia real.")
            return 2
        print("STATUS: PASSED - Entrada de ideia inicial substantiva detectada.")
        return 0

    elif gate in ('g1', '1'):
        env_res = check_env(root)
        doc_res = check_docs(root)
        
        print("\n--- Verificação de Documentação e Requisitos ---")
        if doc_res.get('status') != 'ok':
            print(f"Alerta: {doc_res.get('message')}")
        else:
            print(f"Requisitos Funcionais (RF-###): {doc_res['rf_count']}")
            print(f"Requisitos Não-Funcionais (RNF-###): {doc_res['rnf_count']}")
            print(f"Requisitos de Segurança (SEC-###): {doc_res['sec_count']}")
            for f in doc_res['findings']:
                print(f"Aviso: {f}")

        print("\n--- Verificação de Ambiente (.env) ---")
        if not env_res.get('has_env'):
            print("Aviso: Arquivo .env local não criado ainda. (Verifique variáveis necessárias antes de integrar)")
        else:
            print(f"Variáveis configuradas no .env: {env_res['configured_count']}")
            if env_res['missing']:
                print(f"Variáveis não configuradas ou vazias ({len(env_res['missing'])}):")
                for m in env_res['missing'][:10]:
                    print(f"  - {m}")
                if len(env_res['missing']) > 10:
                    print(f"  ... e mais {len(env_res['missing']) - 10} variáveis.")

        print("\nSTATUS: G1 pronto para submissão à aprovação humana. Nenhuma credencial foi exibida.")
        return 0

    else:
        print(f"Gate {gate_id} não possui validação determinística automatizada prévia.")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Auditor de Gates e Ambiente do Antigravity Orchestrator")
    subparsers = parser.add_subparsers(dest="command")

    env_parser = subparsers.add_parser("env-check", help="Checa presença de variáveis do .env sem expor valores")
    docs_parser = subparsers.add_parser("docs-check", help="Checa contagem de requisitos RF/RNF/SEC")
    gate_parser = subparsers.add_parser("gate", help="Valida um gate específico")
    gate_parser.add_argument("--id", required=True, help="Identificador do gate (g0, g1, g2)")

    args = parser.parse_args()

    if args.command == "env-check":
        res = check_env()
        if res.get('status') != 'ok':
            print(res.get('message'))
            sys.exit(1)
        print(f"Arquivo .env presente: {res['has_env']}")
        print(f"Configuradas: {res['configured_count']}")
        print(f"Ausentes ou vazias: {res['missing_count']}")
        if res['missing']:
            print("Variáveis pendentes:")
            for m in res['missing']:
                print(f"  - {m}")
    elif args.command == "docs-check":
        res = check_docs()
        print(f"RF: {res['rf_count']} | RNF: {res['rnf_count']} | SEC: {res['sec_count']}")
        for f in res['findings']:
            print(f"  - {f}")
    elif args.command == "gate":
        sys.exit(verify_gate(args.id))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
