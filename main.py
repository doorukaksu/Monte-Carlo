import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr

# Function to fetch stock data
def fetch_stock_data(stocks, startDate, endDate):
    stockData = pdr.get_data_yahoo(stocks, startDate, endDate)
    
    stockData = stockData['Close']
    returns = stockData.pct_change()
    
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    
    return meanReturns, covMatrix

stockList = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
stocks = [stock + ".US" for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

