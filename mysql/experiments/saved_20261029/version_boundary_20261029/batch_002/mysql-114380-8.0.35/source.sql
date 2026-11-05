-- Report #114380; source anchors: cmain, c541693
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0(c1 FLOAT) ;
INSERT INTO t0(c1) VALUES(0.1);

SELECT f1 FROM (SELECT (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) AS f1 FROM t0) as t WHERE f1;

SELECT f1 FROM (SELECT (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) AS f1, (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) IS TRUE AS flag FROM t0) as t WHERE flag=1;
