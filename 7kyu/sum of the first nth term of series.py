def series_sum(n):
    tot = 0
    denom = 1
    count = 0
    while count < n:
        tot += 1/denom
        count += 1
        denom += 3.00
    return '%.2f' % tot