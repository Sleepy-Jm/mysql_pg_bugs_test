USE `replay_09e455bf3d96f6b7fa1757f7`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #107424; source: cmain, c522894, c531290
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(g1 GEOMETRY NOT NULL SRID 4326);
INSERT INTO t1 VALUES(ST_GeomFromText('point(-6.124932923690693 23.43701608651873)',4326));
INSERT INTO t1 VALUES(ST_GeomFromText('point(-6.124932923690693 23.43701608651874)',4326));
SELECT ST_AsText(g1) FROM t1 WHERE ST_Intersects(ST_GeomFromText('point(-6.124932923690693 23.43701608651873)',4326),g1);
CREATE SPATIAL INDEX spidx ON t1(g1);
SELECT ST_AsText(g1) FROM t1 WHERE ST_Intersects(ST_GeomFromText('point(-6.124932923690693 23.43701608651873)',4326),g1);

-- Read-only postchecks for report 107424; run in the same disposable schema/session.
SELECT ST_AsText(g1), ST_SRID(g1) FROM t1 ORDER BY ST_AsText(g1);
