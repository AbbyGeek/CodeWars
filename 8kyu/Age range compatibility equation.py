def dating_range(age):
    if age <= 14:
        low = age-0.10*age
        high = age+0.10*age
    else:
        low = age/2+7
        high = (age-7)*2
    return str(int(low)) + "-" + str(int(high))