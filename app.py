from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/1")
def index():
  connection = sqlite3.connect('db_price.db')
  connection.row_factory =sqlite3.Row
  db_price = connection.execute('SELECT * FROM price').fetchall()
  connection.close()
  return render_template('index.html', price = db_price)

@app.route("/")
def conn_product():
  connection = sqlite3.connect('db_price.db')
  connection.row_factory =sqlite3.Row
  db_price = connection.execute('SELECT * FROM prezzi').fetchall()
  connection.close()
  return render_template('product.html', prezzi = db_price, articolo = 'Campagnole Biscotti con Farina di Riso 700g', marca = 'Mulino Bianco', test = [1.1,2.4,5,4,5,6,7.9])

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)