-- Report #111304; source anchors: cmain, c533246
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE DATABASE test_jfg;
CREATE TABLE test_jfg.t(id INT PRIMARY KEY,v INT);
INSERT INTO test_jfg.t VALUES(1,1),(2,2),(3,3);
SELECT id,v FROM test_jfg.t ORDER BY id LIMIT 1 OFFSET 2;
INSERT INTO query_rewrite.rewrite_rules (pattern,replacement) VALUES('select id, v from test_jfg.t order by id limit ? offset ?','select id, v + 1 from test_jfg.t order by id limit ? offset ?');
SET @case_rule1=LAST_INSERT_ID();
CALL query_rewrite.flush_rewrite_rules();
SELECT id,v FROM test_jfg.t ORDER BY id LIMIT 1 OFFSET 2;
SHOW WARNINGS;

DELETE FROM query_rewrite.rewrite_rules WHERE id=@case_rule1;
INSERT INTO query_rewrite.rewrite_rules(pattern,replacement) VALUES('select id, v from test_jfg.t order by id limit ? offset ?','select id, v + 1 from test_jfg.t order by id limit ?, ?');
SET @case_rule1=LAST_INSERT_ID();
CALL query_rewrite.flush_rewrite_rules();
SELECT id,v FROM test_jfg.t ORDER BY id LIMIT 1 OFFSET 2;
SHOW WARNINGS;
