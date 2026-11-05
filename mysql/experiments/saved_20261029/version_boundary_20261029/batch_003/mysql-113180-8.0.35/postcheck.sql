-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT c0,c1,SIN(1150199883) AS sin_value,SIN(1150199883) IS NULL AS sin_is_null FROM t0;
