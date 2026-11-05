create extension postgres_fdw;
do $d$
    begin
        execute $$create server loopback foreign data wrapper postgres_fdw
            options (dbname '$$||current_database()||$$',
                     port '$$||current_setting('port')||$$',
                     async_capable 'true'
            )$$;
    end;
$d$;
create user mapping for current_user server loopback;


create table tab1 (a int);
insert into tab1 values(1), (2), (3);
create foreign table ftab1 (b int) server loopback options (table_name
'tab1');


create foreign table ftab2 () inherits (ftab1) server loopback;
