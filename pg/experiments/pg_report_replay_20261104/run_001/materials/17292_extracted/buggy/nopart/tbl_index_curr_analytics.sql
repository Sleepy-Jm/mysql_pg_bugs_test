create table bmk.index_curr_analytics 
  (index_id numeric  not null 
  ,attribute_id numeric  not null 
  ,as_of_date timestamp(0) without time zone  not null 
  ,source_id numeric  not null 
  ,currency_id numeric  not null 
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone   
  ,nvalue numeric(30,10)  );
