def cooking_time(eggs):
    if eggs == 0: 
        return 0
    if eggs <= 8:
        return 5
    if eggs%8 == 0:
        return eggs / 8 * 5
    else: return int(eggs / 8)*5+5