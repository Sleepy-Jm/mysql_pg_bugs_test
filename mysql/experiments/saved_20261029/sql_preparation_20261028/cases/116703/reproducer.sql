-- MySQL report #116703; source: cmain, c548706
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t(col INT);
INSERT INTO t VALUES(NULL);
SELECT JSON_VALID(t.col) FROM t;
SELECT JSON_VALID(NULL);
