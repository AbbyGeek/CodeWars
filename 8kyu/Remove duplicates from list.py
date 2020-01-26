def distinct(seq):
    new_seq = []
    for x in seq:
        if x not in new_seq:
            new_seq += [x]
    return new_seq