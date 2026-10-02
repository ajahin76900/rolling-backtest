def strategy_returns(px, signal, cost=0.0005):
    returns = px.pct_change()

    position = signal.shift(1).fillna(0)

    turnover = (position.diff().abs()).fillna(0)

    gross = position * returns

    net = gross - turnover * cost

    return net.dropna()