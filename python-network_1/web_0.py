#!/usr/bin/python3
""" Web server
"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['HEAD', 'OPTIONS', 'POST'], strict_slashes=False)
def index():
    """ Root
    """
    print(request.form.get('email'))
    return "Email: {}".format(request.form.get('email'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)