#!/usr/bin/python3
"""a script that starts a Flask web application
Routes:
/: display “Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays hello hbnb"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0' port=5000)
