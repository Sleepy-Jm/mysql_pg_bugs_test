"""Freeze reviewed source excerpts and pre-execution phenomenon oracles."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path('experiments/pg_report_replay_20261104/run_001')
REPORTS = {r['report_id']:r for r in json.loads((ROOT/'frozen_reports.json').read_text(encoding='utf-8'))}
SPECS = []

def excerpt(rid, start, end=None, thread=False, include_end=False):
    path = ROOT/('thread_text' if thread else 'source_text')/f'{rid}.txt'
    text = path.read_text(encoding='utf-8')
    a = text.index(start)
    b = text.index(end, a+len(start)) if end else len(text)
    if end and include_end: b += len(end)
    raw = text[a:b]
    return {'text':raw.strip(), 'source':str(path), 'start_offset':a, 'end_offset':b,
            'start_line':text[:a].count('\n')+1, 'end_line':text[:b].count('\n')+1,
            'excerpt_sha256':hashlib.sha256(raw.encode()).hexdigest(), 'transformations':['trim outer whitespace']}

def exact(rid, text, thread=False):
    return excerpt(rid,text,text,thread) if False else exact_impl(rid,text,thread)

def exact_impl(rid, text, thread):
    p = ROOT/('thread_text' if thread else 'source_text')/f'{rid}.txt'
    raw=p.read_text(encoding='utf-8'); a=raw.index(text)
    return {'text':text,'source':str(p),'start_offset':a,'end_offset':a+len(text),
            'start_line':raw[:a].count('\n')+1,'end_line':raw[:a+len(text)].count('\n')+1,
            'excerpt_sha256':hashlib.sha256(text.encode()).hexdigest(),'transformations':[]}

def add(rid, parts, kind, pattern, claim, expected, *, name='main', config=None, mode='psql', notes='', timeout=45):
    for p in parts:
        if p['text'] and not p['text'].rstrip().endswith(';') and not p['text'].lstrip().startswith('\\'):
            p['text'] += ';'; p['transformations'].append('append SQL terminator at excerpt boundary')
    SPECS.append({'report_id':rid,'scenario_id':rid+'_'+name,'target_version':REPORTS[rid]['version_field'],
                  'source_url':REPORTS[rid]['source_url'],'parts':parts,'mode':mode,
                  'oracle':{'kind':kind,'pattern':pattern,'reported_phenomenon':claim,'author_expected_behavior':expected},
                  'config':config or {},'notes':notes,'timeout':timeout,'preparation_status':'ready'})

def prepare():
    add('17294',[exact('17294','create table test (a text, b varchar);'),exact('17294','create index on test using spgist (a);'),exact('17294','create index on test using spgist (b);')],
        'error',r'compress method must be defined','varchar SP-GiST 索引报 compress method 错误','应与旧版本一样允许创建索引')
    add('17302',[excerpt('17302','CREATE TABLE point_tbl','INSERT INTO point_tbl VALUES'),exact('17302',"INSERT INTO point_tbl VALUES ('(1e-300,-1e-300)'::point);")],
        'error','value out of range: underflow','GiST 索引存在时插入极小坐标报 underflow','插入成功')
    add('17318',[excerpt('17318','WITH RECURSIVE x ( x ) AS\n  ( SELECT 1','and now',thread=True)],'crash',r'terminated by signal (?:6|11)',
        '递归 CTE/CYCLE 嵌套 UNION 导致崩溃','不崩溃，可正常拒绝不支持的语法',notes='使用官方讨论中 Tom Lane 给出的简化 SQL，保留来源，不使用无关后续 INSERT。')
    add('17320',[excerpt('17320','WITH RECURSIVE x ( x ) AS\n (SELECT 1','If I tried',thread=True)],'crash',r'terminated by signal (?:6|11)',
        'SEARCH 子句递归引用导致崩溃/断言','不崩溃，可正常拒绝语法',notes='使用官方回复中第一个完整简化 SQL。')
    add('17334',[excerpt('17334','CREATE TABLE point_tbl','SET enable_seqscan'),excerpt('17334','SET enable_seqscan','I get a failed')],
        'crash',r'terminated by signal 6','GiST NaN 距离扫描断言失败','不发生断言崩溃')
    add('17339',[excerpt('17339','CREATE SEQUENCE seq;','ALTER TABLE range_parted'),exact('17339','ALTER TABLE range_parted DETACH PARTITION seq CONCURRENTLY;')],
        'crash',r'terminated by signal 6','对序列 DETACH PARTITION CONCURRENTLY 导致断言','正常拒绝无效分区对象')
    add('17340',[excerpt('17340','select name,unnest','Actual result set:')],'output',r'(?m)^test_b\|1\ntest_b\|2\ntest_b\|3$',
        'NULL 数组对应 test_a 行被 unnest 删除','作者期望额外的 test_a NULL 行',notes='报告现象不自动等于缺陷；保留官方讨论解释。')
    add('17344',[excerpt('17344','create extension postgres_fdw;','select a from tab1'),exact('17344','select a from tab1 where a in (select a from ftab1);')],
        'crash',r'terminated by signal 6','async foreign table inheritance 查询断言','不崩溃',notes='loopback libpq 通过服务器进程 PGHOST 指向本任务私有 socket。')
    add('17349',[exact('17349','create extension pgcrypto schema pg_catalog;')],'error',r'function "gen_random_uuid" already exists',
        '在 pg_catalog 安装 pgcrypto 因同名函数失败','作者希望消除重复函数')
    add('17351',[excerpt('17351','create table pt (a int','\\d+ t'),exact('17351','\\d+ t')],'crash',r'terminated by signal (?:6|11)',
        '修改分区表行类型后显示约束导致崩溃','不崩溃并正确处理行类型依赖')
    add('17366',[exact('17366','set timezone to "PST8PDT";'),exact('17366',"select (timestamp '2021-03-14 02:00:00')::timestamptz;")],
        'output',r'2021-03-14 03:00:00-07','不存在的 DST 本地时间被转换为 03:00','作者期望 02:00-07')
    add('17385',[excerpt('17385','CREATE TABLE abc (a int);','causes an assertion failure')],'crash',r'terminated by signal 6',
        'serializable 事务内 RESET transaction_isolation 导致提交断言','不发生断言崩溃')
    add('17387',[excerpt('17387','with q_data as (','and results in:')],'error',r'operator is not unique: record\[\] \|\| record\[\]',
        'record[] 拼接运算符歧义报错','与 PG13 一样返回拼接后的数组')
    add('17395',[excerpt('17395','CREATE EXTENSION postgres_fdw;','SELECT t1.a FROM'),exact('17395','SELECT t1.a FROM fprt2 t1 JOIN fprt2 t2 ON (t1.a = t2.a);')],
        'crash',r'terminated by signal 6','外部分区越界数据触发 merge join 断言','不得因越界数据导致服务崩溃',notes='按报告保留越界数据，不修正分区内容。')
    add('17409',[excerpt('17409','CREATE TABLE parent (','ALTER TABLE parent ALTER'),exact('17409','ALTER TABLE parent ALTER COLUMN parent_field SET DATA TYPE BIGINT;')],
        'error',r'has multiple clustered indexes','CLUSTER 后修改被外键引用列的类型失败','允许类型修改')
    add('17415',[exact('17415',"SELECT set_config('_foo.bar', 'foo', FALSE);")],'error',r'invalid configuration parameter name "_foo.bar"',
        '自定义参数首字符下划线被拒绝','允许下划线开头')
    add('17452',[exact('17452',"SELECT 'version'::regproc IN ('version');")],'error',r'invalid input syntax for type oid: "version"',
        '单项 IN 报 oid 转换错误','作者期望单项与多项 IN 一致')
    add('17454',[exact('17454','select inet_server_port();')],'output',r'(?m)^<NULL>$',
        'Unix socket 连接 inet_server_port 返回 NULL','作者期望返回服务器端口',notes='psql 使用私有 Unix socket，保持报告未指定 IPv4 的连接类别。')
    add('17473',[excerpt('17473','CREATE TYPE tstzrange3 AS RANGE','CREATE TYPE\n'),exact('17473','select tstzrange3(NOW(), NULL);')],'output',r'\.\d{4,6}[+-]',
        'range subtype timestamp(3) 未限制时间戳为三位小数','作者期望保留 timestamp(3) 精度')
    add('17477',[exact('17477','create table v0();',True),exact('17477','select * from v0 group by ((values (v0.*)));',True)],'crash',r'terminated by signal (?:6|11)',
        '零列关系 VALUES 触发 transformValuesClause 崩溃','允许或正常拒绝查询，不崩溃',notes='采用官方评论的完整简化复现，未补造原 PoC 缺失角色。')
    add('17479',[exact('17479','create table Card (id uuid);'),excerpt('17479','SELECT\n    -- This line','As the comment says')],
        'error',r"plan should not reference subplan.s variable",'grouping 子查询报内部计划错误','正常处理查询')
    add('17480',[exact('17480','SELECT * FROM XMLTABLE (ROW () passing null COLUMNS v1 TIMESTAMP, v2 int) AS f (v1, v2, v3);',True)],
        'crash',r'terminated by signal 6','过长 XMLTABLE 别名列表触发断言','正常报告别名数量错误',notes='官方回复的单语句最小复现。')
    add('17546',[excerpt('17546','with w_degree as (','Result:')],'output',r'11\.100000000000001',
        'power 隐式浮点计算产生可见舍入差异','作者期望等于显式整数转换结果')
    add('18265',[excerpt('18265',"select * from\n(values('null'::jsonb)",'   j    ')],'output',r'(?m)^\[\]\nnull\n\[null\]\n\[\[\]\]$',
        '空 jsonb 数组排序早于 null，嵌套时顺序不同','作者期望类型排序一致')
    add('18712',[exact('18712',"select '::0.0.0.2'::inet;")],'output',r'(?m)^::2$',
        'IPv6 输出为 ::2','作者期望 ::0.0.0.2')
    add('18722',[excerpt('18722','CREATE FUNCTION make_ia()','SELECT NULLIF(make_ia(), array[1]::int[]);'),exact('18722','SELECT NULLIF(make_ia(), array[1]::int[]);')],
        'error',r'cache lookup failed for type','PLpgSQL 数组 NULLIF 访问损坏类型','不发生内部类型查找错误')
    add('18730',[exact('18730','create table test_smallint(smint smallint);'),exact('18730','insert into test_smallint values (-1);'),exact('18730','select * from test_smallint where smint!=-2;')],
        'error',r'operator does not exist: smallint !=- integer','无空格的 !=-2 被识别为不存在的运算符','作者希望与有空格形式一致')
    add('18741',[excerpt('18741','CREATE TABLE pt1','ALTER TABLE pt2 DETACH'),exact('18741','ALTER TABLE pt2 DETACH PARTITION p2;')],
        'error',r'could not find ON INSERT check triggers of foreign key','分离带外键分区失败','应正常分离')
    add('18758',[excerpt('18758','create table t1','select  t1.c1'),excerpt('18758','select  t1.c1','-- actual:')],
        'output',r'(?m)^<NULL>$','空表 ROLLUP 返回 NULL 行','作者期望空结果')
    add('18764',[excerpt('18764','CREATE TABLE t0','SELECT c2 AS'),excerpt('18764','SELECT c2 AS','-- server closed')],
        'crash',r'terminated by signal (?:6|11)','UNION DISTINCT 查询导致服务端连接意外关闭','返回正确结果不崩溃')
    add('18778',[excerpt('18778','CREATE TABLE t (id int','SELECT 1 FROM'),excerpt('18778','SELECT 1 FROM','fails with:')],
        'error',r'unrecognized node type:','分区查询计划执行报 unrecognized node type','正常处理查询')
    add('18812',[excerpt('18812','CREATE TABLE t\n','-----\n\n\nI\'ve'),exact('18812',"INSERT INTO v (c) VALUES ('testtesttest');")],
        'error',r'value too long for type character varying\(10\)','WHERE FALSE 规则仍报长度约束错误','作者期望跳过规则不检查长度')
    add('18829',[excerpt('18829','DO $$','Expected Result:')],'stderr',r'NOTICE:\s+garths is slim',
        'RAISE NOTICE %s 留下额外 s','作者期望 garth is slim')

    out=ROOT/'prepared'; out.mkdir(exist_ok=True)
    for spec in SPECS:
        spec['spec_sha256']=hashlib.sha256(json.dumps(spec,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        dest=out/spec['scenario_id']; dest.mkdir(exist_ok=True)
        for n,part in enumerate(spec['parts']):
            (dest/f'phase_{n}.sql').write_text(part['text']+'\n',encoding='utf-8')
        (dest/'spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'prepared_specs.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Prepared',len(SPECS),'source-reviewed scenarios')

if __name__ == '__main__':
    prepare()
