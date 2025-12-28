import pandas as pd
from pypfopt import EfficientFrontier, risk_models


class PortfolioOptimizer:
    def __init__(self, min_weight=0.05, max_weight=0.30):
        self.min_weight = min_weight
        self.max_weight = max_weight

    def optimize(self, prices: pd.DataFrame, mu_dict: dict):
        mu = pd.Series(mu_dict)

        cov = risk_models.sample_cov(prices, frequency=252)

        ef = EfficientFrontier(mu, cov)

        ef.add_constraint(lambda w: w >= self.min_weight)
        ef.add_constraint(lambda w: w <= self.max_weight)

        ef.max_sharpe()
        cleaned_weights = ef.clean_weights()

        perf = ef.portfolio_performance()

        return cleaned_weights, {
            "expected_return": perf[0],
            "volatility": perf[1],
            "sharpe": perf[2]
        }
