def stray(arr):
    d = {}
    for x in arr:
        if x not in d:
            d.update({x:1})
        else: d[x] += 1
    for x in d:
        if d[x] == 1:
            return x