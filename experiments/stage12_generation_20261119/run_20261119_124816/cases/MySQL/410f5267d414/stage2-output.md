## T1
候选依据：交接指出 `val_decimal` 仅在 `val->frac > decimals` 时舍入，且 `val_str` 早已舍入；本测试用 DECIMAL 除法构造内部小数位多于声明 scale 的表达式，并对照字符串输出与 DECIMAL 列存储。与其他测试的差异：这是最直接的“字符串路径 vs DECIMAL 消费路径”一致性对照。

```sql
-- 准备
DROP TABLE IF EXISTS t1_src, t1_dst;
CREATE TABLE t1_src (a DECIMAL(10,2), b DECIMAL(10,2));
CREATE TABLE t1_dst (s VARCHAR(64), d DECIMAL(10,2));
INSERT INTO t1_src VALUES (1.00, 3.00), (2.00, 3.00), (10.00, 3.00);

-- 目标 SELECT：同一表达式分别以字符串和 DECIMAL 消费
SELECT a, b,
       a / b            AS str_form,
       CAST(a / b AS DECIMAL(10,2)) AS cast_form
FROM t1_src ORDER BY a;

-- 对照：存入 DECIMAL 列
INSERT INTO t1_dst (s, d)
SELECT CAST(a / b AS CHAR), a / b FROM t1_src ORDER BY a;
SELECT s, d FROM t1_dst ORDER BY s;

-- 清理
DROP TABLE t1_src, t1_dst;
```

预期结果：`1.00/3.00` 字符串形式为 `0.33`（HALF_UP 到 2 位），DECIMAL 列存储也应为 `0.33`；`2.00/3.00` 为 `0.67`；`10.00/3.00` 为 `3.33`。若旧版 `val_decimal` 未舍入，DECIMAL 列可能得到 `0.33` 之外的截断/全精度值，与字符串不一致。仍需以后验证：`result_precision()` 对该除法实际声明的 `decimals` 是否为 2，以及 DECIMAL 列写入是否确实走 `val_decimal`。

## T2
候选依据：交接指出 `val_real` 在 DECIMAL_RESULT 下先舍入再转 double；本测试用 DECIMAL 除法存入 DOUBLE 列，对照字符串输出。与其他测试的差异：消费路径是 `val_real`（REAL_RESULT 目标），而非 T1 的 `val_decimal`。

```sql
-- 准备
DROP TABLE IF EXISTS t2_src, t2_dst;
CREATE TABLE t2_src (a DECIMAL(10,2), b DECIMAL(10,2));
CREATE TABLE t2_dst (s VARCHAR(64), r DOUBLE);
INSERT INTO t2_src VALUES (1.00, 3.00), (2.00, 3.00), (5.00, 3.00);

-- 目标 SELECT：字符串形式
SELECT a, b, a / b AS str_form FROM t2_src ORDER BY a;

-- 对照：存入 DOUBLE 列（走 val_real）
INSERT INTO t2_dst (s, r)
SELECT CAST(a / b AS CHAR), a / b FROM t2_src ORDER BY a;
SELECT s, r FROM t2_dst ORDER BY s;

-- 清理
DROP TABLE t2_src, t2_dst;
```

预期结果：字符串形式 `0.33`、`0.67`、`1.67`；DOUBLE 列应分别为 `0.33`、`0.67`、`1.67`（舍入后转 double）。若旧版 `val_real` 未舍入，DOUBLE 列可能为 `0.3333...`、`0.6666...`、`1.6666...`，与字符串不一致。仍需以后验证：DOUBLE 列写入是否确实调用 `val_real`，以及 double 表示是否引入额外尾差。

## T3
候选依据：交接指出含 DOUBLE/FLOAT 操作数时 `hybrid_type` 为 `REAL_RESULT`，不进入补丁；本测试用 DECIMAL 与 DOUBLE 混合除法作为“不应受影响”的对照组。与其他测试的差异：这是负对照，验证补丁不改变 REAL_RESULT 路径。

```sql
-- 准备
DROP TABLE IF EXISTS t3_src, t3_dst;
CREATE TABLE t3_src (a DECIMAL(10,2), d DOUBLE);
CREATE TABLE t3_dst (s VARCHAR(64), r DOUBLE);
INSERT INTO t3_src VALUES (1.00, 3.0), (2.00, 3.0), (5.00, 3.0);

-- 目标 SELECT：含 DOUBLE 操作数，hybrid_type 应为 REAL_RESULT
SELECT a, d, a / d AS str_form FROM t3_src ORDER BY a;

-- 对照：存入 DOUBLE 列
INSERT INTO t3_dst (s, r)
SELECT CAST(a / d AS CHAR), a / d FROM t3_src ORDER BY a;
SELECT s, r FROM t3_dst ORDER BY s;

-- 清理
DROP TABLE t3_src, t3_dst;
```

预期结果：字符串形式与 DOUBLE 列应一致（均为 double 运算结果，约 `0.3333333333333333`、`0.6666666666666666`、`1.6666666666666667`）。本测试不期望新旧版本有差异；若出现差异，说明补丁意外影响了 REAL_RESULT 路径。仍需以后验证：`set_numeric_type` 对 DECIMAL+DOUBLE 确实返回 REAL_RESULT。

## T4
候选依据：交接指出两个 INT 操作数时 `hybrid_type` 为 INT_RESULT，不进入补丁；本测试用 INT 除法作为第二个负对照。与其他测试的差异：操作数类型为 INT，结果类型为 INT，验证补丁不改变 INT_RESULT 路径。

```sql
-- 准备
DROP TABLE IF EXISTS t4_src, t4_dst;
CREATE TABLE t4_src (a INT, b INT);
CREATE TABLE t4_dst (s VARCHAR(64), i INT);
INSERT INTO t4_src VALUES (1, 3), (2, 3), (10, 3);

-- 目标 SELECT：INT 除法，hybrid_type 应为 INT_RESULT
SELECT a, b, a / b AS str_form FROM t4_src ORDER BY a;

-- 对照：存入 INT 列
INSERT INTO t4_dst (s, i)
SELECT CAST(a / b AS CHAR), a / b FROM t4_src ORDER BY a;
SELECT s, i FROM t4_dst ORDER BY s;

-- 清理
DROP TABLE t4_src, t4_dst;
```

预期结果：INT 除法结果为整数（MySQL 中 `1/3` 得 `0`，`2/3` 得 `0`，`10/3` 得 `3`），字符串形式与 INT 列应一致。本测试不期望新旧版本有差异。仍需以后验证：INT/INT 除法在目标版本中是否确实为 INT_RESULT（部分版本可能返回 DECIMAL），若为 DECIMAL 则本测试转为正对照。

## T5
候选依据：交接指出 `val_decimal` 仅在 `val->frac > decimals` 时舍入，且乘法也可能产生额外小数位；本测试用 DECIMAL 乘法构造舍入临界案例（如 `2.005` 类），并对照字符串与 DECIMAL 列。与其他测试的差异：运算为乘法而非除法，且使用舍入临界值，检验 HALF_UP 而非截断。

```sql
-- 准备
DROP TABLE IF EXISTS t5_src, t5_dst;
CREATE TABLE t5_src (a DECIMAL(10,3), b DECIMAL(10,3));
CREATE TABLE t5_dst (s VARCHAR(64), d DECIMAL(10,2));
INSERT INTO t5_src VALUES (1.005, 1.000), (2.005, 1.000), (1.234, 1.000);

-- 目标 SELECT：DECIMAL 乘法，结果声明 scale 可能小于内部 scale
SELECT a, b, a * b AS str_form FROM t5_src ORDER BY a;

-- 对照：存入 DECIMAL(10,2) 列
INSERT INTO t5_dst (s, d)
SELECT CAST(a * b AS CHAR), a * b FROM t5_src ORDER BY a;
SELECT s, d FROM t5_dst ORDER BY s;

-- 清理
DROP TABLE t5_src, t5_dst;
```

预期结果：若乘法结果声明 scale 为 2，则 `1.005*1.000` 字符串形式应为 `1.01`（HALF_UP），`2.005*1.000` 为 `2.01`，`1.234*1.000` 为 `1.23`；DECIMAL(10,2) 列应一致。若旧版 `val_decimal` 未舍入，列中可能为 `1.00`/`2.00`/`1.23`（截断）或全精度值，与字符串不一致。仍需以后验证：乘法 `result_precision()` 对该表达式声明的 `decimals` 是否为 2，以及 `1.005` 在 DECIMAL(10,3) 中是否精确表示。

缺口说明：以上五个测试覆盖了 DECIMAL 除法的 `val_decimal`/`val_real` 两条消费路径、REAL_RESULT 与 INT_RESULT 两个负对照、以及乘法临界舍入。仍缺少交接中提到的 `%`/`MOD` 运算、`val->frac > decimals` 边界（恰好等于时不触发）、NULL 操作数对照、以及进位溢出（如 `9.99` 舍入到 `10.00`）的测试；这些因交接未提供 `result_precision()` 源码和具体可复现输入，本轮不构造，留待后续验证。