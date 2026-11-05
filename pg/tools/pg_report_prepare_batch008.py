"""Freeze additional diagnostic prerequisites before continuation execution."""
import copy
import hashlib
import json
from pg_report_prepare_replay import ROOT, SPECS, add, excerpt


def main():
    add('18801', [excerpt('18801', 'create table test(a float, b float);', '\n```')],
        'output', r'(?m)^BITCODE_FILES=10001$',
        '10000行的自定义聚合产生10001个LLVM bitcode文件',
        '聚合内部SQL函数不应为每行重复JIT编译', mode='jit_bitcode',
        notes='逐字使用报告代码；LLVM10、debug非cassert构建。以报告原文文件数判定，不以共享服务器执行时间判定。')
    SPECS[-1]['build_variant'] = 'jit_nocassert'
    old = next(s for s in json.loads((ROOT/'prepared_specs_batch006.json').read_text(encoding='utf-8')) if s['report_id']=='18810')
    s = copy.deepcopy(old)
    s.pop('spec_sha256')
    s.update(scenario_id='18810_nocassert', build_variant='jit_nocassert',
             notes='保留原参数、SIGHUP步骤及SIGSEGV oracle，在非cassert构建复核；与旧断言构建场景并列，不覆盖原异常。')
    SPECS.append(s)
    add('17462', [excerpt('17462', 'pgbench -i -s 1', '\n\n\nI get:')],
        'log', r'Invalid read of size 2[\s\S]{0,1000}?heapam_tuple_lock',
        'pgbench并发下Valgrind报告heapam_tuple_lock中2字节无效读取',
        '不发生该无效内存读取', mode='valgrind_pgbench',
        notes='源命令pgbench -i -s1及-t1000 -c10 -j10；任务目录Valgrind3.15，专用--with-valgrind构建。完整保留其他Valgrind输出，不将其他内存告警归为本报告。')
    SPECS[-1]['build_variant'] = 'valgrind'
    SPECS[-1]['parts'][0]['material_kind'] = 'pgbench_commands'
    for s in SPECS:
        s['spec_sha256'] = hashlib.sha256(json.dumps(s, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        d = ROOT/'prepared'/s['scenario_id']; d.mkdir(exist_ok=False)
        for n,p in enumerate(s['parts']):
            (d/f'phase_{n}.sql').write_text(p['text']+'\n', encoding='utf-8')
        (d/'spec.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT/'prepared_specs_batch008.json').write_text(json.dumps(SPECS, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Prepared',len(SPECS))


if __name__=='__main__':
    main()
