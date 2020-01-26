def openOrSenior(data):
    arr = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            arr.append("Senior")
        else: arr.append("Open")
    return arr