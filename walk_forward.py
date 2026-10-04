import pandas as pd

from ma_signal import ma_signal
from strategy_returns import strategy_returns
from optimise import best_params

TRAIN_YEARS = 3
TEST_MONTHS = 12


def run_walk_forward(px, cost=0.0005):
    test_start = px.index[0] + pd.DateOffset(years=TRAIN_YEARS)

    oos_returns = []
    chosen_params = []

    while test_start < px.index[-1]:
        test_end = test_start + pd.DateOffset(months=TEST_MONTHS)
        train_start = test_start - pd.DateOffset(years=TRAIN_YEARS)
        train_end = test_start - pd.Timedelta(days=1)

        combo = best_params(px, train_start, train_end, cost)

        if combo is None:
            test_start = test_end
            continue

        fast, slow = combo

        test_px = px.loc[train_start:test_end]
        signal = ma_signal(test_px, fast, slow)
        rets = strategy_returns(test_px, signal, cost)

        oos_slice = rets.loc[test_start:test_end]
        oos_returns.append(oos_slice)

        chosen_params.append({
            "test_start": test_start.date(),
            "test_end": test_end.date(),
            "fast": fast,
            "slow": slow,
        })

        test_start = test_end

    combined = pd.concat(oos_returns)
    params_log = pd.DataFrame(chosen_params)

    return combined, params_log


if __name__ == "__main__":
    from load_prices import load_prices
    from metrics import annualised_return, annualised_volatility, sharpe_ratio, max_drawdown

    px = load_prices("SPY", "2005-01-01")
    wf_returns, params_log = run_walk_forward(px)

    print("=== Parameters chosen each period ===")
    print(params_log.to_string(index=False))

    print("\n=== Walk-forward out-of-sample performance ===")
    print(f"CAGR:         {annualised_return(wf_returns):.2%}")
    print(f"Volatility:   {annualised_volatility(wf_returns):.2%}")
    print(f"Sharpe:       {sharpe_ratio(wf_returns):.2f}")
    print(f"Max Drawdown: {max_drawdown(wf_returns):.2%}")