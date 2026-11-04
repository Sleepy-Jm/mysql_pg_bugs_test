# MySQL 源码提示词输入

这些文件从工作区已保存的源码上下文中提取目标提交的 after 侧节选；保留上游行号、revision、blob SHA 和公开 URL。不是完整函数或完整调用图。出处详情见 [provenance.json](provenance.json)。当前网络未能重新读取 raw.githubusercontent.com，因此该文件中的 `upstream_verified: false` 表示本次未重新在线核验上游 blob，并非已完成独立校验。

| 输入 | 原分析标识 | 上游固定提交 |
|---|---|---|
| `intersect_join.txt` | C01，`mysql_commit_requirements_50` 保存的源码上下文 | [fac72fe1704c](https://github.com/mysql/mysql-server/commit/fac72fe1704c542ba476ef065dee03d2c1da83ae) |
| `partition_pruning_lock_state.txt` | C04，`mysql_commit_requirements_v3` 保存的源码上下文 | [cb98e45d2fb7](https://github.com/mysql/mysql-server/commit/cb98e45d2fb75f67c2e65cbf8862d512e98ccce8) |
| `window_avg_frame_count.txt` | C17，`mysql_commit_requirements_v3` 保存的源码上下文 | [b6cb5560cc46](https://github.com/mysql/mysql-server/commit/b6cb5560cc46eac38af15b0a9f3a9852038aaea4) |

生成提示词只依赖本仓库内的节选，不依赖原工作区路径。`Requirements` 的两个种子需求依据 C04/C17 v3 分析重新整理，保留源码条件与候选 SQL 映射的区别。主提示词不包含原 commit 标题、bug 报告或已有回归测试；此设计仅说明提供给模型的内容，不宣称历史分析过程是严格盲测。

MySQL 源码节选及其在生成提示词中的副本保留 Oracle 和原贡献者的权利，适用上游 MySQL Server 的许可证及文件声明，参见 [上游 LICENSE](https://github.com/mysql/mysql-server/blob/fac72fe1704c542ba476ef065dee03d2c1da83ae/LICENSE) 和各文件原始头部。这些节选没有被重新许可为本项目自有代码。
