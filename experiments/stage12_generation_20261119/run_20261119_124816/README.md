# DeepSeek 两阶段 SQL 生成记录

运行标识为 run_20261119_124816。仅使用已归档的 12 份模型输入。Stage 1 的完整可见回答插入同一案例的 Stage 2 模板。两个阶段均未使用数据库执行反馈。

Stage 1 使用 deepseek-v4-pro，温度 0.3。Stage 2 使用 deepseek-flash，温度 0.2，并显式关闭思考。模型返回名称和用量记录在每例回执中。官方已将旧别名 deepseek-v4-flash 的请求交由当前 Flash 服务处理。[模型说明](https://api-docs.deepseek.com/quick_start/pricing/)

冻结输入提交为 52c57a9dc837e78b40cd401ef453521766774948。[查看输入集](../../stage1_commit_inputs_20261119/README.md) · [查看 Stage 2 模板](stage2-template.md) · [查看运行清单](run.json)

| 数据库 | 案例 | 引入提交 | Stage 1 分析 | Stage 2 原始回答 | SQL 脚本 |
|---|---|---|---|---|---|
| MySQL | #103331 / Oracle #32773801 | 75bbe1b984ad | [分析](cases/MySQL/75bbe1b984ad/stage1-output.md) | [回答与预期结果](cases/MySQL/75bbe1b984ad/stage2-output.md) | [T1](cases/MySQL/75bbe1b984ad/sql/T1.sql) · [T2](cases/MySQL/75bbe1b984ad/sql/T2.sql) · [T3](cases/MySQL/75bbe1b984ad/sql/T3.sql) · [T4](cases/MySQL/75bbe1b984ad/sql/T4.sql) · [T5](cases/MySQL/75bbe1b984ad/sql/T5.sql) |
| MySQL | Oracle #33603911 | e48f7df66539 | [分析](cases/MySQL/e48f7df66539/stage1-output.md) | [回答与预期结果](cases/MySQL/e48f7df66539/stage2-output.md) | [T1](cases/MySQL/e48f7df66539/sql/T1.sql) · [T2](cases/MySQL/e48f7df66539/sql/T2.sql) · [T3](cases/MySQL/e48f7df66539/sql/T3.sql) · [T4](cases/MySQL/e48f7df66539/sql/T4.sql) · [T5](cases/MySQL/e48f7df66539/sql/T5.sql) |
| MySQL | Oracle #32193123 | 396c83fd995b | [分析](cases/MySQL/396c83fd995b/stage1-output.md) | [回答与预期结果](cases/MySQL/396c83fd995b/stage2-output.md) | [T1](cases/MySQL/396c83fd995b/sql/T1.sql) · [T2](cases/MySQL/396c83fd995b/sql/T2.sql) · [T3](cases/MySQL/396c83fd995b/sql/T3.sql) · [T4](cases/MySQL/396c83fd995b/sql/T4.sql) · [T5](cases/MySQL/396c83fd995b/sql/T5.sql) |
| MySQL | #118033 / Oracle #37864937 | 410f5267d414 | [分析](cases/MySQL/410f5267d414/stage1-output.md) | [回答与预期结果](cases/MySQL/410f5267d414/stage2-output.md) | [T1](cases/MySQL/410f5267d414/sql/T1.sql) · [T2](cases/MySQL/410f5267d414/sql/T2.sql) · [T3](cases/MySQL/410f5267d414/sql/T3.sql) · [T4](cases/MySQL/410f5267d414/sql/T4.sql) · [T5](cases/MySQL/410f5267d414/sql/T5.sql) |
| PG | #17335 | 8edd0e79460b | [分析](cases/PG/8edd0e79460b/stage1-output.md) | [回答与预期结果](cases/PG/8edd0e79460b/stage2-output.md) | [T1](cases/PG/8edd0e79460b/sql/T1.sql) · [T2](cases/PG/8edd0e79460b/sql/T2.sql) · [T3](cases/PG/8edd0e79460b/sql/T3.sql) · [T4](cases/PG/8edd0e79460b/sql/T4.sql) · [T5](cases/PG/8edd0e79460b/sql/T5.sql) |
| PG | #18522 / #18526 | 16dc2703c541 | [分析](cases/PG/16dc2703c541/stage1-output.md) | [回答与预期结果](cases/PG/16dc2703c541/stage2-output.md) | [T1](cases/PG/16dc2703c541/sql/T1.sql) · [T2](cases/PG/16dc2703c541/sql/T2.sql) · [T3](cases/PG/16dc2703c541/sql/T3.sql) · [T4](cases/PG/16dc2703c541/sql/T4.sql) · [T5](cases/PG/16dc2703c541/sql/T5.sql) |
| PG | #19533 | 9d9c02ccd1ae | [分析](cases/PG/9d9c02ccd1ae/stage1-output.md) | [回答与预期结果](cases/PG/9d9c02ccd1ae/stage2-output.md) | [T1](cases/PG/9d9c02ccd1ae/sql/T1.sql) · [T2](cases/PG/9d9c02ccd1ae/sql/T2.sql) · [T3](cases/PG/9d9c02ccd1ae/sql/T3.sql) · [T4](cases/PG/9d9c02ccd1ae/sql/T4.sql) · [T5](cases/PG/9d9c02ccd1ae/sql/T5.sql) |
| PG | #18771 / #19425 | 30a53b792959 | [分析](cases/PG/30a53b792959/stage1-output.md) | [回答与预期结果](cases/PG/30a53b792959/stage2-output.md) | [T1](cases/PG/30a53b792959/sql/T1.sql) · [T2](cases/PG/30a53b792959/sql/T2.sql) · [T3](cases/PG/30a53b792959/sql/T3.sql) · [T4](cases/PG/30a53b792959/sql/T4.sql) · [T5](cases/PG/30a53b792959/sql/T5.sql) |
| SQLite | 多列 IN 连接漏行 | c9a3498113074bbc | [分析](cases/SQLite/c9a3498113074bbc/stage1-output.md) | [回答与预期结果](cases/SQLite/c9a3498113074bbc/stage2-output.md) | [T1](cases/SQLite/c9a3498113074bbc/sql/T1.sql) · [T2](cases/SQLite/c9a3498113074bbc/sql/T2.sql) · [T3](cases/SQLite/c9a3498113074bbc/sql/T3.sql) · [T4](cases/SQLite/c9a3498113074bbc/sql/T4.sql) · [T5](cases/SQLite/c9a3498113074bbc/sql/T5.sql) |
| SQLite | 视图计数优化 | d1ba200234f40b84 | [分析](cases/SQLite/d1ba200234f40b84/stage1-output.md) | [回答与预期结果](cases/SQLite/d1ba200234f40b84/stage2-output.md) | [T1](cases/SQLite/d1ba200234f40b84/sql/T1.sql) · [T2](cases/SQLite/d1ba200234f40b84/sql/T2.sql) · [T3](cases/SQLite/d1ba200234f40b84/sql/T3.sql) · [T4](cases/SQLite/d1ba200234f40b84/sql/T4.sql) · [T5](cases/SQLite/d1ba200234f40b84/sql/T5.sql) |
| SQLite | 复合查询的行数限制 | 4b631364354068af | [分析](cases/SQLite/4b631364354068af/stage1-output.md) | [回答与预期结果](cases/SQLite/4b631364354068af/stage2-output.md) | [T1](cases/SQLite/4b631364354068af/sql/T1.sql) · [T2](cases/SQLite/4b631364354068af/sql/T2.sql) · [T3](cases/SQLite/4b631364354068af/sql/T3.sql) · [T4](cases/SQLite/4b631364354068af/sql/T4.sql) · [T5](cases/SQLite/4b631364354068af/sql/T5.sql) |
| SQLite | 十进制文本与浮点转换 | 761d8fd18b0ee868 | [分析](cases/SQLite/761d8fd18b0ee868/stage1-output.md) | [回答与预期结果](cases/SQLite/761d8fd18b0ee868/stage2-output.md) | [T1](cases/SQLite/761d8fd18b0ee868/sql/T1.sql) · [T2](cases/SQLite/761d8fd18b0ee868/sql/T2.sql) · [T3](cases/SQLite/761d8fd18b0ee868/sql/T3.sql) · [T4](cases/SQLite/761d8fd18b0ee868/sql/T4.sql) · [T5](cases/SQLite/761d8fd18b0ee868/sql/T5.sql) |

## 脚本运行条件

逐行检查脚本后发现 1 份原始输出含客户端命令。对于通过驱动直接发送 SQL 的实验，需要为这些脚本单独处理连接或客户端命令。生成文件保留模型原文。

- [PG 30a53b792959 / T3](cases/PG/30a53b792959/sql/T3.sql) 使用 `\c`。

## 结果

MySQL 4 个案例、20 份脚本，PG 4 个案例、20 份脚本，SQLite 4 个案例、20 份脚本。
共 32 次有记录的 API 尝试，8 次未被采用。提供方已回传的用量合计为 455,194 tokens。生成的 SQL 来源于模型可见回答，保留原字节，包括注释和格式。每个测试的独立预期和运行前提见 Stage 2 原始回答。文件提取、输入出处及交接哈希经过离线复核，本轮未执行 SQL，结果正确性和缺陷命中尚待测量。

运行时间 2026-11-19T04:49:33+00:00 至 2026-11-19T05:09:43+00:00，均为 UTC。记录保留了可见回答、请求设置、响应标识、输入输出哈希与用量。

如需在配置有 DeepSeek 项目凭据的环境中恢复未完成生成，可在此目录运行以下命令。

~~~text
python generate.py --workers 6
~~~

在工作区执行的离线记录校验命令如下。

~~~text
python verify.py
~~~
