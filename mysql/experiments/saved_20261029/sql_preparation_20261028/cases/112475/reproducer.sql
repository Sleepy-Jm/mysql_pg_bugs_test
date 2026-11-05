-- Report #112475; source anchors: cmain, c536346
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 REPLACE AS SELECT -89 AS c14 ORDER BY c14 ;
INSERT INTO t0 VALUES ( DEFAULT ) , ( DEFAULT ) ;
ALTER TABLE t0 RENAME TO t1 ;
INSERT INTO t1 VALUES ( 12 ) , ( 121 ) ;
SELECT t1 . c14 AS c25 FROM ( SELECT t1 . c14 AS c31 FROM ( SELECT CONVERT ( c14 = RAND ( ) IN ( SIGN ( -54 ) & RAND ( ) LIKE CASE -47 WHEN TRUE THEN -94 WHEN -16 THEN 107 ELSE -44 END , -6351076902139315214 , -68 ) , BINARY ) AS c58 FROM t1 ) AS t2 JOIN t1 ON + EXISTS ( SELECT t1 . c14 AS c33 FROM t1 WHERE c58 = ASCII ( -97 ) << t1 . c14 + -119 GROUP BY c14 , c14 ) , t1 AS t3 JOIN t1 AS t4 ON REVERSE ( t3 . c14 ) ) AS t5 JOIN t1 ON t5 . c31 = t5 . c31 ;
