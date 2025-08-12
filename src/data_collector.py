# src/data_collector.py

import yfinance as yf

# Choose a crypto-like ticker (Bitcoin vs USD on Yahoo Finance)
btc = yf.Ticker("BTC-USD")

# Get historical data (last 30 days)
hist = btc.history(period="30d")

# Print preview
print(hist.head())

