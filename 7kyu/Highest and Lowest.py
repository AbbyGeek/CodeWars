def high_and_low(numbers):
    nums = numbers.split()
    new = []
    for x in nums:
        new.append(int(x))

    return str(max(new)) + " " + str(min(new))