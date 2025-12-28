from config.risk_profiles import RISK_PROFILES
from optimization.portfolio_optimizer import PortfolioOptimizer

profile = "balanced"

params = RISK_PROFILES[profile]

optimizer = PortfolioOptimizer(
    min_weight=params["min_weight"],
    max_weight=params["max_weight"]
)
