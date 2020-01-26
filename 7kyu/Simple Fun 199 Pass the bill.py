def pass_the_bill(total, c, r):
    needed = int(total/2)+1
    ind = total - c - r
    if needed > c + ind:
        return -1
    if needed < c:
        return 0
    else:
        return needed - c