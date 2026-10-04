import pandas as pd
import numpy as np

from load_prices import load_prices
from ma_signal import ma_signal
from strategy_returns import strategy_returns
from metrics import annualised_return, annualised_volatility, sharpe_ratio, max_drawdown
from plots import plot_results

ticker = "SPY"
start = "2005-01-01"


if __name__ == "__main__":
    px = load_prices(ticker, start)
    bh_returns = px.pct_change().dropna()

    signal = ma_signal(px, fast=50, slow=200)
    strat_returns = strategy_returns(px, signal, cost=0.0005)

    print(f"{'Metric':<20}{'Strategy':>12}{'Buy & Hold':>12}")
    print(f"{'CAGR':<20}{annualised_return(strat_returns):>12.2%}{annualised_return(bh_returns):>12.2%}")
    print(f"{'Volatility':<20}{annualised_volatility(strat_returns):>12.2%}{annualised_volatility(bh_returns):>12.2%}")
    print(f"{'Sharpe Ratio':<20}{sharpe_ratio(strat_returns):>12.2f}{sharpe_ratio(bh_returns):>12.2f}")
    print(f"{'Max Drawdown':<20}{max_drawdown(strat_returns):>12.2%}{max_drawdown(bh_returns):>12.2%}")

    plot_results(strat_returns, bh_returns)
