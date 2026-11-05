# PostgreSQL 报告重放

冻结收集集合为 **136 份编号报告**：原始 BUG 表单的 PostgreSQL version 字段精确命中 14.1（49）、14.2（42）、17.1（4）、17.2（41）。扫描 pgsql-bugs 2021-11 至 2026-11 月归档，收集截止 2026-11-04；不是所有影响这些版本的缺陷，也不是独立 bug 数。

## 两个统计快照

| 指标 | 67 份历史快照 | 最新补跑结果 |
|---|---:|---:|
| 纳入统计报告 | 136 | 136 |
| 有可执行场景的报告（含 configure） | 67 | 68 |
| 目标版本复现报告现象 | 62 | 63 |
| 有效重放未复现报告 | 2 | 2 |
| 已执行但仍无法判断的报告 | 3 | 3 |
| 尚无可执行场景 | 69 | 68 |
| 场景 × 版本执行项 | 207 | 210 |
| 候选目标小版本引入区间 | 0 | 0 |
| 现象消失边界 | 13 | 13 |

新增报告 **17362**：恢复原文数据、CentOS 7 用户空间、PGDG 14.0/14.1/14.2 RPM 与 ICU 50.2-4.el7_7 后，三个版本均出现原报告错误。Docker 用户空间与原 Vagrant 主机的内核并不相同。首次适配器权限失败未执行 SQL，已保留并由新规格取代。版本字段不是引入版本；此次补跑不支持 14.1 新引入。

## 材料入口

- [136 份报告、版本字段与原文来源](experiments/pg_report_replay_20261104/run_001/frozen_reports.json)
- [136 份报告逐项结果 CSV](experiments/pg_report_replay_20261104/run_001/all_report_results.csv)
- [67 份历史 / 68 份最新可执行报告名单](cases/README.md)
- [最新相邻版本比较报告](experiments/pg_report_replay_20261104/run_001/VERSION_COMPARISON.md)
- [逐场景版本结果 CSV](experiments/pg_report_replay_20261104/run_001/version_comparison.csv)
- [67 份历史快照](experiments/pg_report_replay_20261104/run_001/historical_67_snapshot/VERSION_COMPARISON.md)
- [原 69 份报告逐项缺口、补齐路线及当前状态](experiments/pg_report_replay_20261104/run_001/remaining69_review_20261104/REMAINING_69.md)
- [SQL、来源锚点与冻结 oracle](experiments/pg_report_replay_20261104/run_001/prepared/)
- [有界命令输出与全部尝试记录](evidence/execution_snapshot.compact.json)、[截取规则与原件哈希](evidence/export_notes.json)
- [逐文件哈希及排除清单](publication_manifest.json)

最新剩余 68 份分为：材料不足 32、环境不足 26、非运行时报告 7、静态问题 3。部分需要原作者数据或特殊系统环境，不能编造 SQL 或把这些记录当作有效未复现。

当前 70 个场景包含 1 个 configure 场景，跨相邻版本共 210 项。一个报告可以有多个场景；报告级复现与场景级状态不能相加。消失边界只表示在对应环境和 oracle 下后一版不再出现现象，尚未确认修复提交。没有独立根因去重或新漏洞数结论。

## 使用与证据边界

工具与历史路径以本目录为工作目录（先 `cd pg`）。原始 Windows 路径分隔符和服务器绝对路径保持原样。原始大日志、数据库目录、镜像和压缩附件不入 Git；对应来源、大小、SHA-256 与服务器证据路径保留。`execution_snapshot.compact.json` 是明确标记的有界导出，不能直接作为原始 `execution_snapshot.json` 输入重算。收集范围审计表保留全部扫描记录，但仅随库保存入选 136 份原文网页；其余网页留在原工作区。

离线判定测试：`python -B -m unittest discover -s tests -p "test_*.py"`。服务器 runner 仅作已执行协议的归档；不得因为运行离线测试而自动启动回放。
