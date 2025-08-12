# Crypto Anomaly Detector

This project detects unusual price movements (anomalies) in cryptocurrency data, specifically Bitcoin (BTC), using a combination of two methods: the Z-score statistical method and the Isolation Forest machine learning algorithm. By combining these approaches, we improve the accuracy and reliability of detecting market anomalies such as sudden spikes, drops, or unusual trading patterns.

## Goals
- Collect and analyze real-time market data
- Detect anomalies such as flash crashes, spikes, and outliers
- Visualize results in an interactive Streamlit dashboard

How It Works
Data Collection
We fetch historical Bitcoin price data using the yfinance library.

Z-Score Anomaly Detection
This statistical method calculates how far each price is from the average price in terms of standard deviations. Prices with Z-scores above or below a set threshold (±3) are considered anomalies.

Isolation Forest Anomaly Detection
This machine learning algorithm isolates data points by randomly splitting the data. Points that are easier to isolate (unusual points) are flagged as anomalies.

Combining Results
We flag a data point as an anomaly if it is detected by either the Z-score method or the Isolation Forest method. This combination helps catch a wider range of unusual behaviors.

Using the Project
Run the Python script to download data, detect anomalies, and save results.

Use the Streamlit dashboard to interactively explore anomalies:

View anomalies detected by either or both methods.

Filter anomalies by date.

Visualize the Bitcoin price with anomalies highlighted.

## Why This Matters
Detecting anomalies in financial data can help investors and analysts identify unusual market activity, potentially signaling risks or opportunities. This project showcases fundamental data science and machine learning techniques applied to real-world financial data, demonstrating skills relevant to roles in quantitative finance and data analysis.

## Tools
- Python, Pandas, Scikit-learn, Matplotlib
- API
- Streamlit for dashboard

