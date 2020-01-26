def sum_of_n(n):
  ans = []
  entry = 0 
  if n < 0:
      for x in range(0,(n-1)*-1):
          ans.append(entry*-1)
          entry += len(ans)
  for x in range(0,n+1):
      ans.append(entry)
      entry += len(ans)
  return ans