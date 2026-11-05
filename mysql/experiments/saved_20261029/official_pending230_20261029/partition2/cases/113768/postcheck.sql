-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows,MIN(a) AS min_value,MAX(a) AS max_value FROM tb;
SELECT @@session.sql_mode;
