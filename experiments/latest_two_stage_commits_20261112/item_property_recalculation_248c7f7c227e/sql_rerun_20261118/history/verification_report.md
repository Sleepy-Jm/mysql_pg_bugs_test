# Item 重跑验证报告

- run_id: `run_026_item_rerun_20261118`
- target: `248c7f7c227e76f3422378ca3b9e10d141dcfc86`
- parent: `15980860ac2639f41dfbda2f7fffb7aeeab32921`
- Stage1: `deepseek-v4-pro`
- Stage2 requested: `deepseek-v4-flash`, thinking disabled; response reported `deepseek-flash`
- 执行：5 个完整 SQL 脚本，父/目标各 3 轮，共 30 次完整脚本执行

| 脚本 | 三轮父/目标比较 | SQL 错误 | XML | 退出码 |
|---|---|---:|---|---|
| T1 | 3/3 `no_observed_difference` | 0 | 全部 ok | 全部 0 |
| T2 | 3/3 `no_observed_difference` | 0 | 全部 ok | 全部 0 |
| T3 | 3/3 `no_observed_difference` | 0 | 全部 ok | 全部 0 |
| T4 | 3/3 `no_observed_difference` | 0 | 全部 ok | 全部 0 |
| T5 | 3/3 `no_observed_difference` | 0 | 全部 ok | 全部 0 |

结论仅表示这次生成的五个候选在指定父/目标构建和数据下没有观察到差异；没有插桩，因此不能据此判断内部 `Item` 属性更新分支是否被直接命中，也不等同于缺陷确认。

按仓库的模型追溯规则，Stage2 返回的模型标识与请求不一致，因此候选生成不计为已接受结果。原始请求、响应和 SQL 均保留；上表仅报告这些 SQL 的执行观察，不把它们作为已通过模型身份校验的候选结论。

原始请求、响应、SQL、stdout/stderr、版本元数据和逐轮比较结果位于同目录的 `item_property_recalculation_248c7f7c227e/` 与 `server_evidence/`。
