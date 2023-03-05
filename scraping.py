import requests
from bs4 import BeautifulSoup
from datetime import date
import sqlite3
import re

connection = sqlite3.connect('db_product.db')
cursor = connection.cursor()
products = cursor.execute('SELECT * FROM products').fetchall()
connection.commit()
connection.close()

connection = sqlite3.connect('db_price.db')

for item in products:
  page = requests.get(item[4])
  soup = BeautifulSoup(page.content, "html.parser")

  today = date.today()
  string_date = today.strftime("%d/%m/%Y")
  string_prices = soup.find_all(class_="final-price") 
  string_prices = re.findall("\d+\,\d+", string_prices[0].text)
  float_price = string_prices[0].replace(",",".")

  connection.execute('INSERT INTO prices(code, date, price) VALUES (?,?,?)', (item[1], string_date, float_price))

connection.commit()
connection.close()