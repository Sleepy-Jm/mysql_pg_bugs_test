-- Read-only postcheck appended after unchanged source SQL.
SELECT HEX('abcdéf'),HEX('😂'),@@character_set_connection,@@collation_connection,@@sql_mode;
