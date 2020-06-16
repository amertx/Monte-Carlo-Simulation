
import matplotlib
matplotlib.use('Agg')
import requests
import random
import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from flask import Flask, render_template, jsonify, url_for
from flask import request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
from pandas_datareader import data as wb
from scipy.stats import norm

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods =['GET', 'POST'])
def startPage():
    if request.method == 'POST':
        stockTicker = request.form.get("tradingSymbol")
        time = request.form.get("timePeriod")

        stockTicker = request.args.get("stockTicker", stockTicker)

        # inputData = market.getData(tradingSymbol)
        # a flask route function returns html (or a html render_template)
        # mainFunction(stockTicker)
        #add variables and their template equiv after the renderTemplate
        return render_template('searchPage.html', stockTick = stockTicker)
    return render_template('index.html', stockTick= "")

@app.route("/matplot-as-image-<stockTick>.png")
def graph(stockTick):

    data = pd.DataFrame()
    data[stockTick] = wb.DataReader(stockTick, data_source='yahoo', start='2010-1-1')['Adj Close']
    #percent change of asset price
    log_returns = np.log(1+ data.pct_change())


    #graph showing growth over time beginning from 2015
    data.plot(figsize = (10,6));
    #graph of log returns of input ticker
    #returns are normally distributed and have a consistent mean
    log_returns.plot(figsize = (10,6))


    #calculations
    averageDailyReturn = log_returns.mean()
    variance = log_returns.var()
    drift = averageDailyReturn-(variance/2)
    standardDeviation = log_returns.std()


    #Brownian Motion equation
    #r = drift + standardDeviation * (e^r)
    #prediction of future stock price based on simulation below using numpy for storing data into array
    np.array(drift)
    drift.values
    standardDeviation.values

    #Brownian motion variable correlating to the distance between the mean and the number of standard deviation
    norm.ppf(0.95)

    #10 x 2 Matrix
    x = np.random.rand(10,2)
    norm.ppf(x)

    #stores distances from the mean value, 0, into the 10 x 2 matrix
    Z = norm.ppf(np.random.rand(10,2))

    #time interval for the stock price forecast
    timeInterval = 365
    iterations = 10

    #r = drift + standardDeviation * (e^r)
    #10 sets of 365 random future stock prices of the ticker symbol
    dailyReturns = np.exp(drift.values + standardDeviation.values * norm.ppf(np.random.rand(timeInterval,iterations)))


    #returns into price points
    presentPrice = data.iloc[-1]
    priceList = np.zeros_like(dailyReturns)
    priceList[0] = presentPrice
    #iteration for the time interavl of 365
    for t in range(1, timeInterval):
        priceList[t] = priceList[t-1] * dailyReturns[t]

    #showcases 10 paths of the future stock price
    plt.figure(figsize =(10,6))
    plt.plot(priceList)
    plt.xlabel("Days")
    plt.ylabel("Price $ Value")


    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(priceList)
    axis.set_ylabel("Price $ Value")
    axis.set_xlabel("Days")
    axis.set_title(stockTick)


    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")

#local deployment on  flask server
if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
