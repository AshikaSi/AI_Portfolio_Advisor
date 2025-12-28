import numpy as np
import pandas as pd

from optimization.portfolio_optimizer import PortfolioOptimizer
from simulation.monte_carlo import monte_carlo_simulation
from config.risk_profiles import RISK_PROFILES


def run_advisor(
    capital: float,
    years: int,
    risk_profile: str
):
    # ----------------------------
    # Load Data
    returns = pd.read_csv("data/processed/simple_returns.csv")

    prices = pd.read_csv(
        "data/raw/prices.csv",
        index_col=0,
        parse_dates=True
    )

    cov_matrix = pd.read_csv(
        "data/processed/cov_matrix.csv",
        index_col=0
    )

    # Expected daily returns (from forecasting / assumptions)
    mu_dict = {
        "AAPL": 0.00009135,
        "AMZN": -0.00002627,
        "GOOGL": 0.00004691,
        "JPM": 0.00053149,
        "META": 0.00024350,
        "MSFT": 0.00008505,
        "NVDA": -0.00086558,
        "TSLA": -0.00020471
    }

    # ----------------------------
    # Risk Profile
    params = RISK_PROFILES[risk_profile]

    # ----------------------------
    # Optimization
    optimizer = PortfolioOptimizer(
        min_weight=params["min_weight"],
        max_weight=params["max_weight"]
    )

    mu_annual = {k: v * 252 for k, v in mu_dict.items()}

    weights, stats = optimizer.optimize(
        prices=prices,
        mu_dict=mu_annual
    )

    # ----------------------------
    # Monte Carlo Simulation
    paths = monte_carlo_simulation(
        initial_investment=capital,
        annual_return=stats["expected_return"],
        annual_volatility=stats["volatility"],
        years=years
    )

    final_values = paths[-1]

    # ----------------------------
    # Output
    output = {
        "portfolio": {
            "weights": weights,
            "expected_return": stats["expected_return"],
            "volatility": stats["volatility"],
            "sharpe": stats["sharpe"]
        },
        "projection": {
            "years": years,
            "median": float(np.median(final_values)),
            "worst_10": float(np.percentile(final_values, 10)),
            "best_90": float(np.percentile(final_values, 90))
        }
    }

    return output
