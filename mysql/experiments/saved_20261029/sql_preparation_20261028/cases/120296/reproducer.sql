-- Report #120296; source anchors: cmain, c556697
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_mode=@@session.sql_mode,@case_optimizer=@@session.optimizer_switch;

SET SESSION sql_mode = '';

CREATE TABLE t_main (
    c1 INT NOT NULL PRIMARY KEY,
    c2 VARCHAR(64) NOT NULL,
    c3 VARCHAR(64) NULL,
    c4 INT NULL,
    c5 DATE NULL
);

CREATE TABLE t_ref (
    c1 INT NOT NULL PRIMARY KEY,
    c4 YEAR NOT NULL,
    c5 TIME NULL,
    c11 GEOMETRY NULL,
    c13 TINYBLOB NULL
);

CREATE INDEX idx_main_c2 ON t_main (c2);
CREATE INDEX idx_main_c4 ON t_main (c4);

INSERT INTO t_main (c1, c2, c3, c4, c5) VALUES
(1, 'not-a-date',        'hv_4144',     8, NULL),
(2, 'hv_820',            'not-a-date',  8, NULL),
(3, 'k9zs-031qxa86z954', 'hv_4144',     8, NULL),
(4, 'dldk4w-7o6',        'hv_4144',     8, NULL),
(5, '123',               'hv_4144',     8, NULL),
(6, 'not-a-date',        'short',       8, NULL),
(7, 'not-a-date',        'hv_4144',    12, NULL),
(8, 'other',             'hv_4144',     8, '2023-01-01');

-- INSERT IGNORE is important: NULL becomes YEAR 0000
INSERT IGNORE INTO t_ref (c1, c4, c5, c11, c13) VALUES
(1, NULL, '15:32:26', NULL, NULL),
(2, 2008, '02:57:30', NULL, X'01'),
(3, 2017, '14:12:33', NULL, X'02');

SHOW WARNINGS;
ANALYZE TABLE t_main, t_ref;

-- Optional control: coercion semantics are valid
SELECT 'control' AS stage, c1, c4, c5,
       ('not-a-date' = c4) AS eq_bad_str,
       ('0' = c4) AS eq_zero_str,
       (CAST('not-a-date' AS SIGNED) = c4) AS eq_cast_bad_str
FROM t_ref
ORDER BY c1;

-- S1: FirstMatch semijoin path
SET SESSION optimizer_switch =
  'semijoin=on,firstmatch=on,materialization=off,loosescan=off,duplicateweedout=off';

EXPLAIN FORMAT=TRADITIONAL
SELECT m.c1, m.c2
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND m.c2 = r.c4
  );

SELECT 'S1_count' AS stage, COUNT(*) AS cnt
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND m.c2 = r.c4
  );

SELECT 'S1_rows' AS stage, m.c1, m.c2, m.c4
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND m.c2 = r.c4
  )
ORDER BY m.c1;

-- S2: same data, but force the materialized semijoin path
SET SESSION optimizer_switch =
  'semijoin=on,firstmatch=off,materialization=on,loosescan=off,duplicateweedout=off';

EXPLAIN FORMAT=TRADITIONAL
SELECT m.c1, m.c2
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND m.c2 = r.c4
  );

SELECT 'S2_count' AS stage, COUNT(*) AS cnt
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND m.c2 = r.c4
  );

SELECT 'S2_rows' AS stage, m.c1, m.c2, m.c4
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND m.c2 = r.c4
  )
ORDER BY m.c1;

-- Cross-check: explicit coercion restores the rows under S2
SELECT 'S2_cast_count' AS stage, COUNT(*) AS cnt
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND CAST(m.c2 AS SIGNED) = r.c4
  );

SELECT 'S2_cast_rows' AS stage, m.c1, m.c2, m.c4
FROM t_main m
WHERE m.c5 IS NULL
  AND m.c4 = 8
  AND LENGTH(COALESCE(m.c3, '')) >= 7
  AND EXISTS (
      SELECT 1
      FROM t_ref r
      WHERE (r.c13 IS NULL OR r.c11 IS NOT NULL)
        AND r.c5 IS NOT NULL
        AND CAST(m.c2 AS SIGNED) = r.c4
  )
ORDER BY m.c1;
