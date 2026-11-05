-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows,COUNT(DISTINCT c1+0) AS distinct_values FROM t5;
