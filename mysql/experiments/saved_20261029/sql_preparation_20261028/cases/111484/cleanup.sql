-- MySQL report #111484; source: cmain, c533732
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION optimizer_switch=@old_optimizer_switch;
DROP TABLE IF EXISTS t_doc,t_search_string;
