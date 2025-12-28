import numpy as np
from monte_carlo import monte_carlo_simulation

# Example portfolio stats (replace with optimizer output)
portfolio_return = 0.18
portfolio_volatility = 0.22

paths = monte_carlo_simulation(
    initial_investment=100000,
    annual_return=portfolio_return,
    annual_volatility=portfolio_volatility,
    years=10
)

final_values = paths[-1]

print("10-Year Projection (₹1,00,000 invested):")
print("Median:", round(np.median(final_values), 2))
print("10% Worst Case:", round(np.percentile(final_values, 10), 2))
print("90% Best Case:", round(np.percentile(final_values, 90), 2))
