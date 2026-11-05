create table bmk.currencies 
  (currency_id numeric  not null 
  ,code character varying(50)   
  ,description character varying(1000)   
  ,live_ind numeric   
  ,last_updated_by character varying(50)   
  ,last_updated_datetime timestamp(0) without time zone  );
