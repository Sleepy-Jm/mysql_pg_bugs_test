## T1
依据：交接 1.3-A 与 2.1 中“递增窗口函数 + 上界比较、keep_original=false”分支。与 T2 的差异在于本测试使用 `row_number()` 且无 `PARTITION BY`，考察顶层 `WindowAgg` 在 run condition 失效后进入 `PASSTHROUGH_STRICT` 时是否只返回满足 `rn <= k` 的行；T2 则考察分区切换后恢复 `RUN` 的行为。

```sql
-- 准备
CREATE TEMP TABLE t1 (a int);
INSERT INTO t1 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：row_number() 递增，外层 rn <= 3
SELECT a, rn
FROM (
  SELECT a, row_number() OVER (ORDER BY a) AS rn
  FROM t1
) s
WHERE rn <= 3
ORDER BY a;

-- 对照：物化后过滤，语义真值
WITH w AS MATERIALIZED (
  SELECT a, row_number() OVER (ORDER BY a) AS rn FROM t1
)
SELECT a, rn FROM w WHERE rn <= 3 ORDER BY a;

-- 清理
DROP TABLE t1;
```

预期结果：目标 SELECT 与对照均返回 `(1,1),(2,2),(3,3)`。目标路径应生成 run condition `rn <= 3` 且不保留原 filter；对照路径不进入改动路径。仍需以后验证：`EXPLAIN` 是否出现 `Run Condition`，以及 `PASSTHROUGH_STRICT` 是否在 rn=4 处停止返回。

## T2
依据：交接 1.3-D 与 2.1 中“有 PARTITION BY 时 use_pass_through=true，run condition 失效后进入 PASSTHROUGH_STRICT，下一分区恢复 RUN”。与 T1 的差异在于存在多个分区，考察跨分区恢复是否漏行或多行。

```sql
-- 准备
CREATE TEMP TABLE t2 (g int, a int);
INSERT INTO t2 VALUES
  (1,1),(1,2),(1,3),(1,4),
  (2,1),(2,2),(2,3),(2,4);

-- 目标 SELECT：分区内 row_number()，外层 rn <= 2
SELECT g, a, rn
FROM (
  SELECT g, a, row_number() OVER (PARTITION BY g ORDER BY a) AS rn
  FROM t2
) s
WHERE rn <= 2
ORDER BY g, a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT g, a, row_number() OVER (PARTITION BY g ORDER BY a) AS rn FROM t2
)
SELECT g, a, rn FROM w WHERE rn <= 2 ORDER BY g, a;

-- 清理
DROP TABLE t2;
```

预期结果：两者均返回 `(1,1,1),(1,2,2),(2,1,1),(2,2,2)`。目标路径应在每个分区内 rn=3 处进入 pass-through，并在下一分区恢复。仍需以后验证：分区边界处是否恰好丢弃 rn=3 及之后的行，且下一分区首行是否被正确返回。

## T3
依据：交接 1.3-B 与 2.1 中“递减窗口函数 + 下界比较、keep_original=false”。与 T1/T2 的差异在于窗口帧为 `ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING`，单调方向为递减，操作符为 `>=`，考察方向匹配与 run condition 生成。

```sql
-- 准备
CREATE TEMP TABLE t3 (a int);
INSERT INTO t3 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：递减 count(*)，外层 cnt >= 3
SELECT a, cnt
FROM (
  SELECT a,
         count(*) OVER (ORDER BY a ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS cnt
  FROM t3
) s
WHERE cnt >= 3
ORDER BY a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT a,
         count(*) OVER (ORDER BY a ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS cnt
  FROM t3
)
SELECT a, cnt FROM w WHERE cnt >= 3 ORDER BY a;

-- 清理
DROP TABLE t3;
```

预期结果：cnt 依次为 5,4,3,2,1；两者均返回 `(1,5),(2,4),(3,3)`。目标路径应生成 run condition `cnt >= 3`，在 cnt=2 处失效并停止。仍需以后验证：递减方向下 run condition 的 btree 策略匹配是否正确，以及失效点是否精确在 a=4。

## T4
依据：交接 1.3-C 与 2.1 中“恒定窗口函数 + 等值比较、MONOTONICFUNC_BOTH、keep_original=true”。与 T1–T3 的差异在于无 `ORDER BY` 的 `count(*)` 为常量，等值比较 `= 3` 被转换为 `<=` 并保留原 equal qual，考察等值分支是否与原始 filter 等价。

```sql
-- 准备
CREATE TEMP TABLE t4 (a int);
INSERT INTO t4 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：无 ORDER BY 的 count(*) 为常量 5，外层 cnt = 5
SELECT a, cnt
FROM (
  SELECT a, count(*) OVER () AS cnt
  FROM t4
) s
WHERE cnt = 5
ORDER BY a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT a, count(*) OVER () AS cnt FROM t4
)
SELECT a, cnt FROM w WHERE cnt = 5 ORDER BY a;

-- 清理
DROP TABLE t4;
```

预期结果：cnt 恒为 5；两者均返回全部 5 行 `(1,5)…(5,5)`。目标路径应生成 run condition `cnt <= 5` 并保留原 `cnt = 5` filter。仍需以后验证：等值分支下 `keep_original=true` 是否确实保留 filter，以及常量窗口函数是否被正确识别为 `MONOTONICFUNC_BOTH`。

## T5
依据：交接 1.3-E 与 2.2 中“多层 WindowAgg、非顶层 pass-through 返回行可能影响上层窗口函数计算”。与 T1–T4 的差异在于存在两个不同 `WindowClause`，外层过滤引用顶层窗口函数，考察非顶层 `WindowAgg` 的 pass-through 是否影响上层窗口输入。

```sql
-- 准备
CREATE TEMP TABLE t5 (a int);
INSERT INTO t5 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：两层窗口，外层过滤引用顶层 row_number()
SELECT a, rn1, rn2
FROM (
  SELECT a,
         row_number() OVER (ORDER BY a) AS rn1,
         row_number() OVER (ORDER BY a DESC) AS rn2
  FROM t5
) s
WHERE rn2 <= 3
ORDER BY a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT a,
         row_number() OVER (ORDER BY a) AS rn1,
         row_number() OVER (ORDER BY a DESC) AS rn2
  FROM t5
)
SELECT a, rn1, rn2 FROM w WHERE rn2 <= 3 ORDER BY a;

-- 清理
DROP TABLE t5;
```

预期结果：rn1 为 1..5，rn2 为 5..1；两者均返回 `(3,3,3),(4,4,2),(5,5,1)`。目标路径应堆叠两个 `WindowAgg`，非顶层节点在 run condition 失效后进入 `PASSTHROUGH` 并继续返回元组供上层计算。仍需以后验证：非顶层 pass-through 返回的行是否完整携带下层窗口函数值，以及顶层 `WindowAgg` 的 qual 是否与原始 filter 等价。

## 缺口说明
本轮仅给出 5 个有源码依据的测试，覆盖 A/B/C/D/E 五类构造。交接 2.2 中列出的 `FILTER`、`EXCLUDE`、`CAST`、`get_op_btree_interpretation` 多 interpretation、volatile/相关子查询伪常量等组合，因交接明确标注为“尚待验证的推断”且缺少实现细节证据，未列为强候选测试。这些路径需在获得 `is_pseudo_constant_clause`、`int8inc_support` 对 FILTER/EXCLUDE 的处理细节，以及跨类型操作符 interpretation 返回行为后再构造。