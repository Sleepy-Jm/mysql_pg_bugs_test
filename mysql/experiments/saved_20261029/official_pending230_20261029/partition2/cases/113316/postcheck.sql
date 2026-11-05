-- Read-only evidence after the unchanged source SQL, same session.
SHOW WARNINGS;
SELECT int_col,HEX(bit_col) AS stored_hex FROM t0;
