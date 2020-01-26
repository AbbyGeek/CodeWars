def array_madness(a,b):
    sumA = 0
    sumB = 0
    for x in a:
        sumA += x**2
    for x in b:
        sumB += x**3
    if sumA > sumB:
        return True
    else: return False