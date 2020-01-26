def sumDigits(number):
    sum = 0
    for x in str(number):
        if x in "0123456789":
            sum += int(x)

    return sum