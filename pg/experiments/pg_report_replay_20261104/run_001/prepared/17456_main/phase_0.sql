CREATE SCHEMA my_schema;
CREATE SCHEMA util;
CREATE EXTENSION ltree WITH SCHEMA util;
SET SEARCH_PATH=my_schema,util;
CREATE TABLE my_schema.my_table
    (path ltree);


CREATE FUNCTION my_schema.noop() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    RETURN NEW;
END;
$$;


CREATE TRIGGER path_update_after_trg
    AFTER UPDATE ON my_schema.my_table
    FOR EACH ROW WHEN ((new.path IS DISTINCT FROM old.path))
    EXECUTE FUNCTION my_schema.noop();
