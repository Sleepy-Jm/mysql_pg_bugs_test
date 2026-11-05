-- Read-only postcheck appended after unchanged source SQL.
SELECT HEX(id),OCTET_LENGTH(id) FROM parents; SELECT HEX(parent_id),OCTET_LENGTH(parent_id),text FROM foos; SELECT HEX(parent_id),OCTET_LENGTH(parent_id) FROM bars;
