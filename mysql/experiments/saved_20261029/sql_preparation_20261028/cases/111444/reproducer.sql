-- MySQL report #111444; source: cmain, c533656, c533657
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
CREATE TABLE IF NOT EXISTS v2 ( CONSTRAINT c3 PRIMARY KEY i6 TYPE BTREE ( c1 ) ) INSERT_METHOD = LAST STORAGE MEMORY AS TABLE v0;
INSERT v0 SET c1 = c1 ;
CREATE VIEW v4 AS TABLE v0 UNION DISTINCT TABLE v2 ORDER BY c1 IN ( TABLE v2 ) ;
TABLE v0 ORDER BY 'any_random_text' IN ( TABLE v4) ;
