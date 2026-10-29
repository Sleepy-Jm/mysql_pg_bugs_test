"""Classify bounded, source-backed MySQL replays; never execute SQL or count root causes."""
import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


def rows_of(text):
    """Read mysql --batch --raw with headings; also accept archived --table output."""
    rows = []
    for line in text.splitlines():
        if not line.strip() or re.fullmatch(r'\+[+\-]+', line.strip()):
            continue
        if line.startswith('|') and line.endswith('|'):
            rows.append([v.strip() for v in line[1:-1].split('|')])
        else:
            rows.append(line.rstrip('\r').split('\t'))
    return rows


def split_tables(text, header):
    tables = []
    for row in rows_of(text):
        if header(row):
            tables.append({'columns': row, 'rows': []})
        elif tables:
            if len(row) != len(tables[-1]['columns']):
                raise ValueError('Unexpected column count')
            tables[-1]['rows'].append(row)
        else:
            raise ValueError('Output precedes recognized header')
    return tables


def num(value):
    return None if value == 'NULL' else Decimal(value)


def verdict(outcome, kind, reason, details=None):
    return {'oracle_outcome': outcome, 'oracle_kind': kind, 'reason': reason,
            'details': details, 'root_cause_id': None, 'independent_bug_count': None}


def load_records(path):
    path = Path(path).resolve()
    root = path.parent
    result = []
    for line in path.read_text(encoding='utf8').splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        record['server_crash'] = record.get('server_crash', record.get('server_crash_evidence', False))
        record['timeout'] = record.get('timeout', record.get('timed_out', False))
        for field in ('stdout', 'stderr'):
            source = record.get(field + '_file')
            if source is None:
                record.setdefault(field, '')
                continue
            source_path = (root / source).resolve()
            if not source_path.is_relative_to(root):
                raise ValueError('Output artifact escapes run directory: ' + str(source))
            if not source_path.is_file():
                record['_artifact_load_error'] = 'Missing ' + field + ' artifact: ' + str(source)
                record.setdefault(field, '')
            else:
                record[field] = source_path.read_text(encoding='utf8', errors='replace')
        result.append(record)
    return result


def classify(record):
    bid = str(record.get('report_id', record.get('bug', '')))
    text = record.get('stdout', '')
    if record.get('_artifact_load_error'):
        return verdict('inconclusive', 'missing_artifact', record['_artifact_load_error'])
    actual = record.get('actual_version', record.get('actual'))
    requested = record.get('requested_version', record.get('version'))
    if not actual or not requested or actual != requested:
        return verdict('inconclusive', 'environment', 'Actual version missing or does not match requested version')
    if record.get('oom_killed'):
        return verdict('inconclusive', 'resource_limit', 'Container OOM; not evidence of the intended defect')
    if record.get('timeout'):
        return verdict('inconclusive', 'timeout', 'Execution exceeded its budget')
    if record.get('server_crash') is True:
        return verdict('abnormal', 'crash', 'Runner recorded a server crash signal in this execution; root cause remains unassigned')
    if record.get('returncode') != 0 or re.search(r'(^|\n)ERROR\s+\d+', record.get('stderr', '')):
        return verdict('inconclusive', 'execution_error', 'SQL/client error without independently recorded server crash')
    if record.get('execution_status') not in (None, 'completed', 'executed', 'success'):
        return verdict('inconclusive', 'execution_state', 'Run is not marked completed')
    try:
        if bid == '109699':
            ts = split_tables(text, lambda r: r == ['❤'])
            data = [r for t in ts for r in t['rows']]
            ok = data == [['žlutý_😀']]
            return verdict('normal' if ok else 'abnormal', 'wrong_result', 'Derived constant must survive equality, GROUP BY and HAVING', data)
        if bid == '109725':
            ts = split_tables(text, lambda r: len(r) == 5 and r[0] == 'n' and r[1] == 'sum(n)')
            if len(ts) != 1 or len(ts[0]['rows']) != 4:
                raise ValueError('Expected four window rows')
            got = [[num(v) for v in row] for row in ts[0]['rows']]
            wanted = [[1, 9, 3, Decimal('3'), Decimal('3')], [2, 7, 2, Decimal('3.5'), Decimal('3.5')],
                      [3, 4, 1, Decimal('4'), Decimal('4')], [4, None, 0, None, None]]
            return verdict('normal' if got == wanted else 'abnormal', 'wrong_result', 'Exact four-row arithmetic window oracle', ts[0]['rows'])
        if bid == '110847':
            ts = split_tables(text, lambda r: r in (['result'], ['VERSION()']))
            vals = [t['rows'] for t in ts if t['columns'] == ['result']]
            if len(vals) != 2 or any(len(v) != 2 for v in vals):
                raise ValueError('Expected two executions, each returning two rows')
            return verdict('normal' if vals == [[['1'], ['1']], [['1'], ['1']]] else 'abnormal', 'wrong_result', 'Both prepared executions must compare LAST_VALUE(uid) equal to uid', vals)
        if bid == '110983':
            ts = split_tables(text, lambda r: r == ['A', 'Aplus', 'B', 'Bplus'])
            if len(ts) != 2 or any(len(t['rows']) != 12 for t in ts):
                raise ValueError('Expected two calls with twelve rows each')
            good = all(num(r[1]) == num(r[0]) + 1 and num(r[2]) == 12 and num(r[3]) == 13 for t in ts for r in t['rows'])
            return verdict('normal' if good else 'abnormal', 'wrong_result', 'Each window expression plus one must equal its same-row source plus one', [t['rows'] for t in ts])
        if bid == '112231':
            ts = split_tables(text, lambda r: r == ['id'] or (len(r) == 2 and r[0] == '1' and 'SUM' in r[1]))
            sums = [t['rows'] for t in ts if len(t['columns']) == 2]
            ids = [t['rows'] for t in ts if t['columns'] == ['id']]
            if len(sums) != 2 or len(ids) != 2 or any(x != [['1']] for x in ids):
                raise ValueError('Unexpected procedure output shape')
            return verdict('normal' if sums == [[['1', '1']], [['1', '1']]] else 'abnormal', 'wrong_result', 'SUM(1) over one row must remain one across procedure calls', sums)
        if bid == '112460':
            ts = split_tables(text, lambda r: r == ['c_0', 'c_1'])
            if len(ts) != 2 or any(len(t['rows']) != 1 for t in ts):
                raise ValueError('Expected two one-row queries')
            good = all(t['rows'][0][0] == 'NULL' and num(t['rows'][0][1]) == Decimal('17.61') for t in ts)
            return verdict('normal' if good else 'abnormal', 'wrong_result', 'CASE with identical c20 branches must equal direct c20', [t['rows'] for t in ts])
        if bid == '112524':
            ts = split_tables(text, lambda r: r == ['c_6'])
            if len(ts) != 2 or any(len(t['rows']) != 1 for t in ts):
                raise ValueError('Expected two one-row timestamp queries')
            good = ts[0]['rows'] == ts[1]['rows']
            return verdict('normal' if good else 'abnormal', 'wrong_result', 'CASE TRUE with identical branches must preserve UNIX_TIMESTAMP result; no fixed timestamp expected', [t['rows'] for t in ts])
        if bid == '113892':
            ts = split_tables(text, lambda r: r == ['a'] or (r and r[0] in ('Table', 'id')))
            data = [t for t in ts if t['columns'] == ['a']]
            plans = [t for t in ts if t['columns'][0] == 'id']
            if len(data) != 1 or len(plans) != 2 or sorted(r[0] for r in data[0]['rows']) != ['0', '1', '4', '7']:
                raise ValueError('Expected four actual rows and two EXPLAIN outputs')
            estimates = [t['rows'][0][t['columns'].index('rows')] for t in plans]
            # Estimates are not an exact-result contract; preserve this diagnostic separately.
            return verdict('inconclusive' if estimates != ['4', '4'] else 'normal', 'plan_diff',
                           'Estimate/plan difference needs review; never classified as wrong_result', {'actual_rows': 4, 'estimates': estimates})
        if bid == '121514':
            ts = split_tables(text, lambda r: r == ['c2'])
            if any(t['rows'] for t in ts):
                return verdict('abnormal', 'wrong_result', 'Empty table query unexpectedly produced rows')
            return verdict('normal', 'crash', 'Empty-table query completed without recorded server crash')
        if bid == '118625':
            ts = split_tables(text, lambda r: r == ['ref0'])
            data = [r for t in ts for r in t['rows']]
            return verdict('normal' if not data else 'abnormal', 'wrong_result', 'Integer zero is not equal to DOUBLE 0.4; result must be empty', data)
        if bid == '119670':
            mode = record.get('sql_mode', record.get('environment', {}).get('sql_mode'))
            if mode is None or 'PIPES_AS_CONCAT' in mode.split(','):
                return verdict('inconclusive', 'configuration', 'Oracle requires known SQL mode with || interpreted as OR')
            ts = split_tables(text, lambda r: r == ['c0'])
            if len(ts) > 2:
                raise ValueError('Unexpected number of result sets')
            data = [r for t in ts for r in t['rows']]
            return verdict('normal' if not data else 'abnormal', 'wrong_result', 'Both direct and prepared predicates should reject integer zero', data)
        if bid == '120849':
            ts = split_tables(text, lambda r: r == ['vc'])
            if len(ts) > 3:
                raise ValueError('Unexpected number of TIME result sets')
            values = [t['rows'] for t in ts]
            if any(values):
                return verdict('inconclusive', 'semantic_difference_needs_review', 'Returned TIME values require VIEW/CTE/materialization type-semantics review; raw output retained', values)
            return verdict('normal', 'semantic_comparison', 'All three predicates returned no rows in the recorded configuration')
        if bid == '121512':
            ts = split_tables(text, lambda r: bool(r) and (r[0].startswith('ELT(') or r[0].startswith('SUM(ELT(')))
            if len(ts) != 3 or any(len(t['rows']) != 1 for t in ts):
                raise ValueError('Expected scalar, table expression and aggregate outputs')
            vals = [t['rows'][0] for t in ts]
            good = vals == [['1', 'NULL', 'NULL', 'NULL', 'NULL'], ['1', 'NULL'], ['NULL']]
            return verdict('normal' if good else 'abnormal', 'wrong_result', 'ELT out-of-range NULL must propagate through numeric and aggregate evaluation', vals)
        if bid == '121523':
            ts = split_tables(text, lambda r: bool(r) and r[0].startswith('ST_AsText('))
            if len(ts) != 2 or any(len(t['rows']) != 1 for t in ts):
                raise ValueError('Expected two GIS result sets')
            vals = [t['rows'][0] for t in ts]
            return verdict('normal' if vals == [['NULL', 'NULL'], ['NULL']] else 'abnormal', 'wrong_result', 'Out-of-range GIS element indexes must return NULL', vals)
    except (ValueError, IndexError, InvalidOperation, TypeError) as error:
        return verdict('inconclusive', 'unparsed_output', str(error))
    return verdict('inconclusive', 'missing_oracle', 'No reviewed classifier for this report')


def classify_all(records):
    classified = [dict(r, oracle=classify(r)) for r in records]
    grouped = defaultdict(list)
    for r in classified:
        key = tuple(str(r.get(k, '')) for k in ('cohort', 'report_id', 'target_version', 'requested_version', 'role'))
        grouped[key].append(r)
    stability = []
    for key, values in sorted(grouped.items()):
        labels = Counter(r['oracle']['oracle_outcome'] for r in values)
        repeats = {r.get('repeat') for r in values}
        complete = len(values) == 3 and repeats == {1, 2, 3}
        stability.append(dict(zip(('cohort', 'report_id', 'target_version', 'requested_version', 'role'), key),
                              records=len(values), outcome_counts=dict(labels), three_repeats_complete=complete,
                              stable_outcome=next(iter(labels)) if complete and len(labels) == 1 else None))
    pairs = defaultdict(list)
    for r in classified:
        if r.get('cohort') in ('candidate_replay', 'candidate') and r.get('role') in ('target', 'adjacent_comparison'):
            pairs[(str(r['report_id']), r['target_version'])].append(r)
    boundaries = []
    for (bid, target), values in sorted(pairs.items()):
        roles = {role: [r for r in values if r['role'] == role] for role in ('target', 'adjacent_comparison')}
        complete = all(len(v) == 3 and {r.get('repeat') for r in v} == {1, 2, 3} for v in roles.values())
        labels = {role: {r['oracle']['oracle_outcome'] for r in v} for role, v in roles.items()}
        scripts = {r.get('script_sha256') for r in values}
        adjacent = '8.0.' + str(int(target.split('.')[-1]) - 1)
        versions_match = all(r.get('requested_version') == (target if r['role'] == 'target' else adjacent) for r in values)
        usable = complete and versions_match and len(scripts) == 1 and None not in scripts and all(len(x) == 1 and 'inconclusive' not in x for x in labels.values())
        outcome = 'inconclusive'
        if usable:
            target_outcome = next(iter(labels['target']))
            adjacent_outcome = next(iter(labels['adjacent_comparison']))
            outcome = {('abnormal', 'normal'): 'release_behavior_difference',
                       ('abnormal', 'abnormal'): 'pre_existing_observation',
                       ('normal', 'abnormal'): 'recovery_observed',
                       ('normal', 'normal'): 'not_reproduced_in_recorded_conditions'}[(target_outcome, adjacent_outcome)]
        contracts = {r.get('comparison_contract_sha256') for r in values}
        comparable = bool(usable and len(contracts) == 1 and None not in contracts and all(r.get('comparable_protocol_validated') is True for r in values))
        boundaries.append({'report_id': bid, 'target_version': target, 'adjacent_comparison_version': adjacent,
                           'three_repeats_per_role': complete, 'same_script_sha256': len(scripts) == 1 and None not in scripts,
                           'target_outcomes': sorted(labels['target']), 'adjacent_outcomes': sorted(labels['adjacent_comparison']),
                           'observation': outcome, 'comparison_contract_validated': comparable,
                           'needs_environment_comparability_review': not comparable,
                           'introducing_commit': None, 'root_cause_id': None,
                           'boundary_scope': 'Observed release behavior only; commit introduction and independent root cause remain unproven.'})
    return {'records': classified, 'stability': stability, 'candidate_version_pairs': boundaries,
            'summary': {'executions_recorded': len(records), 'oracle_outcomes': dict(Counter(r['oracle']['oracle_outcome'] for r in classified)),
                        'oracle_kinds': dict(Counter(r['oracle']['oracle_kind'] for r in classified)),
                        'candidate_pair_observations': dict(Counter(r['observation'] for r in boundaries)),
                        'independent_root_causes': None,
                        'policy': 'Outcome counts are execution counts. No automatic bug/root-cause deduplication or introducing-commit claim.'}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--records', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    records = load_records(args.records)
    result = classify_all(records)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps(result['summary'], ensure_ascii=False))
