WITH RECURSIVE x ( x ) AS
  ( SELECT 1
    UNION ALL
    SELECT x FROM
    (
      SELECT 4 AS x
      UNION ALL
      SELECT x FROM x
    ) AS x
  )
CYCLE x SET b USING v
SELECT * FROM x
;
