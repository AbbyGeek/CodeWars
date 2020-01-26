def get_sum(a,b):
    tot = 0
    if a > b:
        high = a
        low = b
    else: 
        high = b
        low = a
    for x in range(low, high+1):
        tot += x
    return tot