import pandas as pd
from portfolio_optimizer import PortfolioOptimizer

prices = pd.read_csv(
    "data/raw/prices.csv",
    index_col=0,
    parse_dates=True
)

mu = {
    "AAPL": 9.135323471433127e-05,
    "AMZN": -2.627848914674116e-05,
    "GOOGL": 4.690975877021386e-05,
    "JPM": 0.0005314935282971732,
    "META": 0.00024350368427016774,
    "MSFT": 8.505053867667019e-05,
    "NVDA": -0.0008655871357152819,
    "TSLA": -0.00020470811452909607
}

optimizer = PortfolioOptimizer(
    min_weight=0.05,
    max_weight=0.30
)

weights, perf = optimizer.optimize(prices, mu)

print("\nOptimized Portfolio Weights:")
for k, v in weights.items():
    print(k, ":", round(v, 3))
