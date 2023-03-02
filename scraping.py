import requests
from bs4 import BeautifulSoup
from datetime import date
import sqlite3
import re

URL = "https://iperdrive.iper.it/spesa-online/it/seriate/bisccampagnole-mbianco-700g"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

oggi = date.today()
data = oggi.strftime("%d/%m/%Y")
articolo = soup.find_all(class_="add-to-cart-product-name")
marca = soup.find_all(class_="add-to-cart-product-brand")
string_prezzo = soup.find_all(class_="final-price")
string_prezzo = re.findall("\d+\,\d+", string_prezzo[0].text)
prezzo = string_prezzo[0].replace(",",".")

connection = sqlite3.connect('db_price.db')
connection.execute('INSERT INTO prezzi(data, articolo, marca, prezzo) VALUES (?,?,?,?)', (data, articolo[0].text, marca[0].text, prezzo))
connection.commit()
connection.close()