def remove(s):
    while s[len(s)-1] == "!":
        s = s[:-1]
    return s