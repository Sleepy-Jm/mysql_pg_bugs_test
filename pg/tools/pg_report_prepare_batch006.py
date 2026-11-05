import copy
import hashlib
import json
from pg_report_prepare_replay import ROOT,SPECS,add,exact,excerpt


def main():
    add('17284',[excerpt('17284','concurrency=2','("fsync=off"')],'crash',r'terminated by signal 6','TEST_SUMMARIZE_SERIAL 下并发 two-ids 触发 SerialAdd 断言','不发生断言崩溃',mode='serial_suite',config={'fsync':'off'},notes='两并发，各100次，专用构建使用原 CPPFLAGS；临时输出目录改为本任务路径，省略原rm及全局coredumpctl。')
    SPECS[-1]['build_variant']='serial';SPECS[-1]['parts'][0]['material_kind']='test_suite_commands'
    add('17456',[excerpt('17456','CREATE SCHEMA my_schema;','===================================\nend of reproduction')],'error',r'operator does not exist: util\.ltree = util\.ltree','pg_dump还原跨schema ltree触发器时报操作符不存在','dump应正确限定操作符并可还原',mode='dump_restore',notes='按原文server13.6固定，分别使用client14.1/14.2/14.3；不是14.2服务端测试。')
    SPECS[-1].update(server_version='13.6',build_variant='ordinary')
    old=next(s for s in json.loads((ROOT/'prepared_specs_batch004.json').read_text(encoding='utf-8')) if s['report_id']=='17335')
    s=copy.deepcopy(old);s.pop('spec_sha256');s.update(scenario_id='17335_owner_revision1',supersedes_spec_sha256=old['spec_sha256'],dump_owner_roles=['yura'],revision_reason='source dump explicitly assigns both tables OWNER TO yura; provision that named non-superuser role as isolated restore prerequisite, keeping dump bytes and oracle unchanged')
    SPECS.append(s)
    add('18810',[excerpt('18810','log detail:','The Segmentation fault')],'crash',r'system logger process .*terminated by signal 11','不存在的slave槽配置在SIGHUP重载时使logger SIGSEGV','无效配置应正常拒绝而不崩溃',mode='config_reload',config={'logging_collector':'on','log_directory':"'log'",'log_filename':"'replay.log'"},notes='从原日志明确给出的参数名、slave值、不存在槽及SIGHUP事件组织配置回放；不是SQL场景，不补造复制槽。')
    SPECS[-1]['reload_slot_value']='slave';SPECS[-1]['parts'][0]['material_kind']='configuration_log_steps'
    for s in SPECS:
        s['spec_sha256']=hashlib.sha256(json.dumps(s,sort_keys=True,ensure_ascii=False).encode()).hexdigest();d=ROOT/'prepared'/s['scenario_id'];d.mkdir(exist_ok=False)
        for n,p in enumerate(s['parts']):(d/f'phase_{n}.sql').write_text(p['text']+'\n',encoding='utf-8')
        (d/'spec.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'prepared_specs_batch006.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2),encoding='utf-8');print('Prepared',len(SPECS))


if __name__=='__main__':main()
