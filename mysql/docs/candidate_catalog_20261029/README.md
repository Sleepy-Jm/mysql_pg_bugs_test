# 候选项与 SQL 内容目录（2026-10-29）

从仓库已有证据离线整理，源基线提交 `b74ebe19359a2d0a1e70e359084981076406685e`。

| 资料 | 项数 | 不同 bug 编号数 | 格式 |
|---|---:|---:|---|
| [895 项候选总表](candidates_895.md) | 895 | 858 | [CSV](candidates_895.csv) · [JSON](candidates_895.json) |
| [125 项目标版本已执行候选及 SQL](executed_125.md) | 125 | 118 | [CSV](executed_125.csv) · [JSON](executed_125.json) |
| [106 项报告现象复现 SQL](reproduced_106.md) | 106 | 99 | [CSV](reproduced_106.csv) · [JSON](reproduced_106.json) |
| [15 项前版正常、目标异常 SQL](boundary_new_15.md) | 15 | 15 | [CSV](boundary_new_15.csv) · [JSON](boundary_new_15.json) |

| 目标版本 | 候选 | 已执行 | 现象复现 | 前版正常、目标异常 |
|---|---:|---:|---:|---:|
| 8.0.32 | 299 | 36 | 32 | 11 |
| 8.0.33 | 242 | 32 | 30 | 4 |
| 8.0.34 | 196 | 25 | 20 | 0 |
| 8.0.35 | 158 | 32 | 24 | 0 |

## 阅读与口径

- 候选内容包含标题、官方 Version 字段、报告链接、当前状态、阶段、结论或待处理原因；895 项中 770 项未执行，保留缺正文、失败和未知。本次不抓取或补写缺失的官方报告全文。
- 125 项包含 215 次目标执行；当前类别为 106 项 reproduced、12 项 execution_failed、4 项 other_anomaly、2 项 inconclusive、1 项 not_reproduced。已执行不等于已复现。
- 106 项指报告现象复现，涉及 99 个 bug 编号；15 项表示保存的严格相邻版本观察，涉及 15 个 bug 编号，并非确认了 15 个新漏洞或独立根因，也未定位引入提交。
- 独立 SQL 分别在 [已执行](sql/executed_125)、[复现](sql/reproduced_106)、[前版正常、目标异常](sql/boundary_new_15) 目录；后三组 Markdown 均内嵌完整默认 SQL 内容。每个文件按 task_id 命名。
- 独立 SQL 是保存的输入脚本，逐字节复制，不添加头注释或拼接成可批量执行脚本；Markdown 内嵌展示统一使用 LF 换行，精确字节以独立 SQL 为准。runner 的 USE/会话前导和 postcheck 并不全部包含于 source SQL，具体以 JSON 中的原始执行记录及原始 manifest/oracle 为准。
- 同一候选有多个已执行输入时，默认展示按开始时间排序的最后一个，所有变体和全部记录均保留。Bug 119646 / 8.0.33 有两个输入，已执行目录因此有 126 个 SQL 文件；复现和边界目录各为 106、15 个。
- 相邻版本所用 source.sql 已与展示的目标 SQL 逐项核对哈希。跨目录同一 task_id 的默认 SQL 完全相同；不对不同版本的同 bug 去重或合并。
- CSV 使用 UTF-8 BOM；所有 CSV SQL 路径相对于本目录，JSON 同样如此。JSON 内 source、evidence_file、record_references 和 boundary 的证据路径相对于仓库根目录。原始哈希和导出文件哈希分别保留。
- [输入及导出 SQL 哈希](provenance.json) 和 [汇总](summary.json) 用于核查；历史材料中的代码提交未知时仍为 unknown，不以本次整理提交冒充历史实验代码。

## 更新与检查

在仓库根目录执行（离线，不运行数据库）：

```powershell
python -X utf8 -B scripts/build_candidate_catalog.py
python -X utf8 -B scripts/build_candidate_catalog.py --check
python -X utf8 -B scripts/check_offline.py
python -X utf8 -B scripts/audit_repository.py
python -X utf8 -B scripts/audit_latest_boundary.py
```
