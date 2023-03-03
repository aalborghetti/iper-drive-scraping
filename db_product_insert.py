import sqlite3

connection = sqlite3.connect('db_product.db')

code = input("Inserisci il codice: ")
product = input("Inserisci il nome dell'articolo: ")
brand = input("Inserisci la marca dell'articolo: ")
link = input("Inserisci il link dal quale recuperare i dati: ")

connection.execute("INSERT INTO products (code, product, brand, link) VALUES (?, ?, ?, ?)", (code, product, brand, link))

connection.commit()

connection.close()