-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows FROM t0;
SELECT @@session.sql_mode;
