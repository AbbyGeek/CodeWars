def calculate_age(x, y):
    if x-y == 1:
        return "You will be born in 1 year."
    if x-y == -1:
        return "You are 1 year old."
    if x-y > 1:
        return "You will be born in %i years." % (x-y)
    if x-y < -1:
        return "You are %i years old." % ((x-y)*(-1))
    if x == y:
        return "You were born this very year!"