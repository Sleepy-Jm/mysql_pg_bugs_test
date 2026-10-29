-- MySQL report #111261; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET GLOBAL innodb_purge_stop_now=OFF;
DROP PROCEDURE IF EXISTS insert_numbers;
DROP TABLE IF EXISTS t1;
