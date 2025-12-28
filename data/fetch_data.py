import yfinance as yf
import pandas as pd

TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN",
    "META", "NVDA", "JPM", "TSLA"
]

START_DATE = "2019-01-01"
END_DATE = None  # up to today

def fetch_prices():
    prices = yf.download(
        TICKERS,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=True
    )["Close"]

    prices.to_csv("data/raw/prices.csv")
    return prices

if __name__ == "__main__":
    fetch_prices()
