# PostgreSQL SQL/oracle 与回放进度

快照 UTC：2026-11-05T04:09:16.257254+00:00。这是进行中的统计，非全部回放完成报告。

|版本|Version字段入选项|已整理脚本/步骤与oracle|已执行目标项|已执行相邻项|
|---|---:|---:|---:|---:|
|14.1|49|26|26|52|
|14.2|42|19|19|38|
|17.1|4|1|1|2|
|17.2|41|21|23|46|

17428 的展示换行修订保留原 oracle；旧尝试以 superseded 标记单独统计，不覆盖原证据。

SQL 片段、操作步骤、场景、报告与执行次数分别统计。配置/网络/客户端测试不是全部由SQL构成；目录片段数量不是SQL语句数。复现报告现象不等于确认独立bug。

```json
{
  "snapshot_utc": "2026-11-05T04:09:16.257254+00:00",
  "report_count": 136,
  "prepared_reports": 67,
  "all_attempts": 226,
  "superseded_attempts": 19,
  "current_attempts": 207,
  "target_attempts": 69,
  "adjacent_attempts": 138,
  "target_statuses": {
    "reproduced": 62,
    "not_reproduced": 2,
    "inconclusive": 4,
    "other_anomaly": 1
  },
  "all_statuses": {
    "reproduced": 167,
    "not_reproduced": 20,
    "inconclusive": 18,
    "other_anomaly": 2
  }
}
```

## 对应文件

- [逐项准备与执行清单](preparation_inventory.csv)
- [来源审查与具体缺口](source_audit.csv)
- [冻结报告及 Version 字段](frozen_reports.json)
- [实际执行快照](execution_snapshot.json)
- [脚本及冻结 oracle](prepared/)
- [原报告文字](source_text/)
- [官方讨论串](thread_text/)
- [附件及来源哈希](materials/manifest.json)

服务器原始尝试、日志和数据库目录：`/mnt/sdb/dufei/pg_report_replay_20261104_run001/attempts/`。SQL提取失败、环境缺失和观察不完整不得算作有效未复现。
