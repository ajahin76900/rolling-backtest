def ma_signal(px, fast, slow):
    fast_ma = px.rolling(fast).mean()
    slow_ma = px.rolling(slow).mean()
    return (fast_ma > slow_ma).astype(int)