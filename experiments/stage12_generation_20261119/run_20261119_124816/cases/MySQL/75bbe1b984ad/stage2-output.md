## T1
依据 1.3：`Item_in_subselect::exec()` 中 `null_value`/`was_null` 重置条件由 `is_executed() && engine->uncacheable()` 改为仅 `is_executed()`。差异只在“子查询已执行过、`unit->uncacheable == 0`、且走 `SubqueryWithResult`（非 index_subquery / hash_sj）”时出现。本测试用外层两行、内层含 NULL 且无匹配，使第一次执行产生 `was_null=true`，第二次左表达式不同且未命中 `left_expr_cache`，从而暴露重置差异。与其他测试的差异：唯一直接针对 NULL 标志重置的测试。

```sql
-- 准备
DROP TABLE IF EXISTS t1_outer, t1_inner;
CREATE TABLE t1_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t1_inner (k INT, PRIMARY KEY(k));
INSERT INTO t1_outer VALUES (1, 10), (2, 20);
INSERT INTO t1_inner VALUES (30), (NULL);

-- 目标：外层两行，IN 子查询对每行重执行；内层含 NULL 且无匹配
-- 期望：两行都不满足 IN（NULL 语义），结果为空集
SELECT id, v FROM t1_outer
WHERE v IN (SELECT k FROM t1_inner)
ORDER BY id;

-- 对照：显式展示每行 IN 的布尔/UNKNOWN 语义
SELECT id, v,
       (v IN (SELECT k FROM t1_inner)) AS in_result
FROM t1_outer
ORDER BY id;

-- 清理
DROP TABLE t1_outer, t1_inner;
```

预期结果：目标 SELECT 返回空集（两行 `v=10`、`v=20` 均不在 `{30, NULL}` 中，IN 结果为 UNKNOWN，WHERE 过滤掉）。对照 SELECT 返回两行，`in_result` 均为 NULL。若新版本在第二次执行时错误清除 `was_null`，第二行可能被误判为 FALSE 而非 UNKNOWN——但 WHERE 过滤下 FALSE 与 UNKNOWN 都排除，故需对照 SELECT 才能观察到差异。仍需以后验证：`SubqueryWithResult` 路径下 `was_null` 是否确实在第一次执行后为 true，以及 `left_expr_cache` 是否在 `v` 变化时未命中。

## T2
依据 1.4：`is_uncacheable()` 改用 `unit->uncacheable`，使非相关 materialized IN 子查询的 `used_tables_cache` 可能被清除外层 const table 位。本测试构造外层 const table + 非相关 IN 子查询，通过结果集核对是否因依赖位变化导致行被错误过滤或重复。与其他测试的差异：聚焦 `update_used_tables` 对 const table 依赖的影响，而非 NULL 标志。

```sql
-- 准备
DROP TABLE IF EXISTS t2_outer, t2_inner, t2_const;
CREATE TABLE t2_const (c INT PRIMARY KEY);
CREATE TABLE t2_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t2_inner (k INT, PRIMARY KEY(k));
INSERT INTO t2_const VALUES (1);
INSERT INTO t2_outer VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t2_inner VALUES (10), (30);

-- 目标：外层含 const table，非相关 IN 子查询
-- 期望：id=1 与 id=3 满足 IN，id=2 不满足
SELECT o.id, o.v
FROM t2_const c, t2_outer o
WHERE o.v IN (SELECT k FROM t2_inner)
ORDER BY o.id;

-- 对照：去掉 const table，验证 IN 语义本身
SELECT o.id, o.v
FROM t2_outer o
WHERE o.v IN (SELECT k FROM t2_inner)
ORDER BY o.id;

-- 清理
DROP TABLE t2_const, t2_outer, t2_inner;
```

预期结果：目标 SELECT 返回 `(1,10)` 和 `(3,30)` 两行；对照 SELECT 返回相同两行。若 `used_tables_cache` 被错误清除导致 const table 依赖丢失，可能出现行重复（const table 与外层笛卡尔积被错误折叠）或行丢失。仍需以后验证：该查询是否实际走 materialization/hash_sj 引擎，以及 `update_used_tables` 是否在优化阶段被调用。

## T3
依据 1.2 / 2.3：`subselect_hash_sj_engine::setup()` 中 `result` 来自 `subselect_indexsubquery_engine` 的成员，且 `cleanup()` 不再调用 `materialize_engine->cleanup()`。本测试用外层多行触发 hash semi-join 多次执行，内层含 NULL，核对聚合值与行数是否符合 IN 语义。与其他测试的差异：聚焦 materialization 引擎的 setup/cleanup 生命周期，而非 NULL 标志或依赖位。

```sql
-- 准备
DROP TABLE IF EXISTS t3_outer, t3_inner;
CREATE TABLE t3_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t3_inner (k INT, PRIMARY KEY(k));
INSERT INTO t3_outer VALUES (1, 10), (2, 20), (3, 30), (4, 40);
INSERT INTO t3_inner VALUES (10), (30), (NULL);

-- 目标：外层多行，非相关 IN 子查询，倾向 materialization
-- 期望：id=1 与 id=3 满足；id=2、id=4 因 NULL 语义为 UNKNOWN 被排除
SELECT o.id, o.v
FROM t3_outer o
WHERE o.v IN (SELECT k FROM t3_inner)
ORDER BY o.id;

-- 对照：聚合值核对
SELECT COUNT(*) AS matched
FROM t3_outer o
WHERE o.v IN (SELECT k FROM t3_inner);

-- 清理
DROP TABLE t3_outer, t3_inner;
```

预期结果：目标 SELECT 返回 `(1,10)` 和 `(3,30)` 两行；对照 SELECT 返回 `matched=2`。若 cleanup 未正确补偿导致第二次执行状态残留，可能出现行数偏差或 NULL 语义错误。仍需以后验证：该查询是否被优化器选择为 materialization + hash semi-join（需 EXPLAIN 确认），以及 `unit->is_prepared()` 在 setup 时的状态。

## T4
依据 1.6：`Item_subselect::cleanup()` 去掉 `old_engine` 恢复机制，`indexsubquery_engine` 销毁后置空。本测试用 prepared statement 多次 EXECUTE，使同一 IN 子查询 item 经历多次 cleanup 与重执行，核对每次结果一致。与其他测试的差异：唯一针对 prepared statement 重执行路径的测试。

```sql
-- 准备
DROP TABLE IF EXISTS t4_outer, t4_inner;
CREATE TABLE t4_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t4_inner (k INT, PRIMARY KEY(k));
INSERT INTO t4_outer VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t4_inner VALUES (10), (30);

-- 目标：prepared statement 多次执行，IN 子查询走 index_subquery
PREPARE stmt FROM
  'SELECT o.id, o.v FROM t4_outer o WHERE o.v IN (SELECT k FROM t4_inner) ORDER BY o.id';

EXECUTE stmt;
EXECUTE stmt;
EXECUTE stmt;

DEALLOCATE PREPARE stmt;

-- 对照：一次性执行
SELECT o.id, o.v FROM t4_outer o
WHERE o.v IN (SELECT k FROM t4_inner)
ORDER BY o.id;

-- 清理
DROP TABLE t4_outer, t4_inner;
```

预期结果：三次 EXECUTE 均返回 `(1,10)` 和 `(3,30)` 两行，与对照 SELECT 一致。若 cleanup 后 `indexsubquery_engine` 未正确恢复导致第二次执行走错误路径，可能出现结果偏差或错误。仍需以后验证：该查询是否实际走 `index_subquery`（需 EXPLAIN 确认），以及 prepared statement 重执行时 `unit->item` 是否被复用。

## T5
依据 1.1：`replace_index_subquery()` 中 `change_engine()` 改为 `set_indexsubquery_engine()`，不再保存 `old_engine`。本测试用带索引内层表的单表 IN 子查询，配合外层多行，核对 `unique_subquery` / `index_subquery` 路径下的结果集与聚合值。与其他测试的差异：聚焦 index_subquery 引擎替换本身，而非 NULL 标志、依赖位或 cleanup。

```sql
-- 准备
DROP TABLE IF EXISTS t5_outer, t5_inner;
CREATE TABLE t5_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t5_inner (k INT, PRIMARY KEY(k));
INSERT INTO t5_outer VALUES (1, 10), (2, 20), (3, 30), (4, 40), (5, 50);
INSERT INTO t5_inner VALUES (10), (30), (50);

-- 目标：单表内层 + 主键索引，倾向 unique_subquery
-- 期望：id=1、3、5 满足
SELECT o.id, o.v
FROM t5_outer o
WHERE o.v IN (SELECT k FROM t5_inner)
ORDER BY o.id;

-- 对照：聚合值
SELECT COUNT(*) AS matched, SUM(o.v) AS sum_v
FROM t5_outer o
WHERE o.v IN (SELECT k FROM t5_inner);

-- 清理
DROP TABLE t5_outer, t5_inner;
```

预期结果：目标 SELECT 返回 `(1,10)`、`(3,30)`、`(5,50)` 三行；对照 SELECT 返回 `matched=3, sum_v=90`。若引擎替换导致 `old_engine` 缺失影响后续清理或重执行，可能出现结果偏差。仍需以后验证：该查询是否实际走 `unique_subquery`（需 EXPLAIN 确认），以及 `set_indexsubquery_engine` 后 `Item_subselect::cleanup()` 的行为是否与旧 `old_engine` 恢复等价。

---

**缺口说明**：依据 1.5（`Item_subselect::init()` 中旧 item 已有 `indexsubquery_engine`）未构造独立测试，因为交接文档明确该场景“是否可由公开 SQL 触发尚不清楚”，缺少可复现的 SQL 入口证据，无法在不引入外部假设的前提下构造有源码依据的测试。其余五个测试分别覆盖 NULL 标志重置、依赖位更新、materialization 生命周期、prepared statement 重执行、index_subquery 引擎替换，操作数关系与执行分支互不重复。