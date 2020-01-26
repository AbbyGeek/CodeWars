def fake_bin(x):
	new_x = ""
	for thing in x:
		if thing < '5':
			new_x += '0'
		else:
			new_x += '1'
	return new_x