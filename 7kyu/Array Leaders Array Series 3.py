def array_leaders(numbers):
    arr = []
    for x, y in enumerate(numbers):
        if y > sum(numbers[x+1:]):
            arr.append(y)
    return arr