-- Run in a NEW connection, same isolated schema; report #109874 cmain.
DELETE FROM t0;
SELECT 1 AS server_alive;
