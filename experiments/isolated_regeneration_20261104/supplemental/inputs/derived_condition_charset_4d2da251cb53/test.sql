-- Supplemental attempt: informed by historical successful SQL; NOT blind generation.
SET @saved_optimizer=@@SESSION.optimizer_switch;
SET NAMES utf8mb4 COLLATE utf8mb4_bin;
CREATE TABLE sup_charset (id INT PRIMARY KEY,s VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
INSERT INTO sup_charset VALUES (1,'a'),(2,'b'),(3,''),(4,'a'),(5,NULL);
SET SESSION optimizer_switch='derived_condition_pushdown=off';
-- case_id SC_IMPLICIT_OFF
SELECT d.id,HEX(d.tag) AS tag_hex,CHAR_LENGTH(d.tag) AS char_len,OCTET_LENGTH(d.tag) AS byte_len FROM (SELECT DISTINCT id,CONCAT(s,'é') AS tag FROM sup_charset) d WHERE d.tag=_utf8mb4'aé' COLLATE utf8mb4_bin ORDER BY d.id;
SET SESSION optimizer_switch='derived_condition_pushdown=on';
-- case_id SC_IMPLICIT_ON
SELECT d.id,HEX(d.tag) AS tag_hex,CHAR_LENGTH(d.tag) AS char_len,OCTET_LENGTH(d.tag) AS byte_len FROM (SELECT DISTINCT id,CONCAT(s,'é') AS tag FROM sup_charset) d WHERE d.tag=_utf8mb4'aé' COLLATE utf8mb4_bin ORDER BY d.id;
SET SESSION optimizer_switch='derived_condition_pushdown=off';
-- case_id SC_EXPLICIT_OFF
SELECT d.id,HEX(d.tag) AS tag_hex,CHAR_LENGTH(d.tag) AS char_len,OCTET_LENGTH(d.tag) AS byte_len FROM (SELECT DISTINCT id,CONCAT(s,_utf8mb4'é') AS tag FROM sup_charset) d WHERE d.tag=_utf8mb4'aé' COLLATE utf8mb4_bin ORDER BY d.id;
SET SESSION optimizer_switch='derived_condition_pushdown=on';
-- case_id SC_EXPLICIT_ON
SELECT d.id,HEX(d.tag) AS tag_hex,CHAR_LENGTH(d.tag) AS char_len,OCTET_LENGTH(d.tag) AS byte_len FROM (SELECT DISTINCT id,CONCAT(s,_utf8mb4'é') AS tag FROM sup_charset) d WHERE d.tag=_utf8mb4'aé' COLLATE utf8mb4_bin ORDER BY d.id;
SET SESSION optimizer_switch='derived_condition_pushdown=off';
-- case_id SC_ASCII_OFF
SELECT d.id,HEX(d.tag) AS tag_hex,CHAR_LENGTH(d.tag) AS char_len,OCTET_LENGTH(d.tag) AS byte_len FROM (SELECT DISTINCT id,CONCAT(s,'x') AS tag FROM sup_charset) d WHERE d.tag=_utf8mb4'ax' COLLATE utf8mb4_bin ORDER BY d.id;
SET SESSION optimizer_switch='derived_condition_pushdown=on';
-- case_id SC_ASCII_ON
SELECT d.id,HEX(d.tag) AS tag_hex,CHAR_LENGTH(d.tag) AS char_len,OCTET_LENGTH(d.tag) AS byte_len FROM (SELECT DISTINCT id,CONCAT(s,'x') AS tag FROM sup_charset) d WHERE d.tag=_utf8mb4'ax' COLLATE utf8mb4_bin ORDER BY d.id;
DROP TABLE sup_charset;
SET SESSION optimizer_switch=@saved_optimizer;
-- Fresh connection closes after script; SET NAMES is scoped to this connection.
