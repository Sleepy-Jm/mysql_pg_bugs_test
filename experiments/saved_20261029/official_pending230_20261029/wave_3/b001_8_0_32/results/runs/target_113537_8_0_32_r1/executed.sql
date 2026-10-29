USE `replay_c07385b1273516cbf063b264`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113537; source anchors: cmain, c539414, c539449
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET NAMES utf8mb4;
SELECT LOCATE(x'00','abcdef'),LOCATE(x'00','abcdéf'),LOCATE(x'00',CAST('abcdéf' AS BINARY));

SELECT
    LOCATE(UNHEX('00'), "😂"),
    LOCATE(UNHEX('01'), "😂"),
    LOCATE(UNHEX('02'), "😂"),
    LOCATE(UNHEX('03'), "😂"),
    LOCATE(UNHEX('04'), "😂"),
    LOCATE(UNHEX('05'), "😂"),
    LOCATE(UNHEX('06'), "😂"),
    LOCATE(UNHEX('07'), "😂"),
    LOCATE(UNHEX('08'), "😂"),
    LOCATE(UNHEX('09'), "😂"),
    LOCATE(UNHEX('0A'), "😂"),
    LOCATE(UNHEX('0B'), "😂"),
    LOCATE(UNHEX('0C'), "😂"),
    LOCATE(UNHEX('0D'), "😂"),
    LOCATE(UNHEX('0E'), "😂"),
    LOCATE(UNHEX('0F'), "😂"),
    LOCATE(UNHEX('10'), "😂")
;

-- Read-only postcheck appended after unchanged source SQL.
SELECT HEX('abcdéf'),HEX('😂'),@@character_set_connection,@@collation_connection,@@sql_mode;
