USE `replay_0774a6962fff374a149c6426`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111737; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE TABLE tab(col VARCHAR(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,CONSTRAINT cons CHECK(col REGEXP '''+')) ENGINE=InnoDB;
DROP TABLE tab;
SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_BACKSLASH_ESCAPES';
CREATE TABLE tab(col VARCHAR(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,CONSTRAINT cons CHECK(col REGEXP '''+')) ENGINE=InnoDB;
SELECT 'aaa' REGEXP '''+';
SELECT 'a''aa' REGEXP '''+';

-- Read-only postchecks for report 111737; run in the same disposable schema/session.
SELECT @@sql_mode; SELECT COUNT(*) AS tab_exists FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='tab';
