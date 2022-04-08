#!/usr/bin/python3
"""
Simple flask application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_root():
    """ index page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ another page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def varaible_sections_c(text):
    """ shows the text for the variable c"""
    text = text.replace("_", " ")
    return 'C {:s}'.format(text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def varaible_sections_p(text):
    """shows the output for variable python"""
    text = text.replace("_", " ")
    return 'Python {:s}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
