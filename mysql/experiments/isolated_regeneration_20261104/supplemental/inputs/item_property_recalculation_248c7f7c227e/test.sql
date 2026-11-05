-- Supplemental attempt: B data reused; IN/PREPARE supplied using historical case knowledge.
CREATE TEMPORARY TABLE sup_values(p INT,id INT,v INT,PRIMARY KEY(p,id));
CREATE TEMPORARY TABLE sup_lookup(k INT);
INSERT INTO sup_values VALUES(1,1,2),(1,2,5),(1,3,11),(1,4,17),(2,1,3),(2,2,NULL);
INSERT INTO sup_lookup VALUES(8),(29),(NULL);
PREPARE sup_stmt FROM 'SELECT p,id,1+SUM(v) OVER w AS wrapped,(1+SUM(v) OVER w) IN (SELECT k FROM sup_lookup) AS in_result FROM sup_values WINDOW w AS (PARTITION BY p ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) ORDER BY p,id';
-- case_id SI_FIRST
EXECUTE sup_stmt;
-- case_id SI_REPEAT
EXECUTE sup_stmt;
-- case_id SI_DIRECT
SELECT p,id,1+SUM(v) OVER w AS wrapped,(1+SUM(v) OVER w) IN (SELECT k FROM sup_lookup) AS in_result FROM sup_values WINDOW w AS (PARTITION BY p ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) ORDER BY p,id;
-- case_id SI_NO_NULL
DELETE FROM sup_lookup WHERE k IS NULL;
EXECUTE sup_stmt;
-- case_id SI_EMPTY
DELETE FROM sup_lookup;
EXECUTE sup_stmt;
-- case_id SI_EMPTY_DIRECT
SELECT p,id,1+SUM(v) OVER w AS wrapped,(1+SUM(v) OVER w) IN (SELECT k FROM sup_lookup) AS in_result FROM sup_values WINDOW w AS (PARTITION BY p ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) ORDER BY p,id;
DEALLOCATE PREPARE sup_stmt;
DROP TEMPORARY TABLE sup_lookup;
DROP TEMPORARY TABLE sup_values;
