-- MySQL report #112512; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE x ( x INT ) ;
 INSERT INTO x ( x ) VALUES ( 1 ) ;
 UPDATE x SET x = 1 WHERE x = 1 ;
 INSERT INTO x ( x ) VALUES ( 1 ) , ( 1 ) ;
 WITH x ( x ) AS ( SELECT x FROM x ORDER BY x ASC ) SELECT 1 FROM x WHERE EXISTS ( SELECT * FROM x WHERE x = x ) GROUP BY x HAVING ( SELECT x GROUP BY 1 , 'x' , 1 , 1 HAVING ( SELECT ( SELECT x WHERE x < 1 * 1 GROUP BY NOT 1 > 'x' , 1 , 1 HAVING x = 1 ) ) > x ) IN ( SELECT x FROM ( SELECT x FROM x UNION SELECT x FROM x ) AS x ) ;
