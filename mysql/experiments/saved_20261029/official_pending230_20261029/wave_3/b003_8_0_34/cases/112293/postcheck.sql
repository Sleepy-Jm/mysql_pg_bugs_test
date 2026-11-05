-- Read-only evidence after the unchanged source SQL, same session.
SELECT HEX(b) AS stored_hex FROM t ORDER BY a;
SELECT @@session.internal_tmp_mem_storage_engine;
