-- MySQL report #111527; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
CREATE TABLE v0 ( v1 INT ) ;
INSERT INTO v0 ( v1 ) VALUES ( 0 ) ;
UPDATE v0 SET v1 = 0 WHERE ( EXISTS ( WITH v0 AS ( SELECT NULL , v1 = v1 ) SELECT v1 , v1 FROM v0 AS v3 NATURAL JOIN v0 AS v4 ) )  ;
