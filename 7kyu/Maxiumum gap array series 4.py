def max_gap(numbers):
    max = 0
    num = sorted(numbers)
    for x, y in enumerate(num):
        if num[x] - num[x-1] > max:
            max = num[x] - num[x-1]
    return max