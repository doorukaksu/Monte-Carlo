# Monte-Carlo
Monte Carlo Simulation to visualise stock portfolio return


- Fetches historical stock price data from Yahoo Finance  
- Calculates daily returns, mean returns, and the covariance matrix  
- Builds a randomly weighted stock portfolio  
- Runs a Monte Carlo simulation of the portfolio value over time  
- Plots the simulated portfolio value paths


Requirements:
    - Python 3.9+
    - Pandas
    - NumPy
    - MatPlotLib
    - yFinance

Tweaks:
    - Change tickers to simulate different stocks
    - Change timedelta to look over a different historical window
    - Change parameters numSims, T, initialPortfolio to observe different results