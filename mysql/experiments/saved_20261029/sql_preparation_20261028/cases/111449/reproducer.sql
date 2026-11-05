-- MySQL report #111449; source: cmain, c533666, c533667, c535184
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
CREATE TABLE IF NOT EXISTS v0 ( c1 INT ) ;
INSERT INTO v0 SET c1 = c1 IS TRUE;
HANDLER v0 OPEN ;
HANDLER v0 READ FIRST WHERE c1 MEMBER ( c1 ) IS NOT FALSE LIMIT 100 , 100 ;
