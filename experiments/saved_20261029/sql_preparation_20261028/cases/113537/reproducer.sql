-- MySQL report #113537; source anchors: cmain, c539414, c539449
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET NAMES utf8mb4;
SELECT LOCATE(x'00','abcdef'),LOCATE(x'00','abcdéf'),LOCATE(x'00',CAST('abcdéf' AS BINARY));

SELECT
    LOCATE(UNHEX('00'), "😂"),
    LOCATE(UNHEX('01'), "😂"),
    LOCATE(UNHEX('02'), "😂"),
    LOCATE(UNHEX('03'), "😂"),
    LOCATE(UNHEX('04'), "😂"),
    LOCATE(UNHEX('05'), "😂"),
    LOCATE(UNHEX('06'), "😂"),
    LOCATE(UNHEX('07'), "😂"),
    LOCATE(UNHEX('08'), "😂"),
    LOCATE(UNHEX('09'), "😂"),
    LOCATE(UNHEX('0A'), "😂"),
    LOCATE(UNHEX('0B'), "😂"),
    LOCATE(UNHEX('0C'), "😂"),
    LOCATE(UNHEX('0D'), "😂"),
    LOCATE(UNHEX('0E'), "😂"),
    LOCATE(UNHEX('0F'), "😂"),
    LOCATE(UNHEX('10'), "😂")
;
