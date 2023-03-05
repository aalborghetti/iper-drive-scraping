drop table if exists products;

create table products (
  id integer primary key autoincrement,
  code text,
  product text,
  brand text,
  url text
);