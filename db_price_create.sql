drop table if exists prices;

create table prices (
  id integer primary key autoincrement,
  code text,
  data text,
  price float
);