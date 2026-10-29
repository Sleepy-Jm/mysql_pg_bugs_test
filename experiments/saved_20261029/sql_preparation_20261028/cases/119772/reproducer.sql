-- MySQL report #119772; source: cmain, c555778, c555780, c555783, c555785, c555786
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0 (c0 SMALLINT UNSIGNED);
SELECT ALL t0.c0 AS ref0 FROM t0 WHERE ((! ((-1030413543) NOT IN (t0.c0)))) && ((+ (LEAST(t0.c0, t0.c0)))) ;
