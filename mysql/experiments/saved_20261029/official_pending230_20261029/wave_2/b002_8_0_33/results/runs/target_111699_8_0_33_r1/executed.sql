USE `replay_acc49de5ae421191763b7402`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111699; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t0` (
  `c0` text
);

CREATE TABLE `t1` (
  `c0` tinyint(3) unsigned zerofill,
  `c1` float DEFAULT NULL,
  UNIQUE KEY `c0` (`c0`)
);

INSERT INTO `t0` VALUES ('292269042'),(''),(NULL),('IcK5A'),(NULL),('z)]s'),('292269042'),('4f*T');

INSERT INTO `t1` VALUES (255,NULL),(NULL,0),(NULL,292269000),(000,NULL),(NULL,NULL);
SET optimizer_switch='subquery_to_derived=on';
SELECT t1.c0 AS ref0 FROM t1 LEFT OUTER JOIN t0 ON t1.c1 = t0.c0 WHERE (t1.c1 IN (SELECT t0.c0 AS ref1 FROM t0 )) OR (t0.c0);
SELECT t1.c0 AS ref0 FROM t1 LEFT OUTER JOIN t0 ON t1.c1 = t0.c0 WHERE (t1.c1 IN (SELECT t0.c0 AS ref1 FROM t0 ));
SELECT t1.c0 AS ref0 FROM t1 LEFT OUTER JOIN t0 ON t1.c1 = t0.c0 WHERE (t0.c0);

-- Read-only postchecks for report 111699; run in the same disposable schema/session.
SELECT COUNT(*) AS t0_rows FROM t0; SELECT COUNT(*) AS t1_rows FROM t1; SELECT @@optimizer_switch;
