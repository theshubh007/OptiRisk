import yfinance as yf


def download_data(assets, start_date, end_date):
    data = yf.download(assets, start=start_date, end=end_date)["Adj Close"]
    return data
