from fastapi import APIRouter, Depends
from core.optimization import optimize_portfolio
from datamodels import PortfolioRequest
from utils import download_data

router = APIRouter()


@router.post("/optimize-portfolio")
def optimize_portfolio_endpoint(request: PortfolioRequest):
    data = download_data(request.assets, request.start_date, request.end_date)
    mean_returns = data.pct_change().dropna().mean()
    cov_matrix = data.pct_change().dropna().cov()
    num_assets = len(request.assets)

    optimal_weights = optimize_portfolio(mean_returns, cov_matrix, num_assets)
    optimized_portfolio = dict(zip(request.assets, optimal_weights))

    return {"optimized_portfolio": optimized_portfolio}
