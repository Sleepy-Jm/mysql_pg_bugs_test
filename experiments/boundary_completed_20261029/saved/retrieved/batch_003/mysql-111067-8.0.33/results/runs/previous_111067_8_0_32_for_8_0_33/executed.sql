USE `replay_0f01e2da4470c4c8ed8081a8`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111067; source anchors: cmain, c532705
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a CHAR(10), fulltext(a)) ENGINE = InnoDB;
INSERT INTO t1 VALUES('aaa15');
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
ALTER TABLE t1 ADD COLUMN y INT;
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
ANALYZE TABLE t1;
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;

-- Read-only postchecks for report 111067; run in the same disposable schema/session.
SELECT a,y FROM t1;
