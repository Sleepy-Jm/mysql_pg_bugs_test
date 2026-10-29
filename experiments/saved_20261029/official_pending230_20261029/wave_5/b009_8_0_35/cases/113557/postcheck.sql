-- Read-only evidence after the unchanged source SQL, same session.
SELECT a,CAST(d AS CHAR) AS stored_json FROM t IGNORE INDEX(iad) ORDER BY a;
EXPLAIN SELECT * FROM t USE INDEX(iad) WHERE a=1;
