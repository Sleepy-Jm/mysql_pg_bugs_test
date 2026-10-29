-- Report #119621; source anchors: cmain, c555442, c556034
-- Static preparation only; not executed. See case.json before any future isolated run.
create table t1 (
  id int not null,
  json_col json,
  KEY `i1` (`id`,(cast(json_extract(`json_col`,_utf8mb4'$[*]') as char(100) array)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 PARTITION BY KEY (id) PARTITIONS 4;

insert into t1 values (1, '["a1"]'), (2, '["a2"]'), (2, '["a3"]');

select * from t1 where id = 2 and ((json_contains(json_col -> '$[*]',  ('"a2"'))));

create table t2 (
  id int not null,
  json_col json,
  KEY `i1` (`id`,(cast(json_extract(`json_col`,_utf8mb4'$[*]') as char(100) array)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

insert into t2 values (1, '["a1"]'), (2, '["a2"]'), (2, '["a3"]');

select * from t2 where id = 2 and ((json_contains(json_col -> '$[*]',  ('"a2"'))));

SELECT * FROM t1 IGNORE INDEX(i1) WHERE id=2 AND JSON_CONTAINS(json_col->'$[*]','"a2"');
