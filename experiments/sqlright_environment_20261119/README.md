# SQLRight 环境核验

2026-11-19 在项目服务器的三个 Linux amd64 镜像中进行了启动检查。三套 SQLRight 前端均能显示 2.56b 的用法，所查前端和数据库可执行文件的动态依赖均齐全。SQLite 使用内存数据库，MySQL 和 PostgreSQL 使用各自的临时数据目录和专用套接字。三者的 `SELECT 6*7` 均返回 `42`。

| 后端 | 镜像中实测的数据库版本 | 镜像内 inputs / 上游文件数 | 比对结果 |
|---|---|---:|---|
| MySQL | 8.0.32-tr，镜像标注的目标提交为 `4d2da251cb53`，解析器基线为 8.0.27 | 111 / 110 | 110 个同名文件均仅有 LF 与 CRLF 差异。另外有一份历史 LLM 种子 `llm_latest_plain_cafe_distinct_dcp_off.sql`。 |
| PostgreSQL | 14.0 | 305 / 305 | 文件名、内容字节全部一致。 |
| SQLite | 3.34.0 | 116 / 116 | 文件名、内容字节全部一致。单次覆盖采集对相同的算术查询收到了 3,982 个覆盖图条目。 |

默认语料以 [SQLRight 上游提交 9457f031](https://github.com/PSU-Security-Universe/sqlright/tree/9457f0311b70562a3423ee86ac7e2ebdaaa6664b) 的对应目录为准。MySQL 对照组需从该提交提取干净语料。表中数量是目录文件数，入队、被选为父本、产生变异的数量须在预实验中另行测量。

| 后端 | 本次检查的镜像 ID |
|---|---|
| MySQL | `sha256:70a12f7bd7e48744570d4b6d947290a90312c9a8d6c45363063020ddd549f3a7` |
| PostgreSQL | `sha256:c81460ccb000a9ab2c667db1a3060f93e7f95d4a488b425507ac16f9ddc1a246` |
| SQLite | `sha256:437ff3867d91ff697b6225201c91623d20dbc2714973942ddefb3b0eb2578b9f` |

本次核验覆盖预装版本。三个拟选目标在精确历史提交上的 SQLRight 在线运行、默认组与加种子组的 A/B 结果均待测。[已有 SQL 的直接执行结果](../stage12_execution_20261119/README.md)
