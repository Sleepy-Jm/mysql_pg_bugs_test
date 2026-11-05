-- Cleanup for report #85918; only objects in the fresh case schema.
DROP TABLE IF EXISTS zerodate;
SET SESSION sql_mode=@saved_sql_mode;
