USE `replay_4a13548100aeac1e1b3c6802`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
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

-- No additional postcheck required by the reviewed oracle.
