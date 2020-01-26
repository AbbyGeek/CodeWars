def find_difference(a, b):
    Avol = 1
    Bvol = 1
    for x in a:
        Avol *= x
    for x in b:
        Bvol *= x
    diff = Avol - Bvol
    if diff > 0:
        return diff
    else:
        return diff*(-1)