import yfinance as yf  
import pandas as pd  

def fetch_stock_data(ticker, start, end):  
    stock = yf.download(ticker, start=start, end=end, interval="1h")  
    stock.to_csv(f"{ticker}.csv")  
    return stock  

data = fetch_stock_data("AAPL", "2025-01-01", "2025-01-23")  
print(data.tail())  