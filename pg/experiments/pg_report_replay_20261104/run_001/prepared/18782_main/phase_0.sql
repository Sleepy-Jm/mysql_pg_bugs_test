CREATE USER app_user;
CREATE TABLE no_rls_table
(
    id BIGSERIAL PRIMARY KEY,
    should_not_duplicate uuid
);
GRANT SELECT, INSERT, DELETE ON TABLE no_rls_table to app_user;
GRANT USAGE, SELECT ON SEQUENCE no_rls_table_id_seq to app_user;
CREATE TABLE rls_table
(
    id BIGSERIAL PRIMARY KEY,
    team_id uuid,
    should_not_duplicate uuid
);
GRANT SELECT, INSERT, DELETE ON TABLE rls_table to app_user;
GRANT USAGE, SELECT ON SEQUENCE rls_table_id_seq to app_user;


CREATE POLICY rls_table_policy
    ON rls_table
    TO app_user
    USING (
        team_id = current_setting('team.team_id') :: uuid
        )
    WITH CHECK (
        team_id = current_setting('team.team_id') :: uuid
    );


ALTER TABLE rls_table ENABLE ROW LEVEL SECURITY;
CREATE OR REPLACE FUNCTION ensure_not_duplicated_on_rls_table() RETURNS
TRIGGER AS
$$
    BEGIN
        IF EXISTS (
            SELECT 1
            FROM rls_table
            WHERE rls_table.should_not_duplicate =
NEW.should_not_duplicate
        )
        THEN
            RAISE EXCEPTION 'This value should not be duplicated between the
two tables';
        END IF;


        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER check_not_duplicated_on_rls_table
    BEFORE INSERT OR UPDATE ON no_rls_table
    FOR EACH ROW
EXECUTE PROCEDURE ensure_not_duplicated_on_rls_table();
BEGIN;
SET ROLE app_user;
SET LOCAL team.team_id = '6a43cea8-4a5c-4989-bae2-ef5a77d92620';
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
COMMIT;
BEGIN;
SET ROLE app_user;
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
COMMIT;
BEGIN;
SET ROLE app_user;
SET LOCAL team.team_id = '6a43cea8-4a5c-4989-bae2-ef5a77d92620';
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
COMMIT;
BEGIN;
SET ROLE app_user;
INSERT INTO no_rls_table (should_not_duplicate) VALUES (
gen_random_uuid());
COMMIT;
