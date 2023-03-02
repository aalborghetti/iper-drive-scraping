import sqlite3

connection = sqlite3.connect('db_price.db')

prezzi = connection.execute("SELECT * FROM prezzi")
connection.commit()

print(prezzi.fetchall())

connection.close()

