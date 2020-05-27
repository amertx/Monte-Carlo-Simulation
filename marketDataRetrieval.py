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
data[tradingSymbol] = wb.DataReader(tradingSymbol, data_source='yahoo', start='2019-1-1')['Adj Close']
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


#calling of function
retrievals()

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
iterations = 5

#r = drift + standardDeviation * (e^r)
#10 sets of 365 random future stock prices of the ticker symbol
dailyReturns = np.exp(drift.values + standardDeviation.values * norm.ppf(np.random.rand(timeInterval,iterations)))
print(dailyReturns)

#returns into price points
presentPrice = data.iloc[-1]
print(presentPrice)
priceList = np.zeros_like(dailyReturns)
priceList[0] = presentPrice
#iteration for the time interavl of 365
for t in range(1, timeInterval):
    priceList[t] = priceList[t-1] * dailyReturns[t]

print(priceList[-1])
#showcases 10 paths of the future stock price
plt.figure(figsize =(10,6))
plt.plot(priceList)
plt.show()

exit()
