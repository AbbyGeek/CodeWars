def min_value(digits):
    numlist = []
    for x in digits:
        if x not in numlist:
            numlist.append(x)
    numlist = sorted(numlist)
    tot = 0

    for x in numlist:
        tot += + x*(10**(len(numlist)-numlist.index(x)))/10
    return tot