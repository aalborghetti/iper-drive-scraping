drop table if exists price;

create table price (
  id integer primary key autoincrement,
  articolo text,
  prezzo integer
);

insert into price (articolo,prezzo) values (
  'Campagnole',
  3
);

insert into price (articolo,prezzo) values (
  'Biscottone',
  4
);