drop table if exists prezzi;

create table prezzi (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  data text,
  articolo text,
  marca text,
  prezzo float
);
