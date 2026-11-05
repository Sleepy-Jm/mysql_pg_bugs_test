CREATE TEMPORARY TABLE wf_avg_p (p INT NOT NULL, ord INT NOT NULL, v INT NULL);
INSERT INTO wf_avg_p VALUES
  (1, 1, 1),
  (1, 2, NULL),
  (1, 3, 3),
  (1, 4, 5),
  (2, 1, 10),
  (2, 2, NULL),
  (2, 3, NULL),
  (2, 4, 8);

SELECT
  p,
  ord,
  v,
  AVG(v) OVER (
    PARTITION BY p
    ORDER BY ord
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
  ) AS avg_v
FROM wf_avg_p
ORDER BY p, ord;

DROP TEMPORARY TABLE wf_avg_p;
