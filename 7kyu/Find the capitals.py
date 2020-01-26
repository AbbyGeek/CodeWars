def capitals(word):
    ans = []
    for x, y in enumerate(word):
       if y.isupper():
           ans.append(x)
    return ans
