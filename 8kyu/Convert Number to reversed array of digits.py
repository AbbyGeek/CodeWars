def digitize(n):
    n = str(n)
    n = list(n[::-1])
    n = list(map(int, n))
    return n