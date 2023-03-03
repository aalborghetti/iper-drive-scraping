import sqlite3

connection = sqlite3.connect('db_price.db')

with open('db_price_create.sql') as file:
  connection.executescript(file.read())
  connection.commit()
  connection.close()