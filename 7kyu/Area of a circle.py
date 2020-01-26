def circleArea(r):
  import math
  if type(r) != int or r < 1:
      return False
  return round((math.pi)*r**2, 2)