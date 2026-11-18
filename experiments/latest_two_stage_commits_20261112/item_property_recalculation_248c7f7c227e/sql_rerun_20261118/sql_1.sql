-- T1: C1 — outer Item_func (arithmetic) containing a scalar subquery
-- Sensitive operand: the scalar subquery value reaches the outer Item_func
-- via the derived-table field after replacement. Use a negative value so
-- the arithmetic result differs from a naive positive-only assumption.
CREATE TEMPORARY TABLE t1_outer (id INT PRIMARY KEY, k INT NOT NULL);
INSERT INTO t1_outer VALUES (1, 10), (2, 20), (3, 30);
CREATE TEMPORARY TABLE t1_inner (k INT NOT NULL, v INT NOT NULL);
INSERT INTO t1_inner VALUES (10, -7), (20, 5), (30, 0);

SELECT id, k, (SELECT v FROM t1_inner WHERE t1_inner.k = t1_outer.k) + 1 AS r
FROM t1_outer
ORDER BY id;

-- Contrast: same shape but with a positive-only inner value, to show the
-- outer Item_func sees the replaced field value, not a stale subquery.
SELECT id, k, (SELECT v FROM t1_inner WHERE t1_inner.k = t1_outer.k AND v > 0) + 1 AS r
FROM t1_outer
ORDER BY id;

DROP TEMPORARY TABLE t1_inner;
DROP TEMPORARY TABLE t1_outer;
