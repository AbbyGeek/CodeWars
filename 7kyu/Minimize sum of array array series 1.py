def min_sum(arr):
    total = 0
    while len(arr) > 1:
        total += max(arr) * min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return total