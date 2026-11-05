-- Read-only evidence after the unchanged source SQL, same session.
SELECT id FROM ta;
SELECT value,HEX(value) AS stored_hex FROM tb;
SELECT @@session.sql_mode;
