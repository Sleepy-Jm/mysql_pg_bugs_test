-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS n,MIN(created_at) AS lo,MAX(created_at) AS hi FROM t1;
SELECT COUNT(*) AS n,MIN(created_at) AS lo,MAX(created_at) AS hi FROM t2;
