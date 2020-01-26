def get_number_from_string(string):
    num = ""
    for x in string:
        if x in "0123456789":
            num+=x
    return int(num)