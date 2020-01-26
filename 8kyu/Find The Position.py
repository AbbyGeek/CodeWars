def position(alphabet):
    d = list("abcdefghijklmnopqrstuvwxyz")
    n = list(range(1,27))
    dic = dict(zip(d, n))
    return "Position of alphabet: " + str(dic[alphabet])