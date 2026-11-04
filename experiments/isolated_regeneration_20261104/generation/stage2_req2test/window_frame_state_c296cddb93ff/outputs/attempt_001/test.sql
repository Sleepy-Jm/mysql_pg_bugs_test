-- One fresh connection, already selected disposable schema; table r2t_wf_data absent.
-- Target build must support AVG OVER ROWS, DECIMAL casts, and session windowing_use_high_precision.
-- Single connection, sequential execution, stop on any error. No DISTINCT, no PREPARE needed.
-- Syntax availability and source reachability were not database-tested here.
SET @r2t_wf_saved_precision = @@SESSION.windowing_use_high_precision;
CREATE TEMPORARY TABLE r2t_wf_data (
 p INT NOT NULL, id INT NOT NULL, v DECIMAL(10,0), r DOUBLE, PRIMARY KEY(p,id));
INSERT INTO r2t_wf_data VALUES
 (1,1,60,60),(1,2,180,180),(1,3,120,120),(1,4,300,300),(1,5,240,240),
 (1,6,420,420),(1,7,360,360),(1,8,540,540),(1,9,480,480),
 (2,1,120,120),(2,2,300,300),(3,1,240,240);
-- case_id WF_BASE; C1 R1,R2,R3,R4,R5,R6,R7
SELECT p,id,CAST(AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) AS DECIMAL(18,6)) AS a
FROM r2t_wf_data WHERE p=1 ORDER BY p,id;
-- case_id WF_CURRENT; C2 R3,R4,R5,R6,R7
SELECT p,id,CAST(AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS DECIMAL(18,6)) AS a
FROM r2t_wf_data ORDER BY p,id;
-- case_id WF_UNBOUNDED; C2 R3,R4,R5,R6,R7
SELECT p,id,CAST(AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND UNBOUNDED FOLLOWING) AS DECIMAL(18,6)) AS a
FROM r2t_wf_data ORDER BY p,id;
-- case_id WF_CUMULATIVE; C4 R2,R3,R7
SELECT p,id,CAST(AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS DECIMAL(18,6)) AS a
FROM r2t_wf_data ORDER BY p,id;
-- NULL phase: mutate only our temporary table.
UPDATE r2t_wf_data SET v=NULL,r=NULL WHERE p=1 AND id IN (2,5,8);
INSERT INTO r2t_wf_data VALUES (4,1,NULL,NULL),(4,2,NULL,NULL),(4,3,NULL,NULL);
-- case_id WF_NULLS; C3 R3,R4,R5,R6,R7
SELECT p,id,CAST(AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) AS DECIMAL(18,6)) AS a
FROM r2t_wf_data ORDER BY p,id;
-- case_id WF_EMPTY; C3 R2,R7
SELECT p,id,CAST(AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 FOLLOWING AND 3 FOLLOWING) AS DECIMAL(18,6)) AS a
FROM r2t_wf_data ORDER BY p,id;
SET SESSION windowing_use_high_precision=0;
-- case_id WF_REAL_LOW; C4 R2,R3,R7,R8
SELECT p,id,AVG(r) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) AS a
FROM r2t_wf_data ORDER BY p,id;
SET SESSION windowing_use_high_precision=1;
-- case_id WF_REAL_HIGH; C4 R2,R3,R7,R8
SELECT p,id,AVG(r) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) AS a
FROM r2t_wf_data ORDER BY p,id;
DROP TEMPORARY TABLE r2t_wf_data;
SET SESSION windowing_use_high_precision=@r2t_wf_saved_precision;
-- On error stop, restore saved precision if possible, then close connection.
