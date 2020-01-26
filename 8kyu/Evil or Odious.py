def evil(n):
    n = str(bin(n))
    count = 0
    for x in n:
        if x == "1":
            count += 1
    if count % 2 == 0:
        return "It's Evil!"
    else: return "It's Odious!"