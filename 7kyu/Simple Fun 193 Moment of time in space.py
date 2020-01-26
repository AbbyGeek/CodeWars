def moment_of_time_in_space(moment):
  time = sum(int(x) for x in moment if x.isdigit())
  space = 0
  for x in moment:
      if not x.isdigit() or x == "0":
          space += 1 
  return [time<space, time == space, time>space]