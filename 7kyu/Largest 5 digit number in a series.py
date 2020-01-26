def solution(digits):
    nums = []
    for x, y in enumerate(digits):
        nums.append(digits[x:x+5])
    return int(max(nums))