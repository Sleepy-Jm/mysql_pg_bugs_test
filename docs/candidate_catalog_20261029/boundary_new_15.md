# 15 项前版正常、目标异常 SQL

[返回目录](README.md)

按目标版本、bug 编号排序；每项为报告 × 目标版本。状态来自保存证据，本次没有运行数据库。

| 候选项 | Bug | 目标版本 | 标题 | 目标执行状态 | 相邻版本状态 | SQL |
|---|---|---|---|---|---|---|
| mysql-109699-8.0.32 | [109699](https://bugs.mysql.com/bug.php?id=109699) | 8.0.32 | utf8mb4 identifiers stopped working since 8.0.32 release | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-109699-8.0.32.sql) |
| mysql-109725-8.0.32 | [109725](https://bugs.mysql.com/bug.php?id=109725) | 8.0.32 | Wrong result for AVG() OVER(ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-109725-8.0.32.sql) |
| mysql-109833-8.0.32 | [109833](https://bugs.mysql.com/bug.php?id=109833) | 8.0.32 | UTF-8 strings are broken when comparing to UNIONs | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-109833-8.0.32.sql) |
| mysql-110005-8.0.32 | [110005](https://bugs.mysql.com/bug.php?id=110005) | 8.0.32 | When using union, when the value of the field in the where condition is Chinese | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110005-8.0.32.sql) |
| mysql-110104-8.0.32 | [110104](https://bugs.mysql.com/bug.php?id=110104) | 8.0.32 | Query exception caused by union in 8.0.32 | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110104-8.0.32.sql) |
| mysql-110375-8.0.32 | [110375](https://bugs.mysql.com/bug.php?id=110375) | 8.0.32 | upgrade mysql from 8.0.29 to 8.0.32，union error | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110375-8.0.32.sql) |
| mysql-110376-8.0.32 | [110376](https://bugs.mysql.com/bug.php?id=110376) | 8.0.32 | upgrade mysql from 8.0.29 to 8.0.32, union error | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110376-8.0.32.sql) |
| mysql-110384-8.0.32 | [110384](https://bugs.mysql.com/bug.php?id=110384) | 8.0.32 | LIKE query on union result with Unicode characters returns no results | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110384-8.0.32.sql) |
| mysql-110521-8.0.32 | [110521](https://bugs.mysql.com/bug.php?id=110521) | 8.0.32 | 8.0.32 subquery with utf8mb4 equal case empty result | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110521-8.0.32.sql) |
| mysql-110709-8.0.32 | [110709](https://bugs.mysql.com/bug.php?id=110709) | 8.0.32 | Chinese query conditions unable to return results correctly | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110709-8.0.32.sql) |
| mysql-111363-8.0.32 | [111363](https://bugs.mysql.com/bug.php?id=111363) | 8.0.32 | If you use "UNION ALL" for items with Japanese double-byte characters in a subqu | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-111363-8.0.32.sql) |
| mysql-110847-8.0.33 | [110847](https://bugs.mysql.com/bug.php?id=110847) | 8.0.33 | Prepared SELECT returns different results on consecutive executions. | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110847-8.0.33.sql) |
| mysql-110983-8.0.33 | [110983](https://bugs.mysql.com/bug.php?id=110983) | 8.0.33 | issue with window functions in stored procedures | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-110983-8.0.33.sql) |
| mysql-112231-8.0.33 | [112231](https://bugs.mysql.com/bug.php?id=112231) | 8.0.33 | Inconsistent result for OVER() when used in stored procedure over InnoDB table | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-112231-8.0.33.sql) |
| mysql-112460-8.0.33 | [112460](https://bugs.mysql.com/bug.php?id=112460) | 8.0.33 | Inconsistent results of SELECT statement with window functions | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/boundary_new_15/mysql-112460-8.0.33.sql) |

## 逐项内容

### mysql-109699-8.0.32 · Bug #109699

utf8mb4 identifiers stopped working since 8.0.32 release

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109699](https://bugs.mysql.com/bug.php?id=109699)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：{"normal": "Exactly one žlutý_😀 row survives equality/GROUP BY/HAVING.", "same_target_anomaly": "The query returns empty.", "case_gates": "utf8mb4 source bytes and connection; derived_condition_pushdown=on.", "unknown": "Syntax/unsupported feature errors, failed setup/postcheck, timeouts/OOM/connection errors, mismatching environment, uncomparable plan or any other unexplained result are unknown; never normal.", "conclusion": "Previous normal plus validated target abnormal => observed_new_at_release; same anomaly on previous => pre_existing; otherwise unknown."}

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109699-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109699-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_109699_8_0_32_target_r3。

[下载独立 SQL](sql/boundary_new_15/mysql-109699-8.0.32.sql)；SHA256：`6d3714af281c13ceb2cff741a4c8b164b2deaf63f5ff76d4b46379ed60c38fee`。

```sql
SET NAMES utf8mb4;
CREATE TABLE `employee` (
  `id` INT UNSIGNED AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) DEFAULT NULL,
  `surname` VARCHAR(255) DEFAULT NULL,
  `retired` TINYINT(1) DEFAULT NULL,
  PRIMARY KEY(`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB;

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (1, 'Oliver', 'Smith', 0);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (2, 'Jack', 'Williams', 1);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (3, 'Harry', 'Taylor', 1);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (4, 'Charlie', 'Lee', 0);

select
  *
from
  (
    select
      'žlutý_😀' `❤`
  ) `🚀`
where
  `❤` = 'žlutý_😀'
group by
  `🚀`.`❤`
having
  (`❤` = 'žlutý_😀');
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_109699_8_0_32_target_r1`，实际版本 8.0.32，completed；[records.jsonl:61](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L61)
- `candidate_109699_8_0_32_target_r2`，实际版本 8.0.32，completed；[records.jsonl:62](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L62)
- `candidate_109699_8_0_32_target_r3`，实际版本 8.0.32，completed；[records.jsonl:63](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L63)

### mysql-109725-8.0.32 · Bug #109725

Wrong result for AVG() OVER(ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109725](https://bugs.mysql.com/bug.php?id=109725)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：{"normal": "Four rows: sums 9,7,4,NULL; counts 3,2,1,0; averages 3,3.5,4,NULL equal SUM/COUNT.", "same_target_anomaly": "Second-row AVG=7 while SUM/COUNT=3.5.", "case_gates": "Four input integers 1..4; div_precision_increment=4.", "unknown": "Syntax/unsupported feature errors, failed setup/postcheck, timeouts/OOM/connection errors, mismatching environment, uncomparable plan or any other unexplained result are unknown; never normal.", "conclusion": "Previous normal plus validated target abnormal => observed_new_at_release; same anomaly on previous => pre_existing; otherwise unknown."}

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109725-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109725-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_109725_8_0_32_target_r3。

[下载独立 SQL](sql/boundary_new_15/mysql-109725-8.0.32.sql)；SHA256：`c99c4e02d242a02a8417c4ad59e0c738268ccea9a25c06d6e0a624cf849dcc9a`。

```sql
SET NAMES utf8mb4;
CREATE TABLE t (
    n INTEGER
);

INSERT INTO t VALUES (1), (2), (3), (4);

SELECT n
     , SUM(n)   OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "sum(n)"
     , COUNT(*) OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "count(n)"
     , AVG(n)   OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "avg(n)"
     , SUM(n)   OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
     / COUNT(*) OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "sum(n)/count(n)"
  FROM t
 ORDER BY n;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_109725_8_0_32_target_r1`，实际版本 8.0.32，completed；[records.jsonl:67](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L67)
- `candidate_109725_8_0_32_target_r2`，实际版本 8.0.32，completed；[records.jsonl:68](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L68)
- `candidate_109725_8_0_32_target_r3`，实际版本 8.0.32，completed；[records.jsonl:69](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L69)

### mysql-109833-8.0.32 · Bug #109833

UTF-8 strings are broken when comparing to UNIONs

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109833](https://bugs.mysql.com/bug.php?id=109833)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 直接查询与 UNION 过滤均返回 ERRÖR 一行且无字符转换警告；8.0.32 UNION 过滤为空并有 1300/1366 警告。源数据 HEX、源 SQL、postcheck、关键环境及 optimizer_switch 相同。支持所记录条件下 8.0.31→8.0.32 行为边界，不证明独立根因。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109833-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109833-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 2 次；下列默认 SQL 对应 target_109833_8_0_32_r2。

[下载独立 SQL](sql/boundary_new_15/mysql-109833-8.0.32.sql)；SHA256：`c2ab8c2e0bb8cda8fba5938660b1026031a012c44e5c89969f542a84b06cb2ff`。

```sql
-- MySQL report #109833; source anchors: cmain, c529335, c529371
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
CREATE TABLE `vals0` (
  `k` VARCHAR(8) CHARSET utf8mb4 COLLATE utf8mb4_bin NOT NULL PRIMARY KEY
);
INSERT INTO `vals0` VALUES ('OK');

CREATE TABLE `vals1` (
  `k` VARCHAR(8) CHARSET utf8mb4 COLLATE utf8mb4_bin NOT NULL PRIMARY KEY
);
INSERT INTO `vals1` VALUES ('ERRÖR');

-- this works as expected
SELECT * FROM `vals1` WHERE `k` = 'ERRÖR';

-- this works as expected
-- Original undefined view_vals control omitted; use the complete derived query below.

-- this returns empty result set, and a warning about converting D6 to utf8
SELECT * FROM (SELECT `v0`.`k` AS `k` FROM `vals0` AS `v0` UNION ALL SELECT `v1`.`k` AS `k` FROM `vals1` as `v1`) AS `a` WHERE `a`.`k` = 'ERRÖR';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_109833_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L6)
- `target_109833_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L2)

### mysql-110005-8.0.32 · Bug #110005

When using union, when the value of the field in the where condition is Chinese

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110005](https://bugs.mysql.com/bug.php?id=110005)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION ALL filtered result empty with conversion warning 1300; postcheck confirms the inserted Chinese name row exists.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 UNION ALL 过滤正确返回两行 (1,姜志福)，8.0.32 空集并有转换警告；两侧源数据控制均为一行 (1,姜志福)，关键环境及 optimizer_switch 相同。仅确认相邻版本现象边界，保留与 #109699 的重复报告关联。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110005-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110005-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110005_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110005-8.0.32.sql)；SHA256：`92a443eb1d53f97e643b57d22d717a4ae07853524bba722568f2a6dff044d77a`。

```sql
CREATE TABLE test (id int unsigned auto_increment key,name varchar(50)) ENGINE=INNODB;
INSERT INTO test(id,name) VALUES(1,'姜志福');
SELECT * FROM (SELECT * FROM test UNION ALL SELECT * FROM test) a WHERE id=1 AND name='姜志福';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110005_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110005-8.0.32/results/records.jsonl#L1)

### mysql-110104-8.0.32 · Bug #110104

Query exception caused by union in 8.0.32

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110104](https://bugs.mysql.com/bug.php?id=110104)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source UNION control returns (5,测试), outer filtered query is empty with warning1300, pushdown-off control restores (5,测试).

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 原始 UNION 控制、外层过滤及 pushdown-off 控制均返回 (5,测试)；8.0.32 中间过滤为空。源数据、关键环境、初始 optimizer_switch 和 SQL 字节一致，满足前版正常目标异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110104-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110104-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110104_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110104-8.0.32.sql)；SHA256：`71734de210b5a41c9acbcc03293d6bbc4ca45683f61b2967465c2dcb937f4c6f`。

```sql
SET NAMES utf8mb4;
CREATE TABLE test_1(id INT,NAME VARCHAR(100));
CREATE TABLE test_2(id INT,NAME VARCHAR(100));
INSERT INTO test_1 VALUES(1,'aaa'),(2,'bbb'),(3,'ccc'),(4,'ddd'),(5,'测试');
INSERT INTO test_2 VALUES(11,'eee');
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp;
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110104_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110104-8.0.32/results/records.jsonl#L1)

### mysql-110375-8.0.32 · Bug #110375

upgrade mysql from 8.0.29 to 8.0.32，union error

官方版本字段：8.0.32 linix-generic

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110375](https://bugs.mysql.com/bug.php?id=110375)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- LIKE Chinese-name filter returns both China and France with conversion warning 1300.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 中文 LIKE 仅返回中国且无转换警告；8.0.32 同一常量源查询错误返回中国、法国并有1300警告。两侧 SQL、UTF8 环境及 optimizer_switch 一致。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110375-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110375-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110375_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110375-8.0.32.sql)；SHA256：`27e05069c1b7dd202709b9327f9c9973f04298f682df9bd7bd4f98ae345fd329`。

```sql
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110375_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110375-8.0.32/results/records.jsonl#L1)

### mysql-110376-8.0.32 · Bug #110376

upgrade mysql from 8.0.29 to 8.0.32, union error

官方版本字段：8.0.32 linix-generic

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110376](https://bugs.mysql.com/bug.php?id=110376)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- LIKE returns China and France initially; pushdown-off returns only China.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 初始 pushdown-on 和 off 控制都仅返回中国；8.0.32 初始错误返回中国、法国，off 才恢复中国。相同 SQL 与关键环境，符合前版正常目标异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110376-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110376-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110376_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110376-8.0.32.sql)；SHA256：`4e613f0b1fbe17c3e3421522d95e3766cab9ea3424322c395e379ff8ab951668`。

```sql
SET NAMES utf8mb4;
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110376_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110376-8.0.32/results/records.jsonl#L1)

### mysql-110384-8.0.32 · Bug #110384

LIKE query on union result with Unicode characters returns no results

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110384](https://bugs.mysql.com/bug.php?id=110384)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Japanese LIKE returns no rows with warning 1300; ASCII value control returns both rows.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 Unicode LIKE 与 ASCII LIKE 控制均返回两个原始名字；8.0.32 Unicode LIKE 空集、ASCII 控制两行且有1300字符转换警告。数据与字符集条件相同。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110384-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110384-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110384_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110384-8.0.32.sql)；SHA256：`a8bb7e34d631b0706918c04bb1ce39f44c528cbc5a9e201a2f9f828919422faf`。

```sql
CREATE TABLE t1 (Name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);
CREATE TABLE t2 (Name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);
INSERT INTO t1(Name) VALUES ('valueテスト');
INSERT INTO t2(Name) VALUES ('テストvalue');
SELECT Name FROM (SELECT Name FROM t1 UNION SELECT Name FROM t2) derived WHERE Name LIKE '%テスト%';
SHOW WARNINGS;
SELECT Name FROM (SELECT Name FROM t1 UNION SELECT Name FROM t2) derived WHERE Name LIKE '%value%';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110384_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110384-8.0.32/results/records.jsonl#L1)

### mysql-110521-8.0.32 · Bug #110521

8.0.32 subquery with utf8mb4 equal case empty result

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110521](https://bugs.mysql.com/bug.php?id=110521)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION equality on Japanese character returns no rows with warning 1300; source-row postcheck succeeds.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 两个查询分别返回 の 与 (1,の)，源数据校验成功、无转换异常；8.0.32 两查询为空且有1300警告，源数据仍存在。符合相邻版本边界。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110521-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110521-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110521_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110521-8.0.32.sql)；SHA256：`5472b343730bedbe7f1624b7e2fc1897935dce97bc571f282dc7843c2052bd13`。

```sql
SELECT * FROM (SELECT "の" AS v) tbl WHERE tbl.v = "の";
SHOW WARNINGS;
CREATE TABLE tbl(id INT PRIMARY KEY,v VARCHAR(30)) DEFAULT CHARSET utf8mb4;
INSERT INTO tbl VALUES (1,'の');
SELECT * FROM (SELECT * FROM tbl UNION SELECT * FROM tbl) t WHERE t.v='の';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110521_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110521-8.0.32/results/records.jsonl#L1)

### mysql-110709-8.0.32 · Bug #110709

Chinese query conditions unable to return results correctly

官方版本字段：MySQL Community Server 8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110709](https://bugs.mysql.com/bug.php?id=110709)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION ALL view filtered result empty initially, pushdown-off returns the one source cow row.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 初始及 pushdown-off 控制均返回唯一 (1,牛)；8.0.32 初始为空，关闭 pushdown 后恢复同一行。相同 source/postcheck 和环境，满足前版正常目标异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110709-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110709-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_110709_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-110709-8.0.32.sql)；SHA256：`6ddde2027837ab32fad197918fcc6eadc4a9199a4196ed340d3eaa006febd523`。

```sql
SET NAMES utf8mb4;
CREATE TABLE TEST_01 (编号 INT(2),动物 VARCHAR(20));
INSERT INTO TEST_01(编号,动物) VALUES(1,'牛');
CREATE TABLE TEST_02 (编号 INT(2),动物 VARCHAR(20));
INSERT INTO TEST_02(编号,动物) VALUES(2,'羊');
CREATE VIEW TEST_V AS SELECT 编号,动物 FROM TEST_01 UNION ALL SELECT 编号,动物 FROM TEST_02;
SELECT * FROM TEST_V WHERE 动物='牛';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM TEST_V WHERE 动物='牛';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110709_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110709-8.0.32/results/records.jsonl#L1)

### mysql-111363-8.0.32 · Bug #111363

If you use "UNION ALL" for items with Japanese double-byte characters in a subqu

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #111363](https://bugs.mysql.com/bug.php?id=111363)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION ALL equality on Japanese あ is empty with warning1300 under initial pushdown=on; disabling pushdown returns two identical source rows.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：两侧初始 derived_condition_pushdown=on 已实测；8.0.31 初始和 off 控制都返回两行 あ，无转换警告；8.0.32 初始空集并有1300警告，off 才恢复两行。支持 8.0.31→8.0.32 行为边界，保留与 #109699 的重复报告关系。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-111363-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-111363-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 1 次；下列默认 SQL 对应 target_111363_8_0_32_r1。

[下载独立 SQL](sql/boundary_new_15/mysql-111363-8.0.32.sql)；SHA256：`208affe805f33811274e0b4ce06d0e2427cf63dbec3715a82153f125621085e2`。

```sql
SET NAMES utf8mb4;
SELECT @@optimizer_switch;
CREATE TABLE TEST01(A VARCHAR(4));
INSERT INTO TEST01(A) VALUES ('あ');
SELECT * FROM (SELECT A FROM TEST01 UNION ALL SELECT A FROM TEST01) SUB WHERE SUB.A='あ';
SHOW WARNINGS;
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT A FROM TEST01 UNION ALL SELECT A FROM TEST01) SUB WHERE SUB.A='あ';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111363_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_005/mysql-111363-8.0.32/results/records.jsonl#L1)

### mysql-110847-8.0.33 · Bug #110847

Prepared SELECT returns different results on consecutive executions.

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110847](https://bugs.mysql.com/bug.php?id=110847)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：Two prepared LAST_VALUE executions over uids 100,101 must both return 1,1. Target second returns NULL,NULL; archived preceding version normal in three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110847/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110847/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_110847_8_0_33_target_r3。

[下载独立 SQL](sql/boundary_new_15/mysql-110847-8.0.33.sql)；SHA256：`c5b3b43bd6f65d90cf5d645eff7ae24d33fea1053da272b85fb4f6d53aed9061`。

```sql
CREATE DATABASE IF NOT EXISTS window_lag_bug;
USE window_lag_bug; 
DROP TABLE IF EXISTS `data_table`;
CREATE TABLE IF NOT EXISTS `data_table` (`uid` INT) ENGINE=InnoDB;
INSERT INTO `data_table` (`uid`) VALUES (100), (101);

PREPARE stmt1 FROM "SELECT (LAST_VALUE(a.`uid`) OVER `outer_window`) = a.`uid` as `result`
FROM 
	(	
		SELECT 
		LAG(`uid`) OVER `inner_window` AS `uid_lag`,
		`uid` AS `uid`
		FROM data_table
		WINDOW `inner_window` AS (ORDER BY `uid`)
	) AS a 
	WINDOW `outer_window` AS (ORDER BY a.`uid`)
";
EXECUTE stmt1;
EXECUTE stmt1;
SELECT VERSION();
DROP DATABASE window_lag_bug;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_110847_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:157](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L157)
- `candidate_110847_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:158](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L158)
- `candidate_110847_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:159](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L159)

### mysql-110983-8.0.33 · Bug #110983

issue with window functions in stored procedures

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110983](https://bugs.mysql.com/bug.php?id=110983)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：Both procedure calls must preserve Aplus=A+1 and Bplus=B+1 on 12 rows. Target second call arithmetic diverges; archived preceding version normal three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110983/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110983/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_110983_8_0_33_target_r3。

[下载独立 SQL](sql/boundary_new_15/mysql-110983-8.0.33.sql)；SHA256：`550eac49593a675f236dad80a3cec1563c59f6747f2a047648558e0eccd6a7fc`。

```sql
CREATE TABLE table1(id INT);
INSERT INTO table1 VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12);
DELIMITER $$
CREATE PROCEDURE test2()
BEGIN
SELECT count(*) over(rows between 5 preceding and 5 following) AS A,
count(*) over(rows between 5 preceding and 5 following)+1 AS Aplus,
count(*) over() AS B, count(*) over()+1 AS Bplus FROM table1;
END$$
DELIMITER ;
CALL test2();
CALL test2();
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_110983_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:166](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L166)
- `candidate_110983_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:167](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L167)
- `candidate_110983_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:168](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L168)

### mysql-112231-8.0.33 · Bug #112231

Inconsistent result for OVER() when used in stored procedure over InnoDB table

官方版本字段：8.0.33, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112231](https://bugs.mysql.com/bug.php?id=112231)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：SUM(1) OVER()+0 must remain 1 on both calls over same single id=1. Target second 2; previous version normal in three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/112231/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/112231/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_112231_8_0_33_target_r3。

[下载独立 SQL](sql/boundary_new_15/mysql-112231-8.0.33.sql)；SHA256：`9f19682601cca5cfe9a5b3b69b4e24e5b7952c95fb7ec7f260e3b5d73e2c912d`。

```sql
DROP TEMPORARY TABLE IF EXISTS tbTestBad2;
CREATE TEMPORARY TABLE tbTestBad2 (id int unsigned) ENGINE InnoDB;
INSERT INTO tbTestBad2 SELECT 1 AS id;

DROP PROCEDURE IF EXISTS spTestBad;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS spTestBad()
  BEGIN
    SELECT 1, (SUM( 1 ) OVER()) + 0 FROM tbTestBad2 ;
    SELECT * FROM tbTestBad2;
  END$$
DELIMITER ;

CALL spTestBad();
CALL spTestBad();
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_112231_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:175](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L175)
- `candidate_112231_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:176](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L176)
- `candidate_112231_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:177](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L177)

### mysql-112460-8.0.33 · Bug #112460

Inconsistent results of SELECT statement with window functions

官方版本字段：8.0.33, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112460](https://bugs.mysql.com/bug.php?id=112460)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：Identical CASE branches must yield c20=17.61 just like direct projection. Target CASE NULL, direct17.61. Previous version normal three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/112460/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/112460/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_112460_8_0_33_target_r3。

[下载独立 SQL](sql/boundary_new_15/mysql-112460-8.0.33.sql)；SHA256：`ec07f399b75c41b712de132bbc2ad717567e88317b1cbf27b8c5d93b80454677`。

```sql


create table t2 (vkey int, pkey int, c19 int, c20 double, c22 int);
insert into t2 values (135, 145000, -13, 17.61, 0);


select  
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0, 
  case when ((LAST_VALUE(ref_0.pkey) over (partition by ref_0.c19 order by ref_0.vkey desc, ref_0.pkey desc)) in (select  
          ref_0.c22 as c_0
        from 
          t2 as ref_8
        )) then ref_0.c20 else ref_0.c20 end
       as c_1 
from 
  t2 as ref_0
order by c_1 desc;
select
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0,
  ref_0.c20 as c_1
from
  t2 as ref_0
order by c_1 desc;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_112460_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:184](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L184)
- `candidate_112460_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:185](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L185)
- `candidate_112460_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:186](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L186)
