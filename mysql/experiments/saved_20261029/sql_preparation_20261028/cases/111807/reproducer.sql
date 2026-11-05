-- MySQL report #111807; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0 (c0 MEDIUMINT UNSIGNED);
SELECT 1 FROM (SELECT 1) x(x) JOIN t0 WHERE least(t0.c0, t0.c0) AND (-unix_timestamp(), 1) = (t0.c0, x.x);
