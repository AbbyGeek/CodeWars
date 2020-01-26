def accum(s):
    newS = ""
    count = 0
    for x in s:
        newS += x.upper() + x.lower() * count + "-"
        count += 1
    return newS[:len(newS)-1]