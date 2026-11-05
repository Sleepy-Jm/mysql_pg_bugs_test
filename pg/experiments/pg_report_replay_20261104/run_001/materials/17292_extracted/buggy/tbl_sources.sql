create table bmk.sources 
  (source_id numeric  not null 
  ,src_name character varying(50)   
  ,description character varying(1000)   
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone   
  ,migrated_from_opalis character varying(1)  );
