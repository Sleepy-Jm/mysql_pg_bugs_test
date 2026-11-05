create table bmk.index_main 
  (index_id numeric  not null 
  ,as_of_date timestamp(0) without time zone  not null 
  ,source_id numeric  not null 
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone  );
