"""Build a source-preserving reading guide; never execute SQL or rewrite evidence."""
from pathlib import Path
import hashlib
import json
import os
import re
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
FIRST = BASE / 'prompt_pipeline_20261104'
DEEP = BASE / 'prompt_pipeline_deepseek_20261105'
CASES = [
    ('derived_condition_charset_4d2da251cb53', '派生表条件下推与字符集', '首次要求行依赖 CONCAT、无前缀非 ASCII 字面量、DISTINCT 与下推 ON/OFF；DeepSeek Stage 1 偏向显式字符集前缀，Stage 2 使用可折叠的 ASCII 常量 alpha，且没有 DISTINCT。两者均谈到克隆路径，但 DeepSeek 未保留首次暴露异常的构造。', '首次：父提交每轮 8/8、目标 7/8；DCP01_ON 目标空集，父提交返回 id=1、4，HEX=61C3A9。DeepSeek：两侧每轮均为两组相同的 4 行结果。'),
    ('item_property_recalculation_248c7f7c227e', 'Item 属性重算', '首次要求把窗口表达式放在 IN 左侧，并在同一个 PREPARE 上重复 EXECUTE，另有直接查询对照；DeepSeek Stage 1 和 Stage 2 转为窗口 SUM 的参数内部包含 IN 子查询，以及存储函数参数。表达式树方向与生命周期压力都改变了。', '首次：父提交每轮 8/8、目标 6/8；两个检查点错误，详见下方结果表。DeepSeek：两侧每轮均为两组相同的 5 行结果。'),
    ('window_frame_state_c296cddb93ff', '窗口帧状态', '首次从 lower_limit=current_row+1 推导前向缩小帧，要求 1 FOLLOWING..UNBOUNDED FOLLOWING、DECIMAL/DOUBLE、高精度开关及其他帧对照；DeepSeek Stage 1 选择 1 PRECEDING..CURRENT ROW，Stage 2 沿用整数列和后向两行帧。', '首次：父提交每轮 9/9、目标 4/9；5 个检查点错误。DeepSeek：两侧每轮均为相同的 8 行结果。'),
]
inventory = {}

def read(p):
    return p.read_text(encoding='utf-8-sig')

def link(p, label=None):
    if not p.is_file():
        raise FileNotFoundError(p)
    rel = os.path.relpath(p, OUT).replace(os.sep, '/')
    inventory[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return f'[{label or p.name}]({rel})'

def embed(p, title, lang='text'):
    body = read(p).rstrip()
    fence = '`' * max(4, max([len(m.group()) + 1 for m in re.finditer(r'`+', body)] or [4]))
    return f'### {title}\n\n原件：{link(p)}\n\n{fence}{lang}\n{body}\n{fence}\n\n'

def xml_table(p):
    data = re.sub(br'<\?xml[^?]*\?>', b'', p.read_bytes())
    root = ET.fromstring(b'<archive>' + data + b'</archive>')
    parts = []
    for i, rs in enumerate(root.findall('resultset'), 1):
        rows = rs.findall('row')
        if not rows:
            parts.append(f'结果集 {i}：空集。\n\n')
            continue
        cols = [f.attrib['name'] for f in rows[0].findall('field')]
        def cell(f):
            if any(k.endswith('nil') and v == 'true' for k, v in f.attrib.items()):
                return 'NULL'
            return (f.text or '').replace('|', '\\|').replace('\n', '<br>')
        parts.append(f'结果集 {i}：\n\n| ' + ' | '.join(cols) + ' |\n| ' + ' | '.join(['---'] * len(cols)) + ' |\n')
        parts.extend('| ' + ' | '.join(cell(f) for f in row.findall('field')) + ' |\n' for row in rows)
        parts.append('\n')
    return ''.join(parts)

overview = '''# 首次实验与 DeepSeek 重跑：逐阶段输入输出对照

整理日期：2026-11-06。首次指 `prompt_pipeline_20261104`，重跑指 `mysql_three_prompt_deepseek_20261105_run_002`。本文从现有归档整理，未新增模型调用或数据库实验，未修改历史证据。

## 总体结果与阅读入口

| 目标 | 首次父提交 / 目标提交每轮通过数 | DeepSeek 重跑 | 完整逐阶段读本 |
|---|---|---|---|
'''
scores = ['8/8 / 7/8', '8/8 / 6/8', '9/9 / 4/9']
for (key, title, diff, result), score in zip(CASES, scores):
    overview += f'| {title} | {score} | 父/目标三轮均无差异 | [{title}]({key}.md) |\n'
overview += '''
首次共 18 次脚本执行、150 次检查点观测，其中 24 次错误观测来自 8 个不同失败检查点，每个重复三轮；检查点数不等于独立缺陷数。DeepSeek 共 18 次脚本执行、9 组父/目标配对，均为 `no_observed_difference`。两批统计单位不同，不能把 150 和 9 直接比较为命中率。

## 每一步保存了什么

| 步骤 | 输入 | 输出 | 本次整理方式 |
|---|---|---|---|
| 0 固定材料 | 精确目标/父提交、源码节选、模板与 INTERSECT ALL 示例 | 输入包、哈希 | 各读本全文展示源码与共同 Stage 1 提示词，并验证两批字节一致 |
| 1 src2req | Stage 1 完整提示词；DeepSeek 实际 API messages | 测试偏好/需求：目标、源码条件、构造、oracle、覆盖观测、不确定性 | 两批原文全文保留；分别概括差异 |
| 2 req2test | 同一模板和示例，填入各自新 Stage 1 输出 | 完整响应（SQL、预期行、覆盖建议、执行状态） | 两批实际提示词、完整响应与提取 SQL 全文展示；旧种子不冒充实际输入 |
| 3 运行 | SQL、首次独立 expected JSON、精确构建、命令与 schema | 父/目标各三轮 XML、stderr、返回码和结果元数据 | 第一轮两侧结果转为可读表，所有三轮 XML/stderr/JSON 均有链接和哈希 |
| 4 判断 | 运行结果、首次语义 oracle / 重跑配对比较 | 首次逐检查点正确性；重跑结果/错误/退出码差异 | 保留原口径，不将无差异等同于分支覆盖或不存在缺陷 |

## 上下文与可比性

两批三个目标的 Stage 1 提示词和目标源码节选逐字节一致。模板参考提交为 `fadce4b16df62f362662754ee8e9745b478a643c`；输入包内的 Requirements 和旧 req2test 带人工种子，实际第二阶段均填入本次 Stage 1 输出。输入包存在文件不等于模型读过文件。

首次由同一 Codex 助手在共享聊天上下文直接完成两阶段，没有独立模型 API；归档没有可还原完整模型隐含上下文的独立请求信封。窗口案例生成前曾接触另一版本相关 AVG 分母实现。详见 [首次上下文审查](../prompt_pipeline_20261104/contamination_review.md)。首次可作为源码引导的开发复现样例，不能作无污染盲测。

DeepSeek 保存实际请求/响应；每次请求只含归档 messages，三组无共享对话历史。Stage 1 请求/返回 `deepseek-v4-pro`；Stage 2 请求 `deepseek-v4-flash`、返回 `deepseek-flash`，版本别名未独立确认。参数 temperature=0.7、max_tokens=16384、thinking=disabled。首次没有对应的独立 API 参数记录，不能补造同参数实验。

两批都未插桩测量目标源码分支。首次有稳定行为差异，DeepSeek 没有差异；这说明本次重跑未复现首次效果，但上下文、生成方式及 SQL 均改变，不能仅据此断言模型是唯一原因。

## 逐案例差异

'''

for key, title, diff, result in CASES:
    first_gen = FIRST / 'generation'
    src = first_gen / 'input_bundle/source-code-data/mysql' / (key + '.txt')
    p1 = first_gen / 'input_bundle/Prompts/mysql/src2req' / (key + '.txt')
    ds_src = DEEP / 'input_bundle/source-code-data/mysql' / (key + '.txt')
    ds_p1 = DEEP / 'input_bundle/Prompts/mysql/src2req' / (key + '.txt')
    assert src.read_bytes() == ds_src.read_bytes()
    assert p1.read_bytes() == ds_p1.read_bytes()
    req1 = json.loads(read(DEEP / key / 'stage1_request.json'))
    assert len(req1['messages']) == 1 and req1['messages'][0]['content'] == read(p1)
    req2 = json.loads(read(DEEP / key / 'stage2_request.json'))
    assert len(req2['messages']) == 1 and req2['messages'][0]['content'] == read(DEEP / key / 'stage2_prompt.txt')
    overview += f'### {title}\n\n{diff}\n\n{result}\n\n'
    doc = f'# {title}：两批实验完整读本\n\n[返回总览](README.md)\n\n{diff}\n\n{result}\n\n'
    if key.startswith('window'):
        note = '整理新增勘误：DeepSeek Stage 1 将 (1,NULL,3) 的第三行后向两行帧 AVG 写成 3/2=1.5；实际帧为 (NULL,3)，非 NULL 计数为 1，正确值为 3。Stage 2 已写成 3.0000，父/目标 XML 也均为 3.0000。此处保留两阶段原文，不静默修正历史回答。'
        doc += note + '\n\n'
        overview += note + '\n\n'
    doc += '## 0. 共同源码与 Stage 1 正式输入\n\n两批以下文件逐字节一致。源码节选已含精确提交、父提交、源文件、行号、blob、Target observation 与局部范围说明。\n\n'
    doc += f'DeepSeek 对应副本：{link(ds_src, "源码")}、{link(ds_p1, "Stage 1 提示词")}。\n\n'
    doc += embed(src, '目标源码片段与上下文', 'text')
    doc += embed(p1, '共同的完整 Stage 1 提示词（含示例及当前源码）')
    doc += '### 输入包中其他上下文与来源\n\n下列文件用于区分模板、示例、种子和正式输入；完整正式提示词已经展示在本读本，不能将包内每个文件都视为实际进入模型上下文。\n\n'
    for rel in ['provenance.json', 'README.txt', 'optim/mysql.json', 'template-mysql/src2req.txt', 'template-mysql/req2test.txt', 'source-code-data/mysql/intersect_join.txt', 'template-mysql/examples/intersect_join.requirements.txt', 'template-mysql/examples/intersect_join.test.txt', f'Requirements/mysql/req/{key}/{key}_1.txt', f'Prompts/mysql/req2test/{key}.txt']:
        doc += '- ' + link(first_gen / 'input_bundle' / rel, rel) + '\n'
    doc += '\n'
    for run, gen in [('首次 Codex', first_gen), ('DeepSeek 重跑', DEEP / key)]:
        is_first = run.startswith('首次')
        s1 = gen / 'stage1_src2req' / (key + '.txt') if is_first else gen / 'stage1_output.txt'
        p2 = gen / 'stage2_req2test/prompts' / (key + '.txt') if is_first else gen / 'stage2_prompt.txt'
        s2 = gen / 'stage2_req2test/responses' / (key + '.txt') if is_first else gen / 'stage2_output.txt'
        sql = gen / 'sql' / (key + '.sql') if is_first else gen / 'generated.sql'
        doc += f'## {"1" if is_first else "2"}. {run}\n\n'
        if is_first:
            doc += f'上下文：同一助手共享对话，无独立 API 信封；{link(gen / "generation_manifest.json", "生成清单")}，{link(FIRST / "contamination_review.md", "上下文审查")}。生成清单中的未执行状态为历史快照，后续执行见本节运行证据。\n\n'
        else:
            for n, req in [(1, req1), (2, req2)]:
                envelope = {k: v for k, v in req.items() if k != 'messages'}
                envelope['messages_summary'] = [{'role': m['role'], 'content_characters': len(m['content'])} for m in req['messages']]
                doc += f'Stage {n} 实际请求 {link(gen / f"stage{n}_request.json")}；原始响应 {link(gen / f"stage{n}_response_raw.json")}。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。\n\n```json\n{json.dumps(envelope, ensure_ascii=False, indent=2)}\n```\n\n'
        doc += embed(s1, 'Stage 1 输出：测试偏好与需求原文')
        doc += embed(p2, 'Stage 2 实际输入：填入本次 Stage 1 后的完整提示词')
        doc += embed(s2, 'Stage 2 完整输出：SQL、预期结果与覆盖建议')
        doc += embed(sql, '提取后实际执行的完整 SQL', 'sql')
        if is_first:
            doc += embed(gen / 'expected' / (key + '.json'), '独立保存的预期结果与 oracle', 'json')
        else:
            doc += '本批没有独立 expected JSON；预期行在上方 Stage 2 响应。自动汇总主要判断父/目标结果、错误与退出码是否相同，不能等同于首次逐检查点 oracle 审计。\n\n'
        doc += '### 执行环境、命令与三轮结果\n\n'
        for side, name in [('parent', '父提交'), ('target', '目标提交')]:
            folder = (FIRST / 'runtime/results' if is_first else DEEP / 'server_evidence/results') / key / side
            result_p = folder / 'result.json'
            obj = json.loads(read(result_p))
            doc += f'#### {name}\n\n执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：{link(result_p)}。精确 revision：`{obj["revision"]}`。\n\n'
            metadata = {k: v for k, v in obj.items() if k != 'trials'}
            metadata['trial_execution_metadata'] = [{k: v for k, v in t.items() if k not in ('evaluation', 'resultsets')} for t in obj['trials']]
            doc += '以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。\n\n```json\n' + json.dumps(metadata, ensure_ascii=False, indent=2) + '\n```\n\n'
            doc += '| 轮次 | 返回码 | XML 原件 | stderr 原件 |\n|---|---|---|---|\n'
            for t in obj['trials']:
                n = t['repeat']
                doc += f'| {n} | {t["returncode"]} | {link(folder / f"trial-{n}.stdout.xml")} | {link(folder / f"trial-{n}.stderr.txt")} |\n'
            doc += '\n第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。\n\n'
            doc += xml_table(folder / 'trial-1.stdout.xml')
        if is_first:
            doc += f'判定与环境补充：{link(FIRST / "runtime/comparison.json", "逐检查点比较")}、{link(FIRST / "runtime/final_report.txt", "完整执行报告")}、{link(FIRST / "lineage.json", "输入构建执行关联")}。\n\n'
        else:
            doc += f'判定与环境补充：{link(DEEP / "server_evidence/summary.json", "逐轮配对与二进制身份")}、{link(DEEP / "run_manifest.json", "参数及 run_id")}、{link(DEEP / "verification_report.md", "执行报告")}。原始远端 runner 未公开，公开包不能还原其完整启动命令；其 SHA256 见导出清单。\n\n'
    (OUT / (key + '.md')).write_text(doc, encoding='utf-8', newline='\n')

overview += '''## 归档边界与复核

每份读本均展示全部正式提示词、目标源码、两阶段输出和完整 SQL；执行部分展示两侧第一轮完整结果，并链接全部三轮原始文件。Markdown 是阅读副本，原始字节与 SHA256 以链接原件和 `evidence_index.json` 为准。目录内 `build_readers.py` 可从历史归档重新生成这些读本。

首次完整聊天上下文没有作为独立模型请求公开保存；重跑早期参数未冻结的部分试跑、缺依赖且未执行 SQL 的启动失败批次及原始服务大日志不进入成功执行统计，也不在本读本冒充可访问原件。排除项见两批 export_manifest.json。

本次整理没有新增服务器实验。复核可在首次目录执行 `verify.py`、重跑目录执行 `verify_export.py`；本目录的证据索引用于定位全部引用原件及其 SHA256。
'''
(OUT / 'README.md').write_text(overview, encoding='utf-8', newline='\n')
(OUT / 'evidence_index.json').write_text(json.dumps({'source_archive_commit': 'ab97f561317c7f696684f33121f6299bffe1bb2c', 'purpose': 'reading guide; no new generation or SQL execution', 'files_sha256': inventory}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(f'Built overview and {len(CASES)} complete readers; indexed {len(inventory)} evidence files.')
