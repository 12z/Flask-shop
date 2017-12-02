from flask import Flask


app = Flask(__name__)


@app.route('/')
def root():
    return 'r'


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    app.run(host=host, port=port, debug=True)
