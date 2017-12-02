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


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    app.run(host=host, port=port, debug=True)
