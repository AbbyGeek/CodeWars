def find_multiples(integer, limit):
    new = []
    prod = 0
    count = 1
    while prod <= limit:
        new.append(integer*count)
        count += 1
        prod = count * integer
    return new