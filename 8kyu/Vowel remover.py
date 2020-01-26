def shortcut( s ):
    for x in s:
        if x in "aeiou":
            s = s.replace(x, "")
    return s