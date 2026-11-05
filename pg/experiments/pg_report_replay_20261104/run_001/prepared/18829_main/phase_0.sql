DO $$
DECLARE
    my_var TEXT := 'garth';
BEGIN
    RAISE NOTICE '%s is slim', my_var;
END
$$;
