create table bmk.attributes 
  (attribute_id numeric  not null 
  ,attribute_type_id numeric   
  ,att_name character varying(250)   
  ,description character varying(1000)   
  ,last_updated_by character varying(50)   
  ,code character varying(50)   
  ,data_type_id numeric   
  ,last_updated_datetime timestamp(0) without time zone  );
