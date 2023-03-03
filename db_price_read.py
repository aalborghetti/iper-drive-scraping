import sqlite3

connection = sqlite3.connect('db_price.db')

prices = connection.execute("SELECT * FROM prices")

connection.commit()

print(prices.fetchall())

connection.close()