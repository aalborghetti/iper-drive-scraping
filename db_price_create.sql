drop table if exists prices;

create table prices (
  id integer primary key autoincrement,
  code text,
  date text,
  price float
);