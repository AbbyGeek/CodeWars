def lowercase_count(strng):
    count = 0
    for x in strng:
        if x.islower() == True:
            count += 1
    return count