-- MySQL report #120047; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
-- MIN-REPRO for round-002 / over


CREATE TABLE t1 (
  c1 INT PRIMARY KEY,
  c6 VARCHAR(10)
);

CREATE TABLE t2 (
  c1 INT PRIMARY KEY,
  c7 VARCHAR(32),
  c13 DATETIME
);

CREATE TABLE t3 (
  c1 INT PRIMARY KEY,
  c2 INT,
  c3 INT,
  c10 TEXT
);

INSERT INTO t1 VALUES
(3, 'gzn');

INSERT INTO t2 VALUES
(2, 'a', '2021-10-07 06:26:24');

INSERT INTO t3 VALUES
(2, 3, 2, 'before');

START TRANSACTION;
SAVEPOINT s0;

-- ORIGINAL
UPDATE IGNORE t3 CROSS JOIN t1 ON t3.c2 = t1.c1
SET t3.c10 = 'pwhgaodsctpvhsxbyvaebgaitectfnzfysgucsukksvdaxbwsjsj',
    t1.c6 = 'gb'
WHERE (t3.c1 = 2 AND t1.c1 = 3 AND t3.c2 = t1.c1)
  AND (
    t3.c3 IN (
      SELECT t2.c1
      FROM t2
      WHERE CASE
              WHEN t2.c13 < t2.c13 THEN t2.c7
              ELSE t2.c7
            END
            < CASE
                WHEN t2.c13 BETWEEN '2001-12-18 10:44:33' AND '2011-12-18 05:56:12'
                  THEN STR_TO_DATE('2006-06-21', '%Y-%m-%d')
                ELSE SUBDATE(t2.c13, INTERVAL 10 DAY)
              END
    )
  );
SHOW WARNINGS;

SELECT 'original' AS tag, t1.c1, t1.c6, t3.c1, t3.c10
FROM t3 JOIN t1 ON t3.c2 = t1.c1
WHERE t3.c1 = 2 AND t1.c1 = 3;

ROLLBACK TO s0;

-- MUTATED
UPDATE IGNORE t3 CROSS JOIN t1 ON t3.c2 = t1.c1
SET t3.c10 = 'pwhgaodsctpvhsxbyvaebgaitectfnzfysgucsukksvdaxbwsjsj',
    t1.c6 = 'gb'
WHERE (t3.c1 = 2 AND t1.c1 = 3 AND t3.c2 = t1.c1 OR TRUE)
  AND (
    t3.c3 IN (
      SELECT t2.c1
      FROM t2
      WHERE CASE
              WHEN t2.c13 < t2.c13 THEN t2.c7
              ELSE t2.c7
            END
            < CASE
                WHEN t2.c13 BETWEEN '2001-12-18 10:44:33' AND '2011-12-18 05:56:12'
                  THEN STR_TO_DATE('2006-06-21', '%Y-%m-%d')
                ELSE SUBDATE(t2.c13, INTERVAL '10' DAY)
              END
    )
  );
SHOW WARNINGS;

SELECT 'mutated' AS tag, t1.c1, t1.c6, t3.c1, t3.c10
FROM t3 JOIN t1 ON t3.c2 = t1.c1
WHERE t3.c1 = 2 AND t1.c1 = 3;

ROLLBACK;
