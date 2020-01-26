def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    elif volume / side / side == side:
        return True
    else: return False