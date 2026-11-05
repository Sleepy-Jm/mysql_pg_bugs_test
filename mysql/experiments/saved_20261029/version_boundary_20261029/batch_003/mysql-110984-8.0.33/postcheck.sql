-- Read-only postcheck appended after unchanged source SQL.
SELECT flowid,CHARSET(flowid) AS cs,COLLATION(flowid) AS coll FROM t1;
