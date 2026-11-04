SELECT VERSION() AS version, @@version_comment AS version_comment, @@SESSION.sql_mode AS sql_mode, @@SESSION.div_precision_increment AS div_precision_increment, @@SESSION.windowing_use_high_precision AS windowing_use_high_precision;
-- Prerequisites: target build supports SUM window functions and ROWS FOLLOWING.
-- One fresh connection, an already selected disposable schema; no objects named r2t_ip_data.
-- Run sequentially, stop on any SQL error. No session settings changed.
-- Syntax and internal reachability are unmeasured, not validated by a DB here.
CREATE TEMPORARY TABLE r2t_ip_data (p INT NOT NULL, id INT NOT NULL, v INT, PRIMARY KEY(p,id));
INSERT INTO r2t_ip_data VALUES (1,1,2),(1,2,5),(1,3,11),(1,4,17),(2,1,3),(2,2,NULL);
-- case_id IP_BASE; C1 R1 R2 R6: direct baseline
SELECT p,id,SUM(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS s
FROM r2t_ip_data ORDER BY p,id;
-- case_id IP_WRAP; C1 R1 R2 R6: ordinary arithmetic wrapper
SELECT p,id,1+SUM(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS calc
FROM r2t_ip_data ORDER BY p,id;
-- case_id IP_REF; C3 R3 R6: local projection alias in legal sorting position
SELECT p,id,1+SUM(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS calc
FROM r2t_ip_data ORDER BY calc DESC,p,id;
-- case_id IP_EMPTY_BASE; C1 and partial C4: empty/all-NULL frame precursor, no IN
SELECT p,id,SUM(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 1 FOLLOWING AND 1 FOLLOWING) AS s
FROM r2t_ip_data ORDER BY p,id;
DROP TEMPORARY TABLE r2t_ip_data;
-- On error stop; close this fresh connection to release its temporary table.
