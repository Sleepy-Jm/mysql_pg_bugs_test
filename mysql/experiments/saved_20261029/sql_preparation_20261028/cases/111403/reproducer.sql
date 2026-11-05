-- MySQL report #111403; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
CREATE TABLE v2 PARTITION BY LIST COLUMNS ( v2 ) ( PARTITION v2 VALUES IN ( MICROSECOND ( 'abc' ) ) ) AS TABLE v0 ;
