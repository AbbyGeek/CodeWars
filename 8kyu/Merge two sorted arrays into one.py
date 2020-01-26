def merge_arrays(arr1, arr2):
	new_array = arr1 + arr2
	sort_array = sorted(new_array)
	final = []
	for x in sort_array:
		if x not in final:
			final.append(x)
	return final