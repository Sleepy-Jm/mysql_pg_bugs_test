-- MySQL report #119630; source: cmain, c555462, c555698, c555719
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
-- Step 1: Create test tables
DROP TABLE IF EXISTS t_bug_mat1, t_bug_mat2;
CREATE TABLE t_bug_mat1 (id INT, val INT);
CREATE TABLE t_bug_mat2 (id VARCHAR(20), num_val INT);
INSERT INTO t_bug_mat1 VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t_bug_mat2 VALUES ('1', 10), ('2', 25), ('4', 40);


SELECT id, val FROM t_bug_mat1 
WHERE id IN (SELECT CAST(id AS UNSIGNED) FROM t_bug_mat2 WHERE num_val > 15)
ORDER BY id;
SELECT t1.id, t1.val  FROM t_bug_mat1 t1 WHERE t1.id IN (   SELECT /*+ NO_MERGE(subq) */ casted_id FROM (     SELECT CAST(id AS UNSIGNED) AS casted_id      FROM t_bug_mat2      WHERE num_val > 15   ) AS subq ) ORDER BY t1.id;
SELECT t1.id, t1.val FROM t_bug_mat1 t1 WHERE t1.id IN (   SELECT casted_id FROM (     SELECT CAST(id AS UNSIGNED) AS casted_id FROM t_bug_mat2 WHERE num_val > 15   ) AS subq ) ORDER BY t1.id;
