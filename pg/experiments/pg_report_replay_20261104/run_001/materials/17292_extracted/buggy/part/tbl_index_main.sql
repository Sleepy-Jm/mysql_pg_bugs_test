create table bmk.index_main 
  (index_id numeric   
  ,as_of_date timestamp(0) without time zone   
  ,source_id numeric   
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone  )
 partition by RANGE (as_of_date);
