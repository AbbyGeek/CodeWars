def disemvowel(string):
    for x in string:
        if x in "aeiouAEIOU":
            string = string.replace(x, "")
    return string