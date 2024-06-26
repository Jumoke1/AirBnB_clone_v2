#!/usr/bin/python3
"""
Start Flask application
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays C and the value of the text"""
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
