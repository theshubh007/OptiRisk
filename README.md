
# OptiRisk

OptiRisk is a portfolio optimization and risk management API designed to enhance investment strategies by providing sophisticated tools for portfolio optimization and risk assessment. Built with FastAPI, the application offers endpoints for optimizing portfolio allocations and calculating various risk metrics using historical asset data. The project integrates advanced optimization techniques, comprehensive risk assessments, and modular code for easy maintenance and extensibility.
## Features

### 1. Portfolio Optimization:
- OptiRisk uses historical asset data to optimize portfolio weights, aiming to maximize the Sharpe Ratio. This involves calculating the optimal mix of assets to achieve the best risk-adjusted returns. The core optimization is performed using the Mean-Variance Optimization approach, facilitated by the Sequential Least Squares Quadratic Programming (SLSQP) algorithm.
- **Key Aspects:**
  - **Historical Data Analysis:** Downloads historical price data and computes mean returns and covariance matrix.
  - **Optimization Algorithm:** Uses the SLSQP method to determine the optimal asset weights.
  - **Performance Calculation:** Evaluates portfolio returns and standard deviation to maximize the Sharpe Ratio.

### 2. Risk Management:
- The API provides comprehensive risk management tools to evaluate the potential financial risks associated with the portfolio. It calculates essential risk metrics, including Value at Risk (VaR), Conditional Value at Risk (CVaR), and Maximum Drawdown.
- **Key Aspects:**
  - **Value at Risk (VaR):** Measures the maximum expected loss over a specified time period with a given confidence level.
  - **Conditional Value at Risk (CVaR):** Estimates the average loss given that the loss exceeds the VaR, highlighting tail risk.
  - **Maximum Drawdown:** Assesses the peak-to-trough decline in portfolio value, providing insights into the severity of potential losses.

### 3. Authentication and Rate Limiting:
- OptiRisk incorporates authentication and rate limiting to secure API access and prevent abuse. These features ensure that the API remains responsive and available while protecting against excessive requests.
- **Key Aspects:**
  - **Rate Limiting:** Enforces limits on the number of requests per minute/hour to prevent abuse and ensure fair usage.
  
  
  



## API Endpoints:

#### 1. Portfolio Optimization

```
 GET: http://127.0.0.1:8000/api/v1/portfolio/optimize-portfolio
```
- Description: Optimizes portfolio weights to maximize the Sharpe Ratio using historical asset data.


```
Request body:
{
  "assets": ["AAPL", "MSFT", "GOOGL"],
  "start_date": "2020-01-01",
  "end_date": "2023-01-01"
}


```

``` 
Returns:
{
  "optimized_portfolio": {
    "AAPL": 0.3,
    "MSFT": 0.4,
    "GOOGL": 0.3
  }
}

   ```

#### 2. Risk Calculation:

```
 POST: http://127.0.0.1:8000/api/v1/risk/calculate-risk
```
- Description: Calculates VaR, CVaR, and Maximum Drawdown for the portfolio based on historical data.

```
Request body:
{
  "assets": ["AAPL", "MSFT", "GOOGL"],
  "start_date": "2020-01-01",
  "end_date": "2023-01-01"
}

```
```
Returns:
{
  "VaR": -0.05,
  "CVaR": -0.07,
  "Max Drawdown": -0.2
}

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or features.

