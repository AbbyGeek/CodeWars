def printer_error(s):
    count = 0
    for x in s:
        if x not in "abcdefghijklm":
            count += 1
    return str(count) + "/" + str(len(s))