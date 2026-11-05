"""Source-grounded correction and additional executable scenarios."""
import copy
import hashlib
import json
import re
from pg_report_prepare_replay import ROOT, SPECS, add, exact, excerpt


def main():
    old=next(s for s in json.loads((ROOT/'prepared_specs_batch002.json').read_text(encoding='utf-8')) if s['report_id']=='17428')
    fixed=copy.deepcopy(old);fixed.pop('spec_sha256');fixed['scenario_id']='17428_revision1'
    p=excerpt('17428','create table mytable (','-- etc')
    p['text']=re.sub(r'-- ([0-3]),\s*\n[0-3]',r'-- \1 (displayed expected output removed)',p['text'])
    p['transformations'].append('remove wrapped demonstration-output comment continuation; do not change executable SQL or frozen oracle')
    fixed['parts']=[p];fixed['supersedes_spec_sha256']=old['spec_sha256'];fixed['revision_reason']='presentation line wrap left bare numeric expected-output fragments before INSERT; source correction only'
    SPECS.append(fixed)
    add('17443',[excerpt('17443','create temp table teste as','EXPLAIN (analyze'),exact('17443','EXPLAIN (analyze on, wal on, verbose on, format text)\n  select id2 from teste where id2 = 1000000;')],
        'output',r'Seq Scan on pg_temp\.teste','默认 enable_seqscan=on 时 id2 查询使用顺序扫描','作者希望使用 BRIN 索引',timeout=180)
    add('18802',[exact('18802','set log_statement to "all";'),exact('18802',"create user some_user password '123456';")],
        'log',r"statement: create user some_user password '123456';",'log_statement=all 将报告示例口令写入日志','作者询问是否预期行为；未给出应有行为断言',notes='123456 是报告公开测试字面量，不是服务器凭据。')
    add('18792',[exact('18792',"alter system set synchronized_standby_slots='standby_slot';"),exact('18792','select pg_reload_conf();')],
        'crash',r'system logger process .*terminated by signal 11','修改 synchronized_standby_slots 并 reload 导致 logger SIGSEGV','logger 不崩溃',config={'logging_collector':'on','log_directory':"'log'",'log_filename':"'replay.log'"})
    SPECS[-1]['observation_delay']=3
    add('17355',[excerpt('17355','CREATE EXTENSION postgres_fdw;','\nEOF'),excerpt('17355','INSERT INTO async_pt SELECT i','\nEOF')],
        'crash',r'terminated by signal 11','20 并发会话 INSERT/DELETE/UPDATE 外部分区导致 SIGSEGV','不发生服务进程崩溃',mode='concurrent',config={'max_connections':'100'})
    SPECS[-1]['workers']=[1]*20
    add('17372',[exact('17372','CREATE TABLE ab1 (a INTEGER, b INTEGER, c INTEGER);'),exact('17372','CREATE STATISTICS ab1_a_b_stats ON a, b FROM\nab1; DROP STATISTICS ab1_a_b_stats;'),exact('17372','ALTER STATISTICS ab1_a_b_stats SET\nSTATISTICS -1;')],
        'crash',r'terminated by signal 11','并发删除和修改扩展统计导致 SIGSEGV','不崩溃',mode='concurrent')
    for part in SPECS[-1]['parts'][1:]:
        part['text']='\n'.join([part['text']]*20);part['transformations'].append('expand source seq 20 loop')
    SPECS[-1].update(workers=[1,2],iterations=100,iteration_delay=2)
    add('17698',[exact('17698','select pg_sleep(1234)')],'output',r'^1$','SIGTERM 终止 psql 后查询仍活动','psql 退出前应取消正在执行的查询',mode='signal_client',config={'listen_addresses':"'127.0.0.1'"},notes='诊断查询 pg_stat_activity 只观测本任务 PGAPPNAME；退出后停止隔离集群。')
    for spec in SPECS:
        spec['spec_sha256']=hashlib.sha256(json.dumps(spec,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        dest=ROOT/'prepared'/spec['scenario_id'];dest.mkdir(exist_ok=False)
        for n,p in enumerate(spec['parts']):(dest/f'phase_{n}.sql').write_text(p['text']+'\n',encoding='utf-8')
        (dest/'spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'prepared_specs_batch003.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Prepared',len(SPECS))


if __name__=='__main__':main()
