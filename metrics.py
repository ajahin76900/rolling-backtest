import numpy as np

PPY = 252  # trading days per year

def annualised_return(r, ppy=PPY):
    total_growth = (1 + r).prod()
    years = len(r) / ppy
    return total_growth ** (1 / years) - 1

def annualised_volatility(r, ppy=PPY):
    return r.std() * np.sqrt(ppy)

def sharpe_ratio(r, rf=0.0, ppy=PPY):
    excess = r - rf / ppy
    return excess.mean() / excess.std() * np.sqrt(ppy)

def drawdown_series(r):
    equity = (1 + r).cumprod()
    running_max = equity.cummax()
    return equity / running_max - 1

def max_drawdown(r):
    return drawdown_series(r).min()
