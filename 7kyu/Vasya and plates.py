def count_clean(b, p, dishes):
    washes = 0
    for x in dishes:
        if x == 1:
            if b > 0:
                b = b-1
            else: washes += 1
        if x == 2:
            if p > 0:
                p -= 1
            elif b > 0:
                b -= 1
            else: washes += 1
    return washes