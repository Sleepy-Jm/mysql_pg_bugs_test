## T1
依据：交接 §1.3/§2.3 指出 predicate push-down 会把外层 WHERE 中的 `IN (SELECT ...)` 复制进 FROM 子查询，`sqlite3SelectDup` 保留 `selId`，从而产生两个共享 `selId` 的 IN RHS。本测试用确定性 RHS，验证复用后结果集与“逻辑上只有一个 IN 条件”的参考改写一致。与其他测试的差异：这是基线正例，RHS 确定、affinity 与 collation 均一致，只考察复用是否改变结果集。

```sql
-- 准备
CREATE TABLE t1(a INTEGER, b TEXT);
INSERT INTO t1 VALUES (1,'x'),(2,'y'),(3,'z'),(4,'w'),(5,'v');
CREATE TABLE t2(k INTEGER);
INSERT INTO t2 VALUES (2),(4);

-- 目标 SELECT：外层 WHERE 的 IN 可被下推进 FROM 子查询
SELECT a, b FROM (SELECT a, b FROM t1) AS s
WHERE a IN (SELECT k FROM t2)
ORDER BY a;

-- 对照：等价改写，逻辑上只有一个 IN 条件
SELECT a, b FROM t1
WHERE a IN (SELECT k FROM t2)
ORDER BY a;

-- 清理
DROP TABLE t1;
DROP TABLE t2;
```

预期结果：目标 SELECT 返回 `(2,'y')`、`(4,'w')` 两行，按 a 升序；对照 SELECT 返回相同两行。两者应完全一致。仍需以后验证：目标 SELECT 的 VDBE 是否真的出现 `REUSE LIST SUBQUERY` / `OP_OpenDup`，即是否命中复用路径；本测试只核对结果集语义。

## T2
依据：交接 §2.2 风险 1 指出源码未检查 RHS 是否含非确定函数，复用会导致 RHS 只求值一次。本测试用 `random()` 构造 RHS，使两次独立求值几乎必然不同；正确语义下（逻辑上只有一个 IN 条件）应等价于“RHS 只物化一次”。与其他测试的差异：唯一考察非确定 RHS 的复用语义，用显式物化一次的参考改写作为 oracle。

```sql
-- 准备
CREATE TABLE t3(a INTEGER);
INSERT INTO t3 VALUES (1),(2),(3),(4),(5),(6),(7),(8);

-- 目标 SELECT：RHS 含 random()，若被复用则只求值一次
SELECT count(*) FROM (SELECT a FROM t3) AS s
WHERE a IN (SELECT (abs(random()) % 8) + 1 FROM t3);

-- 对照：显式把 RHS 物化一次，再让 IN 使用同一结果集
WITH rhs AS MATERIALIZED (
  SELECT (abs(random()) % 8) + 1 AS k FROM t3
)
SELECT count(*) FROM t3
WHERE a IN (SELECT k FROM rhs);

-- 清理
DROP TABLE t3;
```

预期结果：目标 SELECT 与对照 SELECT 都返回 0 到 8 之间的整数（具体值依赖随机数，无法预先确定）。关键预期是：目标 SELECT 的计数应等于“RHS 只求值一次”的语义结果，即与对照 SELECT 的分布一致，而不是两次独立求值 RHS 的语义。仍需以后验证：目标 SELECT 是否真的只物化一次 RHS（VDBE 中只有一个 RHS 子例程）；以及 SQL 标准对非确定 RHS 在重复 IN 中的求值次数定义，本测试以“逻辑上只有一个 IN 条件”为 oracle 前提。

## T3
依据：交接 §2.2 风险 2/3 指出 `SubrtnSig` 只含 `selId` 与 `zAff`，不含 collation；`zAff` 来自 `exprINAffinity`，只编码 affinity。本测试构造相同 affinity、不同 collation 的 LHS，考察复用是否忽略 collation 差异。与其他测试的差异：唯一考察 collation 维度，且用 `COLLATE NOCASE` 与默认 BINARY 对照。

```sql
-- 准备
CREATE TABLE t4(a TEXT);
INSERT INTO t4 VALUES ('A'),('b'),('C'),('d');
CREATE TABLE t5(k TEXT);
INSERT INTO t5 VALUES ('a'),('B');

-- 目标 SELECT：外层 IN 的 LHS 带 NOCASE collation，可被下推
SELECT a FROM (SELECT a FROM t4) AS s
WHERE a COLLATE NOCASE IN (SELECT k FROM t5)
ORDER BY a;

-- 对照：等价改写，逻辑上只有一个 IN 条件，collation 显式
SELECT a FROM t4
WHERE a COLLATE NOCASE IN (SELECT k FROM t5)
ORDER BY a;

-- 清理
DROP TABLE t4;
DROP TABLE t5;
```

预期结果：目标 SELECT 返回 `'A'`、`'b'` 两行（NOCASE 下 'A' 匹配 'a'，'b' 匹配 'B'），按 a 升序；对照 SELECT 返回相同两行。两者应一致。仍需以后验证：该 SQL 是否真的到达 `findCompatibleInRhsSubrtn`（即两个 IN 是否共享 `selId` 且 `zAff` 相同）；若到达，复用是否因未编码 collation 而改变结果。本测试只核对结果集语义。

## T4
依据：交接 §1.2 条件 2 指出 `SF_All` 的 RHS 不创建 `SubrtnSig`，§2.3 建议用 `UNION ALL` RHS 作负对照。本测试用 `UNION ALL` 构造 RHS，验证该路径不复用、结果与参考改写一致。与其他测试的差异：唯一考察 `SF_All` 负对照，验证排除条件不改变结果集。

```sql
-- 准备
CREATE TABLE t6(a INTEGER);
INSERT INTO t6 VALUES (1),(2),(3),(4),(5);
CREATE TABLE t7(k INTEGER);
INSERT INTO t7 VALUES (2),(4);
CREATE TABLE t8(k INTEGER);
INSERT INTO t8 VALUES (3),(5);

-- 目标 SELECT：RHS 为 UNION ALL，应被 SF_All 排除复用
SELECT a FROM (SELECT a FROM t6) AS s
WHERE a IN (SELECT k FROM t7 UNION ALL SELECT k FROM t8)
ORDER BY a;

-- 对照：等价改写
SELECT a FROM t6
WHERE a IN (SELECT k FROM t7 UNION ALL SELECT k FROM t8)
ORDER BY a;

-- 清理
DROP TABLE t6;
DROP TABLE t7;
DROP TABLE t8;
```

预期结果：目标 SELECT 返回 `2,3,4,5` 四行，按 a 升序；对照 SELECT 返回相同四行。两者应一致。仍需以后验证：目标 SELECT 的 VDBE 中是否确实没有 `P4_SUBRTNSIG` / `OP_OpenDup`（即 `SF_All` 排除生效）；本测试只核对结果集语义。

## T5
依据：交接 §1.2 条件 1 指出相关子查询（`EP_VarSelect`）不进入复用路径，§2.3 建议用相关子查询作负对照。本测试构造相关 RHS，验证不复用且结果与参考改写一致。与其他测试的差异：唯一考察相关性负对照，且 RHS 依赖外层列，考察执行分支差异。

```sql
-- 准备
CREATE TABLE t9(a INTEGER, b INTEGER);
INSERT INTO t9 VALUES (1,10),(2,20),(3,30),(4,40);
CREATE TABLE t10(k INTEGER, m INTEGER);
INSERT INTO t10 VALUES (1,10),(2,99),(3,30),(4,99);

-- 目标 SELECT：RHS 相关子查询，引用外层 s.b
SELECT a, b FROM (SELECT a, b FROM t9) AS s
WHERE a IN (SELECT k FROM t10 WHERE t10.m = s.b)
ORDER BY a;

-- 对照：等价改写
SELECT a, b FROM t9
WHERE a IN (SELECT k FROM t10 WHERE t10.m = t9.b)
ORDER BY a;

-- 清理
DROP TABLE t9;
DROP TABLE t10;
```

预期结果：目标 SELECT 返回 `(1,10)`、`(3,30)` 两行（a=1 时 b=10 匹配 t10 的 (1,10)；a=3 时 b=30 匹配 (3,30)），按 a 升序；对照 SELECT 返回相同两行。两者应一致。仍需以后验证：目标 SELECT 的 VDBE 中是否确实没有 `P4_SUBRTNSIG`（即 `EP_VarSelect` 排除生效）；本测试只核对结果集语义。

---

说明：以上五个测试分别覆盖交接中源码直接支持的正例（T1）、非确定 RHS 推断风险（T2）、collation 推断风险（T3）、`SF_All` 负对照（T4）、相关子查询负对照（T5）。交接 §1.4 提到的虚拟表 `IN (SELECT ...)` 路径（`sqlite3WhereCodeOneLoopStart`）因需要虚拟表扩展，超出“不使用扩展下载”的脚本约束，未构造独立测试，构成一个有依据的缺口。所有预期值均依据 SQL 语义与交接中的源码条件推导，未执行、未观察、未声称命中缺陷。