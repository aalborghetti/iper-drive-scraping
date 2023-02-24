import sqlite3

connection = sqlite3.connect('db_price.db')
with open('sql_command.sql') as file:
  connection.executescript(file.read())
  connection.commit()
  connection.close()