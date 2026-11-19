"""Verify archived Item generation and all 30 executions without local originals or a DB."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
REVISIONS = {
    'parent': '15980860ac2639f41dfbda2f7fffb7aeeab32921',
    'target': '248c7f7c227e76f3422378ca3b9e10d141dcfc86',
}


def load(path):
    return json.loads(path.read_bytes())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_xml(raw):
    body = re.sub(rb'<\?xml[^?]*\?>', b'', raw)
    tree = ET.fromstring(b'<all>' + body + b'</all>')
    nil = '{http://www.w3.org/2001/XMLSchema-instance}nil'
    sets = []
    for result in tree:
        assert result.tag == 'resultset'
        rows = result.findall('row')
        columns = [c.get('name') for c in rows[0]] if rows else []
        assert all([c.get('name') for c in row] == columns for row in rows)
        sets.append({'columns': columns, 'rows': [
            [None if c.get(nil) == 'true' else c.text or '' for c in row] for row in rows
        ]})
    return sets


def main():
    provenance = load(ROOT / 'provenance.json')
    for item in provenance['files']:
        assert digest(ROOT / item['destination']) == item['archive_sha256'], item['destination']
        if item['byte_preserved']:
            assert item['source_sha256'] == item['archive_sha256']
    manifest = load(ROOT / 'history/run_manifest.json')
    summary = load(ROOT / 'history/verification_summary.json')
    assert manifest['run_id'] == summary['run_id'] == 'run_026_item_rerun_20261118'
    assert manifest['generation_acceptance'] == 'unaccepted_model_identity_mismatch'
    assert manifest['feedback'] is False and manifest['trials_per_side'] == 3
    assert manifest['parent'] == summary['parent_revision'] == REVISIONS['parent']
    assert manifest['target'] == summary['target_revision'] == REVISIONS['target']
    generation = ROOT / 'generation'
    requests, responses = {}, {}
    for stage in (1, 2):
        requests[stage] = load(generation / f'stage{stage}_request.json')
        responses[stage] = load(generation / f'stage{stage}_response_raw.json')
        choice = responses[stage]['choices'][0]
        assert choice['finish_reason'] == 'stop'
        assert choice['message']['content'] == (generation / f'stage{stage}_output.txt').read_text('utf-8-sig')
    assert requests[1]['model'] == responses[1]['model'] == 'deepseek-v4-pro'
    assert requests[2]['model'] == 'deepseek-v4-flash' and responses[2]['model'] == 'deepseek-flash'
    assert requests[2]['thinking'] == {'type': 'disabled'}
    assert summary['stage2']['accepted'] is False
    assert requests[1]['messages'][0]['content'] == (generation / 'stage1_construction_prompt.txt').read_text('utf-8-sig')
    assert responses[1]['choices'][0]['message']['content'] in requests[2]['messages'][0]['content']
    assert '{{STAGE1_OUTPUT}}' not in requests[2]['messages'][0]['content']
    for name, expected in manifest['input_sha256'].items():
        folder = 'source' if name in ('commit_metadata.txt', 'production_change.patch') else 'generation'
        assert digest(ROOT / folder / name) == expected, name
    blocks = load(generation / 'sql_blocks.json')
    assert blocks['count'] == len(blocks['blocks']) == 5
    output = responses[2]['choices'][0]['message']['content']
    fences = re.findall(r'(?ms)^```sql\s*\n(.*?)^```\s*$', output)
    assert [s.strip() for s in fences] == [s.strip() for s in blocks['blocks']]
    executions = comparisons = 0
    for number, block in enumerate(blocks['blocks'], 1):
        sql = ROOT / f'sql_{number}.sql'
        # The historical driver exported LF model blocks as CRLF SQL files.
        # Compare text here; the execution/provenance SHA256 checks preserve bytes.
        assert sql.read_text('utf-8-sig') == block
        assert digest(sql) == summary['sql_sha256'][f'T{number}']
        directory = ROOT / 'evidence' / f'sql_{number}'
        comparison = load(directory / 'comparison.json')
        assert comparison['sql_sha256'] == digest(sql)
        for side, revision in REVISIONS.items():
            assert comparison[f'{side}_revision'] == revision
        observed = {}
        for side, revision in REVISIONS.items():
            receipt = load(directory / side / 'result.json')
            assert receipt['revision'] == receipt['build_manifest']['sha'] == revision
            assert receipt['startup_error'] is None
            assert receipt['binary_sha256'] in receipt['build_manifest']['binary_hashes']
            assert receipt['server_metadata_tsv']
            assert [t['repeat'] for t in receipt['trials']] == [1, 2, 3]
            observed[side] = []
            for trial in receipt['trials']:
                stem = directory / side / f"trial-{trial['repeat']}"
                stdout, stderr = stem.with_suffix('.stdout.xml'), stem.with_suffix('.stderr.txt')
                assert digest(stdout) == trial['stdout_sha256']
                assert digest(stderr) == trial['stderr_sha256']
                assert not stderr.read_bytes() and trial['sql_errors'] == []
                assert trial['returncode'] == 0 and trial['xml_parse'] == 'ok'
                sets = parse_xml(stdout.read_bytes())
                assert sets == trial['resultsets'] and len(sets) == 2
                observed[side].append(sets)
                executions += 1
            assert all(s == observed[side][0] for s in observed[side])
        assert len(comparison['comparisons']) == 3
        for number, item in enumerate(comparison['comparisons'], 1):
            assert item == {'repeat': number, 'resultsets_equal': True, 'sql_errors_equal': True,
                            'returncode_equal': True, 'status': 'no_observed_difference'}
            assert observed['parent'][number - 1] == observed['target'][number - 1]
            comparisons += 1
    assert summary['execution'] == {
        'scripts': 5, 'trials_per_side': 3, 'full_script_executions': executions,
        'sql_errors': 0, 'xml_parse_failures': 0, 'nonzero_exit_codes': 0,
        'paired_comparisons': comparisons, 'no_observed_difference': comparisons,
        'observed_difference': 0, 'inconclusive': 0,
    }
    assert (executions, comparisons) == (30, 15)
    print('PASS: Item rerun; complete Stage1 handoff; 5 byte-preserved SQL scripts; '
          '30 verified executions, 15 equal pairs; model identity remains unaccepted')


if __name__ == '__main__':
    main()
