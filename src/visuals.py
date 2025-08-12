import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data
btc = yf.download('BTC-USD', start='2022-01-01', end='2024-12-31')
btc['Daily Return'] = btc['Adj Close'].pct_change()

# Plot Adjusted Close Price
plt.figure(figsize=(14, 5))
plt.plot(btc['Adj Close'], label='BTC Adj Close')
plt.title('BTC-USD Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Plot Daily Returns
plt.figure(figsize=(14, 4))
btc['Daily Return'].plot()
plt.title('BTC Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.grid()
plt.show()

