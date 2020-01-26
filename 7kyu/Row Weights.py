def row_weights(array):
    one = 0
    two = 0
    for x, y in enumerate(array, 1):
        if x%2 != 0:
            one += y
        else:
            two += y
    return (one,two)