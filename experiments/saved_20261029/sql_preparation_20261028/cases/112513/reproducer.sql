-- MySQL report #112513; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE x ( x VARCHAR ( 1 ) ) ;
 INSERT INTO x ( x ) VALUES ( 'x' ) , ( NULL ) , ( 'x' ) , ( NULL ) ;
 SELECT x FROM x WHERE NULL = x GROUP BY EXISTS ( WITH x ( x ) AS ( SELECT 1 INTERSECT SELECT CASE WHEN x >= 1 THEN ( NULL ) ELSE ( 1 * x ) END + x % 1 ^ 1 + 1 ^ 1 <= CASE WHEN 1 THEN 1.000000 IS NULL END FROM x ) SELECT 1 + 1 FROM x WHERE TRUE > 1 OR CASE x WHEN 1 THEN x WHEN x * x * 1 + x THEN 'x' ELSE 1 END != 1 OR CASE WHEN CASE WHEN 1 THEN 1 - 1 WHEN 1.000000 THEN x ELSE x END THEN 1.000000 WHEN 'x' THEN 1 WHEN 1.000000 THEN 1 / 1 WHEN 1 THEN 1 ELSE x END ^ ( TRUE ) ^ 1.000000 LIKE CASE WHEN x >= 1 THEN x < 1.000000 IS NOT NULL ELSE ( 'x' * x ) END ) HAVING x = 1 ;
