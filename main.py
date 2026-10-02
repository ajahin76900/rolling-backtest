import pandas as pd
import numpy as np

from load_prices import load_prices
from ma_signal import ma_signal
from strategy_returns import strategy_returns

ticker = "SPY"
start = "2005-01-01"


if __name__ == "__main__":
    px = load_prices(ticker, start)
    returns = px.pct_change()

    signal = ma_signal(px, fast=50, slow=200)
    print(signal.value_counts())

    cheat = (signal * returns).dropna()

    position = signal.shift(1).fillna(0)
    honest = (position * returns).dropna()

    print("Honest total return (net of costs):  ", (1 + honest).prod() - 1)
    print("Buy & hold total return:             ", (1 + returns.dropna()).prod() - 1)

    num_trades = signal.diff().abs().fillna(0).sum()
    print("Number of trades:", int(num_trades))