import copy
import hashlib
import json
from pg_report_prepare_replay import ROOT,SPECS,add,exact,excerpt


def main():
    add('17304',[exact('17304','select;')],'stderr',r'print\.c:\d+:\d+: runtime error: null pointer passed as argument 1','对齐输出空 SELECT 触发 psql UBSan 空指针报告','客户端不应触发未定义行为',mode='ubsan_client',notes='保留 psql 默认对齐格式；无 -A/-t；对应客户端版本开启报告要求的UBSan。')
    add('17283',[excerpt('17283',"Currently, PostgreSQL defaults",None)],'output',r'^IPV4_ONLY$','默认localhost只监听IPv4而未监听IPv6','默认同时监听127.0.0.1和::1',mode='listen_probe',config={'listen_addresses':"'localhost'"},notes='这是监听配置与网络探测，不是SQL；localhost解析结果随环境记录。')
    a=excerpt('17357','create table elements (','// CREATE TABLE');b=excerpt('17357','insert into elements (priority)','// INSERT')
    a['text']+='\n'+b['text'];a['additional_sources']=[b];a['transformations'].append('concatenate explicitly supplied DDL and INSERT, remove displayed command tags')
    baseline=excerpt('17357','select\n     *,','4. and the result')
    filtered=excerpt('17357','select *\n    from (', '// (20 rows)')
    # The final query repeats the subquery verbatim; select its source occurrence after the complaint.
    text=(ROOT/'source_text/17357.txt').read_text(encoding='utf-8');start=text.index('select *',text.index('The result is the same, but here'))
    query=text[start:text.index('Is that logical?',start)].strip();filtered=exact('17357',query)
    add('17357',[a,baseline,filtered],'output',r'^ROW_CHANGED$','增加过滤条件后窗口编号为1的priority3记录id发生变化','作者期望过滤前后的编号稳定',mode='window_compare',notes='比较原文两条查询的返回行，不为并列排序补充tie-breaker。')
    add('17538',[excerpt('17538','Then, I update log_hostname','The full logfile:')],'output',r'disconnection:.*host=127\.0\.0\.1','log_hostname从no改yes后已有TCP连接的断开日志仍记IP','作者期望断开时记录localhost',mode='hostname_reload',config={'listen_addresses':"'127.0.0.1'",'log_connections':'on','log_disconnections':'on','log_hostname':'off'},notes='用户wang/dbwang映射为隔离集群postgres；无业务SQL，保留同一已建立TCP连接。')
    add('17393',[excerpt('17393','Steps in script:','Notes:')],'output',r'^CATALOG_WITHOUT_FILES$','PITR到DROP之前恢复catalog却缺数据库目录','catalog及数据文件均恢复',mode='pitr',timeout=180,notes='按原文步骤编排；路径/端口/用户替换为隔离任务；原数据目录rename保留，不执行rm -rf。')
    # SQL is explicitly present in the attachment README; only qualify its supplied schema.
    path=ROOT/'materials/17292_extracted/buggy/README';raw=path.read_text(encoding='utf-8');q='explain select * from vw_ftrucf_index;';pos=raw.index(q)
    part=dict(text=q.replace('from vw_','from bmk.vw_'),source=str(path),start_offset=pos,end_offset=pos+len(q),excerpt_sha256=hashlib.sha256(q.encode()).hexdigest(),transformations=['qualify view with bmk schema explicitly created by supplied install_part.sql'])
    add('17292',[part],'output',r'(?s)Nested Loop Left Join.*Join Filter:.*InitPlan 24','219分区及索引下规划极慢并产生报告所示不完整计划','正常时间内生成完整计划',mode='attachment_plan',notes='180秒有界规划；超时一律无法判断，不当作未复现；计划匹配另要求不存在Append，保留附件计划原文。')
    SPECS[-1]['attachment_scripts']=['install_part.sql','install_partitions.sql','install_index_nopart.sql','install_index_part.sql']
    SPECS[-1]['additional_oracle_checks']=[dict(stream='stdout',pattern='Append',count=0)]
    prior=json.loads((ROOT/'prepared_specs_batch002.json').read_text(encoding='utf-8'));s=copy.deepcopy(next(s for s in prior if s['report_id']=='18806'));s.pop('spec_sha256');s.update(report_id='18805',scenario_id='18805_linked18806',source_url=__import__('pg_report_prepare_replay').REPORTS['18805']['source_url'])
    s['linked_source_evidence']=excerpt('18805','It is the same project scenario','BUG #18806',thread=True)
    s['notes']='官方18805回复明确链接18806同一项目场景；重放18806官方简化例，不声称复现原XFS损坏，不计独立根因。'
    SPECS.append(s)
    for s in SPECS:
        if s['mode'] in ['pitr','hostname_reload','listen_probe']:s['parts'][0]['material_kind']='operational_steps'
        s['spec_sha256']=hashlib.sha256(json.dumps(s,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        d=ROOT/'prepared'/s['scenario_id'];d.mkdir(exist_ok=False)
        for n,p in enumerate(s['parts']):(d/f'phase_{n}.sql').write_text(p['text']+'\n',encoding='utf-8')
        (d/'spec.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'prepared_specs_batch005.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2),encoding='utf-8');print('Prepared',len(SPECS))


if __name__=='__main__':main()
