USE `replay_264c014a36fde60132ddc374`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113768; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table tb(a bigint);
insert into tb values(9223372036854775807),(-9223372036854775808);
SELECT 1 FROM tb A WHERE (A.a, A.a) NOT IN  ((CAST(9223372036854775807 AS REAL),CAST(110 AS SIGNED INTEGER)),(CAST(92 AS REAL),CAST(NULL AS SIGNED INTEGER)));
SELECT CAST(9223372036854775807 AS REAL);
SHOW WARNINGS;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows,MIN(a) AS min_value,MAX(a) AS max_value FROM tb;
SELECT @@session.sql_mode;
