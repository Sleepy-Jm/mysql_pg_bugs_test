-- MySQL report #109917; source anchors: cmain, c529530, c529548, c529572
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
SET @v=10;
PREPARE stmt FROM 'CREATE TABLE t1 (id INT CHECK(id != ?))';
EXECUTE stmt USING @v;
SELECT 1 AS server_alive;
