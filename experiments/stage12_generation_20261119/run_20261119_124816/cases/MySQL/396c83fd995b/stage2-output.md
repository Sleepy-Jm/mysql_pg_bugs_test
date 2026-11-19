## T1
候选依据：交接候选 1，SELECT 别名被 GROUP BY 引用（`GROUP BY x+3`），与直接写 `(a+2)+3` 的语义等价改写对照。差异：本测试用聚合值（SUM）而非逐行值，使别名引用必须读取已物化的临时表列，且用多行分组放大顺序影响。

```sql
-- 准备
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (id INT PRIMARY KEY, a INT NOT NULL);
INSERT INTO t1 VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6);

-- 目标 SELECT：别名 x 被 GROUP BY 引用
SELECT a+2 AS x, COUNT(*) AS c
FROM t1
GROUP BY x+3
ORDER BY x;

-- 对照：语义等价，不使用别名
SELECT a+2 AS x, COUNT(*) AS c
FROM t1
GROUP BY (a+2)+3
ORDER BY x;

-- 清理
DROP TABLE IF EXISTS t1;
```

预期结果：两条 SELECT 均返回 6 行，x 依次为 3,4,5,6,7,8，每行 c=1（因为 a+2 与 a+5 对每个 a 唯一，分组键 x+3 与 a 一一对应）。两结果集应完全一致。仍需以后验证：目标版本是否真的把别名 Item_ref 后置、是否出现某行 c 异常或 x 与 a+2 不符。

## T2
候选依据：交接候选 1 的非确定性求值次数风险，注释用 `RAND()` 说明别名被重复求值会得到不同值。差异：用用户变量计数替代 RAND，直接观测别名表达式被求值的次数，且用 GROUP BY 别名引用强制走临时表路径。

```sql
-- 准备
DROP TABLE IF EXISTS t2;
CREATE TABLE t2 (id INT PRIMARY KEY, a INT NOT NULL);
INSERT INTO t2 VALUES (1,1),(2,2),(3,3),(4,4);

SET @cnt := 0;

-- 目标 SELECT：别名 x 被 GROUP BY 引用，x 内含副作用
SELECT (@cnt := @cnt + 1) + a AS x, COUNT(*) AS c
FROM t2
GROUP BY x + 1
ORDER BY x;

-- 观测副作用次数
SELECT @cnt AS eval_count;

-- 对照：不使用别名
SET @cnt2 := 0;
SELECT (@cnt2 := @cnt2 + 1) + a AS x, COUNT(*) AS c
FROM t2
GROUP BY ((@cnt2 := @cnt2 + 1) + a) + 1
ORDER BY x;
SELECT @cnt2 AS eval_count2;

-- 清理
DROP TABLE IF EXISTS t2;
```

预期结果：目标 SELECT 返回 4 行，x 为 2,3,4,5（每行 a 唯一，分组键 x+1 唯一），c 均为 1；`@cnt` 应为 4（每行别名表达式只求值一次）。对照 SELECT 因 GROUP BY 中重复写了带副作用的表达式，`@cnt2` 预期为 8（每行两次求值），x 值可能因求值顺序不同而与目标不同。仍需以后验证：目标版本 `@cnt` 是否恰为 4、x 是否与 a+1 一致；对照的 8 次是语义推导，实际次数依赖优化器是否合并重复表达式。

## T3
候选依据：交接候选 2，`(x,y) IN (SELECT expr1,expr2 ...)` 转换为相关 EXISTS 后生成无别名 Item_ref。差异：构造多列 IN 子查询，使转换后的 HAVING 引用外层列，且外层列同时出现在 SELECT 列表别名中，形成别名引用与转换引用的叠加。

```sql
-- 准备
DROP TABLE IF EXISTS outer_t;
DROP TABLE IF EXISTS inner_t;
CREATE TABLE outer_t (id INT PRIMARY KEY, a INT NOT NULL, b INT NOT NULL);
CREATE TABLE inner_t (id INT PRIMARY KEY, p INT NOT NULL, q INT NOT NULL);
INSERT INTO outer_t VALUES (1,1,10),(2,2,20),(3,3,30),(4,4,40);
INSERT INTO inner_t VALUES (1,1,10),(2,2,20),(3,9,90);

-- 目标 SELECT：多列 IN 子查询，可能转换为相关 EXISTS
SELECT a, b, a+b AS s
FROM outer_t
WHERE (a, b) IN (SELECT p, q FROM inner_t)
ORDER BY a;

-- 对照：显式 EXISTS 改写，语义等价
SELECT a, b, a+b AS s
FROM outer_t o
WHERE EXISTS (SELECT 1 FROM inner_t i WHERE i.p = o.a AND i.q = o.b)
ORDER BY a;

-- 清理
DROP TABLE IF EXISTS outer_t;
DROP TABLE IF EXISTS inner_t;
```

预期结果：两条 SELECT 均返回 2 行：(1,10,11) 和 (2,20,22)，按 a 升序。两结果集应完全一致。仍需以后验证：目标版本是否将 IN 转为 EXISTS、转换后 HAVING 中的 Item_ref 是否被正确后置、s 列是否等于 a+b 而非未填充值。

## T4
候选依据：交接候选 1 与候选 2 的叠加，别名引用出现在 HAVING 中且 HAVING 引用聚合别名，同时 GROUP BY 引用同一别名，形成多个后置元素之间的相对顺序依赖。差异：T1 只测 GROUP BY，本测试同时测 HAVING 与 GROUP BY 对同一别名的引用，检验 stable_partition 后置集合内部顺序。

```sql
-- 准备
DROP TABLE IF EXISTS t4;
CREATE TABLE t4 (id INT PRIMARY KEY, g INT NOT NULL, v INT NOT NULL);
INSERT INTO t4 VALUES (1,1,10),(2,1,20),(3,2,30),(4,2,40),(5,3,50);

-- 目标 SELECT：别名 s 同时被 GROUP BY 和 HAVING 引用
SELECT g, SUM(v) AS s
FROM t4
GROUP BY g
HAVING s > 25
ORDER BY g;

-- 对照：不使用别名
SELECT g, SUM(v) AS s
FROM t4
GROUP BY g
HAVING SUM(v) > 25
ORDER BY g;

-- 清理
DROP TABLE IF EXISTS t4;
```

预期结果：两条 SELECT 均返回 2 行：(2,70) 和 (3,50)，按 g 升序。g=1 的 SUM=30 也 >25，故实际返回 3 行：(1,30),(2,70),(3,50)。两结果集应完全一致。仍需以后验证：目标版本 HAVING 中的别名 Item_ref 是否读取到已填充的 s 列、是否出现 g=1 被错误过滤或 s 值异常。

## T5
候选依据：交接候选 3，窗口函数与聚合组合导致隐藏项被物化，注释提到 split_sum_func 产生的隐藏聚合项可能引用 select 列表表达式。差异：构造窗口函数 + 聚合 + 别名引用，检验物化临时表中隐藏聚合项与别名引用的顺序。

```sql
-- 准备
DROP TABLE IF EXISTS t5;
CREATE TABLE t5 (id INT PRIMARY KEY, g INT NOT NULL, v INT NOT NULL);
INSERT INTO t5 VALUES (1,1,10),(2,1,20),(3,2,30),(4,2,40),(5,3,50);

-- 目标 SELECT：窗口函数 + 聚合 + 别名被 ORDER BY 引用
SELECT g, SUM(v) AS s, SUM(SUM(v)) OVER (ORDER BY g) AS running
FROM t5
GROUP BY g
ORDER BY s DESC;

-- 对照：不使用别名，ORDER BY 直接写 SUM(v)
SELECT g, SUM(v) AS s, SUM(SUM(v)) OVER (ORDER BY g) AS running
FROM t5
GROUP BY g
ORDER BY SUM(v) DESC;

-- 清理
DROP TABLE IF EXISTS t5;
```

预期结果：两条 SELECT 均返回 3 行，按 s 降序：(2,70,120),(3,50,170),(1,30,30)。running 列按 g 升序累加：g=1 时 30，g=2 时 30+70=120，g=3 时 120+50=170。两结果集应完全一致。仍需以后验证：目标版本是否真的物化隐藏聚合项、running 列是否与按 g 升序累加一致、s 列是否等于各 g 的 SUM(v)。

## 缺口说明
交接材料直接支持的构造为候选 1（别名引用）和候选 2（IN 子查询转换），候选 3（窗口函数）证据较弱。T1–T5 覆盖了别名在 GROUP BY、HAVING、ORDER BY 中的引用，副作用求值次数，多列 IN 转换，以及窗口+聚合物化。仍缺少：交接未给出可稳定触发 `sort_copy_func` 且谓词返回 true 的完整可执行 SQL，也未提供 EXPLAIN 或 optimizer_trace 证据；T3 的 IN 转换是否实际发生、T5 的隐藏项是否实际物化，均需以后用执行计划验证。若目标版本未进入该路径，T1–T5 仍可作为语义正确性基线，但不能单独证明改动被命中。