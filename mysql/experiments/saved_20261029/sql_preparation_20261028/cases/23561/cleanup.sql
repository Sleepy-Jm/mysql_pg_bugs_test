-- Cleanup for report #23561; only objects in the fresh case schema.
DROP TABLE IF EXISTS price;
SET SESSION sql_mode=@saved_sql_mode;
