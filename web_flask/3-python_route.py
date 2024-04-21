#!/usr/bin/python3
from flask import Flask

""" 
Start Flask application
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/<text>: Display 'Python', followed by the value of the text.
"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):  # Changed 'test' to 'text', added default value
    formatted_text = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
