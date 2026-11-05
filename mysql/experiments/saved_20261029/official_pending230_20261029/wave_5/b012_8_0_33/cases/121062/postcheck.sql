-- Read-only evidence after the unchanged source SQL, same session.
SELECT id,a,b FROM t;
SELECT CURRENT_DATE(),@@session.sql_mode,@@session.time_zone;
