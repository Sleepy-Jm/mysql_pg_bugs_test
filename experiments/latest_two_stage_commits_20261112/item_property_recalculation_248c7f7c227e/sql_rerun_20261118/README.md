# Item SQL rerun

这组 SQL 替代上一组生成脚本作为当前无错误候选集。上一组 `sql/` 及其父/目标执行证据保留在原路径，旧哈希不改写。

- run: `run_026_item_rerun_20261118`
- target: `248c7f7c227e76f3422378ca3b9e10d141dcfc86`
- parent: `15980860ac2639f41dfbda2f7fffb7aeeab32921`
- 文件：`sql_1.sql` 至 `sql_5.sql`
- 执行：父/目标各 3 轮，共 30 次完整脚本执行
- 结果：15 组父/目标比较全部 `no_observed_difference`；SQL 错误、XML 解析失败和非零退出码均为 0

本轮 Stage2 请求模型为 `deepseek-v4-flash`，响应模型字段为 `deepseek-flash`，因此按流程标记为模型身份未接受。SQL 和执行证据仍完整保留，不能据此确认或排除独立缺陷。

完整可复核归档已保存在本目录：[生成请求与响应](generation/)、[源码输入](source/)、[30 次执行的原始 stdout/stderr 与逐轮回执](evidence/)、[历史 run 清单](history/run_manifest.json)、[历史验证摘要](history/verification_summary.json)和[执行环境与命令选项](execution_environment.json)。本次仅整理 2026-11-18 的已有记录，没有重新调用模型或执行数据库。

[provenance.json](provenance.json) 分别记录本地原件和发布副本的 SHA256。SQL、模型请求与响应、stdout/stderr 保留原字节；历史元数据中的服务器专用路径替换为占位符，原哈希保留。服务器日志、重复的服务器端 SQL 副本和依赖本机路径的历史 runner 保留在本地，排除文件的路径、大小与哈希列在同一清单中。历史执行代码的 Git commit 未记录，保留原有 runner/driver/verifier 文件哈希，不追填归档提交。

历史驱动将模型回答中的 LF SQL 块导出为 CRLF 文件；这里保留实际执行文件的 CRLF 字节与原有哈希，提取一致性按换行归一后的文本核对。执行器使用 `--force`，复核同时检查 stderr、XML 与退出码，确保零退出码没有掩盖 SQL 错误。

离线复核会重新解析全部 XML，核对输入和输出哈希、父/目标版本、三轮稳定性、15 组比较、完整 Stage1 交接及模型身份未接受标记：

```powershell
py -X utf8 -B experiments/latest_two_stage_commits_20261112/item_property_recalculation_248c7f7c227e/sql_rerun_20261118/verify.py
```
