USE `replay_20eac2737e152ceb7e9bd9da`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110587; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
set sql_mode = '';
CREATE TABLE t5(c1  BIT(16) NOT NULL, c2  BIT(16));
INSERT IGNORE INTO t5 VALUES (95, 46), (31, 438), (61, 152), (78, 123), (88, 411), (122, 118), (0, 177),(75, 42), (108, 67), (79, 349), (59, 188), (69, 206), (49, 345), (118, 380),(111, 368), (94, 468), (56, 379), (77, 133), (29, 399), (9, 363), (23, 36),(116, 390), (119, 368), (87, 351), (123, 411), (24, 398), (34, 202), (28, 499),(30, 83), (5, 178), (60, 343), (4, 245), (104, 280), (106, 446), (127, 403),(44, 307), (68, 454), (57, 135);
SELECT HEX(c1) FROM t5 WHERE c1 BETWEEN '16' AND '64';
ALTER TABLE t5 ADD KEY idx(c1);
SELECT HEX(c1) FROM t5 WHERE c1 BETWEEN '16' AND '64';
SELECT HEX(c1) FROM t5 IGNORE INDEX(idx) WHERE c1 BETWEEN '16' AND '64';
EXPLAIN FORMAT=TREE SELECT c1 FROM t5 WHERE c1 BETWEEN '16' AND '64';

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows,COUNT(DISTINCT c1+0) AS distinct_values FROM t5;
