-- Read-only postcheck appended after unchanged source SQL.
SELECT c1,HEX(c8),c2,c3,c4,c5,c6,vc1,vc2,c12,c7 IS NULL AS c7_null,c9 IS NULL AS c9_null FROM t3 ORDER BY c1,c3; SHOW CREATE TABLE t3; SELECT @@session.time_zone,@@session.sql_mode;
