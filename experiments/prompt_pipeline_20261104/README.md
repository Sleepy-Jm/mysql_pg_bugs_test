# 三组提示词到 SQL 与精确提交实测（2026-11-04）

三组均已在目标提交和其直接父提交上实际运行，每个版本三轮，共 18 次完整脚本运行、150 次检查点观测。父提交全部符合原预期；目标提交的 8 个检查点稳定出现错误结果，共 24 次失败观测。没有 SQL ERROR、超时、崩溃或 OOM。失败检查点数不是独立缺陷数。

| 组 | 父提交每轮通过 | 目标提交每轮通过 | 结论 |
|---|---|---|---|
| 派生表条件下推与字符集 | `e248166db3c9`：8/8 | `4d2da251cb53`：7/8 | 三轮稳定错误结果 |
| Item 属性重算 | `15980860ac26`：8/8 | `248c7f7c227e`：6/8 | 三轮稳定错误结果 |
| 窗口帧状态 | `74c7ccfa27f4`：9/9 | `c296cddb93ff`：4/9 | 三轮稳定错误结果 |

- [详细实测报告](runtime/final_report.txt)：错误行、对照条件和判定范围。
- [逐项比较](runtime/comparison.json) / [150 次观测 CSV](runtime/case_results.csv)。
- [端到端对应关系](lineage.json)：六个阶段输入输出、源码提交、case_id、每轮运行文件及 SHA256。
- [导出来源与原件/脱敏件哈希](export_manifest.json)：包含未入库日志的路径标识、哈希和排除原因。

## 按目标阅读完整链

### 派生表条件下推与字符集：`derived_condition_charset_4d2da251cb53`

[源码分析提示词](generation/input_bundle/Prompts/mysql/src2req/derived_condition_charset_4d2da251cb53.txt) → [实际分析输出](generation/stage1_src2req/derived_condition_charset_4d2da251cb53.txt) → [测试生成提示词](generation/stage2_req2test/prompts/derived_condition_charset_4d2da251cb53.txt) → [完整测试响应](generation/stage2_req2test/responses/derived_condition_charset_4d2da251cb53.txt) → [SQL](generation/sql/derived_condition_charset_4d2da251cb53.sql) → [预期 JSON](generation/expected/derived_condition_charset_4d2da251cb53.json)

执行结果：[父提交](runtime/results/derived_condition_charset_4d2da251cb53/parent/result.json) / [目标提交](runtime/results/derived_condition_charset_4d2da251cb53/target/result.json)。逐轮原始 XML 和 stderr 在相同目录。

### Item 属性重算：`item_property_recalculation_248c7f7c227e`

[源码分析提示词](generation/input_bundle/Prompts/mysql/src2req/item_property_recalculation_248c7f7c227e.txt) → [实际分析输出](generation/stage1_src2req/item_property_recalculation_248c7f7c227e.txt) → [测试生成提示词](generation/stage2_req2test/prompts/item_property_recalculation_248c7f7c227e.txt) → [完整测试响应](generation/stage2_req2test/responses/item_property_recalculation_248c7f7c227e.txt) → [SQL](generation/sql/item_property_recalculation_248c7f7c227e.sql) → [预期 JSON](generation/expected/item_property_recalculation_248c7f7c227e.json)

执行结果：[父提交](runtime/results/item_property_recalculation_248c7f7c227e/parent/result.json) / [目标提交](runtime/results/item_property_recalculation_248c7f7c227e/target/result.json)。逐轮原始 XML 和 stderr 在相同目录。

### 窗口帧状态：`window_frame_state_c296cddb93ff`

[源码分析提示词](generation/input_bundle/Prompts/mysql/src2req/window_frame_state_c296cddb93ff.txt) → [实际分析输出](generation/stage1_src2req/window_frame_state_c296cddb93ff.txt) → [测试生成提示词](generation/stage2_req2test/prompts/window_frame_state_c296cddb93ff.txt) → [完整测试响应](generation/stage2_req2test/responses/window_frame_state_c296cddb93ff.txt) → [SQL](generation/sql/window_frame_state_c296cddb93ff.sql) → [预期 JSON](generation/expected/window_frame_state_c296cddb93ff.json)

执行结果：[父提交](runtime/results/window_frame_state_c296cddb93ff/parent/result.json) / [目标提交](runtime/results/window_frame_state_c296cddb93ff/target/result.json)。逐轮原始 XML 和 stderr 在相同目录。

## 目录与历史快照

`generation/` 原样保存生成阶段的输入包、两阶段实际输出、SQL、预期值和构建/静态验证程序。生成阶段由同一助手完成，两阶段共享对话上下文，没有调用独立模型 API；不能称为隔离双模型或盲测实验。

实际第二阶段输入是 `generation/stage2_req2test/prompts/`，已填入本次 `stage1_src2req/` 输出。`generation/input_bundle/Requirements/` 和其中旧 `req2test/` 是原包种子，供追溯，不是实际执行链采用的分析答案。原模板固定于 `fadce4b`；不静默替换成仓库随后修改的模板。

`generation/generation_manifest.json`、其 README 和静态验证记录中的 `database_executed=false` 是生成时的历史状态。运行状态以 `runtime/` 和本索引为准。`runtime/final_report.txt` 中“未提交到 GitHub”描述报告形成时的状态，本次归档才将其提交。

`runtime/` 保留六个版本的精简构建身份、执行命令/环境、18 份小型客户端 XML 与错误流、逐行比较及执行时审计。构建大日志、服务日志、数据库目录、镜像和压缩包不入库；日志原件以导出清单中的哈希追踪。原生成文件、SQL、预期 JSON 和客户端输出字节不变。执行元数据、报告及归档脚本中的个人服务器目录替换为 `/EXPERIMENT_ROOT`、`/CACHE_ROOT`，原/导出哈希分别保存；不得拿导出哈希替代历史运行哈希。

`runtime/runner.py`、build/server/prepare 脚本仅为执行代码存档，含脱敏占位符，不是现行数据库入口；导入 runner 只用于离线 XML 比较。该 runner 当时未先提交 Git，故运行代码 commit 明记 unknown，通过原始脚本 SHA256 追踪；本次归档 commit 不能冒充运行前 commit。Item 两个版本复用已核验无补丁缓存，其他四个版本从精确提交增量构建。完整 SQL 每轮在一个新连接、新 schema 内执行，每个版本三轮共用一个隔离服务器进程，均为 Release 构建。

## 离线复核

在本目录运行（Python 标准库，不连接服务器、不执行数据库）：

```shell
python -X utf8 -B verify.py
```

核对导出文件哈希、提示词填充、响应 SQL 字节、输入/预期哈希、六个构建与运行的对应关系，再从 18 份原始输出重算 150 个检查点。可选的 `generation/validate.py` 依赖 SQLGlot 30.17.0，用于从 INSERT 数据重新推导 oracle；它会写回生成阶段静态验证文件，审计归档时无需运行它。

本实验单列，不修改已有 895 项报告集合、106 项历史复现统计或 15 项版本边界统计。结果没有源码分支插桩证据，也未验证 Debug 断言；同组多个失败检查点不能直接计为多个独立缺陷。
