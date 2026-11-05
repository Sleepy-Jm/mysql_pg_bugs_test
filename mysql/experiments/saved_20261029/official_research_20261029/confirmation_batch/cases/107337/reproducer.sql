-- MySQL report #107337; source anchors: cmain, c522679, c554592
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t(a TIME);
INSERT INTO t VALUES('08:00:00');
SELECT * FROM t WHERE a IN ('08:00:00',NULL);
SELECT * FROM t WHERE a IN ('08:00:00','');
SELECT * FROM t WHERE a IN ('08:00:00','07:59:59');
SELECT * FROM t WHERE a IN (TIME'08:00:00',NULL);
