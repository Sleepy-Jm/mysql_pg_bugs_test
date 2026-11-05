import hashlib
import json
import re
from pg_report_prepare_replay import ROOT,SPECS,add,exact,excerpt


def main():
    add('17368',[excerpt('17368','setup\n{','causes an assertion failure')],'crash',r'terminated by signal 6','隔离测试 read-only-anomaly-3 触发 GetSafeSnapshot 断言','可正常完成或报告序列化冲突，不应断言崩溃',mode='isolation')
    p=excerpt('18882','conn1 = psycopg2.connect','--- I see')
    p['text']=re.sub(r'cur[12]\.execute\(".*?"\)',lambda m:m[0].replace('\n',' '),p['text'],flags=re.S)
    p['transformations'].append('join display-wrapped Python string literal lines only')
    add('18882',[excerpt('18882','CREATE TABLE tJ6mtoSl','---case'),p], 'output',r'(?s)14691, 16705.*14714, 16730.*14715, 16731','原文 psycopg2 代码没有序列化失败','作者期望出现序列化失败',mode='python_source',notes='仅用私有集群连接参数替换 dbconfig；保留原文隐式事务行为，不调用 set_isolation_level。')
    SPECS[-1]['additional_oracle_checks']=[dict(stream='stdout',pattern='could not serialize|ERROR|Traceback',count=0)]
    add('18750',[exact('18750','CREATE TABLE t(a INT, b INT);',True),exact('18750','BEGIN;'),exact('18750','SET TRANSACTION ISOLATION LEVEL READ COMMITTED;'),exact('18750','UPDATE t SET b=3;'),exact('18750','UPDATE t SET b=2 WHERE a IS NOT NULL;'),exact('18750','UPDATE t SET a=1;'),exact('18750','COMMIT;'),exact('18750','SELECT * FROM t;')],
        'output',r'(?m)^1\|2\n1\|3$','被阻塞的 READ COMMITTED UPDATE 只更新最初命中的行，得到 (1,3)/(1,2)','作者最初期望两行均 (1,2)，讨论后接受官方解释',mode='ordered_sessions')
    s=SPECS[-1];initial=exact('18750','INSERT INTO t VALUES (null, 1), (1, 1);',True)
    s['parts'][0]['text']+='\n'+initial['text'];s['parts'][0]['additional_sources']=[initial];s['parts'][0]['transformations'].append('append author-provided initial rows from official reply')
    s['schedule']=[dict(session=0,part=1),dict(session=0,part=2),dict(session=1,part=1),dict(session=1,part=2),dict(session=0,part=3),dict(session=1,part=4,**{'async':True}),dict(session=0,part=5),dict(session=0,part=6,await_pending=True),dict(session=1,part=6),dict(session=0,part=7)]
    p=excerpt('18782','CREATE USER app_user;','-- Cleanup Phase')
    # Remove only explicitly identified comments and their display-wrapped continuation.
    p['text']=re.sub(r'(?m)^\s*--[^\n]*\n(?:permissions to app user|\(team.team_id\)|particular value|team.team_id|syntax for type uuid: ""`|work correctly|time no exception is thrown\. THIS IS THE UNEXPECTED BEHAVIOUR)?\n?', '', p['text'])
    p['transformations'].append('remove display-wrapped narrative comments and enumerated continuation lines; preserve SQL strings including exception text')
    add('18782',[p],'output',r'(?s)ROLLBACK.*INSERT 0 1.*INSERT 0 1\nCOMMIT\s*$', '第2步 UUID 转换报错，但6次成功 INSERT 后第4步无异常','作者期望第4步仍然抛 UUID 转换异常',notes='同一 psql 会话完成4个阶段；判据同时要求恰好一次来源预期的 UUID 错误。')
    SPECS[-1]['additional_oracle_checks']=[dict(stream='stderr',pattern='ERROR:.*invalid input syntax for type uuid',count=1),dict(stream='stderr',pattern='ERROR:',count=1)]
    add('17434',[exact('17434','\\startpipeline\ncreate database test;\nselect 1/0;\n\\endpipeline')],'output',r'^ORPHAN$','pipeline CREATE DATABASE 事务回滚后遗留没有 catalog 项的数据目录','回滚后 catalog 与 base 目录一致',mode='pipeline_create',notes='只执行报告 CREATE 分支；原文额外 test0 与该分支无关，不补造其 CREATE。')
    q=excerpt('17335','    SELECT count(1)','When `set max_parallel')
    serial=exact('17335','set max_parallel_workers_per_gather = 0;');parallel=exact('17335','set max_parallel_workers_per_gather = 2;')
    serial['text']+='\n'+q['text'];serial['additional_sources']=[q];serial['transformations'].append('execute reported query after the reported serial setting')
    parallel['text']+='\n'+('\n'.join([q['text']]*10));parallel['additional_sources']=[q];parallel['transformations'].append('repeat exact source query 10 times because report explicitly says timing-dependent')
    add('17335',[serial,parallel],'output',r'(?m)^88$','并行查询将正确44行计成88行','串行和并行均应44',timeout=120,notes='固定10次并行尝试；阴性只表示该有界回放未命中。')
    SPECS[-1]['setup_dump']='17335_repro_dump.sql.zst'
    SPECS[-1]['additional_oracle_checks']=[dict(stream='stdout',pattern='^44$',count=1)] # serial baseline only if all parallel trials reproduce
    # Baseline must be 44; count across the complete output is not constrained because parallel may also return 44.
    SPECS[-1]['additional_oracle_checks']=[dict(stream='stdout',pattern=r'__PG_PHASE_0__[\s\S]*?\n44\n[\s\S]*?__PG_PHASE_DONE_0__',count=1)]
    for s in SPECS:
        s['spec_sha256']=hashlib.sha256(json.dumps(s,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        d=ROOT/'prepared'/s['scenario_id'];d.mkdir(exist_ok=False)
        for n,p in enumerate(s['parts']):(d/f'phase_{n}.sql').write_text(p['text']+'\n',encoding='utf-8')
        (d/'spec.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'prepared_specs_batch004.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2),encoding='utf-8');print('Prepared',len(SPECS))


if __name__=='__main__':main()
