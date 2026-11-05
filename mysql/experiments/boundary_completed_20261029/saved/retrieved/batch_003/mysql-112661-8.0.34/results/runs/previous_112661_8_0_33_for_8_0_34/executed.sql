USE `replay_cdaba9d77217228904dc48ee`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112661; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE table1 ( v0 TEXT NOT NULL , v1 TINYTEXT , v2 VARCHAR(255) DEFAULT 'v21' , v3 TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , v4 TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , v5 FLOAT NOT NULL DEFAULT 1450916748.971549286 , v6 LONGTEXT NOT NULL , v7 DATE NOT NULL DEFAULT '1983-03-19 15:11:54.823209' ) ENGINE = ARCHIVE CHARACTER SET=latin1 COLLATE=latin1_bin;
CREATE INDEX index0 ON table1 (v4) USING BTREE;

-- Read-only postchecks for report 112661; run in the same disposable schema/session.
SHOW CREATE TABLE table1; SHOW INDEX FROM table1; SHOW ENGINES; SELECT @@sql_mode;
