import sqlite3

connection = sqlite3.connect('db_product.db')

products = connection.execute("SELECT * FROM products")

connection.commit()

print(products.fetchall())

connection.close()