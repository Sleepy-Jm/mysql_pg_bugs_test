USE `replay_1599c695329b0480b39aa92f`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #112147; source anchors: cmain, c535553, c535600
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t(a INT,j JSON,INDEX kj((CAST(j AS DATE ARRAY))));
INSERT INTO t VALUES(1,JSON_ARRAY(CAST("2010-10-10" AS DATE),CAST("2010-10-10" AS DATE)));
SELECT * FROM t USE INDEX(kj) WHERE "2010-10-10" MEMBER OF(j);
SELECT * FROM t IGNORE INDEX(kj) WHERE "2010-10-10" MEMBER OF(j);
SELECT * FROM t IGNORE INDEX(kj) WHERE DATE'2010-10-10' MEMBER OF(j);

-- Read-only evidence after the unchanged source SQL, same session.
SELECT a,CAST(j AS CHAR) AS stored_json,JSON_TYPE(JSON_EXTRACT(j,'$[0]')) AS element_type FROM t;
SELECT @@session.sql_mode;
