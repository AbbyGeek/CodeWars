def max_multiple(divisor, bound):
    if divisor == bound or divisor == 1: return bound
    if divisor > bound: return 0
    for x in range(bound):
        if divisor * x > bound:
            return (x - 1)*divisor