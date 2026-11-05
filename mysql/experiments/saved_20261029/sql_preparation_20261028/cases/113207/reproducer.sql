-- MySQL report #113207; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET @g1 = ST_GeomFromText('GEOMETRYCOLLECTION(POLYGON((300 190,935 665,720 885,300 190)))');
SET @g2 = ST_GeomFromText('POLYGON((300 190,935 665,720 885,300 190))');
SET @g3 = ST_GeomFromText('GEOMETRYCOLLECTION(POLYGON((655 435,55 75,90 5,655 435)),POLYGON((300 190,935 665,720 885,300 190)))');

SELECT ST_Contains(@g3, @g1);
-- result{1}
SELECT ST_Contains(@g3, @g2);
-- expected{1}; actual{0}

SELECT ST_IsValid(@g1),ST_IsValid(@g2),ST_IsValid(@g3),ST_SRID(@g1),ST_SRID(@g3);
