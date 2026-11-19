## T1
候选依据：交接 §2.3 的“正面对照”。这是唯一由源码直接支持的形态：外层 `count(*)`、单项 `FROM` 子查询、`UNION ALL`、各项无 `WHERE`、非聚合。与其他测试的差异在于它不引入任何“未检查构造”，用于确认基线语义等于各项行数之和。

```sql
-- 准备：两张小表，行数不同，含 NULL 与重复值
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(2),(2),(NULL);
INSERT INTO t2 VALUES (10),(20),(NULL);

-- 目标 SELECT：安全形态，预期等于 (count t1)+(count t2)
SELECT count(*)
FROM (
    SELECT x FROM t1
    UNION ALL
    SELECT y FROM t2
);

-- 对照：等价形式，独立给出预期
SELECT (SELECT count(*) FROM t1) + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期结果：目标 SELECT 与对照 SELECT 都返回单行单列 `7`（t1 有 4 行，t2 有 3 行）。仍需以后验证：该查询是否真的进入 `countOfViewOptimization()`（可用 `EXPLAIN`/`SELECTTRACE` 0x400 确认路径），但结果正确性本身不依赖路径。

## T2
候选依据：交接 §2.2“高风险：内层 `DISTINCT`”。改变的操作数关系是：原语义统计去重后的值个数，而转换后可能统计物理行数。与其他测试的差异在于它只加内层 `DISTINCT`，其余保持安全形态，用于隔离该单一构造。

```sql
-- 准备：t1 含重复值，使 DISTINCT 与物理行数不同
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(1),(2),(NULL),(NULL);
INSERT INTO t2 VALUES (7),(8);

-- 目标 SELECT：内层第一项带 DISTINCT
SELECT count(*)
FROM (
    SELECT DISTINCT x FROM t1
    UNION ALL
    SELECT y FROM t2
);

-- 对照：按原始语义手工等价形式
SELECT (SELECT count(*) FROM (SELECT DISTINCT x FROM t1))
     + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期结果：目标 SELECT 与对照 SELECT 都应返回 `5`（t1 去重后为 {1,2,NULL} 共 3 个值，t2 有 2 行）。仍需以后验证：`SF_Distinct` 是否被 `countOfViewOptimization()` 忽略而进入优化；若进入，转换后第一项是否退化为 `SELECT count(*) FROM t1`（会得到 5+2=7，与正确值 5 不同）。

## T3
候选依据：交接 §2.2“高风险：外层 `WHERE`”。改变的操作数关系是：原语义先对 `UNION ALL` 结果过滤再计数，转换后外层 `pSrc` 被清空而 `pWhere` 保留。与其他测试的差异在于它只加外层 `WHERE`，用于隔离该构造。

```sql
-- 准备：正负值混合，使过滤改变计数
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(-1),(2),(-2);
INSERT INTO t2 VALUES (3),(-3);

-- 目标 SELECT：外层 WHERE 过滤
SELECT count(*)
FROM (
    SELECT x FROM t1
    UNION ALL
    SELECT y FROM t2
)
WHERE x > 0;

-- 对照：按原始语义手工等价形式
SELECT count(*) FROM (
    SELECT x FROM t1 WHERE x > 0
    UNION ALL
    SELECT y FROM t2 WHERE y > 0
);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期结果：目标 SELECT 与对照 SELECT 都应返回 `3`（正值：1、2、3）。仍需以后验证：外层 `pWhere` 在 `pSrc` 被清空后如何被解释——可能列引用失效、可能过滤未按原语义应用；这需要实际执行确认，本测试只给出语义基准。

## T4
候选依据：交接 §2.2“中高风险：内层 `LIMIT` / `OFFSET`”。改变的操作数关系是：原语义中第一项只贡献至多 N 行，转换后可能变成对 `count(*)` 结果再套 `LIMIT`，或零行导致 `NULL` 传播。与其他测试的差异在于它只加内层 `LIMIT`，且用 `LIMIT 0` 触发零行边界。

```sql
-- 准备：t1 多行，t2 少量行
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(2),(3),(4),(5);
INSERT INTO t2 VALUES (10),(20);

-- 目标 SELECT：第一项带 LIMIT 0（边界：零行贡献）
SELECT count(*)
FROM (
    SELECT x FROM t1 LIMIT 0
    UNION ALL
    SELECT y FROM t2
);

-- 对照：按原始语义手工等价形式
SELECT (SELECT count(*) FROM (SELECT x FROM t1 LIMIT 0))
     + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期结果：目标 SELECT 与对照 SELECT 都应返回 `2`（第一项贡献 0 行，第二项贡献 2 行）。仍需以后验证：SQLite 语法是否允许复合项携带 `LIMIT`；若允许且进入优化，转换后 `(SELECT count(*) FROM t1 LIMIT 0)` 返回零行，标量子查询在 `+` 中是否产生 `NULL` 传播（会得到 `NULL` 而非 2）。

## T5
候选依据：交接 §2.2“中高风险：内层 `GROUP BY` / `HAVING`”。改变的操作数关系是：原语义按组计数，转换后内层项变成带 `GROUP BY` 的聚合子查询，可能多行或零行。与其他测试的差异在于它只加内层 `GROUP BY`，且用重复值使分组数与物理行数不同。

```sql
-- 准备：t1 有重复值，分组数少于行数
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(1),(2),(3),(3),(3);
INSERT INTO t2 VALUES (9);

-- 目标 SELECT：第一项带 GROUP BY
SELECT count(*)
FROM (
    SELECT x FROM t1 GROUP BY x
    UNION ALL
    SELECT y FROM t2
);

-- 对照：按原始语义手工等价形式
SELECT (SELECT count(*) FROM (SELECT x FROM t1 GROUP BY x))
     + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期结果：目标 SELECT 与对照 SELECT 都应返回 `4`（t1 分组后为 {1,2,3} 共 3 组，t2 有 1 行）。仍需以后验证：`GROUP BY` 是否设置 `SF_Aggregate` 从而被循环中的 `if( pSub->selFlags & SF_Aggregate ) return 0;` 拦截；若未拦截，转换后内层 `SELECT count(*) FROM t1 GROUP BY x` 作为标量子查询返回多行时的行为（报错或取首行）需要实际执行确认。

---

说明：以上五个测试分别对应交接中“安全形态基线”“内层 DISTINCT”“外层 WHERE”“内层 LIMIT/OFFSET”“内层 GROUP BY”五个有源码依据且实质不同的构造。交接中提到的外层 `GROUP BY`/`HAVING`、外层 `DISTINCT`、外层 `ORDER BY`/`LIMIT`/`OFFSET`、内层 `HAVING`、内层 `ORDER BY` 等构造，或与上述测试共享同一未检查机制（如外层 `GROUP BY` 与 T3 同属外层未检查项），或交接自身标注为“较低风险/组合场景”，为避免重复换数值，未单列为独立测试。缺口：内层 `HAVING` 单独出现、外层 `DISTINCT` 与外层 `GROUP BY` 的组合、`count()` 无参数形式是否等价于 `count(*)`，这些在交接中仍缺少源码证据，未构造测试。