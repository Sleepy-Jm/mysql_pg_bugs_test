select version();
drop schema if exists tst cascade;
create schema tst;
create function tst.caller1() returns text language plpgsql as 
$$ BEGIN return tst.caller2(); END; $$;
create function tst.caller2() returns text language plpgsql as 
$$ BEGIN return tst.called(); END; $$;
CREATE OR REPLACE FUNCTION tst.called()
RETURNS text LANGUAGE plpgsql
SECURITY DEFINER SET search_path = pg_catalog, pg_temp AS
$$
  DECLARE
    v_stack                  TEXT;
  BEGIN
    GET DIAGNOSTICS v_stack = PG_CONTEXT;
    IF v_stack NOT LIKE '%tst.caller2()%' THEN
      RAISE WARNING 'Beware: the calling function is not the expected
one!';
    END IF;
    RETURN v_stack;
  END;
$$;
set search_path = tst;
show search_path;
select caller1() as stack_in_called;
reset search_path;
show search_path;
select tst.caller1() as stack_in_called;
