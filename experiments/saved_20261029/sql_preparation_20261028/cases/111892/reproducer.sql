-- MySQL report #111892; source: cmain, c534780, c534799, c534813
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_sql_mode=@@SESSION.sql_mode;
SET SESSION sql_mode='NO_BACKSLASH_ESCAPES';
SELECT '''';
CREATE TABLE t_check(c0 TEXT CHECK(c0 = ''''));
CREATE TABLE t_default(c0 TEXT DEFAULT(''''));
CREATE TABLE t_generated(c0 TEXT GENERATED ALWAYS AS (''''));
SELECT """";
CREATE TABLE t_double(c0 TEXT CHECK(c0 = """"));
SET SESSION sql_mode='';
SELECT '''';
CREATE TABLE t_control(c0 TEXT CHECK(c0 = ''''));
