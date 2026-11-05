-- MySQL report #112959; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE DATABASE test_jfg;
CREATE TABLE test_jfg.t(id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,v1 INT NOT NULL,v2 INT NOT NULL,KEY(v1),KEY(v2));
INSERT INTO test_jfg.t(v1,v2) VALUES(1,1),(2,2),(3,3);
EXPLAIN SELECT COUNT(*) FROM test_jfg.t WHERE v1=1 OR v2=2;
TRUNCATE TABLE performance_schema.events_statements_summary_by_digest;
TRUNCATE mysql.slow_log;
FLUSH STATUS;
SELECT COUNT(*) FROM test_jfg.t WHERE v1=1 OR v2=2;
SHOW SESSION STATUS LIKE 'Handler_read%';
SELECT DIGEST_TEXT,SUM_ROWS_EXAMINED FROM performance_schema.events_statements_summary_by_digest WHERE DIGEST_TEXT LIKE '%test_jfg%';
SELECT rows_examined,sql_text FROM mysql.slow_log WHERE sql_text LIKE '%test_jfg%' AND sql_text NOT LIKE '%events%';
