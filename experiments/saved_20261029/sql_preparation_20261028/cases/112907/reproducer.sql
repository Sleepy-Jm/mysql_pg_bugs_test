-- MySQL report #112907; source: cmain, c537517, c537518, c537519
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0 ( c0 CHAR ( 0 ) CHAR SET koi8r DEFAULT NULL , c1 VARCHAR ( 1 ) PRIMARY KEY , c2 INT GENERATED ALWAYS AS ( CAST( ( false < true ) AS FLOAT ) + 8.000000 ) STORED ) ENGINE = InnoDB ;
INSERT IGNORE INTO t0 ( c0 , c1 ) VALUES ( 'fixme' , 'fixme' ) , ( 'SH' , 'SH' ) , ( t0.c1 , 'fixme' ) , ( NOW( ) - INTERVAL 1 SQL_TSI_DAY , CAST( t0.c2 + 1 + t0.c2 AS CHAR ) ) , ( CAST( + 0.000001 AS CHAR ) , 'honeypot' ) ;
