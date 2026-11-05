-- MySQL report #66480; source anchors: cmain, c395723
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET time_zone='+00:00';
SET timestamp=1704110400;
SET NAMES utf8 COLLATE utf8_general_ci;
SELECT '00:00:00'<CURTIME();
SELECT CURTIME()>'00:00:00';
SET NAMES utf8 COLLATE utf8_unicode_ci;
SELECT '00:00:00'<CURTIME();
SELECT CURTIME()>'00:00:00';
