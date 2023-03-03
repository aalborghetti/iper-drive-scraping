import sqlite3

connection = sqlite3.connect('db_product.db')

with open('db_product_create.sql') as file:
  connection.executescript(file.read())
  connection.commit()
  connection.close()