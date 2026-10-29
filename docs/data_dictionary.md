# 数据字典与统计边界

`task_id` 是报告编号 × 目标版本的唯一键；`report_id` 指 bugs.mysql.com 报告。`target_version` 为待核版本。`official_version_field` 保存官方 Version 字段；`version_match` 保存精确匹配证据。字段命中是纳入候选的标准，不等于确认该版本有缺陷。

cases/report_version_items.json 将冻结的 scope_items.json 与 current_results.json 按 task_id 联结；current_category 保留 reproduced、not_reproduced、other_anomaly、inconclusive、not_executed、execution_failed。executed 是独立执行标志，inconclusive 不能自动视为未执行。remaining_reasons 保留条件不足、失败与未知。

cases/version_boundary_items.json 的 category 为 new_at_release、pre_existing、evidence_insufficient。6 项仅表示已保存两侧证据支持前版正常/目标异常，不能据此定位引入提交。5 项前版同异常、95 项未知，本阶段新增 SQL 执行为 0。106 项涉及 99 报告，并非根因去重后的缺陷数。

完整字段、case.json、oracle、requirements、source anchors 和脚本哈希保留于 experiments/saved_20261029。output、sql_preparation_20261028 含历史探索集合，不能直接合并到 895 项官方 Version 主集合。source_snapshot_sha256 指原始材料，不是整理后文件哈希。

`<USER_HOME>`、`<EXPERIMENT_ROOT>` 为脱敏的历史定位信息，不可直接执行。原始位置以 ORIGINAL_PROJECT 加迁移/排除清单中的相对路径还原。原件仍在原项目；仓库外缺失材料不得虚称已随仓库分发。
