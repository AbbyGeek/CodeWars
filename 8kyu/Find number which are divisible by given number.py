def divisible_by(numbers, divisor):
    new = []
    for x in numbers:
        if x % divisor == 0:
            new.append(x)
    return new