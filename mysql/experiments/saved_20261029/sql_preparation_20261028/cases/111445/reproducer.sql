-- MySQL report #111445; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
CREATE TABLE IF NOT EXISTS v0 ( c1 INT , c2 ENUM ( 0x0 ) ASCII BINARY PRIMARY KEY ) ;
INSERT v0 SET c1 = DEFAULT ;
UPDATE v0 SET c1 = 0x0 WHERE CONVERT ( c2 MEMBER OF ( c2 ) , SIGNED INT ) ;
