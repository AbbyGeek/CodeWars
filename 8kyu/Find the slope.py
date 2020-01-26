def find_slope(p):
    if p[0] - p[2] == 0:
        return "undefined"
    if p[1] - p[3] == 0:
        return "0"
    return str((p[1]-p[3]) / (p[0]-p[2]))