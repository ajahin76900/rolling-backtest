import pandas as pd
import yfinance as yf

def load_prices(ticker, start):
    df = yf.download(ticker, start=start, auto_adjust=True, progress=False)
    px = df["Close"]
    if isinstance(px, pd.DataFrame):
        px = px.squeeze(axis=1)
    return px.dropna()