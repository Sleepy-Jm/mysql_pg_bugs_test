## T1
依据：`setrefs.c` 中 `set_append_references()` 在 `appendplans` 长度为 1 时移除 Append 节点，并用 `apply_tlist_labeling()` 把父 tlist 的 `resname`/`resjunk`/`ressortgroupref` 传播到 child。差异点：本测试只考察“单子 Append 被消除后，顶层 `ORDER BY` 引用未出现在 SELECT 输出中的列”这一分支，不涉及聚合或并行。构造：单分区表 + `WHERE` 剪枝到该分区 + `ORDER BY` 一个未选出的列。

```sql
-- 准备
DROP TABLE IF EXISTS t1_p CASCADE;
CREATE TABLE t1_p (k int, v int, s text) PARTITION BY RANGE (k);
CREATE TABLE t1_p1 PARTITION OF t1_p FOR VALUES FROM (0) TO (10);
INSERT INTO t1_p VALUES (1,30,'a'),(2,10,'b'),(3,20,'c'),(4,10,'d');
ANALYZE t1_p;

-- 目标 SELECT：单子 Append，ORDER BY 未输出列 v
SELECT s FROM t1_p WHERE k < 10 ORDER BY v, s;

-- 对照：直接查唯一 child
SELECT s FROM t1_p1 WHERE k < 10 ORDER BY v, s;

-- 清理
DROP TABLE t1_p CASCADE;
```

预期结果：目标查询与对照查询都应返回 4 行，顺序为 `b`(v=10,s='b')、`d`(v=10,s='d')、`c`(v=20)、`a`(v=30)。列描述应只有一列 `s`，不应出现隐藏列 `v`。若 `apply_tlist_labeling` 把 `resjunk` 错误传播或丢失，可能出现多余列或排序键丢失。仍需以后验证：`EXPLAIN (VERBOSE, COSTS OFF)` 是否确实生成单子 Append 并被消除；`resjunk` 标记在 child tlist 上的实际状态。

## T2
依据：`setrefs.c` 中 `set_mergeappend_references()` 在 `mergeplans` 长度为 1 时移除 MergeAppend，并传播 `ressortgroupref`。差异点：本测试针对 MergeAppend 分支，且用 `GROUP BY` 让上层节点消费 `ressortgroupref`，与 T1 的纯 Sort 路径不同。构造：单分区表 + 索引 + `GROUP BY` 一个列 + `ORDER BY` 聚合结果。

```sql
-- 准备
DROP TABLE IF EXISTS t2_p CASCADE;
CREATE TABLE t2_p (k int, g int, v int) PARTITION BY RANGE (k);
CREATE TABLE t2_p1 PARTITION OF t2_p FOR VALUES FROM (0) TO (10);
CREATE INDEX t2_p1_k_g ON t2_p1 (k, g);
INSERT INTO t2_p VALUES (1,1,10),(2,1,20),(3,2,5),(4,2,7),(5,1,1);
ANALYZE t2_p;

-- 目标 SELECT：单子 MergeAppend + GROUP BY
SELECT g, sum(v) AS sv FROM t2_p WHERE k < 10 GROUP BY g ORDER BY g;

-- 对照：直接查 child
SELECT g, sum(v) AS sv FROM t2_p1 WHERE k < 10 GROUP BY g ORDER BY g;

-- 清理
DROP TABLE t2_p CASCADE;
```

预期结果：两查询都应返回两行：`(1, 31)`、`(2, 12)`，按 `g` 升序。列名应为 `g`、`sv`。若 `ressortgroupref` 在消除 MergeAppend 时未正确传播，可能出现“could not find pathkey item to sort”错误或分组错位。仍需以后验证：规划器是否实际选择 MergeAppend 路径（受成本与索引影响），以及 `EXPLAIN VERBOSE` 中 Group 节点的 tlist 引用。

## T3
依据：`pathnode.c` 中 `create_append_path()` 在 `subpaths` 长度为 1 时继承 child 的 `pathkeys`、`rows`、`cost`。差异点：本测试考察“单子 AppendPath 继承 pathkeys 后规划器省略 Sort”的可观察后果——输出顺序是否仍满足 `ORDER BY`。与 T1 不同，T1 关注标签传播，本测试关注顺序语义本身。构造：单分区表 + child 索引 + `ORDER BY` 索引列，并加入 `LIMIT` 使顺序可观察。

```sql
-- 准备
DROP TABLE IF EXISTS t3_p CASCADE;
CREATE TABLE t3_p (k int, v int) PARTITION BY RANGE (k);
CREATE TABLE t3_p1 PARTITION OF t3_p FOR VALUES FROM (0) TO (10);
CREATE INDEX t3_p1_v ON t3_p1 (v);
INSERT INTO t3_p VALUES (1,50),(2,10),(3,40),(4,20),(5,30);
ANALYZE t3_p;

-- 目标 SELECT：单子 Append，ORDER BY 索引列
SELECT v FROM t3_p WHERE k < 10 ORDER BY v LIMIT 3;

-- 对照：直接查 child
SELECT v FROM t3_p1 WHERE k < 10 ORDER BY v LIMIT 3;

-- 清理
DROP TABLE t3_p CASCADE;
```

预期结果：两查询都应返回 `10, 20, 30`（升序前三）。若单子 AppendPath 错误继承 pathkeys 而实际执行未按该顺序产出，可能返回乱序结果。仍需以后验证：`EXPLAIN (VERBOSE, COSTS OFF)` 是否显示 Append 被消除且 Sort 被省略；child 索引扫描是否真正按 `v` 有序。

## T4
依据：`execAmi.c` 中 `ExecSupportsMarkRestore()` 新增 `T_Append`/`T_MergeAppend` 单子分支，返回唯一 child 的 mark/restore 能力。差异点：本测试用滚动游标触发 mark/restore 判定，考察 `FETCH BACKWARD`/`FETCH PRIOR` 的行序与完整性，与 T1–T3 的普通 SELECT 路径不同。构造：单分区表 + 滚动游标 + 前后向读取。

```sql
-- 准备
DROP TABLE IF EXISTS t4_p CASCADE;
CREATE TABLE t4_p (k int, v int) PARTITION BY RANGE (k);
CREATE TABLE t4_p1 PARTITION OF t4_p FOR VALUES FROM (0) TO (10);
INSERT INTO t4_p VALUES (1,10),(2,20),(3,30),(4,40);
ANALYZE t4_p;

-- 目标：单子 Append 上的滚动游标
BEGIN;
DECLARE c SCROLL CURSOR FOR SELECT v FROM t4_p WHERE k < 10 ORDER BY v;
FETCH FORWARD 2 FROM c;   -- 期望 10, 20
FETCH BACKWARD 1 FROM c;  -- 期望 20
FETCH PRIOR FROM c;       -- 期望 10
FETCH LAST FROM c;        -- 期望 40
FETCH PRIOR FROM c;       -- 期望 30
CLOSE c;
COMMIT;

-- 对照：直接查 child 的滚动游标
BEGIN;
DECLARE c2 SCROLL CURSOR FOR SELECT v FROM t4_p1 WHERE k < 10 ORDER BY v;
FETCH FORWARD 2 FROM c2;
FETCH BACKWARD 1 FROM c2;
FETCH PRIOR FROM c2;
FETCH LAST FROM c2;
FETCH PRIOR FROM c2;
CLOSE c2;
COMMIT;

-- 清理
DROP TABLE t4_p CASCADE;
```

预期结果：两个游标的每次 FETCH 应返回相同值序列：`10,20` → `20` → `10` → `40` → `30`。若 `ExecSupportsMarkRestore` 对单子 Append 误判为不支持，规划器可能插入 Materialize 或拒绝 SCROLL，导致 `FETCH BACKWARD` 报错或返回错误行。仍需以后验证：`EXPLAIN` 中是否出现 Materialize；`ExecSupportsMarkRestore` 是否被该游标路径实际调用。

## T5
依据：`setrefs.c` 中 `set_subqueryscan_references()` 改为调用 `clean_up_removed_plan_level()`，在平凡 SubqueryScan 消除时传播 `resjunk`/`ressortgroupref`。差异点：本测试针对 SubqueryScan 消除分支，而非 Append/MergeAppend；用外层 `ORDER BY` 引用子查询内部未输出的列，考察标签传播。构造：可被 `trivial_subqueryscan` 消除的子查询 + 外层排序。

```sql
-- 准备
DROP TABLE IF EXISTS t5_t CASCADE;
CREATE TABLE t5_t (a int, b int, c text);
INSERT INTO t5_t VALUES (1,30,'x'),(2,10,'y'),(3,20,'z');
ANALYZE t5_t;

-- 目标 SELECT：平凡子查询 + 外层 ORDER BY 未输出列
SELECT c FROM (SELECT a, b, c FROM t5_t) sub ORDER BY b, c;

-- 对照：等价直接查询
SELECT c FROM t5_t ORDER BY b, c;

-- 清理
DROP TABLE t5_t CASCADE;
```

预期结果：两查询都应返回 3 行，顺序为 `y`(b=10)、`z`(b=20)、`x`(b=30)，列描述只有 `c`。若 SubqueryScan 消除时 `resjunk` 标记未正确传播，可能多出隐藏列或排序键丢失导致顺序错误。仍需以后验证：`trivial_subqueryscan()` 是否对该子查询返回真（当前对 resjunk 差异有保守限制，可能阻止消除）；`EXPLAIN VERBOSE` 中是否出现 SubqueryScan 节点。

---

说明：以上五个测试分别对应交接中的 1.1（Append 标签传播）、1.1（MergeAppend + ressortgroupref）、1.2（AppendPath 继承 pathkeys）、1.5（ExecSupportsMarkRestore）、1.6（SubqueryScan 消除）五个不同分支，输入边界与执行路径互不重复。1.3（MergeAppend 成本继承）与 1.4（ordered partial path）因需要精确成本/并行参数才能稳定触发，且其可观察结果与 T2/T3 重叠，未单列；若需覆盖，可在 T2/T3 基础上调整 `enable_mergejoin`、`parallel_setup_cost` 等参数，但本轮未执行反馈，无法确认可达性。所有预期值均由 SQL 语义推导，未声称已执行或观察到差异。