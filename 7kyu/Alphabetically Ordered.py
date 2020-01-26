def alphabetic(s):
    for x in range(len(s)-1):
        if s[x] > s[x+1]:
            return False
    else: return True