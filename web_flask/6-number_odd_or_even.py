#!/usr/bin/python3
"""
    Web flask 06
"""


from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n=None):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_even_odd(n=None):
    if n and n % 2 == 0:
        that = 'even'
    else:
        that = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, what=that)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
