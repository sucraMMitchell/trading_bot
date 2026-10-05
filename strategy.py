# simple moving average crossover logic

import numpy as np
import pandas as pd
import yfinance as yf


def generate_signals(ticker="AAPL"):
    # Fetch historical data using Yahoo Finance
    data = yf.download(ticker, period="1y", interval="1d")

    # Calculate 50-day and 200-day Simple Moving Averages
    data["SMA50"] = data["Close"].rolling(window=50).mean()
    data["SMA200"] = data["Close"].rolling(window=200).mean()

    # Generate signals: 1 = Buy, -1 = Sell
    data["Signal"] = 0
    data.iloc[50:, data.columns.get_loc("Signal")] = np.where(
        data["SMA50"][50:] > data["SMA200"][50:], 1, -1
    )

    # Track position changes
    data["Position"] = data["Signal"].shift()
    return data


# Example preview
df = generate_signals("AAPL")
print(df[["Close", "SMA50", "SMA200", "Signal"]].tail())