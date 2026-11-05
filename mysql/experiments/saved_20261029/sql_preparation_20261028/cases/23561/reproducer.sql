-- MySQL report #23561; source anchors: cmain, c89031, c141174
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
SET @saved_sql_mode=@@SESSION.sql_mode;
SET SESSION sql_mode='';
CREATE TABLE `price` (
`assetid` int(11) NOT NULL default '0',
`date` date NOT NULL default '0000-00-00',
`open` double default NULL,
`high` double default NULL,
`low` double default NULL,
`close` double default NULL,
`volume` bigint(20) default NULL,
`last_update` TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
  ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY  (`assetid`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO price (assetid,date,open,high,low,close,volume) 
VALUES (202690,'2006-05-18','334.25','334.25','334.25','334.25','1') 
ON DUPLICATE KEY UPDATE
  open='334.25',high='334.25',low='334.25',close='334.25',volume='1';

DO SLEEP(2);
SELECT now();
SELECT * FROM price; 

INSERT INTO price (assetid,date,open,high,low,close,volume) 
VALUES (202690,'2006-05-18','334.25','334.25','334.25','334.25','1') 
ON DUPLICATE KEY UPDATE
  open='334.25',high='334.25',low='334.25',close='334.25',volume='1';

DO SLEEP(2);
SELECT now();
SELECT * FROM price;

UPDATE price 
SET open='334.25',high='334.25',low='334.25',close='334.25',volume='1' 
WHERE assetid=202690 AND date='2006-05-18';

DO SLEEP(2);
SELECT now();
SELECT * FROM price;
SET SESSION sql_mode=@saved_sql_mode;
