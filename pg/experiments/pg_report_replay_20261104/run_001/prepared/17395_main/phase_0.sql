CREATE EXTENSION postgres_fdw;
DO $d$
    BEGIN
        EXECUTE $$CREATE SERVER loopback FOREIGN DATA WRAPPER postgres_fdw
            OPTIONS (dbname '$$||current_database()||$$',
                     port '$$||current_setting('port')||$$'
            )$$;
    END;
$d$;
CREATE USER MAPPING FOR CURRENT_USER SERVER loopback;


CREATE TABLE fprt2 (a int) PARTITION BY RANGE(a);
CREATE TABLE fprt2_p1 (LIKE fprt2);
CREATE TABLE fprt2_p2 (LIKE fprt2);
INSERT INTO fprt2_p1 VALUES (2);
INSERT INTO fprt2_p2 VALUES (1);


CREATE FOREIGN TABLE ftprt2_p1 PARTITION OF fprt2 FOR VALUES FROM (0) TO
(1)
    SERVER loopback OPTIONS (table_name 'fprt2_p1');
CREATE FOREIGN TABLE ftprt2_p2 PARTITION OF fprt2 FOR VALUES FROM (1) TO
(2)
    SERVER loopback OPTIONS (table_name 'fprt2_p2', use_remote_estimate
'true');
