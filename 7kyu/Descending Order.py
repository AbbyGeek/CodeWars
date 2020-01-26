def Descending_Order(num):
    num = sorted([int(x) for x in str(num)])[::-1]
    thing = ""
    for x in num:
        thing += str(x)
    return int(thing)