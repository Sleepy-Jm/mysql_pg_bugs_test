-- MySQL report #112911; source: cmain, c537525
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0 ( c0 INT, PRIMARY KEY ( c0 ) ) ;
CREATE VIEW v0 AS SELECT ra1.c0 ca1 FROM t0 ra0 INNER JOIN t0 ra1 ON ra1.c0 IN ( SELECT ra1.c0 ca0 FROM t0 ra2 ) ;
INSERT INTO t0 VALUES ( 1 ), ( -1 ) ;

SELECT COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; -- result: 4
SELECT /*+ JOIN_ORDER(ra5, ra2, ra1, ra0) SEMIJOIN(DUPSWEEDOUT) */ COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; -- result: 8
