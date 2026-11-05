USE `replay_46a96626ddd13fac27aea183`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111484; source: cmain, c533732
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
SET SESSION optimizer_switch='subquery_to_derived=off';
create table t_doc (id int, doc JSON );
insert into t_doc values
  (1, '{"match11": "eleven", "match12": "element", "notMatch": "elven" }' ),
  (2, '{"match21": "eleven", "match22": "element", "notMatch": "elven" }' ),
  (3, '{"match31": "tw%elve", "match32": "tw%ilight", "notMatch": "twitter" }' );

create table t_search_string (id int, search_string varchar(20) );
insert into t_search_string values
  (1, 'ele%' ),
  (2, 'ele%' ),
  (3, 'tw|%%' );

select t.id, json_search( doc, 'all', (select search_string from t_search_string s where s.id = t.id), '|' )
from t_doc t order by id;
SET SESSION optimizer_switch='subquery_to_derived=on';
select t.id, json_search( doc, 'all', (select search_string from t_search_string s where s.id = t.id), '|' ) from t_doc t order by id;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS doc_rows FROM t_doc;
SELECT COUNT(*) AS search_rows,COUNT(DISTINCT id) AS unique_ids FROM t_search_string;
