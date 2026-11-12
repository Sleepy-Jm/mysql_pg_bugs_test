# 两阶段生成与执行反馈

Stage1 与 `two_stage_path_and_failure_20261112` 逐字节一致。Stage2 增加执行反馈输入，用已执行的 SQL 指导下一批生成；不增加第三个分析阶段。

## 使用顺序

1. Stage1 分析源码，得到本次构造依据。
2. 将实际输出填入 Stage2 的 `{{STAGE1_OUTPUT}}`。
3. 首轮没有反馈时，将 `initial_execution_feedback.txt` 全文填入 `{{EXECUTION_FEEDBACK}}`。
4. 运行 Stage2 候选并核对实际证据，按 `execution_feedback_template.md` 记录可复用样例。它是空白记录格式，不是真实成功样例。
5. 下一轮仍使用 Stage2，把上述记录及完整实测 SQL 填入 `{{EXECUTION_FEEDBACK}}`，指导下一批生成。保留已有样例身份与证据，不把新变体自动标成成功。

`feedback_pipeline.py` 已接入执行结果目录作为离线适配器。它不启动数据库，也不调用模型；现有父/子提交执行器完成运行后，用它读取归档证据、分类样例，并生成下一轮 Stage2 请求。

## 执行后的自动回填

执行器应将每条 SQL 保存为 `sql_1.sql` ... `sql_5.sql`，并将配对结果保存为 `server_evidence/results/sql_N/`。如果有源码插桩、EXPLAIN/trace 或独立 oracle 结果，写入一个 observations JSON；其中 `path.evidence_files` 和 `oracle.evidence_files` 必须是运行目录内的相对路径。

```text
py -3.13 -X utf8 -B feedback_pipeline.py collect <run_dir> --observations <observations.json> --output-dir <feedback_dir>
py -3.13 -X utf8 -B feedback_pipeline.py prepare <stage1_output.txt> <feedback_dir>/feedback.json --output-dir <next_stage2_dir>
```

`collect` 会把完整 SQL、SQL 哈希、父/目标 revision、三轮执行摘要和证据文件哈希写入 `feedback.json`/`feedback.md`。`prepare` 将这份记录自动插入 Stage2 的 `{{EXECUTION_FEEDBACK}}`，同时插入当前 Stage1 输出；仍只生成 Stage2 请求，不把执行反馈变成第三个模型阶段。

只有下列情况会进入下一轮样例：

- `PATH_REACHED`：path status 为 `confirmed`，且存在哈希可核验的路径证据；表示目标对象进入了修改路径，不表示发生异常。
- `ANOMALY_OBSERVED`：独立 oracle 明确给出 expected/observed，状态为 anomaly/runtime_anomaly，且存在哈希可核验的结果证据；路径和归因仍单独记录。

父子结果不同但没有独立 oracle 或路径证据时，自动记为排除项；SQL 错误、建表失败和环境失败也不会被伪装成目标异常。两个标签可以同时写入同一个样例。新一轮生成的 SQL 不继承样例的成功标签，必须重新执行。

## 两种样例标签

| 标签 | 依据 | 后续用途 |
| --- | --- | --- |
| PATH_REACHED | 实测确认目标对象进入修改路径或相关分支 | 保留已验证的路径构造，继续探索有源码依据的敏感输入 |
| ANOMALY_OBSERVED | 实测结果违背独立正确预期，或记录到待分析的运行时异常 | 在证据允许范围内保留异常构造，探索边界、变体与对照 |

两个标签可以同时存在。异常样例还必须分别注明路径是否确认、是否已归因到目标变更；出现异常不自动证明目标路径或根因。仅父子输出不同仍是待调查差异，语法/建表等生成或环境失败不作为目标异常成功样例。

五条差异化目标测试要求继续保留：复用样例时说明其编号、保留的已证实关系、每条新 SQL 验证的不同假设，避免只围绕一个未经证实前提变换写法。新 SQL 仍需重新执行验证。

## 不变与新增

- Stage1、源码、diff、commit message 和注释不变。
- Stage2 的原有三个输出部分、无关示范、目标元数据保留；新增反馈说明和 `{{EXECUTION_FEEDBACK}}` 输入，并在角色与候选来源中接入反馈。
- 未填入本案例任何历史手工复现 SQL 或触发答案，也没有把历史未观测路径的 SQL 标为成功。
- Stage2 模板为 6,857 字节。

本次只生成提示词与反馈记录格式，未启动模型或数据库实验。
