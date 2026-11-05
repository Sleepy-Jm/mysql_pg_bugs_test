-- MySQL report #113358; source: cmain, c538763, c538769, c538772
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION optimizer_switch=@old_optimizer_switch;
SET SESSION sql_mode=@old_sql_mode;
DROP TABLE IF EXISTS t1,t2;
