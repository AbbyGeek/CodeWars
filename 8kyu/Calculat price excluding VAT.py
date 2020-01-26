def excluding_vat_price(price):
    if price == None:
        return -1
    elif price == 0:
        return -1
    else:
        x = price/1.15
        x = round(x,2)
        return x