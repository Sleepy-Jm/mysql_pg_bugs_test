-- Read-only evidence after the unchanged source SQL, same session.
SELECT id,HEX(c1) AS stored_hex FROM t ORDER BY id;
SELECT COLLATION_NAME,PAD_ATTRIBUTE FROM information_schema.COLLATIONS WHERE COLLATION_NAME='utf8mb4_bin';
SELECT @@character_set_connection,@@collation_connection;
