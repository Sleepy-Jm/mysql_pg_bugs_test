CREATE EXTENSION postgres_fdw;


CREATE SERVER testserver1 FOREIGN DATA WRAPPER postgres_fdw;
DO $d$
    BEGIN
        EXECUTE $$CREATE SERVER loopback FOREIGN DATA WRAPPER postgres_fdw
            OPTIONS (dbname '$$||current_database()||$$',
                     port '$$||current_setting('port')||$$'
            )$$;
    END;
$d$;


CREATE USER MAPPING FOR CURRENT_USER SERVER loopback;
CREATE TABLE async_pt (a int, b int) PARTITION BY RANGE (a);
CREATE TABLE base_tbl2 (a int, b int);
CREATE FOREIGN TABLE async_p2 PARTITION OF async_pt FOR VALUES FROM (2000)
TO (3000)
  SERVER loopback OPTIONS (table_name 'base_tbl2');
CREATE TABLE async_p3 PARTITION OF async_pt FOR VALUES FROM (3000) TO
(4000);
