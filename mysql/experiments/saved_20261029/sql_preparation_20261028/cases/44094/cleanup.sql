-- Cleanup for report #44094; only objects in the fresh case schema.
DROP TABLE IF EXISTS table10;
SET SESSION sql_mode=@saved_sql_mode;
