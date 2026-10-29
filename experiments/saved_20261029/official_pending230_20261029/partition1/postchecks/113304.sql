-- Read-only postcheck appended after unchanged source SQL.
SELECT c0,HEX(c0) FROM t0; SELECT c0,c0+0 FROM t1; SELECT @@sql_mode;
