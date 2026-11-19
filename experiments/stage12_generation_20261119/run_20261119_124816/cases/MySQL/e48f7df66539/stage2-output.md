## T1
候选依据：交接 §1.1 派生表/CTE 物化，`MaterializeIterator::MaterializeQueryBlock()` 由 `copy_fields_and_funcs()` 改为 `copy_funcs()`，字段进入 `items_to_copy` 后经 `Item_field::save_in_field()` 求值保存。与其他测试差异：考察派生表物化时源字段类型与物化列类型不一致（VARCHAR 源 → 派生表列被外层引用为整数比较），验证求值后保存与直接位复制在类型转换上的结果集差异。

```sql
-- 准备
DROP TABLE IF EXISTS t1_derived;
CREATE TABLE t1_derived (
  id INT PRIMARY KEY,
  s  VARCHAR(10)
) ENGINE=InnoDB;
INSERT INTO t1_derived VALUES
  (1,'10'),(2,'2'),(3,' 3'),(4,NULL),(5,'04');

-- 目标 SELECT：派生表物化，外层对派生列做数值比较与排序
SELECT d.id, d.s
FROM (SELECT id, s FROM t1_derived) AS d
WHERE d.s + 0 >= 3
ORDER BY d.s + 0, d.id;

-- 对照：等价但强制不同路径（直接基表，无派生物化）
SELECT id, s
FROM t1_derived
WHERE s + 0 >= 3
ORDER BY s + 0, id;

-- 清理
DROP TABLE IF EXISTS t1_derived;
```

预期结果：目标 SELECT 与对照 SELECT 应返回相同行集与顺序：`(2,'2'),(3,' 3'),(5,'04'),(1,'10')`（按 `s+0` 升序：2,3,4,10；NULL 行被 `>=3` 过滤）。若派生表物化路径在字段复制时改变了字符串到数值的求值语义，则两查询结果可能不一致。仍需以后验证：`EXPLAIN FORMAT=TREE` 是否出现 `Materialize` 节点；`sql_mode` 默认与严格模式下 `' 3'`、`'04'` 的转换警告是否一致。

## T2
候选依据：交接 §1.2 UNION 物化，`Query_expression::setup_materialization()` 设 `copy_items=true`，各分支字段经 `copy_funcs()` 写入临时表。与其他测试差异：考察 UNION 各分支字段类型不一致（INT 与 DECIMAL 与字符串数字）时，物化结果列类型由首分支决定，验证分支值经 `Item_field::save_in_field()` 保存后的聚合与排序是否符合 SQL 语义。

```sql
-- 准备
DROP TABLE IF EXISTS t2a;
DROP TABLE IF EXISTS t2b;
CREATE TABLE t2a (v INT) ENGINE=InnoDB;
CREATE TABLE t2b (v DECIMAL(10,2)) ENGINE=InnoDB;
INSERT INTO t2a VALUES (1),(2),(3);
INSERT INTO t2b VALUES (1.50),(2.25),(3.75);

-- 目标 SELECT：UNION ALL 物化后外层聚合与排序
SELECT u.v, COUNT(*) AS c
FROM (
  SELECT v FROM t2a
  UNION ALL
  SELECT v FROM t2b
) AS u
GROUP BY u.v
ORDER BY u.v;

-- 对照：显式合并后聚合（不依赖 UNION 物化列类型推导）
SELECT v, COUNT(*) AS c
FROM (
  SELECT CAST(v AS DECIMAL(10,2)) AS v FROM t2a
  UNION ALL
  SELECT v FROM t2b
) AS u2
GROUP BY v
ORDER BY v;

-- 清理
DROP TABLE IF EXISTS t2a;
DROP TABLE IF EXISTS t2b;
```

预期结果：目标 SELECT 中 UNION 结果列类型由首分支 INT 决定，`1.50`、`2.25`、`3.75` 在物化时按 INT 语义处理（四舍五入/截断取决于列类型推导），预期分组为 `1→2, 2→2, 3→2, 4→0`（若按四舍五入）或 `1→2,2→2,3→2`（若截断，3.75→3 与 3 合并为 3 行）。对照 SELECT 显式 DECIMAL 后分组为 `1.00→1,1.50→1,2.00→1,2.25→1,3.00→1,3.75→1`。两查询语义不同，用于确认 UNION 物化列类型推导是否与首分支一致。仍需以后验证：`EXPLAIN FORMAT=TREE` 是否出现 `Materialize`；UNION 结果列的实际类型（`SHOW CREATE` 临时表不可见，需通过 `SELECT u.v+0` 观察）。

## T3
候选依据：交接 §1.4 聚合 DISTINCT 内部临时表，`Aggregator_distinct::add()` 删除 `copy_fields()` 仅保留 `copy_funcs()`。与其他测试差异：考察 `COUNT(DISTINCT)`/`SUM(DISTINCT)` 参数为字符串字段且含前导空格、大小写、尾随空格时，去重键经 `Item_field::save_in_field()` 保存到临时表后的比较语义（字符集/校对规则、尾随空格处理）。

```sql
-- 准备
DROP TABLE IF EXISTS t3_distinct;
CREATE TABLE t3_distinct (
  id INT PRIMARY KEY,
  s  VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
) ENGINE=InnoDB;
INSERT INTO t3_distinct VALUES
  (1,'a'),(2,'A'),(3,'a '),(4,' a'),(5,'b'),(6,NULL),(7,'B');

-- 目标 SELECT：DISTINCT 聚合，去重键为字符串字段
SELECT
  COUNT(DISTINCT s) AS cd,
  SUM(DISTINCT LENGTH(s)) AS sdl,
  GROUP_CONCAT(DISTINCT s ORDER BY s) AS gc
FROM t3_distinct;

-- 对照：显式去重后聚合（不依赖聚合 DISTINCT 内部临时表）
SELECT
  COUNT(*) AS cd,
  SUM(LENGTH(s)) AS sdl,
  GROUP_CONCAT(s ORDER BY s) AS gc
FROM (SELECT DISTINCT s FROM t3_distinct) AS d;

-- 清理
DROP TABLE IF EXISTS t3_distinct;
```

预期结果：`utf8mb4_0900_ai_ci` 下 `'a'`、`'A'`、`'a '`、`' a'` 中 `'a'`/`'A'`/`'a '` 视为相等（尾随空格不敏感、大小写不敏感），`' a'` 前导空格不同视为不同；`'b'`/`'B'` 相等。故 `COUNT(DISTINCT s)` 预期为 3（`'a'` 组、`' a'`、`'b'` 组），`SUM(DISTINCT LENGTH(s))` 预期为 `1+2+1=4`（去重后长度集合 {1,2}，但 DISTINCT 作用于 `LENGTH(s)` 值：`'a'`→1、`' a'`→2、`'b'`→1，去重后 {1,2}，SUM=3）。目标与对照应一致。仍需以后验证：`EXPLAIN FORMAT=TREE` 是否出现 `Duplicate elimination` 或聚合临时表；`GROUP_CONCAT(DISTINCT ...)` 与 `COUNT(DISTINCT ...)` 是否走同一 `Aggregator_distinct` 路径。

## T4
候选依据：交接 §1.6 窗口函数，`WindowIterator::Read()` 与 `BufferingWindowIterator::Read()` 改为 `copy_funcs(..., CFT_FIELDS)`，`bring_back_frame_row()` 改为 `copy_funcs(out_param, CFT_FIELDS)`。与其他测试差异：考察窗口帧回填（`NTH_VALUE`、`LEAD/LAG`）时输出列同时包含字段与表达式，验证 `CFT_FIELDS` 只复制 `Item_field` 是否导致非字段表达式列在帧回填阶段缺失或错位。

```sql
-- 准备
DROP TABLE IF EXISTS t4_win;
CREATE TABLE t4_win (
  id INT PRIMARY KEY,
  grp INT,
  v   INT
) ENGINE=InnoDB;
INSERT INTO t4_win VALUES
  (1,1,10),(2,1,20),(3,1,30),(4,2,40),(5,2,50);

-- 目标 SELECT：窗口帧回填 + 字段与表达式混合输出
SELECT
  id,
  grp,
  v,
  NTH_VALUE(v, 2) OVER (PARTITION BY grp ORDER BY id
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS nth2,
  LAG(v, 1) OVER (PARTITION BY grp ORDER BY id) AS lag1,
  v * 2 AS v2
FROM t4_win
ORDER BY grp, id;

-- 对照：等价窗口查询但输出列全为字段（无表达式列）
SELECT
  id,
  grp,
  v,
  NTH_VALUE(v, 2) OVER (PARTITION BY grp ORDER BY id
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS nth2,
  LAG(v, 1) OVER (PARTITION BY grp ORDER BY id) AS lag1
FROM t4_win
ORDER BY grp, id;

-- 清理
DROP TABLE IF EXISTS t4_win;
```

预期结果：目标 SELECT 预期行：
`(1,1,10,NULL,NULL,20)`,`(2,1,20,20,10,40)`,`(3,1,30,20,20,60)`,`(4,2,40,NULL,NULL,80)`,`(5,2,50,50,40,100)`。
`NTH_VALUE(v,2)` 在帧内第 2 行出现前为 NULL；`LAG` 首行为 NULL。对照 SELECT 除 `v2` 列外应与目标前 5 列完全一致。若 `CFT_FIELDS` 在帧回填时漏复制 `v2` 这类表达式列，目标 `v2` 列可能出现 NULL 或错位。仍需以后验证：`EXPLAIN FORMAT=TREE` 是否出现 `Window` 节点；`BufferingWindowIterator` 是否被触发（需 `EXPLAIN ANALYZE` 或源码断点，本轮不执行）。

## T5
候选依据：交接 §1.7 `GROUP BY` 临时表聚合，`TemptableAggregateIterator::Init()` 改为 `copy_funcs(..., CFT_FIELDS)`，`create_tmp_table()` 字段复制列表改为 `items_to_copy`。与其他测试差异：考察 `GROUP BY` 分组键为 `BIT` 与 `ENUM` 字段（交接 §2.2 列出的类型敏感项），验证分组键经 `Item_field::save_in_field()` 保存到临时表后的分组与聚合值是否符合 SQL 语义。

```sql
-- 准备
DROP TABLE IF EXISTS t5_grp;
CREATE TABLE t5_grp (
  id INT PRIMARY KEY,
  b  BIT(4),
  e  ENUM('x','y','z'),
  n  INT
) ENGINE=InnoDB;
INSERT INTO t5_grp VALUES
  (1, b'0001', 'x', 10),
  (2, b'0001', 'x', 20),
  (3, b'0010', 'y', 30),
  (4, b'0010', 'y', 40),
  (5, b'0001', 'z', 50),
  (6, NULL,    'x', 60);

-- 目标 SELECT：GROUP BY 临时表聚合，分组键为 BIT 与 ENUM
SELECT b, e, COUNT(*) AS c, SUM(n) AS s
FROM t5_grp
GROUP BY b, e
ORDER BY b, e;

-- 对照：显式 CAST 分组键后聚合（不依赖临时表分组键复制）
SELECT CAST(b AS UNSIGNED) AS b, CAST(e AS CHAR) AS e, COUNT(*) AS c, SUM(n) AS s
FROM t5_grp
GROUP BY CAST(b AS UNSIGNED), CAST(e AS CHAR)
ORDER BY b, e;

-- 清理
DROP TABLE IF EXISTS t5_grp;
```

预期结果：目标 SELECT 预期分组：
`(b'0001','x',2,30)`,`(b'0001','z',1,50)`,`(b'0010','y',2,70)`,`(NULL,'x',1,60)`。
`BIT(4)` 分组按数值比较，`b'0001'` 与 `b'0010'` 不同；`ENUM` 按内部序号比较但显示为字符串。对照 SELECT 的 `b` 列为 `1,1,2,NULL`，`e` 列为 `'x','z','y','x'`，聚合值应与目标一致。若 `GROUP BY` 临时表分组键复制改变了 `BIT` 或 `ENUM` 的保存语义（如 `BIT` 被当作字符串、`ENUM` 序号错位），目标与对照可能不一致。仍需以后验证：`EXPLAIN FORMAT=TREE` 是否出现 `Temp table aggregate` 或 `Using temporary`；`BIT` 列在临时表中的实际存储类型（需 `EXPLAIN` 或源码确认）。

---

缺口说明：交接 §1.3 半连接物化、§1.5 `GROUP_CONCAT`（已并入 T3 部分覆盖）、§1.8 普通物化 `DISTINCT`/`ORDER BY`、§1.9 `INFORMATION_SCHEMA`/`SHOW`、§1.10 多表 `UPDATE`、§1.11 `subselect_hash_sj_engine` 未单独成测。原因：§1.11 交接明确标注“需进一步确认”，缺乏可执行构造依据；§1.9/§1.10 涉及系统表或多表更新，构造确定性小数据集与独立预期结果的成本高于本轮五测，且与 T1–T5 的字段复制语义重叠较大。若需覆盖，建议下一轮补充半连接物化（`IN (SELECT ...)` 强制 `semijoin=materialization`）与多表 `UPDATE` 各一测。