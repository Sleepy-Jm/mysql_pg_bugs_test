-- MySQL report #111562; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0 (c1 TINYINT UNSIGNED, c5 BIT);
INSERT INTO `t0` VALUES (255,NULL),(255,NULL),(0,NULL),(0,NULL),(0,NULL),(0,NULL),(0,NULL),(12,_binary '\0'),(206,_binary '\0'),(135,_binary '\0'),(193,_binary '\0'),(244,_binary '\0');
SELECT nth_value(t0.c1, 97) OVER (ORDER BY t0.c1 RANGE BETWEEN 99 FOLLOWING AND 51 FOLLOWING) FROM t0;
