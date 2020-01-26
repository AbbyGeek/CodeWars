def caffeineBuzz(n):
    if n % 3 == 0 and n % 4 == 0:
        x = "Coffee"
        if n % 2 == 0:
            return x+"Script"
        else: return x
    elif n % 3 == 0:
        x = "Java"
        if n % 2 == 0:
            return x + "Script"
        else: return x
    else: return "mocha_missing!"