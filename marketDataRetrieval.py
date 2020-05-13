#import of libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

def getData(tradingSymbol): 
    #ticker selection
    tradingSymbol = input("Enter a trading symbol: ")
    data = pd.DataFrame()
    data[tradingSymbol] = wb.DataReader(tradingSymbol, data_source='yahoo', start='2007-1-1')['Adj Close']

    log_returns = np.log(1+ data.pct_change())
    print("\nHead Data")
    print(log_returns.head())

    print("\nTail Data")
    print(log_returns.tail())

    data.plot(figsize = (10,6));
    plt.show()
