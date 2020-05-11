from flask import Flask, render_template, jsonify, url_for
from flask import request

import requests

import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def startPage():
    return "Hello World"


if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
