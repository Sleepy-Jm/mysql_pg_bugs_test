USE `replay_ad81fd349a240f706bcf2a25`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #114775; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
create table main (id varchar(10));
insert into main values ('a');
insert into main values ('b');

create table dummy (id varchar(10));
insert into dummy values ('c');
insert into dummy values ('d');

create table seq  (id varchar(10));
insert into seq values ('e');
insert into seq values ('f');

select 'main' tab, id from main union all
select 'dummy' tab, id from dummy union all
select 'seq' tab, id from seq ;

/* 2) 오류 케이스 쿼리 */
select main_id
     , max_val
	 , dummy_ID
  from (
        select main.Id  as main_id
             , (
                select id
                  from seq
                 where seq.id = main.id
                ) as max_val -- 해당 구문 제외하면 정상
             , dummy.ID as dummy_ID
          from main
          left outer join (select 'c' as ID
                              from dummy
							) dummy
               on dummy.ID = main.id 
  where main.Id in ('a','b')
    ) test
WHERE dummy_ID = 'c' ;

-- Read-only postchecks for report 114775; run in the same disposable schema/session.
SELECT * FROM main ORDER BY id; SELECT * FROM dummy ORDER BY id; SELECT * FROM seq ORDER BY id;
