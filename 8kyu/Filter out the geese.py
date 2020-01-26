geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    noGeese = [x for x in birds if x not in geese]
    return noGeese