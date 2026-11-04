# 三目标隔离生成与补充执行（2026-11-04）

保存完整的“提示词/源码 → src2req 需求 → req2test → SQL/预期 → 对应提交运行结果”关系，并保留未生成、未复现和 oracle 暂缓判定的结果。与[上一轮实验](../prompt_pipeline_20261104/README.md)分开；不能沿用上一轮的8/8、8/8、9/9分母。

## 原始隔离生成：每版本三轮

| SQL 组 | 父提交通过数（每轮） | 目标提交通过数（每轮） | 结果 |
|---|---:|---:|---|
| 字符集 `4d2da251cb53` | 未执行 | 未执行 | B 未生成 SQL；保持 blocked |
| Item 属性 `248c7f7c227e` | 4/4 | 4/4 | 基础子集未复现；IN 等候选未生成 |
| 窗口帧 `c296cddb93ff` | 7/7 | 4/7 | WF_BASE / WF_NULLS / WF_REAL_LOW 错误；AVG 应为408却返回680，应为450却返回600 |

窗口共生成8个用例，其中 WF_UNBOUNDED 在运行前已标记精度 oracle_hold，因此分母为7，不是8；其实际输出完整保留。两组可执行脚本×两个提交×三轮=12次完整脚本，72次用例观测，其中57 pass、9 mismatch、6 hold。三轮结果一致。

## 用户要求补齐未执行项后的结果

这一步使用历史案例知识，属于**有答案知识的补充执行**，不覆盖上述首次实验，也不提高隔离生成成功数。字符集补齐C1–C3主候选，Item补齐IN C2/C4相关测试；可选存储函数及 FIRST/LAST/NTH 扩展未选择。

| SQL 组 | 父提交通过数（每轮） | 目标提交通过数（每轮） | 复现的异常 |
|---|---:|---:|---|
| 字符集 `4d2da251cb53`（补充） | 6/6 | 5/6 | 开启下推后，无前缀非 ASCII 候选应返回两行却返回空集 |
| Item 属性 `248c7f7c227e`（补充） | 6/6 | 3/6 | 重复执行时 wrapped 应为 `[8,17,29,18,4,NULL]`，实际 `[NULL,3,10,24,47,39]` |
| 窗口帧 `c296cddb93ff`（沿用原始实测） | 7/7 | 4/7 | AVG 应为408却返回680；NULL/低精度用例应为420却返回1260或630 |

补充另执行12次完整脚本、72次用例观测，60 pass、12 mismatch。窗口没有为这张合并展示表重复执行。所有已运行脚本正常退出，无SQL错误/超时/OOM；容器均结束并移除。错误用例数不等于独立缺陷数。

## 导航与对应关系

- [详细源码机制与关键条件](source_mechanisms.md)：按每组分别链接提示词、需求、SQL、预期和实测；区分源码事实、推导、已验证结果、未观测内部状态。
- [lineage.json](lineage.json)：三个目标的完整 SHA、直接父 SHA、各阶段输入/输出路径、原件/导出哈希、运行 trial 路径及补充入口。
- [原始运行报告](runtime/REPORT.md)、[机器可读汇总](runtime/results/summary.json)、[跨提交逐行对比](runtime/revision_comparison.json)。
- [补充运行报告](supplemental/REPORT.md)、[机器可读汇总](supplemental/results/summary.json)、[知识来源](supplemental/provenance.json)。
- [A 总启动提示词](generation/stage1_src2req/START_src2req.txt)、[B 总启动提示词](generation/stage2_req2test/START_req2test.txt)。每组目录包含局部启动提示词、异目标完整示例、白名单、输入和 attempt_001 输出；实际提示词由启动文本加其允许读取的文件组成，不把未展开启动文本误称为完整单一 prompt。
- [第一阶段审查](review/stage1_review.md)、[第二阶段审查](review/stage2_review.md)、[冻结清单](review/stage2_outputs_frozen.json)、[执行后哈希复核](runtime/frozen_integrity_check.json)。审查文档保留当时的“尚未执行”时间状态，以本目录的运行报告为后续事实。
- [精确生产源码 diff](source_analysis/manifest.json)：仅后验分析可读，不是 A/B 输入。

| 组 | 目标提交 | 直接父提交 |
|---|---|---|
| 字符集 | 4d2da251cb536340d19438cc0039bb2846f9a634 | e248166db3c95b4fc998ca14cff914f1fdafbe7b |
| Item | 248c7f7c227e76f3422378ca3b9e10d141dcfc86 | 15980860ac2639f41dfbda2f7fffb7aeeab32921 |
| 窗口 | c296cddb93ffc631f9b43d3b1ff769604e7469d7 | 74c7ccfa27f482576412300e5f92fd3dbeb54cfa |

## 实验资格与保存约定

原始生成 run_id 为 `mysql_three_isolated_regeneration_20261104`，执行 ID 为 `mysql-isolated-regeneration-20261104-b`；补充执行 ID 为 `mysql-supplemental-assisted-20261104`。协议仓库提交为 `14066bae80a1f995a326ec9cb68020cb8d4f90ad`；运行器是独立文件，以实际 SHA-256 标识，没有虚构其已提交版本。MySQL精确提交、二进制/共享库哈希、镜像、启动命令、同会话参数见各 results/builds、launch.json、comparison.json。

原始实验是人工预选已知目标和关键源码的隔离上下文重复生成，不是从完整仓库自主寻找未知缺陷。A/B审查未观察到读取旧答案正文，B存在路径元数据偏离；三组共享各阶段的上下文，训练记忆和不可见上下文无法排除，不能宣称绝对无污染。补充则明确使用已知答案知识。后续盲实验不得把本目录运行结果或 source_analysis 作为生成输入。

[export_manifest.json](export_manifest.json) 记录每份原件及导出 SHA-256；SQL逐字节保留，其余含个人路径/主机的文本做占位符脱敏。清单中的历史哈希代表原件，不会为匹配脱敏件而回写；应同时核对导出清单。启动文件中的占位路径是归档证据，不是直接可执行的全新配置。原始大日志、会话快照、数据目录、镜像均留在本地/原实验主机，不提交仓库。原始服务器启动缺库后，在独立-b目录补挂共享库完成执行，过程见运行报告；共享库未逐提交重新编译，已记录具体哈希。

离线复核（不连接数据库）：

```text
python -X utf8 -B experiments/isolated_regeneration_20261104/verify.py
python -X utf8 -B scripts/check_offline.py
python -X utf8 -B scripts/audit_repository.py
```
