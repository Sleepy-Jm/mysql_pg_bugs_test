-- MySQL report #85918; source anchors: cmain, c459209, c533571, c535731, c535732
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
SET @saved_sql_mode=@@SESSION.sql_mode;
SET SESSION sql_mode='NO_ZERO_DATE,STRICT_TRANS_TABLES';
CREATE TABLE zerodate(added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
SELECT * FROM zerodate WHERE added='0000-00-00 00:00:00';
UPDATE zerodate SET added=NOW() WHERE added='0000-00-00 00:00:00';
UPDATE IGNORE zerodate SET added=NOW() WHERE added='0000-00-00 00:00:00';
SET SESSION sql_mode='';
UPDATE zerodate SET added=NOW() WHERE added='0000-00-00 00:00:00';
SET SESSION sql_mode=@saved_sql_mode;
