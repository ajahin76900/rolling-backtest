from ma_signal import ma_signal
from strategy_returns import strategy_returns
from metrics import sharpe_ratio

FAST_GRID = [10, 20, 30, 50]
SLOW_GRID = [100, 150, 200]


def best_params(px, start, end, cost=0.0005):
    """Find the (fast, slow) pairing that has the best Sharpe ratio
    using price data between start and end."""
    window_px = px.loc[start:end]

    candidates = [(f, s) for f in FAST_GRID for s in SLOW_GRID if f < s]

    best_combo = None
    best_score = float("-inf")

    for fast, slow in candidates:
        signal = ma_signal(window_px, fast, slow)
        rets = strategy_returns(window_px, signal, cost)

        if len(rets) < 30:
            continue

        score = sharpe_ratio(rets)

        if score > best_score:
            best_score = score
            best_combo = (fast, slow)

    return best_combo


if __name__ == "__main__":
    from load_prices import load_prices

    px = load_prices("SPY", "2005-01-01")
    combo = best_params(px, "2005-01-01", "2008-01-01")
    print("Best combo for 2005–2008 training window:", combo)