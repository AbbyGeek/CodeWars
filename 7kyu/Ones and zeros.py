def binary_array_to_number(arr):
  num = ""
  for x in arr:
      num += str(x)
  return int(num, 2)