# run_023 two-stage remaining commits verification

两组新提示词均完成两阶段调用：Stage1 使用 DeepSeek v4 Pro，Stage2 使用 DeepSeek v4 Flash。首次 Stage2 响应因长度限制为空，随后关闭推理输出重试，两个目标均成功生成 5 个 SQL blocks。

| 目标 | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| item_property_recalculation_248c7f7c227e | 三轮均无父子差异 | 三轮均无父子差异 | 两侧三轮均有 SQL 语法错误 | 两侧三轮均有 SQL 语法错误 | 两侧三轮均有 SQL 语法错误 |
| window_frame_state_c296cddb93ff | 三轮均有父子结果差异 | 三轮均有父子结果差异 | 三轮均有父子结果差异 | 三轮均有父子结果差异 | 三轮均无父子差异 |

## 解释

**item_property_recalculation_248c7f7c227e**：T1、T2 均可执行且父子三轮结果一致。T3、T4、T5 两侧均出现相同的 MySQL 1064 语法错误，原因是模型生成了 `IS NULL(expression)`；MySQL 语法应使用 `expression IS NULL`。这些候选不能用于判断提交差异。

**window_frame_state_c296cddb93ff**：T1–T4 在三轮中均出现稳定父子差异，且无 SQL 错误。差异出现在目标提交的窗口 AVG 结果：例如 T1 的 `o=5`，父提交为 `45.0000`，目标提交为 `60.0000`；T2 的 `o=4/5`、T3 的 `o=5`、T4 的分区 1 `o=4` 也出现对应偏大的 AVG。T5 的 MIN/MAX 对照三轮一致。

这些结果是 SQL 可见的父子行为证据；没有插桩，因此不能仅凭结果断言内部属性更新或窗口状态分支已经被直接观测。

原始证据保存在 `server_evidence/`；每条 SQL、Stage1/Stage2 请求与响应也保存在各目标目录中。
