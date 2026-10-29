USE `replay_cdfef0ae6f558d7b2f984c3c`;
SET time_zone="+00:00";
-- Source: bugs.mysql.com/bug.php?id=121523#cmain
-- Source SQL draft. Not executed or confirmed on target versions.
-- Run only in a newly created isolated test schema; no runner is invoked here.
SELECT ST_AsText(ST_PointN(ST_GeomFromText('LINESTRING(0 0,2 2)'), 3)),
       ST_AsText(ST_PointN(ST_GeomFromText('LINESTRING(0 0,2 2)'), 4294967297));
SELECT ST_AsText(ST_GeometryN(ST_GeomFromText('GEOMETRYCOLLECTION(POINT(0 0))'), 4294967297));

