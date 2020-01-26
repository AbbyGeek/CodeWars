def sequence_sum(begin, end, step):
    total = []
    while begin <= end:
        total.append(begin)
        begin += step
    return sum(total)