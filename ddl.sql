CREATE VIEW md_tables AS SELECT table_name, column_name FROM duckdb_columns
;
CREATE TABLE md_comments(table_name VARCHAR, column_name VARCHAR, description VARCHAR)
;
create view md_column_comments
as
select t.*, ifnull(c1.description,c2.description) description
  from md_tables t
  left outer join md_comments c1 on c1.column_name=t.column_name and c1.table_name=t.table_name
  left outer join md_comments c2 on c2.column_name=t.column_name and c2.table_name is null
--  where t.table_name in ('process','process_summary') and t.column_name in ('pid_hash','hostname')
;
