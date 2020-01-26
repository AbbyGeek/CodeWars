def find_short(s):
    s = s.split()
    count = []
    for x in s:
        count.append(len(x))
    return min(count)