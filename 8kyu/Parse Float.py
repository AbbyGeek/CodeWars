def parse_float(string):

    string = "".join(string)
    try:
        string = float(string)
        return string
    except ValueError:
        return None