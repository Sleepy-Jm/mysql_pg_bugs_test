# mysql_bugs_test

研究从 MySQL 8.0.32 开始各版本的已报告现象，以及相邻小版本新出现的现象。主集合冻结范围为 8.0.32–8.0.35，支持后续逐版本扩展。初始基线整理与同步没有新增 SQL 执行；另行归档的 [三组提示词到精确提交实测](experiments/prompt_pipeline_20261104/README.md) 保存 2026-11-04 已完成的生成与运行证据，不并入历史主集合，也不据此评估整体 LLM 方法效果。

## 提示词生成与提交级实测

[三组完整实验索引](experiments/prompt_pipeline_20261104/README.md) 保留源码提示词、实际分析输出、重新填充的测试提示词、完整测试响应、SQL、预期结果和实测报告之间的对应关系。三组在目标提交及其父提交上各运行三轮，共 18 次脚本运行、150 次检查点观测：父提交全部正确，目标提交分别有 1/8、2/8、5/9 个检查点稳定出现错误结果，无 SQL ERROR、超时或崩溃。失败检查点数不是独立缺陷数，未测量源码分支覆盖。

提示词链与每轮运行的文件、提交和哈希见 [lineage.json](experiments/prompt_pipeline_20261104/lineage.json)，错误行见 [详细报告](experiments/prompt_pipeline_20261104/runtime/final_report.txt)。本次入库仅整理已有运行证据，没有重跑数据库。

## 保存的结果

完整候选内容与 SQL 已整理到 [候选项与 SQL 内容目录](docs/candidate_catalog_20261029/README.md)：包含 895 项候选总表、125 项目标版本已执行候选的 bug 编号与 SQL、106 项复现 SQL、15 项前版正常/目标异常 SQL，均提供 Markdown、CSV、JSON 和独立 SQL 文件。目录保留执行失败、未知及 SQL 输入变体，并可从保存证据离线重新生成。检查结果见 [目录整理验证](docs/catalog_validation_20261029.json)。

| 目标版本 | 候选项 | 已执行项 | 标记复现项 |
|---|---:|---:|---:|
| 8.0.32 | 299 | 36 | 32 |
| 8.0.33 | 242 | 32 | 30 |
| 8.0.34 | 196 | 25 | 20 |
| 8.0.35 | 158 | 32 | 24 |
| 合计 | 895 | 125 | 106 |

770 项未执行。106 项涉及 99 个报告，并非独立根因数或新漏洞数。此前基线边界为 6/5/95，尚无该阶段新增 SQL。最新完成阶段为 **15 项前版正常/目标异常、91 项前版同异常、0 项未知**：新增前版本 SQL 执行 95 次，复用历史两侧证据 11 项。97 条尝试记录包含 2 条未提交 SQL 的启动失败，其后各重试一次成功；新增执行均仅 1 次重复。以上是报告现象的两侧证据，未定位引入提交，也不是 15 个新漏洞。

主集合只含官方 Version 字段明确命中目标版本的 MySQL Server 报告项。历史推断延续项和旧探索集合保留在历史目录，不能混入主测试集。报告 Version 字段、SQL 静态准备、目标现象复现与独立缺陷确认是不同阶段。参见 [目标版本汇总](experiments/baseline_20261029/summary.json)、[相邻版本汇总](experiments/baseline_20261029/boundary_summary.json)、[数据字典](docs/data_dictionary.md)。

最新汇总见 [已完成边界阶段](experiments/boundary_completed_20261029/summary.json)、[逐项结果](cases/version_boundary_items.json) 和 [本次同步验证](docs/latest_validation.json)。旧基线与历史运行保留。

| 目标版本 | 前版正常/目标异常 | 前版同异常 | 未知 | 本阶段新增 SQL | 复用历史两侧证据 |
|---|---:|---:|---:|---:|---:|
| 8.0.32 | 11 | 21 | 0 | 30 | 2 |
| 8.0.33 | 4 | 26 | 0 | 23 | 7 |
| 8.0.34 | 0 | 20 | 0 | 18 | 2 |
| 8.0.35 | 0 | 24 | 0 | 24 | 0 |

## 目录

- [Prompts](Prompts/README.md)：WhiteFox 风格的 MySQL `src2req` / `req2test` 提示词、完整 one-shot 示例和离线生成方式。
- src/mysql_bugs_test：可复用回放、SQL 输出解析与 oracle 模块。
- scripts：离线检查入口。
- tests：迁移的 runner、oracle 和相邻版本契约测试。
- configs：版本清单、run_id/commit/输入/环境追溯模板。
- cases：895 项主集合与 106 项相邻版本索引。
- experiments/baseline_20261029：初次上传的历史汇总，包含旧 6/5/95 边界索引。
- experiments/boundary_completed_20261029：完成后汇总、增量证据及逐文件原始/导出哈希。
- experiments/saved_20261029：按原阶段保留的 SQL、oracle、执行记录与审查依据；其中含不同历史范围，不能合并统计。
- docs：口径、工作流程、迁移映射、原件排除清单。

## 环境与离线检查

本次使用 Python 3.13.5，选定模块仅依赖标准库。Windows 建议显式 -X utf8；若 python 不在 PATH，请换为已安装解释器的绝对路径。在项目根目录运行：

```powershell
python -X utf8 -B scripts/check_offline.py
python -X utf8 -B scripts/audit_repository.py
python -X utf8 -B scripts/audit_latest_boundary.py
python -X utf8 -B src/mysql_bugs_test/run_mysql_batch.py --help
python -X utf8 -B src/mysql_bugs_test/run_reviewed_batch.py --help
python -X utf8 -B src/mysql_bugs_test/run_boundary_core.py --help
```

runner 默认校验并预览，不带 --execute 不运行数据库。例如：

```powershell
python -X utf8 -B src/mysql_bugs_test/run_mysql_batch.py --manifest experiments/saved_20261029/execution/batches/mysql_replay_20261028_a/batch_manifest.json --output local/dryrun
```

真实回放需 Linux/Docker、已有正确版本镜像、隔离环境与资源预算；历史 manifest 可能引用外置证据，须先解析路径、核对输入哈希和环境。脱敏占位符不是执行路径。--execute 会实际运行数据库，本次未执行；历史远程脚本没有作为现行入口搬入。

## 来源与日常管理

[迁移映射](docs/migration_manifest.json) 保存源相对路径、原 SHA256、目标路径与目标 SHA256。[排除清单](docs/excluded_files.json) 保存 HTML、大日志、ZIP/压缩包、二进制、重复交付与历史脚本等原件的路径和哈希。原项目实验原件及 Git 历史未改动。个人绝对路径以占位符替换，SQL 保留原始字节；历史内容经脱敏后文件哈希可能变化，不能用新哈希代替旧执行证据哈希。第三方材料保留原有权利，不擅加许可证。

按明确任务创建分支，完成一个小改动即提交；检查后合并 main。实验使用 run_id 追踪代码提交、输入哈希与环境，参见 [工作流程](docs/workflow.md)。本次的工程离线检查不证明数据库研究效果。具体检查结果与未验证项见 [验证记录](docs/validation.json)。
