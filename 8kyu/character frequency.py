def char_freq(message):
  d = {}
  for x in message:
      if x not in d:
          d.update({x:message.count(x)})
  return d 