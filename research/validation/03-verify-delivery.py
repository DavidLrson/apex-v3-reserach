#!/usr/bin/env python3
"""Validate this research handoff's references, not its truth or a live Apex runtime.

Default: require actual linked files in a complete checkout.
--allow-baseline-metadata: permit explicit, pinned baseline metadata when old
files are unavailable locally. This weaker mode is reported, never disguised.
Only the final_documents listed in the index and their simple inline links are
checked. This is not a general Markdown parser. Python standard library only.
"""
from __future__ import annotations
import argparse
import copy
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

INDEX = 'research/03-decision-index.json'
HANDOFF = 'ARCHITECTURE-RESEARCH-HANDOFF.md'
EXPECTED = {f'AR-{n:03d}' for n in range(1, 19)}
STATES = {'RECOMMENDED_FOR_DESIGN', 'DEFER_TO_V2_EVIDENCE', 'CONDITIONAL_PILOT'}
REQUIRED_HEADINGS = (
    '## 1. Mission and owner requirements', '## 2. Your remit and required inputs',
    '## 4. Five responsibility buckets', '## 6. Concrete next sequence for the builder',
    '## 7. Unresolved facts and how they affect progress',
    '## 8. What was actually verified here', '## 9. Expected output from the fourth chat',
)


def anchors(text: str) -> set[str]:
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        title = re.sub(r'<[^>]+>', '', title)
        found.add(re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-'))
    return found


def validate(root: Path, index: dict, documents: dict[str, str], allow_metadata: bool) -> dict:
    errors: list[str] = []
    metadata_targets: set[str] = set()
    rows = index.get('decisions', [])
    ids = [row.get('id') for row in rows]
    if len(ids) != 18 or set(ids) != EXPECTED:
        errors.append('Decision IDs must contain AR-001 through AR-018 exactly once')
    if index.get('production_authorized') is not False:
        errors.append('Research must not authorize production')
    if index.get('live_projects_tests') != 'NOT RUN':
        errors.append('Live Projects test state must remain NOT RUN for this delivery')
    for row in rows:
        if row.get('disposition') not in STATES:
            errors.append(f"Unknown disposition: {row.get('id')}")
        for dep in row.get('design_dependencies', []):
            if dep not in EXPECTED or dep == row.get('id'):
                errors.append(f"Invalid decision dependency: {row.get('id')} -> {dep}")
        if row.get('rationale') != f"research/02-information-architecture.md#{str(row.get('id')).lower()}":
            errors.append(f"Unexpected canonical rationale: {row.get('id')}")
        if any(t not in {f'T{i:02d}' for i in range(1, 16)} for t in row.get('live_test_ids', [])):
            errors.append(f"Unknown live-test ID: {row.get('id')}")
        if any(q not in {f'Q{i:02d}' for i in range(1, 10)} for q in row.get('open_question_ids', [])):
            errors.append(f"Unknown open-question ID: {row.get('id')}")
    graph = {r.get('id'): r.get('design_dependencies', []) for r in rows}
    active, done = set(), set()
    def walk(node: str) -> None:
        if node in active:
            raise ValueError('Decision dependency cycle')
        if node in done or node not in graph:
            return
        active.add(node)
        for dep in graph[node]:
            walk(dep)
        active.remove(node)
        done.add(node)
    try:
        for node in graph:
            walk(node)
    except ValueError as exc:
        errors.append(str(exc))
    for heading in REQUIRED_HEADINGS:
        if heading not in documents.get(HANDOFF, ''):
            errors.append(f'Missing handoff section: {heading}')
    links_checked = 0
    for path, text in documents.items():
        for rid in re.findall(r'\bAR-\d{3}\b', text):
            if rid not in EXPECTED:
                errors.append(f'{path}: unknown decision {rid}')
        for tid in re.findall(r'\bT\d{2}\b', text):
            if tid not in {f'T{i:02d}' for i in range(1, 16)}:
                errors.append(f'{path}: unknown live-test {tid}')
        for qid in re.findall(r'\bQ\d{2}\b', text):
            if qid not in {f'Q{i:02d}' for i in range(1, 10)}:
                errors.append(f'{path}: unknown question {qid}')
        clean = re.sub(r'(?ms)^```[^\n]*\n.*?^```[ \t]*$', '', text)
        targets = re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', clean)
        if path == HANDOFF:
            targets += [r.get('rationale', '') for r in rows]
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            links_checked += 1
            # The index stores repo-relative rationale paths; prose links are file-relative.
            base = root if path == HANDOFF and target.startswith('research/') else (root / path).parent
            candidate = (base / unquote(parsed.path)).resolve() if parsed.path else root / path
            try:
                relative = candidate.relative_to(root).as_posix()
            except ValueError:
                errors.append(f'{path}: target leaves repository: {target}')
                continue
            content = documents.get(relative)
            if content is None and candidate.is_file():
                if candidate.suffix == '.md':
                    content = candidate.read_text(encoding='utf-8')
            elif content is None and not candidate.exists():
                baseline = index.get('baseline_files', {})
                if allow_metadata and relative in baseline:
                    metadata_targets.add(relative)
                    if parsed.fragment and unquote(parsed.fragment) not in index.get('baseline_anchor_evidence', {}).get(relative, []):
                        errors.append(f'{path}: baseline fragment not covered by evidence: {target}')
                    continue
                errors.append(f'{path}: missing local target: {target}')
                continue
            if parsed.fragment and content is not None and unquote(parsed.fragment) not in anchors(content):
                errors.append(f'{path}: missing anchor: {target}')
    return {'ok': not errors, 'errors': errors, 'simple_local_links_checked': links_checked,
            'baseline_metadata_targets': sorted(metadata_targets),
            'scope': 'Final-document reference and index integrity only; no semantic or runtime validation'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--allow-baseline-metadata', action='store_true')
    parser.add_argument('--self-test', action='store_true', help='Run in-memory negative controls')
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        index = json.loads((root / INDEX).read_text(encoding='utf-8'))
        documents = {}
        for p in index['final_documents']:
            candidate = (root / p).resolve()
            if not candidate.is_relative_to(root):
                raise ValueError('Final document leaves repository root')
            documents[p] = candidate.read_text(encoding='utf-8')
        result = validate(root, index, documents, args.allow_baseline_metadata)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, indent=2))
        return 2
    output = {'mode': 'explicit-baseline-metadata' if args.allow_baseline_metadata else 'local-files-required',
              'result': result}
    if args.self_test:
        cases = []
        mutations = ['duplicate_id','dangling_link','unknown_test','bad_disposition','missing_section','dependency_cycle','false_prose']
        for name in mutations:
            modified = copy.deepcopy(index)
            texts = documents.copy()
            expected = name == 'false_prose'
            if name == 'duplicate_id': modified['decisions'][1]['id'] = 'AR-001'
            elif name == 'dangling_link': texts[HANDOFF] += '\n[bad](missing-final-evidence.md)\n'
            elif name == 'unknown_test': modified['decisions'][0]['live_test_ids'].append('T99')
            elif name == 'bad_disposition': modified['decisions'][0]['disposition'] = 'PRODUCTION_CERTIFIED'
            elif name == 'missing_section': texts[HANDOFF] = texts[HANDOFF].replace(REQUIRED_HEADINGS[0], '## Removed section')
            elif name == 'dependency_cycle': modified['decisions'][0]['design_dependencies'] = ['AR-002']
            elif name == 'false_prose': texts[HANDOFF] += '\nSynthetic control: two plus two equals five.\n'
            checked = validate(root, modified, texts, args.allow_baseline_metadata)
            cases.append({'case': name, 'expected_ok': expected, 'actual_ok': checked['ok'],
                          'matched_expectation': checked['ok'] == expected, 'errors': checked['errors']})
        output['negative_controls'] = cases
        output['negative_controls_all_matched'] = all(c['matched_expectation'] for c in cases)
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if result['ok'] and output.get('negative_controls_all_matched', True) else 1

if __name__ == '__main__':
    sys.exit(main())
