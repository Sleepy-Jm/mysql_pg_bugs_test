-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS t0_exists FROM information_schema.tables WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='t0';
