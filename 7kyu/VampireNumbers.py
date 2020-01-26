def vampire_test(x, y):
    z = x*y
    return sorted(str(z)) == sorted(str(x)+str(y))