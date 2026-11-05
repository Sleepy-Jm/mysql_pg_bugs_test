USE `replay_2b08a2130fd32e5253185492`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110771; source anchors: cmain, c533650, c546398
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(a INT,b INT,KEY(b)) ENGINE=InnoDB ROW_FORMAT=REDUNDANT;
INSERT INTO t1 VALUES(0,0),(1,1),(2,2);
ALTER TABLE t1 ADD COLUMN c VARCHAR(25) DEFAULT NULL,ALGORITHM=INSTANT;
UPDATE t1 SET c='' WHERE a=0;
SELECT a,b,c,c IS NULL,LENGTH(c) FROM t1 ORDER BY a;

-- Read-only evidence after the unchanged source SQL, same session.
SHOW TABLE STATUS LIKE 't1';
