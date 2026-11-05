# 数据字典与统计边界

`task_id` 是报告编号 × 目标版本的唯一键；`report_id` 指 bugs.mysql.com 报告。`target_version` 为待核版本。`official_version_field` 保存官方 Version 字段；`version_match` 保存精确匹配证据。字段命中是纳入候选的标准，不等于确认该版本有缺陷。

cases/report_version_items.json 将冻结的 scope_items.json 与 current_results.json 按 task_id 联结；current_category 保留 reproduced、not_reproduced、other_anomaly、inconclusive、not_executed、execution_failed。executed 是独立执行标志，inconclusive 不能自动视为未执行。remaining_reasons 保留条件不足、失败与未知。

旧 category 索引已冻结到 experiments/baseline_20261029/boundary_items.json，保留 6/5/95 与当时零新增 SQL 的口径。当前 cases/version_boundary_items.json 使用 boundary_status：observed_new_at_release=15、pre_existing=91、unknown=0。execution_status 区分 completed_and_adjudicated=95 与 historical_comparable_pair_reused=11。new_actual_runs=95、new_attempt_records=97；2 条未提交 SQL 的失败尝试保留，重试新增 2 次执行已经包含在 95 次中，不能再相加。新增执行仅各 1 次；106 项涉及 99 报告，仍非独立根因数。

完整字段、case.json、oracle、requirements、source anchors 和脚本哈希保留于 experiments/saved_20261029。output、sql_preparation_20261028 含历史探索集合，不能直接合并到 895 项官方 Version 主集合。source_snapshot_sha256 指原始材料，不是整理后文件哈希。

`<USER_HOME>`、`<EXPERIMENT_ROOT>` 为脱敏的历史定位信息，不可直接执行。原始位置以 ORIGINAL_PROJECT 加迁移/排除清单中的相对路径还原。原件仍在原项目；仓库外缺失材料不得虚称已随仓库分发。
