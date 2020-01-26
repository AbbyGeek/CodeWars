def stairs_in_20(stairs):
    all = [sum(i) for i in zip(*stairs)]
    return sum(all)*20