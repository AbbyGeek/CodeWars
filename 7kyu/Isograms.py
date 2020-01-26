def is_isogram(string):
    new = ""
    for x in string:
        if x.lower() not in new:
            new += x.lower()
    return len(new) == len(string)