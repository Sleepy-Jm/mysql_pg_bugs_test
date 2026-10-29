-- MySQL report #111406; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
CREATE TABLE v2 ( PRIMARY KEY i3 ( c1 ) ) TABLE v0 ;
UPDATE ( v2 NATURAL LEFT JOIN v0 ) SET c1 = DEFAULT ORDER BY c1 ;
