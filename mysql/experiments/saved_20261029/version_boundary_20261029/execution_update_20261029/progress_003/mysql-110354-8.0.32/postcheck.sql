-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows,COUNT(b) AS nonnull_b,SUM(b<'06:59:59') AS lower_rows,@@session.sql_mode AS actual_mode,@@session.time_zone AS actual_tz FROM tt;
