USE `replay_a4f1c8951e6f7d5263aff996`;
SET time_zone="+00:00";
-- Source: bugs.mysql.com/bug.php?id=120849#cmain
-- Source SQL draft. Not executed or confirmed on target versions.
-- Run only in a newly created isolated test schema; no runner is invoked here.
DROP VIEW IF EXISTS v0;
DROP TEMPORARY TABLE IF EXISTS tmp;
DROP TABLE IF EXISTS t0;

CREATE TABLE t0 (
  c0 TIME
);

INSERT INTO t0 VALUES ('141:54:33');

CREATE VIEW v0 AS
SELECT SEC_TO_TIME(TIME_TO_SEC(c0)) AS vc
FROM t0;

SELECT vc
FROM v0
WHERE vc < '18:00:00';

WITH cte AS (
  SELECT SEC_TO_TIME(TIME_TO_SEC(c0)) AS vc
  FROM t0
)
SELECT vc
FROM cte
WHERE vc < '18:00:00';

CREATE TEMPORARY TABLE tmp AS
SELECT SEC_TO_TIME(TIME_TO_SEC(c0)) AS vc
FROM t0;

SELECT vc
FROM tmp
WHERE vc < '18:00:00';
