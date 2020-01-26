def shorten_to_date(long_date):
    for x, y in enumerate(long_date):
        if y == ",":
            return long_date[:x]