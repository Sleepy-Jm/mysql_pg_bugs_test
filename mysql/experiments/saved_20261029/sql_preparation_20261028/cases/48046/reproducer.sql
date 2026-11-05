-- MySQL report #48046; source anchors: cmain, c264823
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
#/* Begin test case for query 0 */

DROP TABLE /*! IF EXISTS */ BB;

CREATE TABLE `BB` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `time_key` time DEFAULT NULL,
  `varchar_key` varchar(1) DEFAULT NULL,
  `varchar_nokey` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  KEY `time_key` (`time_key`),
  KEY `varchar_key` (`varchar_key`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
INSERT INTO `BB` VALUES (10,'18:27:58',NULL,NULL);

 
SELECT table1 .`time_key` field1  , table2 .`pk`  
FROM BB table1  LEFT  JOIN BB table2  ON table2 .`varchar_nokey`  = table1 .`varchar_key`  
HAVING field1   ;

#/* Diff: */

#/* --- /tmp//randgen29184-1255519418-server0.dump	2009-10-14 07:23:38.000000000 -0400
# +++ /tmp//randgen29184-1255519418-server1.dump	2009-10-14 07:23:38.000000000 -0400
# @@ -1 +1 @@
# -18:27:58	NULL
# +18:27:58	10 */

DROP TABLE BB;
#/* End of test case for query 0 */

#/* Begin test case for query 1 */

DROP TABLE /*! IF EXISTS */ BB;

CREATE TABLE `BB` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `int_nokey` int(11) DEFAULT NULL,
  `time_key` time DEFAULT NULL,
  `datetime_key` datetime DEFAULT NULL,
  `varchar_key` varchar(1) DEFAULT NULL,
  `varchar_nokey` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  KEY `time_key` (`time_key`),
  KEY `datetime_key` (`datetime_key`),
  KEY `varchar_key` (`varchar_key`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
INSERT INTO `BB` VALUES (10,8,'18:27:58','1900-01-01 00:00:00',NULL,NULL);

 
SELECT    table1 . `time_key` AS field1 , table2 . `pk` AS field2 , table2 . `int_nokey` AS field3 , table1 . `varchar_nokey` AS field4 , table2 . `datetime_key` AS field5 
FROM ( BB AS table1 LEFT  JOIN BB AS table2 ON (table2 . `varchar_nokey` = table1 . `varchar_key` ) )   
GROUP BY field1, field2, field3, field4, field5 
HAVING field1 <= 'y' 
ORDER BY table1 . `time_key`  , field2 DESC;

#/* Diff: */

#/* --- /tmp//randgen29184-1255519418-server0.dump	2009-10-14 07:23:38.000000000 -0400
# +++ /tmp//randgen29184-1255519418-server1.dump	2009-10-14 07:23:38.000000000 -0400
# @@ -1 +1 @@
# -18:27:58	NULL	NULL	NULL	NULL
# +18:27:58	10	8	NULL	1900-01-01 00:00:00 */

DROP TABLE BB;
#/* End of test case for query 1 */
