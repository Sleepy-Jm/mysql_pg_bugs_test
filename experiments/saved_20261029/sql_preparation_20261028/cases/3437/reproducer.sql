-- MySQL report #3437; source anchors: cmain, c7642
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE namefragmentvowel(id INT AUTO_INCREMENT PRIMARY KEY,Fragment VARCHAR(6) UNIQUE) ENGINE=InnoDB;
CREATE TABLE namefragmentconsonant LIKE namefragmentvowel;
INSERT INTO namefragmentvowel(Fragment) VALUES ('a');
INSERT INTO namefragmentconsonant(Fragment) VALUES ('b');
DELIMITER //
CREATE PROCEDURE name_test (OUT sFragment VARCHAR(6), OUT iRand INT)
BEGIN
DECLARE bContinue INT;
--DECLARE iRand INT;

SELECT 1 INTO bContinue;

WHILE bContinue = 1 DO

SELECT CAST((RAND() * 100)/33 AS UNSIGNED) INTO iRand;

IF iRand = 0 
THEN

SELECT Fragment INTO sFragment FROM namefragmentvowel ORDER BY RAND() LIMIT 1;

ELSE IF RAND = 1 THEN
SELECT Fragment INTO sFragment FROM namefragmentconsonant ORDER BY RAND() LIMIT 1;

END IF;
END IF;

SELECT 0 INTO bContinue;

END WHILE;
END
//
DELIMITER ;
CALL name_test(@sTest,@iRand);
SELECT @sTest,@iRand;
SELECT 1 AS server_alive;
