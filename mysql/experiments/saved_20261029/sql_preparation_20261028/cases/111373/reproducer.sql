-- MySQL report #111373; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
CREATE TABLE IF NOT EXISTS v3 ( c4 INT  ) AS TABLE v0 ORDER BY c1 > ALL (VALUES ROW ( TRUE ) ORDER BY TRUE ) ;
