def show_sequence(n):
    tot = 0
    string = ""
    if n == 0:
        return "0=0"
    if n < 0:
        return "%i<0" % (n)
    for x in range(n+1):
        tot += x
        string += "%i+" % (x)
    return string[:len(string)-1] + " = " + str(tot)