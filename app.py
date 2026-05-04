from flask import Flask, render_template, abort
from products import products

app = Flask(__name__)

@app.get('/')
def home():
    # Show first 4 products as "featured"
    featured = products[:4]
    return render_template('fron/home.html', featured=featured)

@app.get('/product')
def product_list():
    return render_template('fron/product.html', products=products)

@app.get('/product/<int:id>')
def product_detail(id):
    product = next((p for p in products if p['id'] == id), None)
    if product is None:
        abort(404)
    return render_template('fron/detail.html', product=product)

@app.get('/cart')
def cart():
    return render_template('fron/cart.html')

@app.get('/checkout')
def checkout():
    return render_template('fron/checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
