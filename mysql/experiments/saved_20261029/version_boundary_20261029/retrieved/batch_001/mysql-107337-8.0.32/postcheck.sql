-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT COUNT(*) AS loaded_rows, MIN(a) AS min_a, MAX(a) AS max_a FROM t;
