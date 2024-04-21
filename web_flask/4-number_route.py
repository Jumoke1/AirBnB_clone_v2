#!/usr/bin/python3
""" 
Start Flask application
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/<text>: Display 'Python', followed by the value of the text.
    /number/<int:n>: Displays '<n> is a number' only if <n> is an integer.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displas hello hbnb"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays C and the value of the text"""
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """displays python and text"""
    formatted_text = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays the value of the number"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
