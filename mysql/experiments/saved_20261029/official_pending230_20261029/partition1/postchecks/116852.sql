-- Read-only postcheck appended after unchanged source SQL.
SELECT id,t,CAST(j AS CHAR) FROM mvi IGNORE INDEX(index1,index2) ORDER BY id; SHOW CREATE TABLE mvi; EXPLAIN SELECT * FROM mvi FORCE INDEX(index1) WHERE t=1 ORDER BY id; EXPLAIN SELECT * FROM mvi FORCE INDEX(index2) WHERE t=1 ORDER BY id;
