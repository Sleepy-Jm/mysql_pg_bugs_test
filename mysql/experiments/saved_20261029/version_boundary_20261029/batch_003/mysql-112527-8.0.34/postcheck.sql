-- Read-only evidence after the unchanged source SQL, same session.
SELECT @@max_allowed_packet AS packet_limit;
SELECT COUNT(*) AS loaded_rows,MAX(5*vkey*pkey) AS maximum_generated_bytes FROM t1;
