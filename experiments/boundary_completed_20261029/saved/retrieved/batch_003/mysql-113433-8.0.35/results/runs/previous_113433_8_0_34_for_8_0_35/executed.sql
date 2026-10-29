USE `replay_9e3c4f43b6e9945096c0b93a`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113433; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `tt` (
  `id_col` int NOT NULL,
  `bigint_col` bigint NOT NULL,
  `year_col` year DEFAULT NULL,
  KEY `ndx_year_col` (`year_col` DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT into tt values (61,-9223372036854775808,'1913');

SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col;
SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col AND A.id_col = 61;
SELECT A.year_col, A.id_col FROM tt A WHERE 61 < A.year_col;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT id_col,year_col,bigint_col FROM tt;
