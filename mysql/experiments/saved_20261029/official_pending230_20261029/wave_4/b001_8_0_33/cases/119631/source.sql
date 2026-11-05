-- MySQL report #119631; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t_cte1(id INT,val INT);
CREATE TABLE t_cte2(id VARCHAR(20),val INT);
INSERT INTO t_cte1 VALUES(1,10),(2,20),(3,30);
INSERT INTO t_cte2 VALUES('1',10),('2',25),('4',40);
SELECT id, val FROM t_cte1 
WHERE id IN (SELECT CAST(id AS UNSIGNED) FROM t_cte2 WHERE val > 15)
ORDER BY id;
WITH cte AS (
  SELECT CAST(id AS UNSIGNED) AS id FROM t_cte2 WHERE val > 15
)
SELECT id, val FROM t_cte1 
WHERE id IN (SELECT id FROM cte)
ORDER BY id;
WITH cte AS (
  SELECT CAST(id AS UNSIGNED) AS id FROM t_cte2 WHERE val > 15
)
SELECT id, val FROM t_cte1 t1
WHERE EXISTS (SELECT 1 FROM cte WHERE cte.id = t1.id)
ORDER BY id;
