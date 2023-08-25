#! /usr/bin/python3
"""
    python flask basic server
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """return string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
