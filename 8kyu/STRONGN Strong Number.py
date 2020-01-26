def strong_num(number):
    from math import factorial
    sum = 0
    numlist = [int(x) for x in str(number)]
    
    for x in numlist:
        sum += factorial(x)
    if sum == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"