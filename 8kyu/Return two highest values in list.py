def two_highest(arg1):
    for x in arg1:
        if type(x) == str:
            return False
    
    if arg1 == []:
        return []
    num1 = max(arg1)
    arg1 = (x for x in arg1 if x != num1)
    num2 = max(arg1)
    return [num1, num2]