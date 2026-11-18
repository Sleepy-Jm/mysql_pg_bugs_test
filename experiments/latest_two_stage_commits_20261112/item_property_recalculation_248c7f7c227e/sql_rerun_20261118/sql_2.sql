-- T2: C1 — outer Item_func (comparison) with a NULL-producing scalar subquery
-- Sensitive operand: the replaced field can be NULL; the comparison must
-- evaluate against the derived-table field, not a stale subquery marker.
CREATE TEMPORARY TABLE t2_outer (id INT PRIMARY KEY, k INT NOT NULL);
INSERT INTO t2_outer VALUES (1, 10), (2, 20), (3, 30);
CREATE TEMPORARY TABLE t2_inner (k INT NOT NULL, v INT NULL);
INSERT INTO t2_inner VALUES (10, NULL), (20, 5), (30, 0);

SELECT id, k, ((SELECT v FROM t2_inner WHERE t2_inner.k = t2_outer.k) > 0) AS r
FROM t2_outer
ORDER BY id;

-- Contrast: IS NULL over the same replaced scalar subquery, exercising the
-- Item_func_isnull container on the same replaced field.
SELECT id, k, ((SELECT v FROM t2_inner WHERE t2_inner.k = t2_outer.k) IS NULL) AS r
FROM t2_outer
ORDER BY id;

DROP TEMPORARY TABLE t2_inner;
DROP TEMPORARY TABLE t2_outer;
