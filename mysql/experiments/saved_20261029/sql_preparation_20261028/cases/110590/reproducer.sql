-- MySQL report #110590; source anchors: cmain, c531380
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt3 (c0 INT);
SELECT 1 FROM (SELECT 1) x(x) JOIN LATERAL (SELECT locate(x.x, 'a', t3.c0) FROM t3 HAVING (SELECT 1) = (SELECT 1)) y(y) ON TRUE WHERE y.y;
SELECT 1 AS server_alive;
