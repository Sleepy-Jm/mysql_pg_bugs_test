## T1
依据：交接指出 `JOIN_RIGHT_ANTI` 在 hash join 匹配分支中不返回元组并继续扫描 bucket，以标记所有匹配的 inner 元组；未匹配 inner 通过 `HJ_FILL_INNER_TUPLES` 以 NULL outer 填充返回。本测试用 `NOT EXISTS` 构造反连接，右表含重复键与 NULL 键，验证“重复匹配全部被标记”与“NULL 键不匹配”的结果集。与其他测试差异：聚焦重复匹配 + NULL 键的基础结果集正确性。

```sql
-- 准备
DROP TABLE IF EXISTS t1_l, t1_r;
CREATE TABLE t1_l (id int, k int);
CREATE TABLE t1_r (id int, k int);
INSERT INTO t1_l VALUES (1,10),(2,20),(3,30),(4,NULL),(5,10);
INSERT INTO t1_r VALUES (100,10),(101,10),(102,20),(103,NULL),(104,40);

-- 目标：反连接，返回 t1_l 中 k 在 t1_r 中无匹配的行
SELECT l.id, l.k
FROM t1_l l
WHERE NOT EXISTS (SELECT 1 FROM t1_r r WHERE r.k = l.k)
ORDER BY l.id;

-- 对照：标准 SQL 等价改写
SELECT l.id, l.k
FROM t1_l l
LEFT JOIN t1_r r ON r.k = l.k
WHERE r.id IS NULL
ORDER BY l.id;

-- 清理
DROP TABLE t1_l;
DROP TABLE t1_r;
```

预期结果：目标 SELECT 返回 `(3,30),(4,NULL),(5,10)`（按 id 排序）。理由：k=10 在右表有匹配（两行重复），k=20 有匹配，k=30 无匹配，k=NULL 因 `=` 对 NULL 不成立而无匹配，k=10 的 l.id=5 有匹配。对照 SELECT 应返回相同三行。仍需以后验证：实际计划是否含 `Right Anti` 节点（需 EXPLAIN 确认），以及 hash join 是否被选中。

## T2
依据：交接指出 `JOIN_RIGHT_ANTI` 在 `match_unsorted_outer` 中禁止 nestloop、merge join 必须使用全部 merge clauses；`select_mergejoin_clauses` 要求非 mergejoinable 且非常量的 join clause 使 mergejoin 不可用。本测试用 `NOT IN` 构造反连接，右表含 NULL 使 `NOT IN` 语义为“空结果”，验证 NULL 语义与反连接路径的交互。与其他测试差异：聚焦 `NOT IN` 的 NULL 三值逻辑边界。

```sql
-- 准备
DROP TABLE IF EXISTS t2_l, t2_r;
CREATE TABLE t2_l (id int, k int);
CREATE TABLE t2_r (id int, k int);
INSERT INTO t2_l VALUES (1,10),(2,20),(3,30);
INSERT INTO t2_r VALUES (100,10),(101,NULL);

-- 目标：NOT IN，右表含 NULL 时整体结果为空
SELECT l.id, l.k
FROM t2_l l
WHERE l.k NOT IN (SELECT r.k FROM t2_r r)
ORDER BY l.id;

-- 对照：右表无 NULL 时的 NOT IN
SELECT l.id, l.k
FROM t2_l l
WHERE l.k NOT IN (SELECT r.k FROM t2_r r WHERE r.k IS NOT NULL)
ORDER BY l.id;

-- 清理
DROP TABLE t2_l;
DROP TABLE t2_r;
```

预期结果：目标 SELECT 返回空集（0 行）。理由：`NOT IN` 子查询含 NULL，`l.k NOT IN (10, NULL)` 对任何 l.k 均为 UNKNOWN，故无行通过。对照 SELECT 返回 `(2,20),(3,30)`。仍需以后验证：planner 是否将含 NULL 的 `NOT IN` 转为反连接（通常不会，因需保留 NULL 语义），以及对照查询是否走 `Right Anti` 路径。

## T3
依据：交接指出 `JOIN_RIGHT_ANTI` 的 hash join 在 `HJ_FILL_INNER_TUPLES` 阶段对未匹配 inner 扫描，且 `ExecHashJoinNewBatch` 在 outer batch 为空时仍扫描 inner；`ExecReScanHashJoin` 重置 match flags。本测试用小 `work_mem` 强制多 batch，右表行数多且未匹配行分布在不同 batch，验证未匹配扫描完整性。与其他测试差异：聚焦批处理 hash join 的未匹配 inner 扫描。

```sql
-- 准备
DROP TABLE IF EXISTS t3_l, t3_r;
CREATE TABLE t3_l (id int, k int);
CREATE TABLE t3_r (id int, k int);
INSERT INTO t3_l VALUES (1,1),(2,2),(3,3);
-- 右表 200 行，k 从 1 到 200，仅 k=1,2,3 匹配左表
INSERT INTO t3_r SELECT g, g FROM generate_series(1,200) g;

-- 目标：反连接，左表 k 在右表无匹配
SET LOCAL work_mem = '64kB';
SELECT l.id, l.k
FROM t3_l l
WHERE NOT EXISTS (SELECT 1 FROM t3_r r WHERE r.k = l.k)
ORDER BY l.id;

-- 对照：标准 SQL 等价改写
SELECT l.id, l.k
FROM t3_l l
LEFT JOIN t3_r r ON r.k = l.k
WHERE r.id IS NULL
ORDER BY l.id;

-- 清理
DROP TABLE t3_l;
DROP TABLE t3_r;
```

预期结果：目标 SELECT 返回空集（0 行）。理由：左表 k=1,2,3 均在右表有匹配，故无未匹配行。对照 SELECT 同样返回空集。仍需以后验证：`work_mem=64kB` 是否实际触发多 batch（需 EXPLAIN ANALYZE 确认 `Batches > 1`），以及 `Right Anti` 计划是否被选中。

## T4
依据：交接指出 `JOIN_RIGHT_ANTI` 的 merge join 要求 extra joinquals 为常量，`EXEC_MJ_ENDOUTER` 阶段对未匹配 inner 做 null-fill；`ExecInitMergeJoin` 初始化 `mj_FillInner=true`。本测试用可排序等值条件 + 常量 true 附加条件，强制 merge join 路径，验证 merge join 的未匹配 inner 填充。与其他测试差异：聚焦 merge join 执行分支与常量 extra qual。

```sql
-- 准备
DROP TABLE IF EXISTS t4_l, t4_r;
CREATE TABLE t4_l (id int, k int);
CREATE TABLE t4_r (id int, k int);
INSERT INTO t4_l VALUES (1,10),(2,20),(3,30),(4,40);
INSERT INTO t4_r VALUES (100,10),(101,20),(102,50),(103,60);

-- 目标：反连接，强制 merge join
SET LOCAL enable_hashjoin = off;
SET LOCAL enable_nestloop = off;
SELECT l.id, l.k
FROM t4_l l
WHERE NOT EXISTS (SELECT 1 FROM t4_r r WHERE r.k = l.k AND true)
ORDER BY l.id;

-- 对照：标准 SQL 等价改写
SELECT l.id, l.k
FROM t4_l l
LEFT JOIN t4_r r ON r.k = l.k
WHERE r.id IS NULL
ORDER BY l.id;

-- 清理
DROP TABLE t4_l;
DROP TABLE t4_r;
```

预期结果：目标 SELECT 返回 `(3,30),(4,40)`。理由：k=10,20 有匹配，k=30,40 无匹配。对照 SELECT 返回相同两行。仍需以后验证：`enable_hashjoin=off, enable_nestloop=off` 是否实际生成 `Right Anti` merge join 计划（需 EXPLAIN 确认），以及常量 `true` 附加条件是否被 planner 保留为 extra qual。

## T5
依据：交接指出 `JOIN_RIGHT_ANTI` 在 `populate_joinrel_with_paths` 的 `JOIN_ANTI` 分支中新增，且 `restriction_is_constant_false` 检查可能提前 `mark_dummy_rel` 导致路径不生成；同时 `ExecReScanHashJoin` 需重置 match flags。本测试将反连接放入嵌套循环内（LATERAL 子查询），验证重扫描时 match flags 重置与结果正确性。与其他测试差异：聚焦重扫描分支与常量 false 条件的交互。

```sql
-- 准备
DROP TABLE IF EXISTS t5_drv, t5_l, t5_r;
CREATE TABLE t5_drv (d int);
CREATE TABLE t5_l (id int, k int);
CREATE TABLE t5_r (id int, k int);
INSERT INTO t5_drv VALUES (1),(2);
INSERT INTO t5_l VALUES (1,10),(2,20),(3,30);
INSERT INTO t5_r VALUES (100,10),(101,20);

-- 目标：LATERAL 内反连接，驱动表两行触发重扫描
SELECT d.d, x.id, x.k
FROM t5_drv d
CROSS JOIN LATERAL (
  SELECT l.id, l.k
  FROM t5_l l
  WHERE NOT EXISTS (SELECT 1 FROM t5_r r WHERE r.k = l.k AND d.d > 0)
) x
ORDER BY d.d, x.id;

-- 对照：标准 SQL 等价改写
SELECT d.d, l.id, l.k
FROM t5_drv d
CROSS JOIN t5_l l
WHERE NOT EXISTS (SELECT 1 FROM t5_r r WHERE r.k = l.k AND d.d > 0)
ORDER BY d.d, l.id;

-- 清理
DROP TABLE t5_drv;
DROP TABLE t5_l;
DROP TABLE t5_r;
```

预期结果：目标 SELECT 返回 4 行：`(1,3,30),(2,3,30)`。理由：对每个 d，反连接返回 l 中 k 无匹配的行，即 k=30 的 l.id=3；d=1 和 d=2 各返回一行，共 2 行。对照 SELECT 返回相同 2 行。仍需以后验证：LATERAL 内反连接是否实际生成 `Right Anti` 计划并被重扫描（需 EXPLAIN 确认），以及 `d.d > 0` 作为相关条件是否影响 planner 对反连接路径的选择。

---

缺口说明：交接中提到的“常量 false 条件导致 `mark_dummy_rel` 提前返回”与“并行 hash/merge join 被禁止”两项，因无法在单条 SELECT 中稳定构造出可观察的结果差异（前者结果为空集，后者需 EXPLAIN 验证计划形状而非结果），未单独列为测试。若需覆盖，建议后续以 EXPLAIN 输出为验证目标，而非结果集比较。