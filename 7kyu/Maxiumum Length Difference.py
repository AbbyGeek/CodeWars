def mxdiflg(a1, a2):
    one = []
    two = []
    if a1 == [] or a2 == []:
        return -1
    for x in a1:
        one.append(len(x))
    for x in a2:
        two.append(len(x))
    ans1 = abs(max(one) - min(two))
    ans2 = abs(max(two) - min(one))
    return max(ans1, ans2)