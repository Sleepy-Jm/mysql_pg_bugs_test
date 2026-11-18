-- T3: C2 (exploratory) — Item_in_optimizer wrapping an IN subquery
-- Sensitive property: PROP_SUBQUERY on the Item_in_optimizer wrapper.
-- Target reset may clear it if args[0] does not re-set it. Use a NOT IN
-- with a NULL in the subquery result to exercise the three-valued branch.
CREATE TEMPORARY TABLE t3_outer (id INT PRIMARY KEY, x INT NULL);
INSERT INTO t3_outer VALUES (1, 1), (2, 2), (3, NULL), (4, 4);
CREATE TEMPORARY TABLE t3_inner (y INT NULL);
INSERT INTO t3_inner VALUES (1), (NULL), (3);

SELECT id, x, x IN (SELECT y FROM t3_inner) AS r
FROM t3_outer
ORDER BY id;

-- Contrast: NOT IN over the same subquery; NULL in the subquery makes the
-- result UNKNOWN for non-matching rows, exercising the wrapper's branch.
SELECT id, x, x NOT IN (SELECT y FROM t3_inner) AS r
FROM t3_outer
ORDER BY id;

DROP TEMPORARY TABLE t3_inner;
DROP TEMPORARY TABLE t3_outer;
