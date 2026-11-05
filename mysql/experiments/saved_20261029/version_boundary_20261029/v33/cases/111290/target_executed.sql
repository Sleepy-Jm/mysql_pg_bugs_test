USE `replay_b3a8f0e2f2bf5f701c65abd5`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111290; source anchors: cmain, c533278, c535147
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
DROP TABLE IF EXISTS `foos`;
DROP TABLE IF EXISTS `bars`;
DROP TABLE IF EXISTS `parents`;

CREATE TABLE `parents` (
  `id` binary(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE `foos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `parent_id` varbinary(16) NOT NULL,
  `text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_foos_on_parent_id` (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12345 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE `bars` (
  `id` binary(16) NOT NULL,
  `parent_id` varbinary(16) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_bars_on_parent_id` (`parent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Create some test data
INSERT INTO parents VALUES (0x93222796caba43ca979f5c96eb6898b7);
INSERT INTO foos (parent_id, text) SELECT parents.id, 'correct output' FROM parents;
INSERT INTO bars (id, parent_id) SELECT 0x79cea9ab6fe14a8ebdfed711a7727763, parents.id FROM parents;

-- Reproduce the problem:
SELECT foos.text
FROM foos
JOIN parents ON parents.id = foos.parent_id
JOIN bars ON bars.parent_id = parents.id
WHERE bars.parent_id = 0x93222796caba43ca979f5c96eb6898b7;

-- Read-only postcheck appended after unchanged source SQL.
SELECT HEX(id),OCTET_LENGTH(id) FROM parents; SELECT HEX(parent_id),OCTET_LENGTH(parent_id),text FROM foos; SELECT HEX(parent_id),OCTET_LENGTH(parent_id) FROM bars;
