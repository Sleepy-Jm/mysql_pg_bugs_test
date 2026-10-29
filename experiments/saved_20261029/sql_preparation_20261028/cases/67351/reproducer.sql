-- MySQL report #67351; source anchors: c409557, c456508, c459759
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (id INT NOT NULL auto_increment, a INT, b INT, UNIQUE KEY (id, b)) stats_sample_pages=10000;

INSERT INTO t1 VALUES (NULL, NULL, NULL);
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;
INSERT INTO t1 SELECT NULL, NULL, NULL FROM t1;

# Partition in a skewed way

alter table t1
partition by range(b)( 
partition p1 values less than (100),
partition p2 values less than (200),
partition p3 values less than (500),
partition p4 values less than (maxvalue)
);

UPDATE t1 SET a=id, b=(FLOOR(id/1000)*1000);

ALTER TABLE t1 ADD INDEX (b, a), ADD INDEX (a, b);

ANALYZE TABLE t1;
show keys from t1;

UPDATE t1 SET a = 1 WHERE b > 5000;
ANALYZE TABLE t1;
show keys from t1;
SELECT COUNT(*) AS n,COUNT(DISTINCT a),COUNT(DISTINCT b) FROM t1;
