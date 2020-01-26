def fillable(stock, merch, n):
    if merch not in stock:
        return False
    if stock[merch] >= n:
        return True
    else: return False