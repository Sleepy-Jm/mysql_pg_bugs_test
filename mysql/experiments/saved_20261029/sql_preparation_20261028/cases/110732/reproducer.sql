-- MySQL report #110732; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE v0 ( v1 INT NOT NULL CHECK ( ( v1 = 93 AND v1 < 'x' ) OR v1 = 18 ) ) ;
 SELECT DISTINCT v1 , v1 * v1 FROM v0 WINDOW v2 AS ( PARTITION BY v1 > ( SELECT 127 FROM v0 ) ORDER BY ( v1 > -128 ) DESC ) ORDER BY v1 , v1 DESC , v1 ASC ;
