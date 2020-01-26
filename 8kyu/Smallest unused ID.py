def next_id(arr):
    ans = 0
    if arr == []:
        return 0
    while ans < max(arr):
        if ans in arr:
            ans += 1
        else: return ans
    return max(arr)+1