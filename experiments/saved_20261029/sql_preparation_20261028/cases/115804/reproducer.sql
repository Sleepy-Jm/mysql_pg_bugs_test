-- MySQL report #115804; source anchors: cmain, c546166
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET optimizer_switch='duplicateweedout=off';
create table t1(id int primary key, col1 int, col2 int, col3 int, key index_col1(col1), key index_col2(col2));
select /*+ JOIN_ORDER(d2@subq1, d1) */ 1 from t1 d1 where exists (select /*+ QB_NAME(subq1) */ 1 from t1 d2 where d1.col1 = (select d3.col1 from t1 d3 where d3.col2 = d2.col2 limit 1));
select /*+ JOIN_ORDER(d1, d2@subq1) */ 1 from t1 d1 where exists (select /*+ QB_NAME(subq1) */ 1 from t1 d2 where d1.col1 = (select d3.col1 from t1 d3 where d3.col2 = d2.col2 limit 1));
