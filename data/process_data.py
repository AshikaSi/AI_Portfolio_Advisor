import pandas as pd
import numpy as np

def process_data():
    prices = pd.read_csv("data/raw/prices.csv", index_col=0, parse_dates=True)

    simple_returns = prices.pct_change().dropna()
    cov_matrix =   simple_returns.cov() * 252

    simple_returns.to_csv("data/processed/simple_returns.csv")
    cov_matrix.to_csv("data/processed/cov_matrix.csv")

    print("Saved processed data")

if __name__ == "__main__":
    process_data()
