def table_game(t):
  tl = t[0][0]
  tr = t[0][2]
  bl = t[2][0]
  br = t[2][2]
  c = t[1][1]
  tc = t[0][1]
  bc = t[2][1]
  if tl+tr+bl+br != c or tc+bc != c:
      return [-1]
  else: return [tl,tr,bl,br]