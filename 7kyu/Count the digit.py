def nb_dig(n, d):
    string = ""
    count = 0
    for x in range(n+1):
        string += str(x**2)
    for x in string:
        if x == str(d):
            count += 1
    return count