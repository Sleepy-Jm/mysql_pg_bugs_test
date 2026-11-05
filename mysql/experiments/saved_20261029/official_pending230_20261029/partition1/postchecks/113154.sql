-- Read-only postcheck appended after unchanged source SQL.
SELECT id FROM parent; SELECT id,parent_id,seq FROM child ORDER BY id;
