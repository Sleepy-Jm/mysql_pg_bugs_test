-- Read-only evidence after the unchanged source SQL, same session.
SELECT HEX(QUOTE(COLUMN1)) AS quoted_hex,CHARSET(QUOTE(COLUMN1)) AS result_charset,QUOTE(COLUMN1) IS NULL AS is_sql_null FROM LATIN1_TABLE;
SELECT COUNT(*) AS loaded_rows,SUM(COLUMN1 IS NULL) AS null_rows FROM UTF16_TABLE;
