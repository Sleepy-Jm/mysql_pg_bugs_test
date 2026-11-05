-- MySQL report #111706; source anchors: cmain
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
SET optimizer_switch='subquery_to_derived=off';
SELECT * FROM t1 LEFT OUTER JOIN t0 ON t1.c1=t0.c0 WHERE t1.c1 IN (SELECT MIN(tin.c0) FROM t0 AS tin GROUP BY c0);
SET optimizer_switch='subquery_to_derived=on';
SELECT * FROM t1 LEFT OUTER JOIN t0 ON t1.c1=t0.c0 WHERE t1.c1 IN (SELECT MIN(tin.c0) FROM t0 AS tin GROUP BY c0);
