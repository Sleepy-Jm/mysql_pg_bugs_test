USE `replay_53d61401de0ff0f14bc8a201`;
SET time_zone="+00:00";
-- Source: bugs.mysql.com/bug.php?id=121523#cmain
-- Source SQL draft. Not executed or confirmed on target versions.
-- Run only in a newly created isolated test schema; no runner is invoked here.
SELECT ST_AsText(ST_PointN(ST_GeomFromText('LINESTRING(0 0,2 2)'), 3)),
       ST_AsText(ST_PointN(ST_GeomFromText('LINESTRING(0 0,2 2)'), 4294967297));
SELECT ST_AsText(ST_GeometryN(ST_GeomFromText('GEOMETRYCOLLECTION(POINT(0 0))'), 4294967297));

