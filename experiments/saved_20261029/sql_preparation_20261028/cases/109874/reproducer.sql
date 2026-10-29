-- MySQL report #109874; source anchors: cmain, c529471
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION SQL_MODE= '';
CREATE TABLE t0 (c1 BOOLEAN);
INSERT INTO t0(c1) VALUES (1);
CREATE INDEX i1 ON t0 (c1, (CAST(X'30575172DB8E23407D25E196ADF68CA2AD11F5B5A8A27B4F' AS CHAR)));
