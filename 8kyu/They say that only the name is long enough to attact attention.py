def is_opposite(s1,s2):
    new = ""
    if s1 =="":
        return False
        
    for x in s1:
	    if x.isupper() == True:
		    new += x.lower()
	    if x.islower() == True:
		    new += x.upper()
        
    return new == s2