
from flask import Flask, render_template, jsonify, url_for
from flask import request

# to have the webpage run the marketDataRetrieval needs to be correctly formatted
# right now it gets messed up when its trying to
# import marketDataRetrieval as market

import requests

import os

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods =['GET', 'POST'])
def startPage():
    if request.method == 'POST':
        # inputData = market.getData(tradingSymbol)
        # a flask route function returns html (or a html render_template)
        return render_template('example.html', data = ["string", "variable", "anything else"])
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
