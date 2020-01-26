def is_vow(inp):
    l = []
    d = {97:"a",
    101:"e",
    105:"i",
    111:"o",
    117:"u"
    }
    for x , y in enumerate(inp):
        if y in d:
            l.append(d[y])
        else: l.append(y)
    return l