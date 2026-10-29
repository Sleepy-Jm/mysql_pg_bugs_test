USE `replay_05c8bd6a9bd6900bdd420593`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #109833; source anchors: cmain, c529335, c529371
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
CREATE TABLE `vals0` (
  `k` VARCHAR(8) CHARSET utf8mb4 COLLATE utf8mb4_bin NOT NULL PRIMARY KEY
);
INSERT INTO `vals0` VALUES ('OK');

CREATE TABLE `vals1` (
  `k` VARCHAR(8) CHARSET utf8mb4 COLLATE utf8mb4_bin NOT NULL PRIMARY KEY
);
INSERT INTO `vals1` VALUES ('ERRÖR');

-- this works as expected
SELECT * FROM `vals1` WHERE `k` = 'ERRÖR';

-- this works as expected
-- Original undefined view_vals control omitted; use the complete derived query below.

-- this returns empty result set, and a warning about converting D6 to utf8
SELECT * FROM (SELECT `v0`.`k` AS `k` FROM `vals0` AS `v0` UNION ALL SELECT `v1`.`k` AS `k` FROM `vals1` as `v1`) AS `a` WHERE `a`.`k` = 'ERRÖR';
SHOW WARNINGS;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT k,HEX(k) AS hex_k FROM vals0;
SELECT k,HEX(k) AS hex_k FROM vals1;
