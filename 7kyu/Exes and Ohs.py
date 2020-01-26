def xo(s):
    ex = 0
    oh = 0
    for x in s:
        if x.upper() == "X":
            ex += 1
        if x.upper() == "O":
            oh += 1
    return ex == oh