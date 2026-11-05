CREATE FUNCTION make_ia() RETURNS int[] LANGUAGE plpgsql AS
  'declare x int[]; begin x := array[0]; return x; end';
CREATE FUNCTION ia_eq(int[], int[]) RETURNS boolean LANGUAGE plpgsql AS
'begin return array_eq($1, $2); end'; 
CREATE OPERATOR = (procedure = ia_eq, leftarg = int[], rightarg = int[]);
