set max_parallel_workers_per_gather = 2;
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
SELECT count(1)
    FROM (
      SELECT fk, id
      FROM testi3
      WHERE flagged
      UNION ALL
      SELECT fk, id
      from testi3
      WHERE false
    ) as t
    LEFT OUTER JOIN testi4
    USING (fk);
