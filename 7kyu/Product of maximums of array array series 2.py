def max_product(lst, n):
    tot = 1
    lst.sort()
    lst = lst[::-1]
    for x in range(n):
        tot = tot * lst[x]
    return tot
    