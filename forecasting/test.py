import pandas as pd
from sarimax_model import SARIMAXForecaster

log_returns = pd.read_csv(
    "data/processed/log_returns.csv",
    index_col=0,
    parse_dates=True
)

forecaster = SARIMAXForecaster(horizon_days=252)
mu = forecaster.forecast_expected_returns(log_returns)

print("\nExpected Returns:")
for k, v in mu.items():
    print(k, ":", v)
