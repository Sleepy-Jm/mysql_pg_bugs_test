"""Additional source-reviewed scenarios; keeps the first frozen batch intact."""
import hashlib
import json
from pg_report_prepare_replay import ROOT, SPECS, add, exact, excerpt

def main():
    add('17428',[excerpt('17428','create table mytable (','-- etc')],'output',r'(?s)0\|1.*1\|1.*2\|2.*3\|3',
        '未调用序列时 count=0、last_value=1，后续计数一致','作者期望未调用序列值为0')
    setup=excerpt('17416','CREATE EXTENSION plpython3u;','\'"\n',include_end=True)
    setup['text']=setup['text'][:-1]
    setup['transformations'].append('remove closing shell double quote; preserve SQL string quote')
    trigger=exact('17416','SELECT plpy_xact_test();')
    trigger['text']='\n'.join([trigger['text']]*500)
    trigger['transformations'].append('expand author shell seq 500 loop into 500 identical statements')
    add('17416',[setup,trigger],'crash',r'terminated by signal (?:6|11)',
        '500次 plpy.rollback() 导致 Python 栈溢出及进程崩溃','错误处理不应导致服务崩溃',timeout=90)
    add('18751',[excerpt('18751','create table t1(','explain analyze select'),excerpt('18751','explain analyze select * from (\n(select * from t1)\nunion all\n(select * from t2 where true)','/* Bad:')],
        'output',r'Gather Merge','增加 WHERE true 的 UNION ALL 使用 Gather Merge/Sort','作者期望保持有序索引的 Merge Append',notes='只判定报告中的计划形状，不比较共享服务器墙钟性能。')
    add('18771',[exact('18771',"CREATE COLLATION custom_ci_ai (provider=icu,\nlocale='und-u-ks-level1', deterministic=false);"),
                 exact('18771',"CREATE COLLATION custom_ci_ai_with_rules (provider=icu,\nlocale='und', deterministic=false, rules = '[strength 1]');"),
                 exact('18771',"SELECT 'a'='á' COLLATE custom_ci_ai as no_rules, 'a'='á' COLLATE\ncustom_ci_ai_with_rules as with_rules;")],
        'output',r'(?m)^t\|f$','ICU rules 中 strength 1 未生效','两列均应为 true',notes='使用服务器 ICU 66.1，记录版本；不声称匹配作者未注明的 ICU 版本。')
    add('18780',[exact('18780','create table foo (f1 timestamptz);',True),exact('18780','prepare foo as insert into foo select $1;',True),
                 exact('18780','prepare foo2 as insert into foo select $1 group by 1;',True)],
        'error',r'column "f1" is of type timestamp with time zone but expression is of type text',
        '复杂查询参数不能从目标列推断时间戳类型','作者希望沿用目标列类型',notes='采用官方回复中明确作为 extended query 代理的 PREPARE 场景，不声称复现 JDBC 实现本身。')
    add('18806',[exact('18806','create table test(order_id int, name varchar);',True),
                 exact('18806','create table orders(order_id int, name char(10)) partition by hash\n(order_id);',True),
                 exact('18806','set enable_partitionwise_join = on;',True),
                 exact('18806','create table orders_p1 partition of orders for values with (\nmodulus 32, remainder 0);',True),
                 exact('18806','explain select * from test t join orders o on\nt.order_id =o.order_id where t.order_id in (select order_id from orders);',True)],
        'crash',r'terminated by signal (?:6|11)','partitionwise join 查询导致断言/崩溃','正常完成规划',notes='使用官方讨论中 Tender Wang 的完整单分区简化复现，不根据表结构猜造建表。')
    # Search-path setting is explicitly given in the author's shell invocation.
    add('18767',[exact('18767','SET search_path = tst;'),excerpt('18767','select version();','A simple shell script :')],
        'stderr',r'WARNING:\s+Beware: the calling function is not the expected',
        '创建函数时的 search_path 使 PG_CONTEXT 省略调用者 schema','作者期望按调用时的路径返回限定名',notes='执行原文第二种启动方式，保持 SET 与脚本同一会话。')
    for spec in SPECS:
        spec['spec_sha256']=hashlib.sha256(json.dumps(spec,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        dest=ROOT/'prepared'/spec['scenario_id'];dest.mkdir(exist_ok=False)
        for n,p in enumerate(spec['parts']):(dest/f'phase_{n}.sql').write_text(p['text']+'\n',encoding='utf-8')
        (dest/'spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'prepared_specs_batch002.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Prepared',len(SPECS))

if __name__=='__main__':main()
