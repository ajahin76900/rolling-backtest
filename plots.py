import matplotlib.pyplot as plt

from metrics import drawdown_series

def plot_results(strat_returns, bh_returns):
    strat_equity = (1 + strat_returns).cumprod()
    bh_equity = (1 + bh_returns).cumprod()

    fig, ax = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    ax[0].plot(strat_equity.index, strat_equity.values, label="Strategy")
    ax[0].plot(bh_equity.index, bh_equity.values, label="Buy & Hold")
    ax[0].set_title("Equity Curve (Growth of £1)")
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    strat_dd = drawdown_series(strat_returns)
    bh_dd = drawdown_series(bh_returns)

    ax[1].fill_between(strat_dd.index, strat_dd.values, 0, alpha=0.4, label="Strategy")
    ax[1].fill_between(bh_dd.index, bh_dd.values, color="grey", label="Buy & Hold")
    ax[1].set_title("Drawdown")
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("backtest_results.png", dpi=150)
    print("Saved chart to backtest_results.png")
    plt.show()