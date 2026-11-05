-- Session setup
SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

CREATE TEMPORARY TABLE wf_dcp_inner (
  id INT NOT NULL PRIMARY KEY,
  tag VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
);

CREATE TEMPORARY TABLE wf_dcp_outer (
  id INT NOT NULL PRIMARY KEY,
  want VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
);

INSERT INTO wf_dcp_inner VALUES
  (1, 'alpha'),
  (2, 'beta'),
  (3, 'gamma'),
  (4, 'delta');

INSERT INTO wf_dcp_outer VALUES
  (1, 'alpha'),
  (2, 'beta'),
  (3, 'omega'),
  (4, 'delta');

-- Query under test: derived table has an explicit utf8mb4 introducer on a
-- string literal in its SELECT list; the outer WHERE references the derived
-- column. Pushdown of "d.tag = 'alpha'" into the derived table triggers
-- clone_expression() on the derived expression containing the Item_string.
SELECT d.id, d.tag
FROM (
  SELECT id, _utf8mb4'alpha' AS tag
  FROM wf_dcp_inner
) AS d
JOIN wf_dcp_outer AS o ON o.id = d.id
WHERE d.tag = _utf8mb4'alpha'
ORDER BY d.id;

-- Reference query: same semantics with pushdown disabled.
SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

SELECT d.id, d.tag
FROM (
  SELECT id, _utf8mb4'alpha' AS tag
  FROM wf_dcp_inner
) AS d
JOIN wf_dcp_outer AS o ON o.id = d.id
WHERE d.tag = _utf8mb4'alpha'
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

DROP TEMPORARY TABLE wf_dcp_outer;
DROP TEMPORARY TABLE wf_dcp_inner;
