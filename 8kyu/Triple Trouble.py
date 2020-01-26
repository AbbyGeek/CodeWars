def triple_trouble(one, two, three):
    new = ""
    for x in range(len(one)):
        new += one[x:x+1] + two[x:x+1] + three[x:x+1]
    return new