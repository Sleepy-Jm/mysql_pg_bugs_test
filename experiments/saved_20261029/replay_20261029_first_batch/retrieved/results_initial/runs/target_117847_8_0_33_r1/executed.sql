USE `replay_fd80f1073be2b84dbfbfd0db`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #117847; source: cmain, c551633
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(c1 DOUBLE);
INSERT INTO t1 VALUES(0);
SELECT NULLIF(-33.26,ref_1.c1) IS NULL AS w1 FROM t1 AS ref_1;
SELECT NULLIF(-33.26,ref_1.c1) IS NULL AS w1 FROM t1 AS ref_1 WHERE NULLIF(-33.26,ref_1.c1) IS NULL;
