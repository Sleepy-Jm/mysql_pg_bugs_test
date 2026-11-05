-- MySQL report #113154; source: cmain, c538218
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
DROP TABLE IF EXISTS `parent`;
CREATE TABLE `parent` (
  `id` bigint NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `child`;
CREATE TABLE `child` (
  `id` bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `parent_id` bigint NOT NULL,
  `seq` int DEFAULT NULL
) ENGINE=InnoDB;

INSERT INTO `parent` VALUES (40);

INSERT INTO `child` VALUES
( 1, 10, 100),
( 2, 20, 200),
( 3, 30, 200),
( 4, 40, 200), -- highest seq for this parent_id
( 5, 50, 200),
( 6, 40, 100), -- lowest seq for this parent_id
( 7, 60, 200),
( 8, 70, 200),
( 9, 80, 100),
(10, 10, 100);

-- For each parent, which child has the highest `seq`?
SELECT t.id_top
FROM (
    SELECT
        c.id AS id_top,
        ROW_NUMBER() OVER (PARTITION BY c.parent_id ORDER BY c.seq DESC) AS rn
    FROM child c
) t
WHERE t.rn = 1;
-- Output: all but 6 and 10, as expected

-- Let’s now join each parent (well, we only have one) with its top child by `seq`.
SELECT child_top.id
FROM parent
LEFT OUTER JOIN child child_top ON (
    parent.id = child_top.parent_id
    AND child_top.id IN (
        SELECT t.id_top
        FROM (
            SELECT
                c.id AS id_top,
                ROW_NUMBER() OVER (PARTITION BY c.parent_id ORDER BY c.seq DESC) AS rn
            FROM child c
        ) t
        WHERE t.rn = 1
    )
);
-- Output: 4, 6
-- Expected: only 4
