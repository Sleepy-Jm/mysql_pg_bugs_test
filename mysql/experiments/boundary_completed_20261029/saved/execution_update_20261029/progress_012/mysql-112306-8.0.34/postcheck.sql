-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS n FROM t0; SELECT COUNT(*) AS n FROM t2; SELECT c0 FROM t1; SELECT c0,c1,c2 FROM t3;
