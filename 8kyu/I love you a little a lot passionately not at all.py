def how_much_i_love_you(p):
    d = {1:"I love you",
    2:"a little",
    3:"a lot",
    4:"passionately",
    5:"madly",
    6:"not at all"
    }
    while p > 6:
        p -= 6
    return d.get(p)