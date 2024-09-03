import numpy as np


def calculate_var(returns, confidence_level=0.95):
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var


def calculate_cvar(returns, var):
    cvar = returns[returns <= var].mean()
    return cvar


def calculate_max_drawdown(returns):
    cumulative_returns = (1 + returns).cumprod()
    drawdowns = 1 - cumulative_returns / cumulative_returns.cummax()
    max_drawdown = drawdowns.max()
    return max_drawdown


# Add more risk metrics and Monte Carlo simulation here
