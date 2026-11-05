-- Read-only postcheck appended after unchanged source SQL.
SELECT c14,COUNT(*) AS n FROM t1 GROUP BY c14 ORDER BY c14;
