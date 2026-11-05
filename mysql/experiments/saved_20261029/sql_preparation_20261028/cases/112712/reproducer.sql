-- MySQL report #112712; source: cmain, c536957, c536958
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0 ( c0 INT NOT NULL , c1 DATETIME DEFAULT ( source_pos_wait( 'fixme' , LENGTH( t0.c0 ) - INSTR( REVERSE( t0.c0 ) , 'fixme' ) , - 1 ) ) DEFAULT ( TIMESTAMPADD( SQL_TSI_MINUTE , 1 , 'x' ) ) , c2 INT DEFAULT NULL , c3 INT ( 1 ) NOT NULL ) ;
CREATE TEMPORARY TABLE t1 ( c4 CHAR ( 1 ) , c5 DATETIME DEFAULT NULL , c6 CHAR ( 1 ) , c7 VARCHAR ( 1 ) , c8 TEXT ) ;
SELECT 1 ca2 FROM t0 ra1 WHERE CAST( ra1.c0 AS UNSIGNED INT ) = 2147483648 AND ra1.c0 = ( SELECT 1 ca0 FROM t1 ra2 ) ORDER BY ra1.c0 DESC ;
