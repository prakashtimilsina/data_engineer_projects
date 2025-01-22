# Building a Free End-to-End AI Trading Bot

This guide walks you through building a **free end-to-end AI trading bot** that predicts stock price movements and executes trades automatically using free tools and services wherever possible. Additionally, we cover how to enable **live trading with real money** safely.

---

## **1. Setup the Environment**
### **1.1 Install Required Packages**
```bash
pip install yfinance alpaca-trade-api pandas numpy scikit-learn ta zipline backtrader tensorflow transformers streamlit
```
- **Free tools used**: Open-source Python libraries.

---

## **2. Fetch Free Stock Data**
Use **Yahoo Finance** (free) to get stock data.
```python
import yfinance as yf  
import pandas as pd  

def fetch_stock_data(ticker, start, end):  
    stock = yf.download(ticker, start=start, end=end, interval="1h")  
    stock.to_csv(f"{ticker}.csv")  
    return stock  

data = fetch_stock_data("AAPL", "2023-01-01", "2024-01-01")  
print(data.head())  
```
- **Free tools used**: Yahoo Finance API (free stock market data).

---

## **3. Add Technical Indicators**
```python
import ta  

def add_indicators(df):  
    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()  
    df["macd"] = ta.trend.MACD(df["Close"]).macd()  
    df["sma50"] = df["Close"].rolling(50).mean()  
    df["sma200"] = df["Close"].rolling(200).mean()  
    return df  

data = add_indicators(data)  
print(data.tail())  
```
- **Free tools used**: `ta` package for technical indicators.

---

## **4. Train AI Model for Buy/Sell Predictions**
```python
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  

data.dropna(inplace=True)  
data["Target"] = (data["Close"].shift(-1) > data["Close"]).astype(int)  

X = data[["rsi", "macd", "sma50", "sma200"]]  
y = data["Target"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  

model = RandomForestClassifier(n_estimators=100)  
model.fit(X_train, y_train)  

print("Model trained!")  
```
- **Free tools used**: Scikit-learn (open-source machine learning library).

---

## **5. Backtest the Strategy**
```python
import backtrader as bt  

class TestStrategy(bt.Strategy):  
    def next(self):  
        if self.data.close[0] > self.data.sma50[0]:  
            self.buy()  
        elif self.data.close[0] < self.data.sma50[0]:  
            self.sell()  

cerebro = bt.Cerebro()  
data_feed = bt.feeds.PandasData(dataname=data)  
cerebro.adddata(data_feed)  
cerebro.addstrategy(TestStrategy)  
cerebro.run()  
cerebro.plot()  
```
- **Free tools used**: Backtrader (open-source backtesting framework).

---

## **6. Execute Trades Using Alpaca API**
### **6.1 Setup Alpaca API**
1. **Sign up at** [Alpaca](https://alpaca.markets/).  
2. **Get API Key & Secret** (from dashboard).  
3. **Use API to place orders**  

#### **6.2 Live Trading with Real Money**
1. **Upgrade to a Live Trading Account** on Alpaca.  
2. **Replace Paper Trading API with Live Trading API**:

```python
import alpaca_trade_api as tradeapi  

API_KEY = "YOUR_ALPACA_LIVE_API_KEY"  
SECRET_KEY = "YOUR_ALPACA_LIVE_SECRET_KEY"  
BASE_URL = "https://api.alpaca.markets"  # Use live URL instead of paper API

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")  

api.submit_order(  
    symbol="AAPL",  
    qty=1,  
    side="buy",  
    type="market",  
    time_in_force="gtc"  
)  
print("Live Trade Executed!")  
```
- **Live trading enabled**: Use real money (ensure you have funds in your Alpaca account).

---

## **7. Automate & Deploy for Free**
### **7.1 Automate Trading with Cron Job**
```bash
crontab -e
```
Add:
```bash
0 * * * * python3 /path/to/trading_bot.py  
```
- **Free tools used**: Linux cron jobs (task automation for free).

### **7.2 Deploy Free on Google Cloud (GCP Free Tier)**
1. **Create a Free VM**:
```bash
gcloud compute instances create trading-bot --machine-type=f1-micro  
```
2. **Upload Your Code**:
```bash
gcloud compute scp trading_bot.py trading-bot:~/  
```
3. **Run Bot on GCP**:
```bash
gcloud compute ssh trading-bot --command="python3 trading_bot.py"  
```
- **Free tools used**: GCP Free Tier (free cloud computing resources).

### **7.3 Web Dashboard with Streamlit**
```python
import streamlit as st  

st.title("AI Trading Bot Dashboard")  
st.write("Latest Predictions & Trade Signals")  

st.line_chart(data["Close"])  
st.dataframe(data.tail())  
```
Run:
```bash
streamlit run dashboard.py  
```
- **Free tools used**: Streamlit (free data visualization tool).

---

## **🚀 Final Checklist for AI Trading Bot**
✅ **Stock Data Fetching (Yahoo Finance, Free)**  
✅ **Technical Indicators (RSI, MACD, Free)**  
✅ **AI Model for Prediction (Random Forest, Free)**  
✅ **Backtesting (Backtrader, Free)**  
✅ **Trade Execution (Alpaca, Free for Paper & Live Trading)**  
✅ **Live Trading with Real Money (Alpaca, Requires Funding)**  
✅ **Cloud Deployment (GCP Free Tier, Free)**  
✅ **Automated Execution (Cron Jobs, Free)**  
✅ **Live Dashboard (Streamlit, Free)**  

---

## **Next Steps**
Would you like:
1. **A GitHub repo template with all this code?**  
2. **More advanced models (LSTM, Reinforcement Learning)?**  
3. **Integration with additional brokers (Interactive Brokers, TD Ameritrade)?**  

Let me know how you'd like to proceed! 🚀

