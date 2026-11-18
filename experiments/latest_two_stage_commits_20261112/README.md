# 最新两阶段提示词：三组提交实测归档

实验日期：2026-11-12；归档日期：2026-11-18。归档现有 `run_022_stage12_v5` 和 `run_023_two_stage_remaining_20261112`，没有重新调用模型或执行数据库。三组均为**无反馈**实验；后来的 `run_024` 样例反馈实验未纳入。

Stage1 使用 DeepSeek v4 Pro；最终成功的 Stage2 使用 DeepSeek v4 Flash，设置 `thinking.type=disabled`。三组实际 Stage2 请求均已核对：包含完整的 Stage1 输出，无未填充的 `{{STAGE1_OUTPUT}}`。首次 Stage2 因长度限制没有生成可用内容；首次请求、响应和最终成功请求、响应分别保存，不能把首次失败的零 SQL 计数当成最终结果。

| 目标 / 原始运行 | 父提交 | 目标提交 | 5 条 SQL 的三轮结果 |
|---|---|---|---|
| [条件下推与字符集](derived_condition_charset_4d2da251cb53/summary.json) / run_022 | `e248166db3c95b4fc998ca14cff914f1fdafbe7b` | `4d2da251cb536340d19438cc0039bb2846f9a634` | T1、T4 稳定差异；T2、T3、T5 无差异 |
| [Item 属性重算](item_property_recalculation_248c7f7c227e/summary.json) / run_023 | `15980860ac2639f41dfbda2f7fffb7aeeab32921` | `248c7f7c227e76f3422378ca3b9e10d141dcfc86` | T1、T2 无差异；T3–T5 两侧均语法错误 |
| [窗口帧状态](window_frame_state_c296cddb93ff/summary.json) / run_023 | `74c7ccfa27f482576412300e5f92fd3dbeb54cfa` | `c296cddb93ffc631f9b43d3b1ff769604e7469d7` | T1–T4 稳定差异；T5 无差异 |

共 15 个完整 SQL 脚本，每个脚本在父、目标提交各执行三轮，共 **90 次完整脚本执行**。脚本可能包含多个 SELECT，脚本数不是单条查询数。6 个脚本存在稳定结果差异、6 个无结果差异、3 个目标查询存在语法错误；这些计数不是独立缺陷数，也不是新漏洞数。

Item 组后续重跑的无错误 SQL 替代集见 [sql_rerun_20261118](item_property_recalculation_248c7f7c227e/sql_rerun_20261118/)。该替代集保留历史 `sql/` 与旧执行证据不变；本轮 5 个脚本父/目标各执行三轮，15 组比较均无观察差异。

## 结果解释

- 字符集 T1、T4：每个脚本的第一个 SELECT 带显式字符集前缀，父子一致；**第二个无前缀 SELECT** 在父提交返回两行，在目标提交为空。这里保存实际执行的完整原始 SQL，没有删除对照或改写字节。T3 在 UTF-8 SQL 字节流中执行 `SET NAMES latin1`，两侧为空不能视为敏感条件已成功落实。
- Item T1、T2：目标查询和保存的优化器 trace 均无父子差异。T3–T5 的 `IS NULL(expression)` 产生 MySQL 1064 语法错误；`--force` 使后续对照 SELECT 仍有输出，XML 可解析及退出码为零不表示目标查询成功。这三条没有经过人工修复或重跑。
- 窗口 T1：`o=5` 的 AVG 父提交为 `45.0000`，目标为 `60.0000`。T2：`o=4/5` 为 `18.0000/19.6667` 对 `36.0000/29.5000`；T3：`o=5` 为 `9.0000` 对 `12.0000`；T4：分区 1 的 `o=4` 为 `400.0000` 对 `600.0000`。T5 的 MIN/MAX 无差异。模型输出中的部分预期值和触发位置推断有误，判定应以 SQL 语义和原始执行证据为准。

未执行源码插桩，不能据结果差异宣称已直接观测目标分支、确认独立根因或发现新漏洞。源码选取和提交说明已有人工目标信息，不属于盲测；五个输出也不等于五个不同机制。本归档保留失败、未解决的假设和模型解释错误。

## 文件和追溯

每个目标的 `generation/` 包含实际 Stage1/Stage2 API 请求、原始响应、Stage1 交接、最终 SQL 输出，以及从实际请求导出的完整提示词与可填充模板。`source/` 保留另外两组提示词的源码选取材料；字符集源码已完整嵌入 Stage1 请求。`sql/` 保存服务器接收的原始 SQL 字节；`evidence/sql_N/{parent,target}/` 保存每轮 stdout XML、stderr 和历史结果 JSON。

各目标 `summary.json` 从保存的 XML、stderr 离线重新解析，校验 SQL、stdout、stderr 哈希，并明确把 SQL 错误排除于有效的差异结论。`*.original.json` 和 `history/` 保留历史结果原貌，不悄悄覆盖历史判定。run_023 历史 runner 的错误提取正则过度转义，错误列表为空；本归档通过原始 stderr 纠正该分类，历史文件保持原字节。

[provenance.json](provenance.json) 记录原件和归档映射、原字节 SHA256 及排除清单；[integrity.json](integrity.json) 记录发布文件的 SHA256。服务器初始化日志、数据库目录、镜像、压缩包、凭据和依赖本机路径的执行程序不上传。

历史执行环境为 Linux x86_64、Docker、MySQL 8.0.32-tr/相应提交构建。历史 runner 使用隔离容器（无网络、2 CPU、3 GiB 内存）、UTF-8 客户端、socket 连接以及 `--xml --force --binary-mode --comments`。每个完整脚本轮次使用新连接及 schema。字符集记录校验了 mysqld SHA256；run_023 保存了 runtime 路径和提交标识，但 runner 未实际执行二进制哈希校验，不能把该部分当成重新验证的构建证明。更多会话信息见各侧 `result.original.json`。

离线检查（不调用模型或数据库）：

```powershell
py -3.13 -X utf8 -B experiments/latest_two_stage_commits_20261112/verify_archive.py
py -3.13 -X utf8 -B scripts/check_offline.py
py -3.13 -X utf8 -B scripts/audit_repository.py
```
