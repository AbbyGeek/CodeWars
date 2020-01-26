def row_sum_odd_numbers(n):
    i = 1
    tot = 0
    x = 1
    while i <= n:
        tot += (n**2)-n+x
        i += 1
        x += 2
    return tot