from flask import Flask,render_template

from products import products

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('fron/home.html')

@app.get('/product')
def product():
    return "product Page"

@app.get('/product-detial')
def product_detial():
    return "product detial Page"

@app.get('/cart')
def cart():
    return "cart Page"

@app.get('/checkout')
def checkout():
    return "checkout Page"

if __name__ == '__main__':
    app.run()
