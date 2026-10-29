-- Read-only postcheck appended after unchanged source SQL.
SELECT * FROM t_cte1 ORDER BY id; SELECT * FROM t_cte2 ORDER BY id; SELECT CAST(id AS UNSIGNED) AS id FROM t_cte2 WHERE val>15 ORDER BY id;
