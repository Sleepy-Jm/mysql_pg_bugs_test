-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT id_col,timestamp_col,HEX(binary_col) AS binary_hex FROM bugtest ORDER BY id_col;
