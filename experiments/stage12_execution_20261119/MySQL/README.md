# MySQL 原始 SQL 执行结果

20 份生成 SQL 在 16 个精确 Git 提交上完成 240 轮执行，**4 个指定的错误结果缺陷均未获确认**。16 份脚本在其全部版本、全部轮次成功，共 192 轮。其余 4 份在全部版本均报错，共 48 轮。原始 SQL 字节、提交身份、构建指纹和每轮结果均已通过离线核验。[生成记录](../../stage12_generation_20261119/run_20261119_124816/README.md) · [核验报告](verification.json)

## 各目标结果

每个目标含 5 份脚本，在引入父提交、引入提交、修复父提交、修复提交上各执行三轮。表中次数按脚本轮次计算。

| 上游报告与引入提交 | 成功 | 报错 | 结果与归因 |
|---|---:|---:|---|
| #32193123 · `396c83fd995b` | 36 | 24 | T1、T2 在四个版本均因 `ONLY_FULL_GROUP_BY` 返回 1055。T3–T5 的输出在两个边界均相同，符合手算结果。T4 三组均满足 HAVING 条件，T5 的累计和按最终输出顺序是 100、150、30。[原始回执](evidence/396c83fd995b/intro/results.json) · [上游修复](https://github.com/mysql/mysql-server/commit/01668774ade2b5a7c8f050fa63bf6fa7afdc55ba) |
| #118033 / #37864937 · `410f5267d414` | 60 | 0 | T2 在引入边界出现可重复的数值变化，修复前后相同。测试观察到 DECIMAL 除法写入 DOUBLE 的精度变化。上游修复针对优化器在比较谓词中替换小数位较多的常量，本组脚本没有展示该谓词返回错误行。[原始 T2](../../stage12_generation_20261119/run_20261119_124816/cases/MySQL/410f5267d414/sql/T2.sql) · [上游修复](https://github.com/mysql/mysql-server/commit/4cff988dbe41a626c1070545d4de4ecbc2d5a63d) |
| #103331 / #32773801 · `75bbe1b984ad` | 36 | 24 | T1、T3 在准备数据时向非空主键插入 NULL，四个版本均报 1048，目标 SELECT 未执行。T2、T4、T5 在两个边界均得到预期匹配行，未观察到报告中的子查询 NULL 真值丢失。[原始错误](evidence/75bbe1b984ad/intro/T1-1.stderr.txt) · [上游修复](https://github.com/mysql/mysql-server/commit/10c953537ab16aacd21e3f8bb19a509d516f35e5) |
| #33603911 · `e48f7df66539` | 60 | 0 | 五份脚本在两个边界的值与行序均相同，未出现聚合漏行。T3 的目标计数和去重长度和为 `(4,3)`，对照为 `(5,6)`，两条查询对 NULL 和去重的处理可解释该差别。T5 的二进制分组键已从原始 XML 字段无损还原并核对。[原始回执](evidence/e48f7df66539/fix/results.json) · [上游修复](https://github.com/mysql/mysql-server/commit/cf599696f2660273139b57e242d78faac6257338) |

## DECIMAL T2 的四个版本

T2 分别将 `1.00 / 3.00`、`2.00 / 3.00` 和 `5.00 / 3.00` 的结果存入字符列和 DOUBLE 列。下表列出第二条 SELECT 中的 DOUBLE 值。每组值的三轮结果完全一致。

| 版本 | 1/3 | 2/3 | 5/3 |
|---|---:|---:|---:|
| [引入前](evidence/410f5267d414/intro-parent/T2-1.xml) | 0.3333333333333333 | 0.6666666666666666 | 1.6666666666666667 |
| [引入后](evidence/410f5267d414/intro/T2-1.xml) | 0.333333 | 0.666667 | 1.666667 |
| [修复前](evidence/410f5267d414/fix-parent/T2-1.xml) | 0.333333 | 0.666667 | 1.666667 |
| [修复后](evidence/410f5267d414/fix/T2-1.xml) | 0.333333 | 0.666667 | 1.666667 |

第一条 SELECT 的输出以及第二条 SELECT 的字符列，在四个版本中均显示六位小数。40 个脚本级父子边界中，31 个边界成功完成且行值、行序相同，8 个边界的两侧均因同一 SQL 错误退出，只有上述引入边界出现行值变化。

## 复核

在本目录运行 `python verify.py --output verification.json`。192 个成功轮次中，120 轮与完整手算结果匹配，48 轮核对了指定列，24 轮按记录的数值容差核对。原始查询没有请求逐语句的服务器警告列表。[判读说明](oracle-notes.md) · [完整版本表](plan.json) · [构建记录](build-records.json) · [原始 SQL 哈希](input-hashes.json) · [执行器](execute.py) · [核验器](verify.py)
