import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

# Function to fetch stock data
def fetch_stock_data(stocks, startDate, endDate):
    stockData = yf.download(stocks, startDate, endDate)
    
    stockData = stockData['Close']
    returns = stockData.pct_change()
    
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    
    return meanReturns, covMatrix

stockList = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = fetch_stock_data(stockList, startDate, endDate)

weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

# Monte Carlo Sim

numSims = 100
T = 100 # Time-Frame in days

meanM = np.full(shape = (T, len(weights)), fill_value=meanReturns)
meanM = meanM.T

portfolioSim = np.full(shape = (T, numSims), fill_value=0.0)

initialPortfolio = 10000

for m in range(0, numSims):
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covMatrix)
    dailyReturn = meanM + np.inner(L, Z)
    portfolioSim[:,m] = np.cumprod(np.inner(weights, dailyReturn.T)+1)*initialPortfolio
    
    
plt.plot(portfolioSim)
plt.ylabel('Portfolio Value')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Stock Portfolio')
plt.show()
