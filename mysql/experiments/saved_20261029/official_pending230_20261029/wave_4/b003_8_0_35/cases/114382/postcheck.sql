-- Read-only postcheck appended after unchanged source SQL.
SELECT c0 FROM t1; SELECT CURDATE(),@@session.timestamp,@@session.time_zone,@@session.sql_mode;
