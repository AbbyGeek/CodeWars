def sum_array(arr):
    if arr == [] or arr == None or len(arr) == 1: return 0
    else: return sum(arr) - max(arr) - min(arr)