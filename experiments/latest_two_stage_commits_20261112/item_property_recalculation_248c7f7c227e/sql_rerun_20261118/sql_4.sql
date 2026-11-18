-- T4: C3 (exploratory) — window function under an ordinary Item_func container
-- Sensitive property: PROP_WINDOW_FUNCTION on the container; downstream
-- CreateFramebufferTable checks has_wf(). Use a windowed SUM over a
-- partitioned, ordered input so materialization is required.
CREATE TEMPORARY TABLE t4_wf (id INT PRIMARY KEY, g INT NOT NULL, v INT NOT NULL);
INSERT INTO t4_wf VALUES (1, 1, 10), (2, 1, 20), (3, 2, 5), (4, 2, 7);

SELECT id, g, v,
       SUM(v) OVER (PARTITION BY g ORDER BY id) + 1 AS r
FROM t4_wf
ORDER BY id;

-- Contrast: IS NULL over the same windowed expression, exercising the
-- Item_func_isnull container over a window-function child.
SELECT id, g, v,
       (SUM(v) OVER (PARTITION BY g ORDER BY id) + 1) IS NULL AS r
FROM t4_wf
ORDER BY id;

DROP TEMPORARY TABLE t4_wf;
