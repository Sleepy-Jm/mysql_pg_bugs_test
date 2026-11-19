## T1
依据：交接指出新增块只在 `UNION ALL` 且顶层有 `LIMIT ... OFFSET ...` 时进入，右臂带 `ORDER BY` 才会经 `pushOntoSorter` 消费 `iOffset+1`。本测试用最小两臂、右臂 `ORDER BY`、左臂 0 行，使右臂开始时 `iLimit`、`iOffset` 仍为初值，检验“两臂都正时 `iOffset+1 = LIMIT+OFFSET`”分支下结果是否仍等于手工拼接后截取。与其他测试差异：左臂空，计数器未被左臂消耗。

```sql
-- 准备
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(x INTEGER);
INSERT INTO t1 VALUES (1),(2),(3);
INSERT INTO t2 VALUES (10),(20),(30);

-- 目标 SELECT：左臂空，右臂带 ORDER BY，顶层 LIMIT/OFFSET
SELECT x FROM t1 WHERE x > 100
UNION ALL
SELECT x FROM (SELECT x FROM t2 ORDER BY x DESC)
LIMIT 2 OFFSET 1;

-- 对照：等价显式拼接
SELECT x FROM (
  SELECT x FROM t1 WHERE x > 100
  UNION ALL
  SELECT x FROM (SELECT x FROM t2 ORDER BY x DESC)
) LIMIT 2 OFFSET 1;

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期：左臂 0 行，右臂按 `x DESC` 为 `30,20,10`；拼接后整体 `OFFSET 1 LIMIT 2` 得 `20,10`。目标 SELECT 与对照应一致返回 `20,10`。需以后验证：右臂 sorter 实际读取的 `iOffset+1` 值，以及 `pushOntoSorter` 保留行数是否影响最终输出。

## T2
依据：交接 2.1 第 4 条，`iOffset <= 0` 时 `iOffset+1` 被覆盖为当前 `iLimit`。本测试令左臂恰好消耗完 OFFSET（`iOffset` 归 0），右臂带 `ORDER BY`，检验该分支下右臂 sorter 保留行数是否仍足以产出正确剩余行。与其他测试差异：左臂行数恰好等于 OFFSET，触发 `iOffset <= 0` 分支。

```sql
-- 准备
CREATE TABLE a(x INTEGER);
CREATE TABLE b(x INTEGER);
INSERT INTO a VALUES (1),(2),(3);
INSERT INTO b VALUES (100),(200),(300);

-- 目标 SELECT：左臂 3 行，OFFSET=3 恰好被左臂吃完
SELECT x FROM a
UNION ALL
SELECT x FROM (SELECT x FROM b ORDER BY x DESC)
LIMIT 2 OFFSET 3;

-- 对照：等价显式拼接
SELECT x FROM (
  SELECT x FROM a
  UNION ALL
  SELECT x FROM (SELECT x FROM b ORDER BY x DESC)
) LIMIT 2 OFFSET 3;

-- 清理
DROP TABLE a;
DROP TABLE b;
```

预期：左臂 `1,2,3`，右臂 `300,200,100`；拼接后 `OFFSET 3 LIMIT 2` 得 `300,200`。目标 SELECT 与对照应一致返回 `300,200`。需以后验证：左臂执行后 `iOffset` 是否确实归 0、`iLimit` 是否仍为 2，从而走 `iOffset <= 0` 分支。

## T3
依据：交接 2.1 第 4 条，`iLimit <= 0` 时 `iOffset+1` 被设为 `-1`。本测试令左臂行数超过 `OFFSET+LIMIT`，使左臂执行后 `iLimit` 归 0，右臂带 `ORDER BY`，检验 `-1` 分支下右臂是否被正确跳过、结果是否仍为左臂前 `LIMIT` 行。与其他测试差异：左臂已满足全部输出，右臂应不产出。

```sql
-- 准备
CREATE TABLE p(x INTEGER);
CREATE TABLE q(x INTEGER);
INSERT INTO p VALUES (1),(2),(3),(4),(5);
INSERT INTO q VALUES (90),(80),(70);

-- 目标 SELECT：左臂 5 行，LIMIT+OFFSET=3，左臂已吃完
SELECT x FROM p
UNION ALL
SELECT x FROM (SELECT x FROM q ORDER BY x DESC)
LIMIT 2 OFFSET 1;

-- 对照：等价显式拼接
SELECT x FROM (
  SELECT x FROM p
  UNION ALL
  SELECT x FROM (SELECT x FROM q ORDER BY x DESC)
) LIMIT 2 OFFSET 1;

-- 清理
DROP TABLE p;
DROP TABLE q;
```

预期：左臂 `1,2,3,4,5`，右臂 `90,80,70`；拼接后 `OFFSET 1 LIMIT 2` 得 `2,3`，全部来自左臂。目标 SELECT 与对照应一致返回 `2,3`。需以后验证：左臂执行后 `iLimit` 是否归 0、右臂是否被 `OP_IfNot` 类跳转跳过。

## T4
依据：交接 2.1 第 3 条，重算发生在左臂之后、右臂之前，左臂消耗量决定右臂开始时计数器。本测试令左臂行数介于 OFFSET 与 OFFSET+LIMIT 之间（部分消耗），右臂带 `ORDER BY`，检验“两臂都正”分支下 `iOffset+1 = 剩余LIMIT + 剩余OFFSET` 是否仍产出正确跨臂结果。与其他测试差异：左臂部分消耗，剩余 LIMIT 与 OFFSET 都为正。

```sql
-- 准备
CREATE TABLE m(x INTEGER);
CREATE TABLE n(x INTEGER);
INSERT INTO m VALUES (1),(2);
INSERT INTO n VALUES (50),(40),(30),(20);

-- 目标 SELECT：左臂 2 行，OFFSET=1 LIMIT=3，左臂消耗 1 行 OFFSET 后剩 1 行输出
SELECT x FROM m
UNION ALL
SELECT x FROM (SELECT x FROM n ORDER BY x DESC)
LIMIT 3 OFFSET 1;

-- 对照：等价显式拼接
SELECT x FROM (
  SELECT x FROM m
  UNION ALL
  SELECT x FROM (SELECT x FROM n ORDER BY x DESC)
) LIMIT 3 OFFSET 1;

-- 清理
DROP TABLE m;
DROP TABLE n;
```

预期：左臂 `1,2`，右臂 `50,40,30,20`；拼接后 `OFFSET 1 LIMIT 3` 得 `2,50,40`。目标 SELECT 与对照应一致返回 `2,50,40`。需以后验证：左臂执行后 `iLimit`、`iOffset` 的剩余值，以及右臂 sorter 保留行数是否覆盖剩余 `LIMIT+OFFSET`。

## T5
依据：交接 1.2 指出 `LIMIT ... OFFSET ...` 即使 OFFSET 运行时为 0 也会生成新增块，且 2.3 对照表要求区分 `OFFSET 0` 与正 OFFSET。本测试用 `OFFSET 0`、右臂带 `ORDER BY`，检验 `iOffset <= 0` 分支（`iOffset+1` 被覆盖为 `iLimit`）下结果是否仍等于无 OFFSET 的截取。与其他测试差异：OFFSET 为 0，仍走新增块但 `iOffset` 非正。

```sql
-- 准备
CREATE TABLE u(x INTEGER);
CREATE TABLE v(x INTEGER);
INSERT INTO u VALUES (7),(8);
INSERT INTO v VALUES (60),(50),(40);

-- 目标 SELECT：OFFSET 0，右臂带 ORDER BY
SELECT x FROM u
UNION ALL
SELECT x FROM (SELECT x FROM v ORDER BY x DESC)
LIMIT 2 OFFSET 0;

-- 对照：等价显式拼接
SELECT x FROM (
  SELECT x FROM u
  UNION ALL
  SELECT x FROM (SELECT x FROM v ORDER BY x DESC)
) LIMIT 2 OFFSET 0;

-- 清理
DROP TABLE u;
DROP TABLE v;
```

预期：左臂 `7,8`，右臂 `60,50,40`；拼接后 `LIMIT 2 OFFSET 0` 得 `7,8`。目标 SELECT 与对照应一致返回 `7,8`。需以后验证：`OFFSET 0` 时 `p->iOffset` 寄存器是否仍存在、新增块是否执行，以及 `iOffset <= 0` 分支下右臂 sorter 保留行数是否影响输出。

缺口说明：交接 3.2 建议覆盖“左右臂都有 ORDER BY”和“多臂 UNION ALL”两类形式，但交接 1.1 指出顶层 `ORDER BY` 会早退到 `multiSelectOrderBy`，而臂内 `ORDER BY` 在左臂是否同样触发 sorter 消费 `iOffset+1` 未在提供的源码中直接展示；多臂情形下新增块在每对相邻臂之间重复执行的精确寄存器状态也缺少完整 select loop 源码佐证。因此本轮只给出上述五个有直接源码依据的测试，未构造这两类以避免超出交接证据。