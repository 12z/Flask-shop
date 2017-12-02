from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    products = [
        {
            'href': '1',
            'name': 'one',
        },
        {
            'href': '2',
            'name': 'two',
        },
    ]

    return render_template('products_list.html', products=products)


@app.route('/<product_id>')
def product(product_id):
    product = {
        'name': 'one',
        'picture_link': 'https://assets.pcmag.com/media/images/396774-the-10-best-ultraportables.jpg',
        'description': 'this is the description of the product'
    }

    return render_template('product.html', product=product)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    app.run(host=host, port=port, debug=True)
