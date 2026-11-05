-- MySQL report #32714; source anchors: c144530, c144817, c144901
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
DROP TABLE IF EXISTS `t1`;
CREATE TABLE `t1` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `foo` text,
  `test2` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `t2`;
CREATE TABLE `t2` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `name` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

DROP FUNCTION IF EXISTS `testfunc`;

DELIMITER //
CREATE FUNCTION `testfunc`(
    the_name VARCHAR(255)
) RETURNS int(10) unsigned
    DETERMINISTIC
BEGIN
    DECLARE the_id INT unsigned;
    DECLARE EXIT HANDLER FOR 1329 RETURN NULL;

    SELECT `id` INTO the_id FROM t2 WHERE `name` = the_name;
    RETURN the_id;
END; //

DELIMITER ;

INSERT INTO t1 (foo, test2) VALUES ('Val1', 'bla'), ('Val2', 'blubb'), ('Val3', 'bla'), ('Val4','klong');
INSERT INTO t2 (name) VALUES ('bla'), ('blubb'), ('baz'), ('klong');

SELECT * from t1 LEFT JOIN t2 on t2.id=testfunc(t1.test2);
SELECT * from t1 LEFT JOIN t2 on t2.name=t1.test2;
