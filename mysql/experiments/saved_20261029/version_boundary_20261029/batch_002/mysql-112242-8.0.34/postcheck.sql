-- Read-only postcheck appended after unchanged source SQL.
SELECT c0 FROM t0; SELECT INDEX_NAME,INDEX_TYPE,IS_VISIBLE FROM information_schema.statistics WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='t0'; SELECT @@optimizer_switch;
