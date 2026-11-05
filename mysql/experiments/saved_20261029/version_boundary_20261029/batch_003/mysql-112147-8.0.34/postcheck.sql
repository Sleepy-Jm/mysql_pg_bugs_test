-- Read-only evidence after the unchanged source SQL, same session.
SELECT a,CAST(j AS CHAR) AS stored_json,JSON_TYPE(JSON_EXTRACT(j,'$[0]')) AS element_type FROM t;
SELECT @@session.sql_mode;
