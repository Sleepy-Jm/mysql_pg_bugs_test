-- T5: C4 — IS NULL over a non-nullable aggregate child
-- Sensitive property: PROP_AGGREGATION on the IS NULL item. Target
-- unconditionally propagates args[0]'s accumulated properties before the
-- is_nullable() check; parent skipped propagation when args[0] was
-- non-nullable. Use a constant-false IS NULL over a non-nullable aggregate.
CREATE TEMPORARY TABLE t5_agg (id INT PRIMARY KEY, g INT NOT NULL, v INT NOT NULL);
INSERT INTO t5_agg VALUES (1, 1, 10), (2, 1, 20), (3, 2, 5), (4, 2, 7);

SELECT g, (SUM(v) IS NULL) AS r
FROM t5_agg
GROUP BY g
ORDER BY g;

-- Contrast: same aggregate without the IS NULL wrapper, to show the
-- aggregate value itself is non-NULL and the IS NULL result is constant false.
SELECT g, SUM(v) AS s
FROM t5_agg
GROUP BY g
ORDER BY g;

DROP TEMPORARY TABLE t5_agg;
