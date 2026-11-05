-- MySQL report #111892; source: cmain, c534780, c534799, c534813
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION sql_mode=@old_sql_mode;
DROP TABLE IF EXISTS t_check,t_default,t_generated,t_double,t_control;
