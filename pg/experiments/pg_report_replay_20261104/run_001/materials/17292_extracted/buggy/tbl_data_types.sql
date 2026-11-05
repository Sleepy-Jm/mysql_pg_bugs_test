create table bmk.data_types 
  (data_type_id numeric  not null 
  ,typ_name character varying(50)   
  ,description character varying(1000)   
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone  );
