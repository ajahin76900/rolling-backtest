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


def plot_walk_forward_comparison(wf_returns, original_returns, bh_returns):
    wf_equity = (1 + wf_returns).cumprod()
    orig_equity = (1 + original_returns).cumprod()
    bh_equity = (1 + bh_returns).cumprod()

    fig, ax = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    ax[0].plot(wf_equity.index, wf_equity.values, label="Walk-forward")
    ax[0].plot(orig_equity.index, orig_equity.values, label="Original (fixed 50/200)")
    ax[0].plot(bh_equity.index, bh_equity.values, label="Buy & Hold")
    ax[0].set_title("Equity Curve (Growth of £1)")
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    wf_dd = drawdown_series(wf_returns)
    orig_dd = drawdown_series(original_returns)
    bh_dd = drawdown_series(bh_returns)

    ax[1].plot(wf_dd.index, wf_dd.values, label="Walk-forward")
    ax[1].plot(orig_dd.index, orig_dd.values, label="Original (fixed 50/200)")
    ax[1].plot(bh_dd.index, bh_dd.values, color="grey", label="Buy & Hold", alpha=0.6)
    ax[1].set_title("Drawdown")
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("walk_forward_results.png", dpi=150)
    print("Saved chart to walk_forward_results.png")
    plt.show()