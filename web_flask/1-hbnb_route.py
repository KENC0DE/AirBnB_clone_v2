#!/usr/bin/python3
"""
    Web flask 01
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
