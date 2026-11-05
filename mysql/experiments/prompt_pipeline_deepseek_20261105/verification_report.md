# MySQL 三组两阶段提示词重跑与提交对照验证

日期：2026-11-05（Asia/Shanghai）

## 执行口径

按归档输入逐组重跑两阶段流程：阶段一请求 `deepseek-v4-pro`，阶段二请求 `deepseek-v4-flash`。阶段一使用 2026-11-04 实验归档中的原始 `src2req` 输入；阶段二使用同一输入包中的 `req2test` 模板和示例，只将当前组的新阶段一输出填入需求位置。三组之间没有共享模型对话历史。参数为 `temperature=0.7`、`max_tokens=16384`、`thinking=disabled`。请求、完整响应、阶段二提示词、SQL 和 SHA256 均保存在本目录。

输入包来自 `mysql_bugs_test` Git 提交 `00fcb55c1b43140835bcd65d4c7349532ed1fda3`；归档 `SHA256SUMS.txt` 中的 22 个条目全部通过核验。最终批次 6 次模型调用均完成。另有一次早期参数不完整的试跑，保留于 `../run_001/output/`，因参数不一致且未完成三组而不纳入本报告。

模型接口返回的阶段一模型名均为 `deepseek-v4-pro`。阶段二请求名为 `deepseek-v4-flash`，但接口响应名为 `deepseek-flash`；同一时点的模型目录只列出 `deepseek-flash` 与 `deepseek-v4-pro`。因此本记录保留用户指定的请求模型名和接口返回名，不声称已独立确认 `deepseek-flash` 的版本别名。

## 服务器验证

使用服务器上已核验的父提交和目标提交构建。每份 SQL 在每侧各运行三轮，每轮使用新 schema；原始 SQL 未修补。MySQL 客户端以 XML 模式执行完整脚本，逐轮保存 XML、stderr 和返回码。

| 组 | 父提交 / 目标提交 | 运行结果 |
|---|---|---|
| 条件下推与字符集 | `e248166db3c95b4fc998ca14cff914f1fdafbe7b` / `4d2da251cb536340d19438cc0039bb2846f9a634` | 两侧均返回两组相同的 4 行结果；三轮一致 |
| Item 属性重算 | `15980860ac2639f41dfbda2f7fffb7aeeab32921` / `248c7f7c227e76f3422378ca3b9e10d141dcfc86` | 两侧均返回两组相同的 5 行结果；三轮一致 |
| 窗口帧状态 | `74c7ccfa27f482576412300e5f92fd3dbeb54cfa` / `c296cddb93ffc631f9b43d3b1ff769604e7469d7` | 两侧均返回相同的 8 行结果；三轮一致 |

合计 18 次完整脚本执行、9 组逐轮父/目标配对比较。所有执行返回码为 0，所有 XML 均成功解析，没有 SQL 错误；9 组比较均为 `no_observed_difference`。结果与各阶段二响应中根据输入数据推导的预期行一致。

第一次启动尝试因容器缺少构建目录中的 `libprotobuf-lite.so.3.19.4` 而失败，SQL 未执行。此启动失败单独保存在 `startup_failure_run_002/`。后续重跑按原运行环境将对应 build 目录以只读方式挂载后成功；失败容器和最终运行容器均已移除，最终远端数据目录已清空，远端结果与日志目录保留。

## 结果边界

这次验证表明生成的三份 SQL 在所测精确提交构建上都可执行，且父提交与目标提交没有观察到结果、错误或退出码差异。没有做源码断点或分支插桩，因此无法确认 SQL 是否触及改动代码路径；零差异不能解释为目标代码没有缺陷。

生成 SQL 与原机制目标仍有明显距离：字符集组用 ASCII 常量 `_utf8mb4'alpha'`，不是含非 ASCII 字面量的行依赖表达式；Item 组测试窗口 `SUM` 参数中的 `IN` 子查询及存储函数，但没有原例中的预处理语句重复执行；窗口组采用 `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`，其结果正常且没有跨提交差异。它们的通过执行不能代替目标分支覆盖证据。

## 证据

- `run_manifest.json`：输入、请求参数、模型返回名、哈希及执行汇总。
- `<目标名>/stage1_request.json`、`stage1_response_raw.json`、`stage1_output.txt`：阶段一完整记录。
- `<目标名>/stage2_prompt.txt`、`stage2_request.json`、`stage2_response_raw.json`、`stage2_output.txt`、`generated.sql`：阶段二完整记录和 SQL。
- `server_evidence/summary.json`：逐组配对比较与二进制 SHA256。
- `server_evidence/results/<目标名>/<parent|target>/`：每轮原始 XML、stderr 和结果元数据。
- `server_evidence/logs/`：容器日志和服务器错误日志。
- `startup_failure_run_002/`：首次缺依赖启动失败证据，未纳入 SQL 执行统计。
- `../run_001/output/`：参数未冻结的部分试跑，未纳入本报告结论。


## Public archive notes

This repository copy preserves the model requests/responses, source input bundle,
generated SQL, successful parent/target result metadata, client XML, stderr, and
comparison summaries. The originating checkout path was redacted. Raw container
and server logs, remote transfer metadata, the remote runner script, and the
initial startup-failure batch are not included because they contain machine or
server location details; their relative names and SHA256 values are recorded in
export_manifest.json. The initial startup failure ran no SQL; the successful
verification batch is the evidence summarized above.
