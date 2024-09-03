from fastapi import APIRouter, Depends
from core.risk import calculate_var, calculate_cvar, calculate_max_drawdown
from datamodels import PortfolioRequest
from utils import download_data

router = APIRouter()


@router.post("/calculate-risk")
def calculate_risk_endpoint(request: PortfolioRequest):
    data = download_data(request.assets, request.start_date, request.end_date)
    returns = data.pct_change().dropna()

    var = calculate_var(returns)
    cvar = calculate_cvar(returns, var)
    max_drawdown = calculate_max_drawdown(returns)

    return {"VaR": var, "CVaR": cvar, "Max Drawdown": max_drawdown}
