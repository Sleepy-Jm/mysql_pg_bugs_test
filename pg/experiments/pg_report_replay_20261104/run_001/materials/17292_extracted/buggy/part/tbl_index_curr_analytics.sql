create table bmk.index_curr_analytics 
  (index_id numeric   
  ,attribute_id numeric   
  ,as_of_date timestamp(0) without time zone   
  ,source_id numeric   
  ,currency_id numeric   
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone   
  ,nvalue numeric(30,10)  )
 partition by RANGE (as_of_date);
