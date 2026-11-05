SELECT
    -- This line causes "variable not found in subplan target list"
    -- grouping(res.cnt)
    -- This line causes "plan should not reference subplan's variable"
   (SELECT grouping(res.cnt))
FROM Card
CROSS JOIN LATERAL
(SELECT
    (SELECT Card.id) AS cnt
) AS res
GROUP BY
    res.cnt;
