USE `replay_9a06385e9e8b7f09c3b17377`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113304; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='';
CREATE TABLE t0(c0 LONGTEXT) ;
INSERT INTO t0(c0) VALUES(0.1);
CREATE TABLE t1(c0 INT ZEROFILL PRIMARY KEY) ;
INSERT IGNORE INTO t1(c0) VALUES(NULL);

SELECT !((LEAST(t0.c0, t1.c0)) || (t1.c0)) FROM t1, t0; -- {0}
SELECT * FROM t1, t0 WHERE !((LEAST(t0.c0, t1.c0)) || (t1.c0)); -- {0000000000, 0.1}

-- Read-only postcheck appended after unchanged source SQL.
SELECT c0,HEX(c0) FROM t0; SELECT c0,c0+0 FROM t1; SELECT @@sql_mode;
