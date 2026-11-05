create table bmk.index_master 
  (index_id numeric  not null 
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone   
  ,source_id numeric  not null);
