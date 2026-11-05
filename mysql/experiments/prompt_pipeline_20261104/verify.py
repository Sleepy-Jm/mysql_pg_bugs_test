"""Offline verification of prompt lineage and the archived exact-revision replay."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def read_json(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def main():
    export = read_json('export_manifest.json')
    exported = {f['destination']:f for f in export['files']}
    assert len(exported)==len(export['files'])
    for path, record in exported.items():
        assert digest(path)==record['exported_sha256'], path
        if not record['transformations']:
            assert record['original_sha256']==record['exported_sha256'], path
    generated = read_json('generation/generation_manifest.json')
    lineage = read_json('lineage.json')
    provenance = read_json('generation/input_bundle/provenance.json')
    sources = {t['name']:t for t in provenance['targets']}
    expected_targets = {t['target']:t for t in generated['targets']}
    pairs = {t['name']:t for t in read_json('runtime/comparison.json')['pairs']}
    assert {t['name'] for t in lineage['targets']}==set(expected_targets)==set(pairs)==set(sources)
    assert lineage['runner_original_sha256']==exported['runtime/runner.py']['original_sha256']
    assert lineage['runner_exported_sha256']==digest('runtime/runner.py')
    # The archived module does not start the workflow when imported.
    spec = importlib.util.spec_from_file_location('archived_runner',ROOT/'runtime/runner.py')
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    counts = {'pass':0,'mismatch':0}
    runs = 0
    for target in lineage['targets']:
        name = target['name']
        original = expected_targets[name]
        assert target['mysql_revision']==sources[name]['revision']
        assert target['parent_revision']==sources[name]['parent']
        for key, artifact in target['artifacts'].items():
            assert artifact['path']=='generation/'+original[key]
            assert digest(artifact['path'])==artifact['sha256']==original[key+'_sha256']
        stage1 = (ROOT/target['artifacts']['src2req_output']['path']).read_text(encoding='utf-8')
        stage2 = (ROOT/target['artifacts']['req2test_input']['path']).read_text(encoding='utf-8')
        assert stage2.count('### Current task')==1
        assert stage1.strip() in stage2.split('### Current task')[1]
        response = (ROOT/target['artifacts']['req2test_output']['path']).read_text(encoding='utf-8')
        sql = (ROOT/target['artifacts']['sql']['path']).read_text(encoding='utf-8')
        assert re.findall(r'```sql\n(.*?)\n```',response,re.S)==[sql.strip()]
        expected = read_json(target['artifacts']['expected']['path'])['cases']
        assert len(expected)==target['case_count']
        for role, execution in target['execution'].items():
            result = read_json(execution['result'])
            assert digest(execution['result'])==execution['result_sha256']
            assert result['revision']==execution['revision']==target['parent_revision' if role=='parent' else 'mysql_revision']
            assert result['run_id']==execution['run_id']
            assert result['sql_sha256']==execution['sql_sha256']==original['sql_sha256']
            assert result['expected_sha256']==execution['expected_sha256']==original['expected_sha256']
            assert result['runner_sha256']==lineage['runner_original_sha256']
            assert result['runtime_error'] is None and result['container_removed']
            build = read_json(execution['build_manifest'])
            manifest = build.get('original_manifest',build)
            assert manifest['sha']==result['revision'] and manifest['patch_mode'] is None and manifest['diff']==''
            assert manifest['builder_image']==result['builder_image']
            hashes = {Path(line.split(None,1)[1]).name:line.split()[0] for line in manifest['binary_hashes'].splitlines()}
            assert hashes['mysqld']==result['mysqld_sha256']
            if 'verified_binary_sha256' in build:
                assert hashes==build['verified_binary_sha256']
            else:
                assert manifest['returncode']==0
                assert manifest['build_script_sha256']==exported['runtime/build.sh']['original_sha256']
            assert [t['repeat'] for t in result['trials']]==[1,2,3]
            assert [t['repeat'] for t in execution['trials']]==[1,2,3]
            evaluations = []
            for trial, pointers in zip(result['trials'],execution['trials']):
                assert trial['returncode']==0 and not trial['timeout']
                assert trial['server_state']['Running'] and not trial['server_state']['OOMKilled']
                for stream in ('stdout','stderr'):
                    assert digest(pointers[stream])==pointers[stream+'_sha256']==trial[stream+'_sha256']
                    assert not exported[pointers[stream]]['transformations']
                evaluated = runner.evaluate((ROOT/pointers['stdout']).read_text(encoding='utf-8'),
                                            (ROOT/pointers['stderr']).read_text(encoding='utf-8'),expected)
                assert evaluated==trial['evaluation']
                assert not evaluated['sql_errors'] and not evaluated['parse_error'] and evaluated['labels_complete_and_ordered']
                for case in evaluated['cases']:
                    counts[case['status']] += 1
                    if role=='parent':
                        assert case['status']=='pass'
                evaluations.append(evaluated)
                runs += 1
            assert evaluations[0]['cases']==evaluations[1]['cases']==evaluations[2]['cases']
            passing = [sum(c['status']=='pass' for c in e['cases']) for e in evaluations]
            assert passing==execution['passing_cases_per_trial']==pairs[name]['sides'][role]['passing_cases_per_trial']
            for i, case in enumerate(expected):
                statuses = [e['cases'][i]['status'] for e in evaluations]
                assert statuses==execution['case_statuses'][case['case_id']]
                saved = pairs[name]['sides'][role]['cases'][case['case_id']]
                assert statuses==saved['statuses'] and saved['stable_across_repeats']
    audit = read_json('runtime/audit.json')
    assert runs==audit['script_runs']==18
    assert sum(counts.values())==audit['case_observations']==150
    assert counts==audit['case_observation_statuses']=={'pass':126,'mismatch':24}
    print(f'PASS: {len(exported)} export hashes; 3 prompt-to-SQL chains; 6 revisions; {runs} script runs; 150 observations ({counts})')


if __name__=='__main__':
    main()
