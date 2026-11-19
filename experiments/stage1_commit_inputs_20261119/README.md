# Stage 1 引入提交输入集

MySQL、PostgreSQL（PG）和 SQLite 各 4 个引入提交，共 12 份输入。本批只归档材料，尚未运行 Stage 1。

[模型输入](model-inputs)按数据库和引入提交编号保存，每个 Markdown 文件是一份完整输入。[取材说明](selection-notes)使用同样的目录和文件名，供研究者核对版本、选段和输入哈希。MySQL、PG 的文件名使用上游 Git 提交前缀，SQLite 使用 Fossil check-in 前缀。

| 数据库 | 案例 | 引入提交 | 模型输入 | 取材说明 |
|---|---|---|---|---|
| MySQL | #103331 / Oracle #32773801 | 75bbe1b984ad | [输入](model-inputs/MySQL/75bbe1b984ad.md) | [说明](selection-notes/MySQL/75bbe1b984ad.md) |
| MySQL | Oracle #33603911 | e48f7df66539 | [输入](model-inputs/MySQL/e48f7df66539.md) | [说明](selection-notes/MySQL/e48f7df66539.md) |
| MySQL | Oracle #32193123 | 396c83fd995b | [输入](model-inputs/MySQL/396c83fd995b.md) | [说明](selection-notes/MySQL/396c83fd995b.md) |
| MySQL | #118033 / Oracle #37864937 | 410f5267d414 | [输入](model-inputs/MySQL/410f5267d414.md) | [说明](selection-notes/MySQL/410f5267d414.md) |
| PG | #17335 | 8edd0e79460b | [输入](model-inputs/PG/8edd0e79460b.md) | [说明](selection-notes/PG/8edd0e79460b.md) |
| PG | #18522 / #18526 | 16dc2703c541 | [输入](model-inputs/PG/16dc2703c541.md) | [说明](selection-notes/PG/16dc2703c541.md) |
| PG | #19533 | 9d9c02ccd1ae | [输入](model-inputs/PG/9d9c02ccd1ae.md) | [说明](selection-notes/PG/9d9c02ccd1ae.md) |
| PG | #18771 / #19425 | 30a53b792959 | [输入](model-inputs/PG/30a53b792959.md) | [说明](selection-notes/PG/30a53b792959.md) |
| SQLite | 多列 IN 连接漏行 | c9a3498113074bbc | [输入](model-inputs/SQLite/c9a3498113074bbc.md) | [说明](selection-notes/SQLite/c9a3498113074bbc.md) |
| SQLite | 视图计数优化 | d1ba200234f40b84 | [输入](model-inputs/SQLite/d1ba200234f40b84.md) | [说明](selection-notes/SQLite/d1ba200234f40b84.md) |
| SQLite | 复合查询的行数限制 | 4b631364354068af | [输入](model-inputs/SQLite/4b631364354068af.md) | [说明](selection-notes/SQLite/4b631364354068af.md) |
| SQLite | 十进制文本与浮点转换 | 761d8fd18b0ee868 | [输入](model-inputs/SQLite/761d8fd18b0ee868.md) | [说明](selection-notes/SQLite/761d8fd18b0ee868.md) |
