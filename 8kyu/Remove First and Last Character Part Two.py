def array(string):
    if len(string) <= 4:
        return None
    string = string.replace(",", " ")
    return string[2:len(string)-2]