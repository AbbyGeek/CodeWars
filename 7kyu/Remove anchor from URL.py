def remove_url_anchor(url):
  for x, y in enumerate(url):
      if y == "#":
          return url[:x]
  else: return url