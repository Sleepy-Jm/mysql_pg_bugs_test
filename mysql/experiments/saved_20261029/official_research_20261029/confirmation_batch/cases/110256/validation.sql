-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT COUNT(*) AS loaded_rows,MIN(c0) AS min_value,MAX(c0) AS max_value FROM t0;
