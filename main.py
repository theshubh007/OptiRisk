from fastapi import FastAPI
from api import portfolio, riskapi

app = FastAPI()

app.include_router(portfolio.router, prefix="/api/v1/portfolio")
app.include_router(riskapi.router, prefix="/api/v1/risk")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio Optimization API"}
