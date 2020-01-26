def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue = float(blue_start - blue_pulled)
    red = float(red_start - red_pulled)
    return blue / (red+blue)