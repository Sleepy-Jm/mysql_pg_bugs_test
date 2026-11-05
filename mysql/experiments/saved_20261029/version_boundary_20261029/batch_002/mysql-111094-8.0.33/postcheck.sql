-- Read-only postcheck appended after unchanged source SQL.
SELECT id,HEX(val) AS value_hex,COLLATION(val) AS coll FROM order_test ORDER BY id;
