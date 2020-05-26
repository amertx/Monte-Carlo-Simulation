#Prediction model using an instance of the Monte Carlo simulation and Brownian Motion equation


#import of libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

#ticker selection
tradingSymbol = input("Enter a trading symbol: ")
data = pd.DataFrame()
data[tradingSymbol] = wb.DataReader(tradingSymbol, data_source='yahoo', start='2010-1-1')['Adj Close']

#percent change of asset price
log_returns = np.log(1+ data.pct_change())

print("\nHead Data")
print(log_returns.head())

print("\nTail Data")
print(log_returns.tail())

#graph showing growth over time beginning from 2015
data.plot(figsize = (10,6));
plt.show()

#graph of log returns of input ticker
#returns are normally distributed and have a consistent mean
log_returns.plot(figsize = (10,6))
plt.show()


#calculations
averageDailyReturn = log_returns.mean()
variance = log_returns.var()
drift = averageDailyReturn-(variance/2)
standardDeviation = log_returns.std()


def retrievals():
    #All retrievals are using Pandas Series Library
    print("\nMean Retrieval")
    print(averageDailyReturn)

    #variance represents how spread out the data is from the average
    #variance will represent the best way to represent the variability and volatility
    print("\nVariance Retrieval")
    print(variance)

    #drift calculation
    #Drift = averageDailyReturn-(variance/2)
    print("\nDrift calculation")
    print(drift)

    #standard deviation calculation
    print("\nStandard Deviation Retrieval")
    print(standardDeviation)

    #Brownian Motion equation
    #r = drift + standardDeviation * (e^r)

    #prediction of future stock price based on simulation below using numpy for storing data into array
    #print(type(drift))

#calling of function
retrievals()


np.array(drift)
drift.values
standardDeviation.values

#Brownian motion variable correlating to the distance between the mean and the number of standard deviation
norm.ppf(0.95)

#10 x 2 Matrix
x = np.random.rand(10,2)
print(x)
j
s
