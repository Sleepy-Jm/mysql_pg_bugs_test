-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS t0_exists FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='t0';
