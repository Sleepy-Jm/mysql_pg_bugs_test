-- MySQL report #120687; source: cmain, c557529
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t(
  j JSON,
  KEY idate((CAST(j->'$[*]' AS DATE ARRAY))),
  KEY idt((CAST(j->'$[*]' AS DATETIME ARRAY)))
);

INSERT INTO t VALUES
  ('["2001-01-01 12:34:56"]'),
  ('["2001-01-02 00:00:00"]');

SELECT COUNT(*) AS cnt
FROM t IGNORE INDEX (idate, idt)
WHERE '2001-01-01 00:00:00' MEMBER OF (j->'$[*]'); -- 0

SELECT COUNT(*) AS cnt
FROM t
WHERE '2001-01-01 00:00:00' MEMBER OF (j->'$[*]'); -- 1
