
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Example data (replace with your own DataFrame)
df = pd.read_csv("/mnt/c/Users/ketsi/crypto-anomaly-detector/src/detected_anomalies.csv", parse_dates=["Date"])

# Sidebar controls
st.sidebar.header("Filters & Options")

# Date range picker
min_date, max_date = df["Date"].min(), df["Date"].max()
date_range = st.sidebar.date_input(
    "Select date range:",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter data by date
start_date, end_date = date_range
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# Toggle buttons for anomaly view
anomaly_view = st.sidebar.radio(
    "Anomaly Type:",
    ["Z-score only", "Isolation Forest only", "Combined anomalies"]
)

# Show/hide price history
show_price_history = st.sidebar.checkbox("Show full price history", value=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))

if show_price_history:
    ax.plot(filtered_df["Date"], filtered_df["Close"], label="Price History", alpha=0.6)

if anomaly_view == "Z-score only":
    anomalies = filtered_df[filtered_df["z_anomaly"] == 1]
    ax.scatter(anomalies["Date"], anomalies["Close"], color="red", label="Z-score Anomaly")
elif anomaly_view == "Isolation Forest only":
    anomalies = filtered_df[filtered_df["iso_anomaly"] == 1]
    ax.scatter(anomalies["Date"], anomalies["Close"], color="blue", label="Isolation Forest Anomaly")
else:
    anomalies = filtered_df[(filtered_df["z_anomaly"] == 1) | (filtered_df["iso_anomaly"] == 1)]
    ax.scatter(anomalies["Date"], anomalies["Close"], color="purple", label="Combined Anomalies")

ax.set_title("Anomaly Detection Dashboard")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)