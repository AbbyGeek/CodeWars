def find_next_square(sq):
    if sq**0.5 % 1 != 0:
        return -1
    else: return (sq**0.5 + 1)**2