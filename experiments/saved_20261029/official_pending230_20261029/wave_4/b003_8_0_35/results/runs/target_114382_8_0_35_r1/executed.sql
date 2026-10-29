USE `replay_b071342b784fe208d8befc55`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #114382; source anchors: cmain, c541572, c541690
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE IF NOT EXISTS t1(c0 TINYINT(199)) ;
INSERT LOW_PRIORITY IGNORE INTO t1(c0) VALUES (1950654919);

SELECT f1 FROM (SELECT (LEAST(CURDATE(), (- (t1.c0)), (~ (t1.c0)),  EXISTS (SELECT 1))) AS f1 FROM t1) as t WHERE (f1) & (921571774);

SELECT f1 FROM (SELECT (LEAST(CURDATE(), (- (t1.c0)), (~ (t1.c0)),  EXISTS (SELECT 1))) AS f1, ((LEAST(CURDATE(), (- (t1.c0)), (~ (t1.c0)),  EXISTS (SELECT 1))) & (921571774)) IS TRUE AS flag FROM t1) as t WHERE flag=1;

-- Read-only postcheck appended after unchanged source SQL.
SELECT c0 FROM t1; SELECT CURDATE(),@@session.timestamp,@@session.time_zone,@@session.sql_mode;
