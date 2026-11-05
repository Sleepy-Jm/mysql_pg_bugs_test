-- UTF-8 file. Run in a fresh session with a selected disposable schema.
-- Target: 4d2da251cb536340d19438cc0039bb2846f9a634.
-- wf_4d2_text must not already exist. No pre-test DROP of unknown objects.
SELECT VERSION() AS server_version, DATABASE() AS test_schema,
       @@SESSION.optimizer_switch AS initial_optimizer_switch;
SET @wf_4d2_optimizer = @@SESSION.optimizer_switch;
SET @wf_4d2_client = @@SESSION.character_set_client;
SET @wf_4d2_results = @@SESSION.character_set_results;
SET @wf_4d2_collation = @@SESSION.collation_connection;
SET NAMES utf8mb4 COLLATE utf8mb4_bin;
CREATE TABLE wf_4d2_text (
  id INT PRIMARY KEY,
  s VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin
) ENGINE=InnoDB;
INSERT INTO wf_4d2_text VALUES (1,'a'),(2,'b'),(3,''),(4,'a'),(5,NULL);

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP01_OFF
SELECT 'DCP01_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP01_ON
SELECT 'DCP01_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP02_OFF
SELECT 'DCP02_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP02_ON
SELECT 'DCP02_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP03_OFF
SELECT 'DCP03_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'中') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'a中' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP03_ON
SELECT 'DCP03_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'中') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'a中' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP04_OFF
SELECT 'DCP04_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'O''Reilly') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aO''Reilly' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP04_ON
SELECT 'DCP04_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'O''Reilly') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aO''Reilly' COLLATE utf8mb4_bin
ORDER BY d.id;

-- Cleanup and session restoration after all data results.
DROP TABLE wf_4d2_text;
SET SESSION optimizer_switch = @wf_4d2_optimizer;
SET SESSION character_set_client = @wf_4d2_client;
SET SESSION character_set_results = @wf_4d2_results;
SET SESSION collation_connection = @wf_4d2_collation;
