-- MySQL report #87518; source anchors: cmain, c463739, c483633, c520430
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1 (FTS_DOC_ID BIGINT UNSIGNED NOT NULL PRIMARY KEY,
       contents TEXT COLLATE utf8mb4_bin,
       FULLTEXT KEY fx_contents (contents) WITH PARSER ngram
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO t1 VALUES (1, 'xyz mnt'), (2, 'xyz mnt'), (3, 'xyz');

# The query completes with or without bug
SELECT * FROM t1 WHERE MATCH(contents) AGAINST ('xyz' IN BOOLEAN MODE);

# The query returns wrong result set with the bug
SELECT * FROM t1 WHERE MATCH(contents) AGAINST ('xyz' IN BOOLEAN MODE) LIMIT 1;

# The query crashes with the bug
SELECT * FROM t1 WHERE MATCH(contents) AGAINST ('xyz mnt' IN BOOLEAN MODE) LIMIT 5;
SELECT 1 AS server_alive;
