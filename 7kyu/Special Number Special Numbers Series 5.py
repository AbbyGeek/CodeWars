def special_number(number):
    num = str(number)
    if len(num) == 1 and number > 5:
        return "NOT!!"
    if len(num) > 1:
        for x in num:
            if int(x) > 5:
                return "NOT!!"
    return "Special!!"