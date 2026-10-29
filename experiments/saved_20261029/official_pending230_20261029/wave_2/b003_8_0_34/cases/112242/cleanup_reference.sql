-- MySQL report #112242; source: cmain, c535808
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION optimizer_switch=@old_optimizer_switch;
DROP TABLE IF EXISTS t0;
