-- MySQL report #111441; source: cmain, c533652, c533653, c533847, c533859, c533861
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
INSERT INTO v0 SELECT * FROM v0 WHERE ! { w2 c1 NOT IN ( TABLE v0) IS NOT FALSE } IN ( TABLE v0 ) IS FALSE GROUP BY c1 HAVING c1 WINDOW w2 AS ( );
