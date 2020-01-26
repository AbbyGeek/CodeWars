def solve(nums,div):
    newnums = []
    for x in nums:
        newnums.append(x + x%div)
    return newnums