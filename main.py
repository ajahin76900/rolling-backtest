import pandas as pd
import numpy as np

from load_prices import load_prices
from ma_signal import ma_signal

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

    print("Cheating total return:", (1 + cheat).prod() - 1)
    print("Honest total return:  ", (1 + honest).prod() - 1)
    print("Buy & hold:           ", (1 + returns.dropna()).prod() - 1)