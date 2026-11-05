USE `replay_4f2f88ee6d556859578e3ca4`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110244; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE FRIENDSHIP (
  USER1_ID INTEGER, 
  USER2_ID INTEGER,
  PRIMARY KEY (USER1_ID, USER2_ID)
);
INSERT INTO FRIENDSHIP VALUES (1, 0);

CREATE TABLE LIKES (
  USER_ID INTEGER, 
  PAGE_ID INTEGER,
  PRIMARY KEY (USER_ID, PAGE_ID)
);
INSERT INTO LIKES VALUES (2, 0);

-- Q1
SELECT * FROM (SELECT B.USER_ID, B.PAGE_ID FROM FRIENDSHIP A LEFT JOIN LIKES B 
ON (A.USER2_ID=B.USER_ID OR A.USER1_ID=B.USER_ID) 
WHERE (A.USER1_ID=1 OR A.USER2_ID=1) ) TMP 
WHERE PAGE_ID NOT IN ( SELECT DISTINCT(PAGE_ID) FROM LIKES WHERE USER_ID=1);

-- Q2
SELECT * FROM (
SELECT * FROM (SELECT B.USER_ID, B.PAGE_ID FROM FRIENDSHIP A LEFT JOIN LIKES B 
ON (A.USER2_ID=B.USER_ID OR A.USER1_ID=B.USER_ID) 
WHERE (A.USER1_ID=1 OR A.USER2_ID=1) ) TMP 
WHERE PAGE_ID NOT IN ( SELECT DISTINCT(PAGE_ID) FROM LIKES WHERE USER_ID=1)
) AS T;

-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT USER1_ID,USER2_ID FROM FRIENDSHIP;
SELECT USER_ID,PAGE_ID FROM LIKES;
SELECT PAGE_ID FROM LIKES WHERE USER_ID=1;
