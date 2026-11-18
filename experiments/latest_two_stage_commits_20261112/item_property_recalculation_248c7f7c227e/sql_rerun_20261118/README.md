# Item SQL rerun

这组 SQL 替代上一组生成脚本作为当前无错误候选集。上一组 `sql/` 及其父/目标执行证据保留在原路径，旧哈希不改写。

- run: `run_026_item_rerun_20261118`
- target: `248c7f7c227e76f3422378ca3b9e10d141dcfc86`
- parent: `15980860ac2639f41dfbda2f7fffb7aeeab32921`
- 文件：`sql_1.sql` 至 `sql_5.sql`
- 执行：父/目标各 3 轮，共 30 次完整脚本执行
- 结果：15 组父/目标比较全部 `no_observed_difference`；SQL 错误、XML 解析失败和非零退出码均为 0

本轮 Stage2 请求模型为 `deepseek-v4-flash`，响应模型字段为 `deepseek-flash`，因此按流程标记为模型身份未接受。SQL 和执行证据仍完整保留，不能据此确认或排除独立缺陷。

完整 run 记录见 `experiments/two_stage_remaining_commits_20261112/executed_runs/run_026_item_rerun_20261118/`。
