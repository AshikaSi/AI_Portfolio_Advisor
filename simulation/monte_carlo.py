import numpy as np

def monte_carlo_simulation(
    initial_investment: float,
    annual_return: float,
    annual_volatility: float,
    years: int = 10,
    simulations: int = 10000
):
    dt = 1  # yearly steps
    paths = np.zeros((years + 1, simulations))
    paths[0] = initial_investment

    for t in range(1, years + 1):
        shocks = np.random.normal(0, 1, simulations)
        paths[t] = paths[t - 1] * np.exp(
            (annual_return - 0.5 * annual_volatility**2) * dt
            + annual_volatility * shocks
        )

    return paths
