-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows FROM t1;
EXPLAIN SELECT AVG(DISTINCT b) FROM t1 FORCE INDEX(PRIMARY);
EXPLAIN SELECT AVG(DISTINCT b) FROM t1;
