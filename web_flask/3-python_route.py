#!/usr/bin/python3
"""
    Web flask 03
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Return 'hello hbnb' """
    return 'Hellow HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return 'hbnb' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def about_c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def about_python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
