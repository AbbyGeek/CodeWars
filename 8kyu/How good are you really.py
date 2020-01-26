def better_than_average(class_points, your_points):
    tot = 0
    for x in class_points:
        tot += x
    avg = tot/len(class_points)
    if your_points > avg:
        return True
    else:
        return False