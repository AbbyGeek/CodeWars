def remove_every_other(my_list):
    list = []
    for x, y in enumerate(my_list):
        if x % 2 == 0:
            list.append(y)
    return list