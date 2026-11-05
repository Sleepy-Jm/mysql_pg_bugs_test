USE `replay_d795b6648854b2bd0a0eade3`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #121062; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
-- Step 1
CREATE TABLE t (
    id   BIGINT AUTO_INCREMENT NOT NULL,
    a    DATE    DEFAULT '1800-01-01' NOT NULL,
    b    TIME    DEFAULT '00:00:00'   NOT NULL,
    CONSTRAINT t_pk PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Step 2
INSERT INTO t VALUES (1, '2000-01-01', '00:00:00');

-- Step 3 Direct string literal comparison — WORKS correctly
SELECT id FROM t
WHERE a = '2000-01-01 00:00:00' AND b = '1800-01-01 00:00:00';
-- Result: Found 1

-- Step 4 Prepared statement
PREPARE x1 FROM "SELECT id FROM t WHERE a = ? AND b = ?";
SET @a = '2000-01-01 00:00:00';
SET @b = '1800-01-01 00:00:00';
EXECUTE x1 USING @a, @b;
-- Result: Empty set (expected 1)

-- Helpful
PREPARE x2 FROM "SELECT id FROM t WHERE a = ? AND b = ?";
SET @a = '2000-01-01 00:00:00';
SET @b = CONCAT(CURDATE(), ' 00:00:00');
EXECUTE x2 USING @a, @b;
-- Result: Found 1

SET @a = '2000-01-01 00:00:00';
SET @b = '00:00:00';
EXECUTE x2 USING @a, @b;
-- Result: Found 1

-- Single parameter — WORKS
PREPARE x4 FROM "SELECT id FROM t WHERE b = ?";
SET @b = '1800-01-01 00:00:00';
EXECUTE x4 USING @b;
-- Result: 1
PREPARE x5 FROM "SELECT id FROM t WHERE a = ?";
SET @a = '2000-01-01 00:00:00';
EXECUTE x5 USING @a;
-- Result: 1
DEALLOCATE PREPARE x1;
DEALLOCATE PREPARE x2;
DEALLOCATE PREPARE x4;
DEALLOCATE PREPARE x5;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT id,a,b FROM t;
SELECT CURRENT_DATE(),@@session.sql_mode,@@session.time_zone;
