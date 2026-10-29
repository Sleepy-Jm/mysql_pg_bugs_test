-- MySQL report #121402; source: cmain, c560058, c560070
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
-- ============================================================
-- 1. Create tables
-- ============================================================
CREATE TABLE nation (
    n_nationkey  INTEGER,
    n_name       CHAR(25),
    n_regionkey  INTEGER,
    n_comment    VARCHAR(152)
);

CREATE TABLE lineitem (
    l_orderkey    INTEGER,
    l_partkey     INTEGER,
    l_suppkey     INTEGER,
    l_linenumber  INTEGER,
    l_quantity    DECIMAL(15,2),
    l_extendedprice  DECIMAL(15,2),
    l_discount    DECIMAL(15,2),
    l_tax         DECIMAL(15,2),
    l_returnflag  CHAR(1),
    l_linestatus  CHAR(1),
    l_shipdate    DATE,
    l_commitdate  DATE,
    l_receiptdate DATE,
    l_shipinstruct CHAR(25),
    l_shipmode     CHAR(10),
    l_comment      VARCHAR(44)
);

-- ============================================================
-- 2. Insert data
-- ============================================================
INSERT INTO nation (n_nationkey, n_name, n_regionkey, n_comment) VALUES
(0, 'ALGERIA', 0, ' haggle. carefully final deposits detect slyly agai'),
(1, 'ARGENTINA', 1, 'al foxes promise slyly according to the regular accounts. bold requests alon'),
(2, 'BRAZIL', 1, 'y alongside of the pending deposits. carefully special packages are about the ironic forges. slyly special '),
(3, 'CANADA', 1, 'eas hang ironic, silent packages. slyly regular packages are furiously over the tithes. fluffily bold'),
(4, 'EGYPT', 4, 'y above the carefully unusual theodolites. final dugouts are quickly across the furiously regular d');

INSERT INTO lineitem (l_orderkey, l_partkey, l_suppkey, l_linenumber, l_quantity, l_extendedprice, l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate, l_receiptdate, l_shipinstruct, l_shipmode, l_comment) VALUES
(1, 1552, 93, 1, 17.00, 21168.23, 0.04, 0.02, 'N', 'O', '1996-03-13', '1996-02-12', '1996-03-22', 'DELIVER IN PERSON', 'TRUCK', 'Regular courts above the'),
(1, 674, 65, NULL, 36.00, 45983.16, 0.09, 0.06, 'N', 'O', '1996-04-12', '1996-02-28', '1996-04-20', 'TAKE BACK RETURN', 'MAIL', NULL),
(2, 637, 65, 1, NULL, 32474.85, 0.09, 0.06, 'N', 'O', '1997-01-28', '1997-01-14', '1997-02-02', NULL, 'RAIL', 'Pending notornis sleep'),
(3, 356, 65, NULL, 24.00, 39747.72, 0.10, 0.04, 'R', 'F', '1993-11-09', '1993-12-20', '1993-11-24', 'NONE', NULL, NULL),
(4, 1072, 65, 1, 32.00, 20509.60, 0.10, 0.02, 'A', 'F', '1994-01-16', '1993-11-22', '1994-01-23', 'DELIVER IN PERSON', 'SHIP', 'Final pinto beans wake');

-- ============================================================
-- 3. Show intermediate results step by step
-- ============================================================

-- ------------------------------------------------------------
-- Step 3.1: View lineitem data
-- Key: l_returnflag and l_shipinstruct are never equal
-- ------------------------------------------------------------
SELECT l_orderkey, l_suppkey, l_returnflag, l_shipinstruct
FROM lineitem
ORDER BY l_orderkey, l_partkey;

-- Result (5 rows):
-- +------------+-----------+--------------+-------------------+
-- | l_orderkey | l_suppkey | l_returnflag | l_shipinstruct    |
-- +------------+-----------+--------------+-------------------+
-- |          1 |        93 | N            | DELIVER IN PERSON |
-- |          1 |        65 | N            | TAKE BACK RETURN  |
-- |          2 |        65 | N            | NULL              |
-- |          3 |        65 | R            | NONE              |
-- |          4 |        65 | A            | DELIVER IN PERSON |
-- +------------+-----------+--------------+-------------------+
-- Note: l_returnflag (N/R/A) is never equal to l_shipinstruct (DELIVER.../TAKE.../NONE)

-- ------------------------------------------------------------
-- Step 3.2: View subquery t3 (key: returns 0 rows)
-- ------------------------------------------------------------
SELECT t2.l_suppkey, 35 + CAST(49 AS DOUBLE PRECISION) / 98367 AS e1
FROM lineitem AS t2
WHERE t2.l_returnflag = t2.l_shipinstruct;

-- Result (0 rows):
-- Empty set
-- Reason: l_returnflag is never equal to l_shipinstruct

-- ------------------------------------------------------------
-- Step 3.3: View LEFT JOIN result (key: t3.e1 is all NULL)
-- ------------------------------------------------------------
SELECT t1.n_nationkey, t3.l_suppkey, t3.e1
FROM nation AS t1
LEFT JOIN (
    SELECT t2.l_suppkey, 35 + CAST(49 AS DOUBLE PRECISION) / 98367 AS e1
    FROM lineitem AS t2
    WHERE t2.l_returnflag = t2.l_shipinstruct
) AS t3
ON t1.n_nationkey >= 10;

-- Result (5 rows, t3.e1 is all NULL):
-- +-------------+-----------+------+
-- | n_nationkey | l_suppkey | e1   |
-- +-------------+-----------+------+
-- |           0 |      NULL | NULL |
-- |           1 |      NULL | NULL |
-- |           2 |      NULL | NULL |
-- |           3 |      NULL | NULL |
-- |           4 |      NULL | NULL |
-- +-------------+-----------+------+
-- Reason: n_nationkey is 0-4, all < 10, so LEFT JOIN never matches

-- ------------------------------------------------------------
-- Step 3.4: View NOT EXISTS subquery (key: returns 0 rows)
-- ------------------------------------------------------------
SELECT 1 FROM lineitem AS t4
WHERE NULL > 137618 OR NULL <= 119489413;

-- Result (0 rows):
-- Empty set
-- Reason: NULL > 137618 is NULL, NULL <= 119489413 is NULL,
--         NULL OR NULL is NULL, WHERE NULL filters out all rows

-- ------------------------------------------------------------
-- Step 3.5: Verify the condition itself (key: result is NULL, not TRUE)
-- ------------------------------------------------------------
SELECT NULL > 137618 OR NULL <= 119489413 AS cond_result;

-- Result:
-- +-------------+
-- | cond_result |
-- +-------------+
-- |        NULL |
-- +-------------+
-- Note: the result is NULL, not TRUE

-- ------------------------------------------------------------
-- Step 3.6: Verify NOT EXISTS semantics (key: should be TRUE)
-- ------------------------------------------------------------
SELECT NOT EXISTS(
    SELECT 1 FROM lineitem AS t4
    WHERE NULL > 137618 OR NULL <= 119489413
) AS not_exists_result;

-- Expected result:
-- +-------------------+
-- | not_exists_result |
-- +-------------------+
-- |                 1 |
-- +-------------------+
-- Reason: subquery returns 0 rows -> EXISTS = false -> NOT EXISTS = true

-- ============================================================
-- 4. Run the full query (reproduce the bug)
-- ============================================================
SELECT t3.l_suppkey, COUNT(t3.e1) AS a1
FROM nation AS t1
LEFT JOIN (
    SELECT t2.l_suppkey, 35 + CAST(49 AS DOUBLE PRECISION) / 98367 AS e1
    FROM lineitem AS t2
    WHERE t2.l_returnflag = t2.l_shipinstruct
) AS t3
ON t1.n_nationkey >= 10
WHERE NOT EXISTS(
    SELECT 1 FROM lineitem AS t4
    WHERE t3.e1 > 137618 OR t3.e1 <= 119489413
)
GROUP BY t3.l_suppkey;

-- Expected result: 1 row
-- +-----------+------+
-- | l_suppkey | a1   |
-- +-----------+------+
-- |      NULL |    0 |
-- +-----------+------+

-- Actual result (MySQL 8.0.46): 0 rows
-- Empty set

-- ============================================================
-- 5. Comparison with other databases (same data, same query)
-- ============================================================
--   SQLite:     1 row (NULL, 0)  -- correct
--   PostgreSQL: 1 row (NULL, 0)  -- correct
--   Dameng:     1 row (NULL, 0)  -- correct
--   MySQL:      0 rows           -- WRONG

-- ============================================================
-- 6. Root cause analysis
-- ============================================================
-- The condition `t3.e1 > 137618 OR t3.e1 <= 119489413` is a "tautological OR",
-- because 137618 < 119489413, so any numeric x satisfies it.
--
-- When t3.e1 is NULL:
--   NULL > 137618 OR NULL <= 119489413  ->  NULL (not TRUE)
--   WHERE NULL  ->  subquery returns 0 rows  ->  NOT EXISTS = TRUE
--
-- But the MySQL optimizer rewrites the condition to TRUE, ignoring NULL:
--   WHERE TRUE  ->  subquery returns all rows  ->  NOT EXISTS = FALSE
--   ->  rows that should be kept are incorrectly filtered out  ->  0 rows
-- Additional source control c560058: without WHERE
SELECT t3.l_suppkey, COUNT(t3.e1) AS a1
FROM nation AS t1
LEFT JOIN (
    SELECT t2.l_suppkey, 35 + CAST(49 AS DOUBLE PRECISION) / 98367 AS e1
    FROM lineitem AS t2
    WHERE t2.l_returnflag = t2.l_shipinstruct
) AS t3
ON t1.n_nationkey >= 10
GROUP BY t3.l_suppkey;
