def add_length(s):
	s = s.split()
	new = []
	for x in s:
		new.append(str(x) + " " + str(len(x)))
		
	return new