def nba_extrap(ppg, mpg):
    x = mpg/48.0
    return round(ppg / x,1)