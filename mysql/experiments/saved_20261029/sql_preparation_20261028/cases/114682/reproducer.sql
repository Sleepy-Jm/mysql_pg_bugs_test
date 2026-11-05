-- Report #114682; source anchors: cmain, c542436, c542439, c542440
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE `t1` (
  `uid` int NOT NULL,
  `col1` json DEFAULT NULL,
  `col2` varchar(10) GENERATED ALWAYS AS (json_unquote(json_extract(`col1`,_utf8mb4'$.id'))) VIRTUAL,
  PRIMARY KEY (`uid`),
  KEY `index_col2` (`col2`)
);

insert into t1 (uid, col1) values (1, '{"id":"1", "name":"Alice"}');
insert into t1 (uid, col1) values (2, '{"id":"1", "name":"Alice"}');

select json_extract(col1, '$.id'), count(json_extract(col1, '$.name')) from t1 where uid in (select uid from t1) group by 1;
ALTER TABLE t1 DROP INDEX index_col2;
select json_extract(col1, '$.id'), count(json_extract(col1, '$.name')) from t1 where uid in (select uid from t1) group by 1;
