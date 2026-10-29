-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows,COUNT(time_col) AS nonnull_time_rows FROM test;
