CREATE EXTENSION plpython3u;


CREATE FUNCTION plpy_xact_test() RETURNS int
LANGUAGE plpython3u
AS '
plpy.rollback()
return 1
';
