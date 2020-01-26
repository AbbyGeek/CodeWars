def filter_list(l):
    new = []
    for x in l:
        if type(x) == int and x >= 0:
            new.append(x)
    return new