def solution(number):
  sum = 0
  for x in range(number):
        if x % 3 == 0:
            sum = sum + x
        elif x % 5 == 0:
            sum = sum + x
  return sum