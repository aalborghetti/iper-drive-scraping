import sqlite3
import requests
from bs4 import BeautifulSoup

url = input("Inserisci il link dal quale recuperare i dati: ")

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

connection = sqlite3.connect('db_product.db')

code = url[url.rfind("-")  + 1:]
product = soup.find_all(class_="add-to-cart-product-name")[0].text
brand = soup.find_all(class_="add-to-cart-product-brand")[0].text
connection.execute("INSERT INTO products (code, product, brand, url) VALUES (?, ?, ?, ?)", (code, product, brand, url))

connection.commit()
connection.close()