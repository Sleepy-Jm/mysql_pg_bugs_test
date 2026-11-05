-- MySQL report #110805; source anchors: cmain, c531927
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt0 (c0 INT);
SELECT 1 FROM t0 HAVING 1 = ((SELECT 1) ORDER BY t0.c0);
SELECT 1 AS server_alive;
