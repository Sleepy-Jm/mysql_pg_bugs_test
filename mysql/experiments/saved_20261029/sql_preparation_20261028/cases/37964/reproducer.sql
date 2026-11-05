-- MySQL report #37964; source anchors: cmain, c175383
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
SET NAMES utf8mb4;
CREATE TABLE `video_categories` (
  `id` int(11) NOT NULL auto_increment,
  `uid` varchar(25) NOT NULL,
  `parent_video_category` int(11) NOT NULL default '0',
  `sort_order` int(11) NOT NULL default '0',
  `category_name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

INSERT INTO `video_categories` VALUES (1, '8732122339511030420583500', 0, 0, 'STAVBY PRO BYDLENÍ');
INSERT INTO `video_categories` VALUES (3, '4520520536171097446293607', 0, 0, 'VEŘEJNÉ STAVBY');

CREATE TABLE `videos` (
  `id` int(11) NOT NULL auto_increment,
  `uid` varchar(25) NOT NULL,
  `title` varchar(100) NOT NULL,
  `keywords` text,
  `description` text,
  `total_length` int(11) NOT NULL COMMENT 'delka celeho nerozestrihaneho videa',
  `videoscount` int(11) NOT NULL default '0' COMMENT 'pocet strihu videa',
  `resolution_w` int(11) NOT NULL default '320' COMMENT 'rozliseni sirka',
  `resolution_h` int(11) NOT NULL default '240' COMMENT 'rozliseni vyska',
  `time_added` datetime NOT NULL,
  `images_last_rotation` datetime NOT NULL,
  `images_rotation_timeout` int(11) NOT NULL default '3600',
  `sort_order` int(11) NOT NULL default '0',
  `selected` tinyint(1) NOT NULL default '0',
  `enabled` tinyint(1) NOT NULL default '0',
  `owner` varchar(25) NOT NULL COMMENT 'GUID vlastnika videa',
  `video_categoriesid` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `uid` (`uid`),
  KEY `FKvideos758264` (`video_categoriesid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=14 ;

INSERT INTO `videos` VALUES (4, '8462518443463578635266479', 'video 4', '', '', 15, 1, 320, 240, '2008-04-22 09:09:54', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 3);
INSERT INTO `videos` VALUES (5, '3227904390799188569201015', 'video 1', '', '', 18, 1, 320, 240, '2008-04-07 21:44:20', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);
INSERT INTO `videos` VALUES (6, '6908280227385544247803464', 'video 2', '', '', 15, 1, 320, 240, '2008-04-07 21:44:24', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);
INSERT INTO `videos` VALUES (7, '3566373516639909720539786', 'video 3', '', '', 15, 1, 320, 240, '2008-04-07 21:44:27', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);
INSERT INTO `videos` VALUES (9, '0731272937526921287482144', 'video 5', '', '', 36, 1, 320, 240, '2008-04-07 21:44:32', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);
INSERT INTO `videos` VALUES (10, '9798971171221584216471877', 'video 6', '', '', 15, 1, 320, 240, '2008-04-07 21:44:34', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);
INSERT INTO `videos` VALUES (11, '2227440085377856907764403', 'video 7', '', '', 15, 1, 320, 240, '2008-04-07 21:47:22', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);
INSERT INTO `videos` VALUES (12, '6202543484191359810966338', 'opravdu pekne / really very nice', 'Rodinný dům, Ostrava.', 'Další ze sady rodinných domků ze všech stran.', 15, 1, 320, 240, '2008-06-23 00:24:15', '2008-07-01 00:00:01', 3600, 0, 0, 1, '', 1);

ALTER TABLE `videos`
  ADD CONSTRAINT `FKvideos758264` FOREIGN KEY (`video_categoriesid`) REFERENCES `video_categories` (`id`);
SELECT * FROM videos WHERE video_categoriesid='1' ORDER BY id DESC LIMIT 2,1;
SELECT id FROM videos WHERE video_categoriesid='1' ORDER BY id DESC;
