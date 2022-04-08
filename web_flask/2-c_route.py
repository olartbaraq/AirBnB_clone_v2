#!/usr/bin/python3
"""
Simple flask application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ index page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_page():
    """ another page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def varaible_sections(text):
    """ shows the text for the variable c"""
    text = text.replace("_", " ")
    return 'C {:s}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
