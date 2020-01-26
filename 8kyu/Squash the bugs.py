def find_longest(string):
    string = string.split()
    return max(len(x) for x in string) 