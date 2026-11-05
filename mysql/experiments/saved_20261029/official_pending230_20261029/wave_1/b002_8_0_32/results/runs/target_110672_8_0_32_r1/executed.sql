USE `replay_ff23752a1fad091880962932`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110672; source anchors: cmain, c531731
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE LATIN1_TABLE (
  COLUMN1 varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO LATIN1_TABLE (COLUMN1) VALUES (NULL);
INSERT INTO LATIN1_TABLE (COLUMN1) VALUES ('NOTNULL');

SELECT QUOTE(COLUMN1) FROM LATIN1_TABLE; -- returns NULL, and 'NOTNULL' as expected.

CREATE TABLE UTF16_TABLE (
  COLUMN1 varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO UTF16_TABLE (COLUMN1) VALUES (NULL);
INSERT INTO UTF16_TABLE (COLUMN1) VALUES ('NOTNULL');

SELECT QUOTE(COLUMN1) FROM UTF16_TABLE; -- returns Japanese/Mojibake and 'NOTNULL'.
SELECT HEX(QUOTE(COLUMN1)),CHARSET(QUOTE(COLUMN1)),QUOTE(COLUMN1) IS NULL FROM UTF16_TABLE;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT HEX(QUOTE(COLUMN1)) AS quoted_hex,CHARSET(QUOTE(COLUMN1)) AS result_charset,QUOTE(COLUMN1) IS NULL AS is_sql_null FROM LATIN1_TABLE;
SELECT COUNT(*) AS loaded_rows,SUM(COLUMN1 IS NULL) AS null_rows FROM UTF16_TABLE;
