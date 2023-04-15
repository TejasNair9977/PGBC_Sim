create database testdb;
\c testdb;
alter user postgres password '1337';
create table example_table(id serial primary key, uname text not null, age integer);
CREATE FUNCTION public.notify() RETURNS trigger LANGUAGE 'plpgsql' AS $FUNCTION$ BEGIN PERFORM pg_notify('change', row_to_json(NEW)::text); RETURN NEW; END; $FUNCTION$;
CREATE TRIGGER update AFTER UPDATE ON example_table FOR EACH ROW EXECUTE PROCEDURE notify();
CREATE TRIGGER remove AFTER DELETE ON example_table FOR EACH ROW EXECUTE PROCEDURE notify();
CREATE TRIGGER change AFTER INSERT ON example_table FOR EACH ROW EXECUTE PROCEDURE notify();
ALTER DATABASE database_name SET log_statement = 'all';