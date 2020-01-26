def remove(s):
    if s == "":
        return ""
    elif s[len(s)-1]== "!":
	    return s[:len(s)-1]
    else: return s