def square_digits(num):
    new = ""
    for x in str(num):
        new += str(int(x)**2)
    return int(new)