def max_tri_sum(numbers):
    nums = (sorted(numbers)[::-1])
    n = []
    for x in nums:
        if x not in n:
            n.append(x)
    return sum(n[:3])