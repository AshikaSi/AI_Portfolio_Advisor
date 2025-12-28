import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX


class SARIMAXForecaster:
    def __init__(self, horizon_days=252):
        self.horizon = horizon_days

    def forecast_expected_returns(self, log_returns: pd.DataFrame):
        mu = {}

        for stock in log_returns.columns:
            series = log_returns[stock].dropna()

            model = SARIMAX(
                series,
                order=(1, 0, 1),
                seasonal_order=(0, 0, 0, 0),
                enforce_stationarity=False,
                enforce_invertibility=False
            )

            fitted = model.fit(disp=False)
            forecast = fitted.forecast(self.horizon)

            expected_return = forecast.mean() * 252
            mu[stock] = expected_return

            print(f"{stock}: expected μ = {expected_return:.4f}")

        return mu
