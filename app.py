from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/1")
def index():
  connection = sqlite3.connect('db_price.db')
  connection.row_factory =sqlite3.Row
  db_price = connection.execute('SELECT * FROM price').fetchall()
  connection.close()
  return render_template('index.html', price = db_price)

@app.route('/product')
def query_product():
  code = request.args.get('code')

  connection = sqlite3.connect('db_price.db')
  connection.row_factory =sqlite3.Row
  db_price = connection.execute('SELECT * FROM prices WHERE code = ?',(code,)).fetchall()
  connection.close()
  connection = sqlite3.connect('db_product.db')
  cursor = connection.cursor()
  db_product = cursor.execute('SELECT * FROM products WHERE code = ?',(code,)).fetchall()
  connection.close()

  return render_template('product.html', prices = db_price, product = db_product[0][2], brand = db_product[0][3])

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)