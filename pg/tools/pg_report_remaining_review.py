"""Describe every unexecuted report's concrete prerequisites and recovery route."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT=Path('experiments/pg_report_replay_20261104/run_001')
OUT=ROOT/'remaining69_review_20261104'
SPECIAL={
    '17362':('优先尝试补环境','恢复原文明确的CentOS7、PGDG 14.1-1PGDG.rhel7与libicu50.2-4.el7_7，核对RPM身份与实际ICU版本；解码原文base64数据，在14.0/14.1/14.2相同环境回放。资源及执行进展见本目录RESOURCE_RECOVERY.md；下载本身不计为重放成功。'),
    '17476':('优先追核扩展环境','官方评论有完整geometry/GiST最小SQL；追核原PostGIS版本及可用扩展包，再构建三个PG版本的相同扩展环境。任意安装现代PostGIS不能证明补齐原环境。'),
    '17445':('追索失效外部材料','尝试恢复原文三个paste链接的历史快照；必须能对应原schema及成功/失败SQL。若只返回首页或无法恢复，继续保留缺口。'),
    '18884':('追索外部材料及客户端','取得原截图、Test_Table建表/数据、JDBC驱动版本及会话timezone设置；截图不能自动补出未显示的DDL。'),
    '17300':('需要原始定义','需要textrange及textmultirange实际类型创建定义或原作者明确引用的初始化脚本；不能按类型名字猜建表或从修复测试反推原设置。'),
    '17406':('需要完整原始恢复材料','需要缺失函数、外键目标表、角色及12→14升级材料；保留现有表数据和索引。不能删除触发器/外键绕过恢复错误。'),
    '17413':('需要原始对象/连接配置','取得trash/staging schema定义、foreign server、user mapping及必要源库数据；凭据另行本地配置，不进入报告。'),
    '17457':('需要拓扑与恢复材料','取得原WAL、完整启动配置及双主机/不同物理卷路径拓扑；可在隔离环境构建，但普通单机目录不等同该前提。'),
    '18789':('需要原始HA配置','取得Patroni4.0.4完整配置、slot状态与故障转移时序，在新隔离集群重放，不在现有HA服务制造故障。'),
    '18800':('需要原始备份链','取得基础/增量备份、对应WAL和manifest；单凭错误消息不能重建备份。'),
}


def main():
    OUT.mkdir(exist_ok=True)
    reports=json.loads((ROOT/'all_report_results.json').read_text(encoding='utf-8'))
    audit={r['report_id']:r for r in json.loads((ROOT/'source_audit.json').read_text(encoding='utf-8'))}
    baseline_path=OUT/'baseline69.json'
    if not baseline_path.exists() and (OUT/'remaining69.json').exists():
        baseline_path.write_bytes((OUT/'remaining69.json').read_bytes())
    baseline={r['report_id']:r for r in json.loads(baseline_path.read_text(encoding='utf-8'))} if baseline_path.exists() else {}
    rows=[]
    for report in reports:
        if baseline and report['report_id'] not in baseline:continue
        if not baseline and report['scenario_count']:continue
        a=audit[report['report_id']];prior=baseline.get(report['report_id'],{});kind=prior.get('original_class',a['review_disposition'])
        if kind=='materials_incomplete':
            route='需要追索原始材料';action='逐项向原报告/讨论串/附件来源追索下列具体缺失项；原始生产数据、损坏页或备份若未公开，需原持有人提供；未取得前不补造SQL或数据。'
        elif kind=='environment_blocked':
            route='需要特定环境或历史包';action='核实原文指明的平台/包/配置，再取得对应镜像、安装器或构建依赖并搭建隔离环境；平台可用不等于报告的其他前提已齐全。'
        elif kind=='static_only':
            route='仅静态核对';action='可比较相邻版本源码及提交；不补造触发SQL，也不将静态核对计为运行时复现或正常执行。'
        else:
            route='不适用数据库运行时回放';action='单列文档/仓库/安装支持问题；如研究历史包行为，需要对应历史包和仓库证据，不计入SQL回归bug对照。'
        route,action=SPECIAL.get(report['report_id'],(route,action))
        rows.append(dict(report_id=report['report_id'],version_field=report['original_version_field'],
            original_class=kind,recovery_route=route,concrete_gap=prior.get('concrete_gap',a['review_note']),
            next_action=action,source_url=a['source_url'],
            source_text=str(ROOT/'source_text'/f"{report['report_id']}.txt"),
            thread_text=str(ROOT/'thread_text'/f"{report['report_id']}.txt"),
            execution_status=('target_results:'+json.dumps(report['target_scenario_statuses'],ensure_ascii=False) if report['target_scenario_statuses'] else 'not_executed_no_new_replay_evidence')))
    assert len(rows)==69 and len({r['report_id'] for r in rows})==69
    (OUT/'remaining69.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    with (OUT/'remaining69.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    lines=['# PG 剩余69份报告：缺口与补齐路线','',
        '136份是固定范围内的报告数：2021-11至2026-11官方pgsql-bugs月归档，截止2026-11-04，带BUG编号的原始表单报告，首帖PostgreSQL version原字段精确匹配14.1/14.2/17.1/17.2。不是所有影响这四个版本的缺陷总数。',
        '采集记录：61个月、129个归档页面、2093个候选URL、2066份原始表单报告；保存的获取错误为0，筛选得136份。未编号邮件、其他列表、正文声称受影响但Version字段不同的报告不纳入此冻结集合。',
        '此前已执行67份；本表保留原剩余69份，分为32份缺材料、27份缺环境、7份非运行时及3份静态问题。10份非运行时/静态问题不应统称为安装依赖后即可运行的SQL案例。',
        '本表是补齐审计，资源下载不等于执行成功；正式统计仍以独立执行记录为准。','',
        '|报告|Version|补齐路线|具体缺口|下一步|当前执行记录|','|---|---|---|---|---|---|']
    lines += [f"|[{r['report_id']}]({r['source_url']})|{r['version_field']}|{r['recovery_route']}|{r['concrete_gap'].replace('|','/')}|{r['next_action'].replace('|','/')}|{r['execution_status']}|" for r in rows]
    (OUT/'REMAINING_69.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(dict(reports=len(rows),classes=dict(Counter(r['original_class'] for r in rows))),ensure_ascii=False))


if __name__=='__main__':main()
