from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  connection = sqlite3.connect('db_price.db')
  connection.row_factory =sqlite3.Row
  db_price = connection.execute('SELECT * FROM price').fetchall()
  connection.close()
  return render_template('index.html', price = db_price)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)