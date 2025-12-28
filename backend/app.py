from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from optimization.portfolio_optimizer import PortfolioOptimizer
from simulation.monte_carlo import monte_carlo_simulation
from config.risk_profiles import RISK_PROFILES
templates = Jinja2Templates(directory="backend/templates")

app = FastAPI(title="Future Portfolio Advisor")

# -------------------------
# Request model
class PortfolioRequest(BaseModel):
    initial_investment: float
    years: int
    risk_profile: str
    custom_mu: Optional[Dict[str, float]] = None


# -------------------------
# Load static data ONCE (important)
prices = pd.read_csv(
    "data/raw/prices.csv",
    index_col=0,
    parse_dates=True
)

DEFAULT_MU = {
    "AAPL": 0.00009135,
    "AMZN": -0.00002627,
    "GOOGL": 0.00004691,
    "JPM": 0.00053149,
    "META": 0.00024350,
    "MSFT": 0.00008505,
    "NVDA": -0.00086558,
    "TSLA": -0.00020471
}


@app.post("/optimize")
def optimize_portfolio(request: PortfolioRequest):

    # -------------------------
    # Guardrails
    if request.initial_investment <= 0:
        raise HTTPException(status_code=400, detail="Investment must be positive")

    if request.years <= 0:
        raise HTTPException(status_code=400, detail="Years must be positive")

    if request.risk_profile not in RISK_PROFILES:
        raise HTTPException(
            status_code=400,
            detail=f"Risk profile must be one of {list(RISK_PROFILES.keys())}"
        )

    # -------------------------
    # Select mu
    mu_daily = request.custom_mu or DEFAULT_MU
    mu_annual = {k: v * 252 for k, v in mu_daily.items()}

    # -------------------------
    # Optimization
    params = RISK_PROFILES[request.risk_profile]

    optimizer = PortfolioOptimizer(
        min_weight=params["min_weight"],
        max_weight=params["max_weight"]
    )

    weights, stats = optimizer.optimize(
        prices=prices,
        mu_dict=mu_annual
    )

    # -------------------------
    # Monte Carlo
    paths = monte_carlo_simulation(
        initial_investment=request.initial_investment,
        annual_return=stats["expected_return"],
        annual_volatility=stats["volatility"],
        years=request.years
    )

    final_values = paths[-1]

    return {
        "portfolio": {
            "weights": weights,
            "expected_return": stats["expected_return"],
            "volatility": stats["volatility"],
            "sharpe": stats["sharpe"]
        },
        "projection": {
            "years": request.years,
            "median": float(np.median(final_values)),
            "worst_10": float(np.percentile(final_values, 10)),
            "best_90": float(np.percentile(final_values, 90))
        }
    }
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
